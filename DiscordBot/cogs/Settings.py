import discord
from discord.ext import commands

from DiscordBot.main import client, logs


def setup(bot):
    bot.add_cog(Settings(bot))


class ColorPalette:
    def __init__(self):
        self.neutral = 0xDCDC1E


colors = ColorPalette()


class Settings(commands.Cog):
    def __init__(self, cl):
        self.client = cl

    @commands.command()
    async def ping(self, ctx):
        latency = round(client.latency) * 1000
        embed = discord.Embed(title="Pong ! :ping_pong:",
                              description=f"Latency : {latency} ms",
                              color=colors.neutral)
        await ctx.send(embed=embed)
        logs.writeline(f"Latency evaluated : {latency} ms")
