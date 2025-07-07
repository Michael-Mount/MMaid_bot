# cogs/question.py
import discord
from discord.ext import commands

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def poll(self, ctx, *, question):
        embed = discord.Embed(title="📊 New Poll", description=question, color=discord.Color.dark_green())
        poll_message = await ctx.send(embed=embed)
        await poll_message.add_reaction("👍")
        await poll_message.add_reaction("👎")

# Needed to load cog
async def setup(bot):
    await bot.add_cog(Poll(bot))
