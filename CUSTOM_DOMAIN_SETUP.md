# Custom Domain Setup for FLASH

## Quick Setup with Cloudflare Tunnel (Recommended)

### 1. Prepare Cloudflare Account
1. Sign up at https://cloudflare.com (free)
2. Add your Namecheap domain
3. Change nameservers in Namecheap to Cloudflare's

### 2. Install Cloudflare Tunnel
```bash
brew install cloudflared
cloudflared tunnel login
cloudflared tunnel create flash-app
```

### 3. Configure Your Domain
Edit the tunnel config to use your actual domain:
```bash
nano cloudflare-tunnel-config.yml
```

Replace `yourdomain.com` with your actual domain.

### 4. Update Frontend Configuration
Create `.env` file in `flash-frontend-apple/`:
```
REACT_APP_API_URL=https://api.yourdomain.com
```

### 5. Start Everything
```bash
# Terminal 1: Start local services
./start_local.sh

# Terminal 2: Start tunnel
cloudflared tunnel --config cloudflare-tunnel-config.yml run
```

### 6. Add DNS Records in Cloudflare
1. Go to Cloudflare Dashboard → DNS
2. Add CNAME record: `api` → `[tunnel-id].cfargotunnel.com`
3. Add CNAME record: `app` → `[tunnel-id].cfargotunnel.com`

## Your URLs Will Be:
- Frontend: https://app.yourdomain.com
- Backend API: https://api.yourdomain.com
- Main domain: https://yourdomain.com

## Benefits:
- ✅ Uses your Namecheap domain
- ✅ Free (Cloudflare tunnel is free)
- ✅ SSL certificates automatic
- ✅ No port forwarding needed
- ✅ Works behind NAT/firewall
- ✅ Can run on your laptop

## Alternative: Quick Testing with Ngrok
For quick testing without domain setup:
```bash
ngrok http 8001
```

This gives you a temporary URL like `https://abc123.ngrok.io`