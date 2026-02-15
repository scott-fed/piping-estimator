# Remote Access to Mission Control - Research

**Problem:** Need to access OpenClaw Mission Control when away from the Mac mini (from phone, laptop, anywhere).

**Date:** February 15, 2026

---

## TL;DR Recommendation

**Use Tailscale** ✅

**Why:**
- Zero-config VPN (just install, sign in, done)
- End-to-end encrypted (WireGuard protocol)
- No port forwarding or firewall config needed
- Works behind NAT/CGNAT
- Access from phone, laptop, anywhere
- **FREE for personal use** (up to 100 devices)
- No public exposure (only your devices can connect)
- Built-in MagicDNS (friendly names like `macmini.tail-scale.ts.net`)

**Better than:**
- ❌ Hosting service (costs money, complex security)
- ❌ Port forwarding (security risk, ISP issues)
- ❌ Traditional VPN (complex setup, slow)
- ❌ Cloudflare Tunnel (more complex, less flexible)

---

## Solution: Tailscale for Remote Access

### What is Tailscale?

**Tailscale** is a zero-config VPN that creates a secure private network between your devices using the WireGuard protocol.

**How it works:**
1. Install Tailscale on Mac mini (where Mission Control runs)
2. Install Tailscale on phone/laptop
3. Sign in with same account
4. Devices can now talk to each other securely
5. Access Mission Control: `http://macmini:18789` (from anywhere)

**Magic:**
- No manual IP addresses
- No port forwarding
- No firewall rules
- No router configuration
- Works on cellular, public WiFi, anywhere

---

## Setup Guide

### Step 1: Install Tailscale on Mac Mini

```bash
# Install via Homebrew
brew install tailscale

# Or download from https://tailscale.com/download

# Start Tailscale
sudo tailscaled install-system-daemon
tailscale up

# Follow the login prompt (opens browser)
# Sign in with Google/Microsoft/GitHub
```

### Step 2: Install on Phone/Laptop

**iPhone/iPad:**
- Download Tailscale from App Store
- Sign in with same account
- Enable VPN profile when prompted

**Mac/Windows/Linux:**
- Download from https://tailscale.com/download
- Install and sign in

**Android:**
- Download from Google Play
- Sign in

### Step 3: Access Mission Control

**From phone/laptop (on Tailscale):**

```bash
# Mac mini hostname (MagicDNS enabled by default)
http://macmini:18789

# Or use Tailscale IP (find in admin console)
http://100.x.x.x:18789
```

**Telegram still works too:**
- Commands work from anywhere (Telegram is already remote)
- Web UI accessible via Tailscale

---

## Advanced: Tailscale Serve (Public HTTPS)

If you want to share Mission Control with someone (e.g., your piping friend):

```bash
# Expose OpenClaw Gateway securely
tailscale serve https / http://localhost:18789

# Generates public HTTPS URL:
# https://macmini.your-tailnet.ts.net

# Only people you share the link with can access
# Or restrict to Tailscale users only
```

**Use cases:**
- Demo Mission Control to others
- Let agents access from isolated sessions
- Share with team members (if you expand)

---

## Cost Comparison

### Tailscale (Recommended)
- **Free:** Personal use, up to 100 devices, 3 users
- **$6/user/month:** Team features, ACLs, SSO
- **Zero infrastructure cost**

### Hosting Service (e.g., Railway, Render)
- **$5-20/month:** Basic hosting
- **$20-100/month:** With database, resources
- **Complex:** Need to secure, manage, update

### Cloudflare Tunnel
- **Free:** Basic tunneling
- **More complex:** Requires cloudflared daemon, config
- **Less flexible:** Harder to access from arbitrary apps

### Port Forwarding
- **Free:** No service cost
- **RISKY:** Exposes machine to internet
- **Doesn't work:** Many ISPs use CGNAT (can't forward)

---

## Security

### Tailscale Security Model

**End-to-End Encrypted:**
- WireGuard protocol (modern, fast, secure)
- Only your devices can decrypt traffic
- Tailscale servers can't see your data

**Authentication:**
- OAuth via Google/Microsoft/GitHub
- Multi-factor auth supported
- Device approval required

**Access Control:**
- ACLs: Define who can access what
- Exit nodes: Route traffic through trusted device
- Subnet routing: Access other devices on Mac mini's network

