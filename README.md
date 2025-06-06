# wg-mikrotik-generate
## A mini web-based key generation service for Mikrotik that provides a ready for use CLI command to add a new wg peer, just put it into your Microtik terminal.
# How to run
1. Firstly, you need `docker` and `docker compose` https://docs.docker.com/engine/install/ubuntu/
2. Make sure for not used tcp port `8055` (if you need another, just edit `docker-compose.yml`
3. Run command `docker build -t wg-generate . && docker compose up -d`
4. its ready to use
# How to use
Run it:
- `curl -X GET "http://localhost:8055/?local_address=1.2.3.4&dns=8.8.8.8,8.8.4.4&endpoint=228.13.37.0&server_pubkey=ADmkdlsnghklsnklsdnlkh=&allowed_ips=192.168.0.0/24,10.10.1.1/32"`
OR
- `curl -X GET "http://localhost:8055/?local_address=1.2.3.4&dns=8.8.8.8,8.8.4.4&endpoint=228.13.37.0&server_pubkey=ADmkdlsnghklsnklsdnlkh=&allowed_ips=192.168.0.0/24,10.10.1.1/32" > test.conf`

You may get something like this:

```bash
# /interface wireguard peer add public-key="QK4wzAuzF0D33YkgAzO+77o12sBAamXGhVZOBFKgPg4=" interface=wg0 allowed-address=1.2.3.4 persistent-keepalive=1m
[Interface]
PrivateKey = dYsxq/oaIY979obGCB2GAnFe6mQF7F6mLGUnQIhuBGc=
ListenPort = 46558
Address = 1.2.3.4
DNS = 8.8.8.8,8.8.4.4

[Peer]
PublicKey = ADmkdlsnghklsnklsdnlkh=
AllowedIPs = 192.168.0.0/24,10.10.1.1/32
Endpoint = 228.13.37.0
```

This part put to your Mikrotik (with configured wg server for ex.):
`/interface wireguard peer add public-key="QK4wzAuzF0D33YkgAzO+77o12sBAamXGhVZOBFKgPg4=" interface=wg0 allowed-address=1.2.3.4 persistent-keepalive=1m`

This part you can save to test.conf and put it to Wireguard client programm:
```bash
[Interface]
PrivateKey = dYsxq/oaIY979obGCB2GAnFe6mQF7F6mLGUnQIhuBGc=
ListenPort = 46558
Address = 1.2.3.4
DNS = 8.8.8.8,8.8.4.4

[Peer]
PublicKey = ADmkdlsnghklsnklsdnlkh=
AllowedIPs = 192.168.0.0/24,10.10.1.1/32
Endpoint = 228.13.37.0
```

Thanks for your stars🙏
