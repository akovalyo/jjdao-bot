import requests
from dotenv import load_dotenv


class CryptoPrice:
    def __init__(self):
        self.jellyUsdPrice = 0
        self.priceChange = 0
        self.jellySolPrice = 0
        self.solUsdPrice = 0
        self.upSign = ""
        self.downSign = ""
        self.jellySolApiUrl = "https://quote-api.jup.ag/v1/price?id=9WMwGcY6TcbSfy9XPpQymY3qNEsvEaYL3wivdwPG2fpp&vsToken=So11111111111111111111111111111111111111112&amount=1"
        self.jellyUsdApiCoingeckoUrl = "https://api.coingecko.com/api/v3/simple/price?ids=jelly-esports&vs_currencies=usd&include_24hr_change=true"
        self.jellyUsdApiJupUrl = "https://quote-api.jup.ag/v1/price?id=9WMwGcY6TcbSfy9XPpQymY3qNEsvEaYL3wivdwPG2fpp&vsToken=USDC&amount=1"
        self.solUsdApiCoingeckoUrl = (
            "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd"
        )

    def updateJellyUsdPrice(self):
        try:
            resp = requests.get(self.jellyUsdApiCoingeckoUrl).json()
            self.jellyUsdPrice = resp["jelly-esports"]["usd"]
            self.priceChange = resp["jelly-esports"]["usd_24h_change"]
        except Exception as e:
            print(f"{e}, cryptoprice-updateJellyUsdPrice")
            self.priceChange = 0
            try:
                resp = requests.get(self.jellyUsdApiJupUrl).json()
                self.jellyUsdPrice = resp["data"]["price"]

            except Exception as e:
                print(f"{e}, cryptoprice-updateJellyUsdPrice")
                self.jellyUsdPrice = 0

    def updateJellySolPrice(self):
        try:
            resp = requests.get(self.jellySolApiUrl).json()
            self.jellySolPrice = resp["data"]["price"]

        except Exception as e:
            self.jellySolPrice = 0
            print(f"{e} - cryptoprice-updateJellySolPrice")

    def updateSolUsdPrice(self):
        try:
            resp = requests.get(self.solUsdApiCoingeckoUrl).json()
            self.solUsdPrice = resp["solana"]["usd"]
        except Exception as e:
            print(f"{e} - cryptoprice-updateSolUsdPrice")
            self.solUsdPrice = 0