**Audit:**
- Logs of all connections
- Device activity tracking
- Revoke access instantly

**Better than:**
- Port forwarding (no encryption, public exposure)
- Traditional VPN (central server sees all traffic)
- Public hosting (attack surface, maintenance burden)

---

## Use Cases for Mission Control

### 1. Check Status from Phone

```bash
# From iPhone (Tailscale connected)
# Open Safari: http://macmini:18789

# View:
# - Agent activity
# - Task status
# - Logs and errors
# - System health
```

### 2. Access from Laptop While Traveling

```bash
# From MacBook Pro (Tailscale connected)
# Open browser: http://macmini:18789

# Or SSH into Mac mini
ssh scott@macmini

# Then use openclaw CLI
openclaw status
openclaw logs friday
```

### 3. Share with Team (Future)

```bash
# Add team member to Tailscale
# They get access to macmini

# Restrict via ACL (only certain ports)
{
  "acls": [
    {
      "action": "accept",
      "src": ["team@example.com"],
      "dst": ["macmini:18789"]
    }
  ]
}
```

### 4. Multi-Device Setup

```bash
# Home setup:
# - Mac mini (Mission Control)
# - MacBook Pro (development)
# - iPhone (monitoring)
# - iPad (dashboards)

# All connected via Tailscale
# Access Mission Control from any device
# No complex networking
```

---

## Alternative: Cloudflare Tunnel

**Cloudflare Tunnel** is another option (also free), but more complex.

### Pros
- Free (no device limit)
- HTTPS by default
- DDoS protection
- Good for public services

### Cons
- Requires cloudflared daemon
- More configuration
- Less flexible for non-HTTP services
- Cloudflare sees your traffic (not end-to-end encrypted)

### Setup

```bash
# Install cloudflared
brew install cloudflared

# Login
cloudflared tunnel login

# Create tunnel
cloudflared tunnel create mission-control

# Route to OpenClaw
cloudflared tunnel route dns mission-control macmini.yourdomain.com

# Run tunnel
cloudflared tunnel run mission-control --url http://localhost:18789
```

**When to use:**
- You want public HTTPS without Tailscale
- Need DDoS protection
- Sharing with non-Tailscale users

**Tailscale is simpler for personal use.**

---

## Comparison Table

| Feature | Tailscale | Cloudflare Tunnel | Port Forwarding | Hosting Service |
|---------|-----------|-------------------|-----------------|-----------------|
| **Setup Complexity** | ⭐⭐⭐⭐⭐ Easy | ⭐⭐⭐ Moderate | ⭐⭐ Hard | ⭐⭐ Hard |
| **Security** | ⭐⭐⭐⭐⭐ E2EE | ⭐⭐⭐⭐ HTTPS | ⭐ Risky | ⭐⭐⭐⭐ Good |
| **Cost (Personal)** | FREE | FREE | FREE | $5-100/mo |
| **Mobile Access** | ✅ Easy | ✅ Yes | ❌ Difficult | ✅ Yes |
| **NAT Traversal** | ✅ Yes | ✅ Yes | ❌ No | N/A |
| **Private Network** | ✅ Yes | ❌ Public | ❌ Public | ❌ Public |
| **Speed** | ⭐⭐⭐⭐⭐ Fast | ⭐⭐⭐⭐ Good | ⭐⭐⭐⭐⭐ Direct | ⭐⭐⭐ Variable |
| **Flexibility** | ⭐⭐⭐⭐⭐ High | ⭐⭐⭐ HTTP only | ⭐⭐⭐⭐ Full | ⭐⭐⭐ Limited |

**Winner: Tailscale** ✅

---

## Implementation Plan

### Week 1: Basic Setup (1 hour)

**Day 1: Install Tailscale**
```bash
# On Mac mini
brew install tailscale
sudo tailscaled install-system-daemon
tailscale up

# On iPhone
# Download Tailscale app
# Sign in
```

**Day 1: Test Access**
```bash
# From iPhone (Safari)
http://macmini:18789

# Should see OpenClaw Gateway UI
```

**Day 2: Configure Telegram Access**
```bash
# Already works (Telegram is remote by default)
# Now web UI also accessible remotely
```

---

