# cogs/question.py
import discord
from discord.ext import commands
import random

class Question(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def question(self, ctx):
        UNO = discord.utils.get(ctx.guild.emojis, name='mmountUNO')
        random_number = random.randint(1, 10)

        responses = {
            1: "I don't know...maybe ask a mod",
            2: "ERM, I'm unsure Pwincess.",
            3: "Hey, I'm a little busy right now. Can you talk later?",
            4: "Sorry, I'm in the middle of a Nightreign Run. Give me a sec.",
            5: "https://tenor.com/view/i-dont-know-you-who-are-you-excuse-me-leave-me-alone-mind-your-business-gif-15629630053949127615",
            8: "☝️ Ummmm chat? Anyone else able to help them with this one?",
            9: "Uhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh",
            10: "Hola! No Se!"
        }

        # Safe emoji reaction handler
        if random_number in [6, 7]:
            if random_number == 6:
                await ctx.message.add_reaction('🙈')
            elif random_number == 7:
                if UNO:
                    await ctx.message.add_reaction(UNO)
                else:
                    await ctx.send("UNO emoji not found, self-reflect 🤔")
        else:
            await ctx.send(responses[random_number])

# Needed to load cog
async def setup(bot):
    await bot.add_cog(Question(bot))