from bsv import PrivateKey

# Generate sender address (Address A) for testnet
priv_key_a = PrivateKey()
wif_a = priv_key_a.wif() # wallet import format
address_a = priv_key_a.address(testnet=True)  # Set testnet=True for testnet address

# print(f"Address A: {address_a}")
# print(f"WIF A: {wif_a}")

# Generate receiver address (Address B) for testnet

priv_key_b = PrivateKey()
wif_b = priv_key_b.wif()
address_b = priv_key_b.address(testnet=True)  # Set testnet=True for testnet address

# Print out the keys and addresses
print("\n===== Sender Information ======")
print(f"Private Key: {wif_a}")
print(f"Address: {address_a}")

print("\n===== Receiver Information ======")
print(f"Private Key: {wif_b}")
print(f"Address: {address_b}")

# Save data to file for easy reference
with open("wallet_info.txt", "w") as f:
    f.write(f"Sender Private Key: {wif_a}\n")
    f.write(f"Sender Address: {address_a}\n")
    f.write(f"Receiver Private Key: {wif_b}\n")
    f.write(f"Receiver Address: {address_b}\n")

print("\nData saved to wallet_info.txt")

# Export the address for use in other scripts
__all__ = ['address_a']