### Week 2: Advanced Features (2 hours)

**Subnet Routing:**
Access other devices on Mac mini's network

```bash
# On Mac mini
tailscale up --advertise-routes=192.168.1.0/24

# In Tailscale admin console
# Approve subnet route

# Now you can access:
# - NAS at 192.168.1.100
# - Printer at 192.168.1.50
# - etc.
```

**Exit Node:**
Route all traffic through Mac mini (VPN-like)

```bash
# On Mac mini
tailscale up --advertise-exit-node

# On iPhone/laptop
tailscale up --exit-node=macmini

# Now all traffic goes through Mac mini
# (appears to be from home IP)
```

**MagicDNS:**
Already enabled by default, but verify:

```bash
# Should work:
ping macmini
ssh macmini
http://macmini:18789
```

---

## Security Best Practices

### 1. Enable Key Expiry
```bash
# Keys expire after 180 days (re-auth required)
# Good for security
```

### 2. Use ACLs (Access Control Lists)
```json
{
  "acls": [
    {
      "action": "accept",
      "src": ["scott@gmail.com"],
      "dst": ["macmini:*"]
    }
  ]
}
```

### 3. Enable MFA
```bash
# In Tailscale admin console
# Settings > Enable Multi-Factor Auth
```

### 4. Review Device List Monthly
```bash
# Remove old/unused devices
# Revoke access for lost devices
```

### 5. Monitor Logs
```bash
# Tailscale admin console
# Activity > Connections
# Review who accessed what
```

---

## Troubleshooting

### Can't Connect to macmini

**Check 1: Tailscale Running?**
```bash
# On Mac mini
tailscale status

# Should show: "connected"
```

**Check 2: Both Devices on Same Tailnet?**
```bash
# Check in Tailscale admin console
# Machines > Should see both devices
```

**Check 3: Firewall Blocking?**
```bash
# Mac mini firewall should allow Tailscale
# System Settings > Network > Firewall
# Add Tailscale to allowed apps
```

**Check 4: OpenClaw Running?**
```bash
# On Mac mini
openclaw gateway status

# Should show: "running"
```

### Slow Connection

**Use Direct Connection:**
```bash
# Tailscale tries direct peer-to-peer
# If stuck on relay (DERP), check:
tailscale netcheck

# Look for "direct" vs "relay"
```

**Enable QUIC:**
```bash
# Better for mobile/lossy networks
tailscale up --enable-quic
```

---

## Next Steps

### Immediate (This Week)

1. **Install Tailscale on Mac mini** (10 min)
2. **Install Tailscale on iPhone** (5 min)
3. **Test access:** `http://macmini:18789` from phone (2 min)
4. **Document experience** in memory

### Future Enhancements

1. **Add Tailscale to piping estimator tool**
   - Friend can access from anywhere
   - Demo tool remotely
   - Share with clients (optional)

2. **Subnet routing**
   - Access Mac mini's entire network
   - NAS, printers, other devices

3. **Exit node**
   - Use Mac mini as VPN when traveling

4. **Team expansion**
   - Add team members to Tailscale
   - Share Mission Control access

---

## Resources

- **Tailscale:** https://tailscale.com
- **Docs:** https://tailscale.com/kb
- **Pricing:** https://tailscale.com/pricing
- **Download:** https://tailscale.com/download
- **Support:** https://tailscale.com/contact/support

---

## Conclusion

**Tailscale is the best solution for remote access to Mission Control.**

✅ **Zero-config** - Install, sign in, done  
✅ **Secure** - End-to-end encrypted (WireGuard)  
✅ **Free** - Personal use, up to 100 devices  
✅ **Fast** - Direct peer-to-peer connections  
✅ **Mobile-friendly** - iPhone, Android apps  
✅ **No public exposure** - Private network only  

**Better than:**
- Hosting services (costly, complex)
- Port forwarding (insecure, doesn't work with CGNAT)
- Cloudflare Tunnel (more complex, less private)

**Total setup time:** ~15 minutes  
**Ongoing cost:** $0  
**Security posture:** Excellent  
**User experience:** Seamless  

**Recommendation:** Install Tailscale today, test from iPhone, enjoy remote Mission Control access! 🚀

---

**Next Action:** Install Tailscale on Mac mini and iPhone, test access from phone.
