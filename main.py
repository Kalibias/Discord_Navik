# This example requires the 'message_content' intent.
import asyncio
import time
from tarot import tarot_reading

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

        if message.content in nexhi_reactions and message.author.id == 206097643934449665:
            time.sleep(3)
            await message.reply("Someone likely said something so unbelievable "
                                "that Nexhi is at a loss for words. This isn't a good thing, btw.")

        if message.content == message.content.upper() and len(
                message.content) >= 14 and message.author.id == 206097643934449665:
            await message.reply("Calm the caps down, Nexhi.")
            await message.delete()

        if message.content in illegal_works:
            await message.delete()

        print(f'Message from {message.author}: {message.content}')

        if message.content == "Tarot Reading Navik":
            # For now, it'll only draw a single card.
            await message.reply(tarot_reading(1))


client = MyClient(intents=intents)
client.run(token)
