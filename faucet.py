import requests
from generate_address import address_a

# Request test coins from faucet
faucet_url = "https://faucet.bitcoincloud.net/faucet"
response = requests.post(faucet_url, json={"address": address_a})

if response.status_code == 200:
    print("Faucet request successful")
    print(f"Test BSV sent to address: {address_a}")
else:
    print(f"Faucet request failed with status code {response.status_code}")
    print("You can also try getting test coins from:")
    print("1. https://testnet.satoshisvision.network/")
    print("2. https://faucet.bitcoincloud.net/")
    