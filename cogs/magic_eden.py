import requests
from dotenv import load_dotenv


class MagicEden:
    def __init__(self):
        self.collectionFP = 0
        self.collectionListings = 0

    def collectionStatsApiUrl(self):
        return f"https://api-mainnet.magiceden.dev/v2/collections/rascals/stats"

    def updateCollectionStats(self):
        try:
            resp = requests.get(self.collectionStatsApiUrl()).json()
            self.collectionFP = resp["floorPrice"]
            self.collectionListings = resp["listedCount"]
        except Exception as e:
            print(f"{e} - MagicEden-updateCollectionStat")
            self.collectionFP = 0
            self.collectionListings = 0
