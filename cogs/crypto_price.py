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
        self.jellySolApiUrl = "https://price.jup.ag/v4/price?ids=JELLY&vsToken=SOL"
        self.jellyUsdApiCoingeckoUrl = "https://api.coingecko.com/api/v3/simple/price?ids=jelly-esports&vs_currencies=usd&include_24hr_change=true"
        self.jellyUsdApiJupUrl = "https://price.jup.ag/v4/price?ids=JELLY&vsToken=USDC"
        self.solUsdApiCoingeckoUrl = (
            "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd"
        )

    def updateJellyUsdPrice(self):
        try:
            resp = requests.get(self.jellyUsdApiJupUrl).json()
            self.jellyUsdPrice = resp["data"]["JELLY"]["price"]
        except Exception as e:
            print(f"jup cryptoprice-updateJellyUsdPrice error: {e}")
            self.priceChange = 0
            try:
                resp = requests.get(self.jellyUsdApiCoingeckoUrl).json()
                self.jellyUsdPrice = resp["jelly-esports"]["usd"]
            except Exception as e:
                print(f"Coingecko cryptoprice-updateJellyUsdPrice error: {e}")
                self.jellyUsdPrice = 0

    def updateJellySolPrice(self):
        try:
            resp = requests.get(self.jellySolApiUrl).json()
            self.jellySolPrice = resp["data"]["JELLY"]["price"]

        except Exception as e:
            self.jellySolPrice = 0
            print(f"Jup cryptoprice-updateJellySolPrice error: {e}")

    def updateSolUsdPrice(self):
        try:
            resp = requests.get(self.solUsdApiCoingeckoUrl).json()
            self.solUsdPrice = resp["solana"]["usd"]
        except Exception as e:
            print(f"{e} - cryptoprice-updateSolUsdPrice")
            self.solUsdPrice = 0
