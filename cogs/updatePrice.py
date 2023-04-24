from discord.ext import commands, tasks
from cogs.magic_eden import MagicEden
from cogs.crypto_price import CryptoPrice


class UpdatePrice(commands.Cog):
    def __init__(self, bot):
        self.cp = CryptoPrice()
        self.me = MagicEden()
        self.bot = bot
        self.jellyUsdChannelId = 1067492731397603370
        self.solUsdChannelId = 1067492877556523029
        self.rascalsId = 1069784203643850845
        self.runawayId = 1077278664221278238
        self.update_left.start()
        # self.update_right.start()

    # @tasks.loop(seconds=60)
    # async def update_right(self):
    #     self.cp.updateJellyUsdPrice()
    #     self.cp.updateJellySolPrice()
    #     self.cp.updateSolUsdPrice()

    #     jpText = f"${self.cp.jellyUsdPrice:.3f} | ◎{self.cp.jellySolPrice:.3f} | ${self.cp.solUsdPrice:.2f}"

    #     await self.bot.change_presence(
    #         activity=discord.Game(
    #             name=jpText,
    #         )
    #     )

    @tasks.loop(seconds=300)
    async def update_left(self):
        jellyUsdStr = "Jelly/SOL: -"
        solUsdStr = "SOL/USD: -"
        data = None

        jellyUsdChannel = self.bot.get_channel(self.jellyUsdChannelId)
        solUsdChannel = self.bot.get_channel(self.solUsdChannelId)
        # rascalsChannel = self.bot.get_channel(self.rascalsId)
        runawayChannel = self.bot.get_channel(self.runawayId)

        if jellyUsdChannel:
            self.cp.updateJellyUsdPrice()
            self.cp.updateJellySolPrice()
            try:
                jellyUsdStr = f"Jelly: ${self.cp.jellyUsdPrice:.3f} | ◎{self.cp.jellySolPrice:.3f}"
                # print(f"jellyUsdChannel API call: ${self.cp.jellyUsdPrice:.3f}")
                await jellyUsdChannel.edit(name=jellyUsdStr)
            except Exception as e:
                print(f"{e} - UpdatePrice-jellyChannel error")

        if solUsdChannel:
            self.cp.updateSolUsdPrice()

            try:
                solUsdStr = f"SOL: ${self.cp.solUsdPrice:.2f}"
                # print(f"jellyUsdChannel API call: ${self.cp.solUsdPrice:.2f}")
                await solUsdChannel.edit(name=solUsdStr)
            except Exception as e:
                print(f"{e} - UpdatePrice-solChannel error")

       # if rascalsChannel:
       #     self.me.updateCollectionStats()
       #     try:
       #         rascalsStr = f"Rascals: ◎{(self.me.rascalsFP / 10**9):.2f} ({self.me.rascalsListings})"
       #         await rascalsChannel.edit(name=rascalsStr)
       #     except Exception as e:
       #         print(f"{e} - UpdatePrice-rascals channel")

        if runawayChannel:
            self.me.updateCollectionStats()
            try:
                runawayStr = f"RR: ◎{(self.me.runawayFP / 10**9):.2f} ({self.me.runawayListings})"
                await runawayChannel.edit(name=runawayStr)
            except Exception as e:
                print(f"{e} - UpdatePrice-runaway channel")

        

    @update_left.before_loop
    async def before_update_left(self):
        print("UpdatePrice waiting...")
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(UpdatePrice(bot))
