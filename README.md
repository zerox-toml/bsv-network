# BSV Tutorial Project

This project demonstrates basic Bitcoin SV (BSV) operations including address generation, faucet requests, and transaction handling on the BSV testnet.

## Features

- Generate BSV testnet addresses and private keys
- Request test BSV from faucets
- Send BSV transactions
- Save wallet information for reference

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd bsv_tutorial
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install bsv requests
```

## Usage

### Generate Addresses
Run the address generation script to create new BSV testnet addresses:
```bash
python generate_address.py
```
This will:
- Generate a sender and receiver address pair
- Save the wallet information to `wallet_info.txt`
- Display the addresses and private keys in the console

### Request Test BSV
To request test BSV from the faucet:
```bash
python faucet.py
```
This will send a request to the Bitcoin Cloud faucet for the generated sender address.

### Send BSV
To send BSV:
```bash
python send_bsv.py
```

## Project Structure

- `generate_address.py`: Generates BSV testnet addresses and private keys
- `faucet.py`: Requests test BSV from faucets
- `send_bsv.py`: Handles BSV transactions
- `wallet_info.txt`: Stores generated wallet information
- `sample_data/`: Contains sample data for testing

## Notes

- This project operates on the BSV testnet
- Always keep your private keys secure and never share them
- Test BSV can be obtained from multiple faucets if one fails

## Faucet Alternatives

If the default faucet is unavailable, you can try:
1. https://testnet.satoshisvision.network/
2. https://faucet.bitcoincloud.net/

## License

[Add your license information here]

## Contributing

[Add contribution guidelines if applicable] 