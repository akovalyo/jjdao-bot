import requests
from dotenv import load_dotenv


class MagicEden:
    def __init__(self):
        self.rascalsFP = 0
        self.rascalsListings = 0
        self.runawayFP = 0
        self.runawayListings = 0

    def collectionStatsApiUrl(self, collection):
        return f"https://api-mainnet.magiceden.dev/v2/collections/{collection}/stats"

    def updateCollectionStats(self):
        try:
            resp = requests.get(self.collectionStatsApiUrl("rascals")).json()
            self.rascalsFP = resp["floorPrice"]
            self.rascalsListings = resp["listedCount"]
            resp = requests.get(self.collectionStatsApiUrl("runaway_rascals")).json()
            self.runawayFP = resp["floorPrice"]
            self.runawayListings = resp["listedCount"]
        except Exception as e:
            print(f"{e} - MagicEden-updateCollectionStat")
            self.collectionFP = 0
            self.collectionListings = 0

    
