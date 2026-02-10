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
4. **info@sacredhaloconnection.com starts receiving mail** ✅

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
**Status:** Pending Implementation
