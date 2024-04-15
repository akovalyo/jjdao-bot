import os
import discord
from dotenv import load_dotenv
from src.embeds import EmbedFactory


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

    @bot.event
    async def on_application_command_error(
        ctx: discord.ApplicationContext, error: discord.DiscordException
    ):
        if isinstance(error, discord.errors.CheckFailure):
            await ctx.respond(
                embed=EmbedFactory(
                    "error", "Sorry, you dont have permissions to use this command"
                ).create(),
                ephemeral=True,
            )
        elif isinstance(error, discord.errors.NotFound):
            await ctx.respond(
                embed=EmbedFactory(
                    "error", "Sorry, the bot didn't respond. Try again"
                ).create(),
                ephemeral=True,
            )
        else:
            print(f"BOT GENERAL ERROR: {error}")
            try:
                await ctx.respond(
                    embed=EmbedFactory("error", "Something went wrong.").create(),
                    ephemeral=True,
                )
            except Exception as e:
                print(f"Failed to send a context response: {error}")

    # bot.load_extension("cogs.urlGuard")
    bot.load_extension("cogs.updatePrice")
    # bot.load_extension("cogs.solsuite")
    bot.run(token)


if __name__ == "__main__":
    main()
