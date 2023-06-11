import requests
from dotenv import load_dotenv


class MagicEden:
    def __init__(self):
        self.dawgsFP = 0
        self.dawgsListings = 0
        self.runawayFP = 0
        self.runawayListings = 0

    def collectionStatsApiUrl(self, collection):
        return f"https://api-mainnet.magiceden.dev/v2/collections/{collection}/stats"

    def updateRunawayStats(self):
        try:
            resp = requests.get(self.collectionStatsApiUrl("runaway_rascals")).json()
            self.runawayFP = resp["floorPrice"]
            self.runawayListings = resp["listedCount"]
        except Exception as e:
            print(f"{e} - MagicEden-updateRunawayStat")
            #self.collectionFP = 0
            #self.collectionListings = 0
        
    def updateDawgsStats(self):
        try:
            resp = requests.get(self.collectionStatsApiUrl("jellydawgs")).json()
            self.dawgsFP = resp["floorPrice"]
            self.dawgsListings = resp["listedCount"]
        except Exception as e:
            print(f"{e} - MagicEden-updateCollectionStat")
            #self.collectionFP = 0
            #self.collectionListings = 0

    
