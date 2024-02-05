import discord
from discord.ext import commands
from discord.commands import option
from src.security import has_ban_perm
from src.embeds import EmbedFactory


class Solsuite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.solsuite = 982212335185833995

    @discord.slash_command(
        name="send-message",
        description="Send message to channels",
    )
    @option(
        "message",
        description="Text of the messsage",
        required=True,
    )
    @option(
        "category",
        description="Channels category",
        required=True,
    )
    @has_ban_perm()
    async def send_message(
        self, ctx: discord.ApplicationContext, message: str, category: str
    ):
        await ctx.defer(ephemeral=True)
        if ctx.guild.id != self.solsuite:
            await ctx.respond(
                embed=EmbedFactory(
                    "error", "Command is not allowed in this server"
                ).create(),
                ephemeral=True,
            )
            return
        counter = 0
        errors = 0
        for channel in ctx.guild.text_channels:
            if str(channel.category) == category:
                try:
                    ch = self.bot.get_channel(channel.id)
                    await ch.send(message)
                    counter += 1
                except Exception as e:
                    errors += 1
        if counter == 0 and errors == 0:
            await ctx.respond("Category not found", ephemeral=True)
        else:
            await ctx.respond(
                f"{counter} messages sent, failed to send messages to {errors} channels",
                ephemeral=True,
            )


def setup(bot):
    bot.add_cog(Solsuite(bot))
