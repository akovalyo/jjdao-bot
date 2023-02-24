import os
import discord
from dotenv import load_dotenv


def main():
    load_dotenv()
    intents = discord.Intents.default()
    intents.message_content = True
    bot = discord.Bot(intents=intents)
    token = os.getenv("DISCORD_TOKEN")

    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user} (ID: {bot.user.id}) ")
        guilds = bot.guilds
        for guild in guilds:
            print(f"{guild.name} - {guild.id}")

    bot.load_extension("cogs.urlGuard")
    bot.load_extension("cogs.updatePrice")
    bot.run(token)


if __name__ == "__main__":
    main()
