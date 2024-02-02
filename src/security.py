from discord.ext import commands


def is_owner():
    """A :func:`.check` that checks if the person invoking this command is the owner of the bot."""

    async def predicate(ctx):
        if await ctx.bot.is_owner(ctx.author):
            return True
        else:
            return False

    return commands.check(predicate)


def is_admin():
    """A :func:`.check` that checks if the person invoking this command is the owner of the bot or
    admin of the guild .
    """

    async def predicate(ctx):
        if await ctx.bot.is_owner(ctx.author):
            return True
        elif ctx.author.guild_permissions.administrator:
            return True
        else:
            return False

    return commands.check(predicate)


def has_ban_perm():
    async def predicate(ctx):
        if await ctx.bot.is_owner(ctx.author):
            return True
        elif ctx.author.guild_permissions.administrator:
            return True
        elif ctx.author.guild_permissions.ban_members:
            return True
        return False

    return commands.check(predicate)
