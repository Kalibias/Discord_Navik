# This example requires the 'message_content' intent.
import asyncio
import time
from tarot import tarot_draw
from beanpick import bean_picker_9000

from discord.ext import commands
from info import token
import discord

nexhi_reactions = ["wh-", ",", ".", "i-", "...", ":D", "HELLO?"]
illegal_works = ["Skinwalker", "skin walker", "skinwalker"]
intents = discord.Intents.default()
intents.message_content = True


class MyClient(discord.Client):

    # async def repeat(self, message):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    # bot.add_command(test)

    async def on_message(self, message):

        if message.author == client.user:
            return

        # if message.content in nexhi_reactions and message.author.id == 206097643934449665:
        #     time.sleep(3)
        #     await message.reply("Someone likely said something so unbelievable "
        #                         "that Nexhi is at a loss for words. This isn't a good thing, btw.")

        # if message.content == message.content.upper() and len(
        #         message.content) >= 14 and message.author.id == 206097643934449665:
        #     await message.reply("Calm the caps down, Nexhi.")
        #     await message.delete()
        #
        # if message.content in illegal_works:
        #     await message.delete()

        print(f'Message hofrom {message.author} in {message.guild} {message.channel}: {message.content}')

        if message.content.lower() in "tarot" and not message.attachments:
            # For now, it'll only draw a single card.
            await message.reply(tarot_draw())
        #
        # if message.content.lower() in "intro":
        #     await message.reply("""Name: Navik\nPronouns: He/Him\nAge: Old Enough.\n
        #                 Characters / Muse List: N/A\n
        #                 Triggers: Bean Please\n
        #                 Extra: I'm a bot.""")

        if message.content.lower() in "bean please" and not message.attachments:
            if message.guild.name == "CRUISE":
                print("no.")
            else:
                await message.reply(bean_picker_9000())
                print(f"Command Activated for {message.author} in {message.guild}")


client = MyClient(intents=intents)
client.run(token)
