import requests

def get_eth_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    return requests.get(url).json()["ethereum"]["usd"]

def calculate_fee(gas_used: int, gas_price_gwei: float):
    # 1 gwei = 1e-9 ETH
    eth_fee = gas_used * gas_price_gwei * 1e-9
    usd_price = get_eth_price()
    usd_fee = eth_fee * usd_price
    return eth_fee, usd_fee

if __name__ == "__main__":
    gas_used = int(input("Enter gas used (e.g. 21000): "))
    gas_price = float(input("Enter gas price in gwei: "))

    eth_fee, usd_fee = calculate_fee(gas_used, gas_price)
    print(f"\nTransaction fee: {eth_fee:.6f} ETH (~${usd_fee:.2f})")
