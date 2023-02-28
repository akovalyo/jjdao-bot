from discord.ext import commands, tasks
import cloudscraper
import discord



class KickStreams(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.streamers = {"wolfietv": 0, 
                          "kcanie": 0, 
                          "carlosomfg": 0, 
                          "karlkulture": 0, 
                          "tomshadywood": 0, 
                          "henixdd": 0,
                          "justjack":0,
                          "flapz": 0,
                          "icOn": 0,
                        }
        self.checkStreams.start()
        self.channelId = 1080034277250568243

        
    @tasks.loop(minutes=5)
    async def checkStreams(self):
        scraper = cloudscraper.create_scraper()

        for streamer in self.streamers.keys():
            try:
                resp = scraper.get(f"https://kick.com/api/v1/channels/{streamer}").json()
                if resp["livestream"]:
                    if self.streamers[streamer] == 0:
                        self.streamers[streamer] = 1
                        url = f"https://kick.com/{streamer}"
                        profilePic = ""
                        banner = ""
                        if resp["user"]["profile_pic"]:
                            profilePic = resp["user"]["profile_pic"]
                        if resp["banner_image"]:
                            banner = resp["banner_image"]["url"]
                        followers = resp["followersCount"]
                        channel = self.bot.get_channel(self.channelId)
        
                        embed = discord.Embed(title=f"**{streamer.capitalize()}** is live on Kick", description=f"", color=0x54F513)
                        embed.add_field(name="", value=url)
                        embed.set_footer(text=f"Followers: {followers}")
                        if profilePic:
                            embed.set_thumbnail(url=profilePic)
                        if banner:
                            embed.set_image(url=banner)
                        await channel.send(embed=embed)
                else:
                    self.streamers[streamer] = 0   
            except Exception as e:
                print(f"KICKSTREAMS. Streamer: {streamer}. Error: {e}")
        

        

    @checkStreams.before_loop
    async def before_update_left(self):
        print("KickStreams waiting...")
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(KickStreams(bot))
