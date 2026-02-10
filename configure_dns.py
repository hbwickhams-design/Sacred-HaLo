#!/usr/bin/env python3
"""
Cloudflare DNS Configuration Script for sacredhaloconnection.com
Automatically configures email DNS records for Namecheap Private Email
"""

import requests
import json
import sys

# Configuration
API_TOKEN = "JJBhxLPLQxhFLde-1dwjTUtFM2w7BehhydCaIGbZ"
DOMAIN = "sacredhaloconnection.com"
API_BASE = "https://api.cloudflare.com/client/v4"

# Headers for API requests
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def get_zone_id():
    """Get the Zone ID for the domain"""
    print(f"🔍 Looking up Zone ID for {DOMAIN}...")
    
    url = f"{API_BASE}/zones"
    params = {"name": DOMAIN}
    
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    
    if not data.get("success"):
        print(f"❌ Error: {data.get('errors')}")
        sys.exit(1)
    
    if not data.get("result"):
        print(f"❌ Domain {DOMAIN} not found in your Cloudflare account")
        sys.exit(1)
    
    zone_id = data["result"][0]["id"]
    print(f"✅ Found Zone ID: {zone_id}")
    return zone_id

def get_dns_records(zone_id):
    """Get all DNS records for the zone"""
    print(f"\n📋 Fetching existing DNS records...")
    
    url = f"{API_BASE}/zones/{zone_id}/dns_records"
    response = requests.get(url, headers=headers)
    data = response.json()
    
    if not data.get("success"):
        print(f"❌ Error: {data.get('errors')}")
        return []
    
    return data.get("result", [])

def delete_old_mx_records(zone_id, records):
    """Delete old MX records (eforwardr)"""
    print(f"\n🗑️  Deleting old MX records...")
    
    mx_records = [r for r in records if r["type"] == "MX"]
    deleted_count = 0
    
    for record in mx_records:
        # Delete any existing MX records to start fresh
        print(f"   Deleting: {record['content']} (Priority: {record['priority']})")
        url = f"{API_BASE}/zones/{zone_id}/dns_records/{record['id']}"
        response = requests.delete(url, headers=headers)
        
        if response.json().get("success"):
            deleted_count += 1
        else:
            print(f"   ⚠️  Warning: Could not delete {record['content']}")
    
    print(f"✅ Deleted {deleted_count} old MX record(s)")

def add_mx_record(zone_id, mail_server, priority):
    """Add a new MX record"""
    print(f"   Adding MX: {mail_server} (Priority: {priority})")
    
    url = f"{API_BASE}/zones/{zone_id}/dns_records"
    data = {
        "type": "MX",
        "name": "@",
        "content": mail_server,
        "priority": priority,
        "ttl": 1  # Auto TTL
    }
    
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    
    if result.get("success"):
        print(f"   ✅ Added {mail_server}")
        return True
    else:
        print(f"   ❌ Error adding {mail_server}: {result.get('errors')}")
        return False

def add_spf_record(zone_id, records):
    """Add SPF TXT record"""
    print(f"\n📝 Configuring SPF record...")
    
    # Check if SPF record already exists
    spf_content = "v=spf1 include:spf.privateemail.com ~all"
    existing_spf = [r for r in records if r["type"] == "TXT" and "spf" in r["content"].lower()]
    
    # Delete existing SPF records
    for record in existing_spf:
        print(f"   Deleting old SPF: {record['content']}")
        url = f"{API_BASE}/zones/{zone_id}/dns_records/{record['id']}"
        requests.delete(url, headers=headers)
    
    # Add new SPF record
    url = f"{API_BASE}/zones/{zone_id}/dns_records"
    data = {
        "type": "TXT",
        "name": "@",
        "content": spf_content,
        "ttl": 1  # Auto TTL
    }
    
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    
    if result.get("success"):
        print(f"   ✅ Added SPF record")
        return True
    else:
        print(f"   ❌ Error adding SPF record: {result.get('errors')}")
        return False

def main():
    print("=" * 60)
    print("🚀 Cloudflare DNS Configuration for sacredhaloconnection.com")
    print("=" * 60)
    
    # Step 1: Get Zone ID
    zone_id = get_zone_id()
    
    # Step 2: Get existing DNS records
    records = get_dns_records(zone_id)
    
    # Step 3: Delete old MX records
    delete_old_mx_records(zone_id, records)
    
    # Step 4: Add new MX records
    print(f"\n✉️  Adding new MX records for Namecheap Private Email...")
    add_mx_record(zone_id, "mx1.privateemail.com", 10)
    add_mx_record(zone_id, "mx2.privateemail.com", 10)
    
    # Step 5: Add SPF record
    add_spf_record(zone_id, records)
    
    print("\n" + "=" * 60)
    print("✅ DNS Configuration Complete!")
    print("=" * 60)
    print("\n📧 Your email (info@sacredhaloconnection.com) will be active in:")
    print("   • 15-60 minutes (usually)")
    print("   • Up to 4 hours (maximum)")
    print("\n🔍 Verify your records at:")
    print("   https://mxtoolbox.com/SuperTool.aspx?action=mx%3asacredhaloconnection.com")
    print("\n✨ Done! Your DNS is now configured for Namecheap Private Email.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Script interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
