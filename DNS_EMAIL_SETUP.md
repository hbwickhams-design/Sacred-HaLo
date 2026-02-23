# DNS Email Setup Guide for sacredhaloconnection.com

## 🚨 URGENT: Email DNS Configuration

This guide will fix the email setup for `info@sacredhaloconnection.com` by configuring the correct DNS records in Cloudflare.

---

## What You Need to Do NOW (Correct Path)

### Step 1: Open Cloudflare
- Log into Cloudflare
- Select **sacredhaloconnection.com**

### Step 2: Go to DNS
- Cloudflare dashboard → **DNS** tab

### Step 3: Add These Records Exactly

#### MX Record #1
- **Type:** MX
- **Name:** @
- **Mail server:** mx1.privateemail.com
- **Priority:** 10
- **TTL:** Auto

#### MX Record #2
- **Type:** MX
- **Name:** @
- **Mail server:** mx2.privateemail.com
- **Priority:** 10
- **TTL:** Auto

#### TXT Record (SPF)
- **Type:** TXT
- **Name:** @
- **Content:** `v=spf1 include:spf.privateemail.com ~all`
- **TTL:** Auto

---

## 🔒 IMPORTANT: Add DKIM and DMARC Records (Prevents Spam)

### Step 3B: Add DKIM Record

You need to get your DKIM record from Namecheap. Here's how:

1. **Go to Namecheap Private Email**
2. **Look for "DKIM Settings"** or check the screenshot/email they sent you
3. **Copy the DKIM record values** - they look like:
   - **Hostname:** `default._domainkey` (or similar)
   - **Value:** A long string starting with `v=DKIM1; k=rsa; p=...`

4. **Add to Cloudflare:**
   - **Type:** TXT
   - **Name:** (paste the hostname from Namecheap - usually `default._domainkey`)
   - **Content:** (paste the long DKIM value)
   - **TTL:** Auto
   - Click **Save**

### Step 3C: Add DMARC Record

This tells email providers how to handle emails that fail authentication:

- **Type:** TXT
- **Name:** `_dmarc`
- **Content:** `v=DMARC1; p=none; rua=mailto:hello@sacredhaloconnection.com`
- **TTL:** Auto
- Click **Save**

**What this does:**
- `p=none` - Monitor mode (doesn't reject emails, just reports)
- `rua=mailto:hello@sacredhaloconnection.com` - Sends reports to your email

---

### Step 4: Check for Old MX Records

If you see any of these:
- Google
- Zoho
- Outlook
- Anything else mail-related

**❌ DELETE THEM**

**Only one mail system gets the throne.**

---

## After That

1. **Save** in Cloudflare
2. **Wait** 15 minutes to 1 hour (sometimes up to 4 hours)
3. The **yellow warning in Namecheap disappears**
4. **hello@sacredhaloconnection.com and info@sacredhaloconnection.com start receiving mail** ✅
5. **Your emails won't go to spam** 🎉

---

## 📧 Where to Find Your DKIM Details

**Option 1: Check the Namecheap screenshot/notification you received**
- Look for the section that says "DKIM record"
- Copy the **Host** and **Value**

**Option 2: Log into Namecheap**
1. Go to https://www.namecheap.com
2. Click on **Private Email**
3. Click on **Email Security** or **DKIM Settings**
4. Copy the values shown

The DKIM record will look something like this:
- **Host:** `default._domainkey`
- **DNS Record:** `v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...` (very long string)

---

## ❌ What NOT to Do

- ❌ Don't change nameservers
- ❌ Don't buy PremiumDNS
- ❌ Don't upgrade email plans
- ❌ Don't touch cPanel

---

## 🎯 Bottom Line

**You are one clean DNS entry away from working email.**

Just add these 3 records in Cloudflare DNS, delete old MX records, and you're done.

---

## Verification Commands

After adding the records, you can verify with these commands:

```bash
# Check MX records
dig MX sacredhaloconnection.com

# Check SPF record
dig TXT sacredhaloconnection.com

# Use online tools
https://mxtoolbox.com/SuperTool.aspx?action=mx%3asacredhaloconnection.com
```

---

**Date Created:** 2026-02-10  
**Last Updated:** 2026-02-23  
**Status:** Pending Implementation

---

## 📝 Quick Summary Checklist

Go to Cloudflare DNS and add these records:

- [ ] MX: mx1.privateemail.com (Priority 10)
- [ ] MX: mx2.privateemail.com (Priority 10)
- [ ] TXT (SPF): `v=spf1 include:spf.privateemail.com ~all`
- [ ] TXT (DKIM): Get from Namecheap (hostname: `default._domainkey`)
- [ ] TXT (DMARC): `_dmarc` → `v=DMARC1; p=none; rua=mailto:hello@sacredhaloconnection.com`

**After adding, wait 1-4 hours for DNS to propagate.**
