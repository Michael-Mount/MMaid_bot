# cogs/question.py
import discord
from discord.ext import commands
import random

class Hug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def hug(self, ctx, member: discord.Member = None):
        # Ensure member is mentioned
        if member is None:
            await ctx.send("You need to mention someone! i.e. `!hug @MMount`")
            return

        # Self-hug prevention
        if member.id == ctx.author.id:
            await ctx.send("I'm glad you love yourself! Just maybe do it behind closed doors, not in chat... 💀")
            return

        responses = [
            f"{ctx.author.display_name} gives {member.display_name} a warm hug!",
            f"{ctx.author.display_name} comforts {member.display_name} with a caring embrace.",
            f"{ctx.author.display_name} opens their arms wide for {member.display_name} to crash into if needed.",
            f"{ctx.author.display_name} gives {member.display_name} a tight, squishy hug!",
            f"{ctx.author.display_name} is here to give {member.display_name} a hug — no questions asked."
        ]

        await ctx.send(random.choice(responses))

# Required setup for cog loader
async def setup(bot):
    await bot.add_cog(Hug(bot))

