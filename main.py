import nacl.public
from flask import Flask, request
import random

app = Flask(__name__)

def generate_keypair() -> tuple[str]:

    private_key = nacl.public.PrivateKey.generate()
    public_key = private_key.public_key


    private_key_str = private_key.encode(encoder=nacl.encoding.Base64Encoder).decode('utf-8')
    public_key_str = public_key.encode(encoder=nacl.encoding.Base64Encoder).decode('utf-8')
    return (private_key_str, public_key_str)

@app.route('/')
def generate_wg_config():
    keypair = generate_keypair()
    local_address = request.args.get(key = "local_address", default = "")
    dns = request.args.get(key = "dns", default = "")
    endpoint = request.args.get(key = "endpoint", default = "")
    server_pubkey = request.args.get(key = "server_pubkey", default = "")
    allowed_ips = request.args.get(key = "allowed_ips", default = "0.0.0.0/0")
    interface = request.args.get(key = "interface", default = "wg0")

    if not all([
        local_address,
        dns,
        endpoint,
        server_pubkey,
        allowed_ips
    ]):
        return "not enough args ._.\nexample GET request with args: \n/?local_address=1.2.3.4&dns=8.8.8.8,8.8.4.4&endpoint=228.13.37.0&server_pubkey=ADmkdlsnghklsnklsdnlkh=&allowed_ips=192.168.0.0/24,10.10.1.1/32"

    return \
        f"""# /interface wireguard peer add public-key="{keypair[1]}" interface={interface} allowed-address={local_address} persistent-keepalive=1m
[Interface]
PrivateKey = {keypair[0]}
ListenPort = {random.randint(20000, 65000)}
Address = {local_address}
DNS = {dns}

[Peer]
PublicKey = {server_pubkey}
AllowedIPs = {allowed_ips}
Endpoint = {endpoint}
        """


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8055)
