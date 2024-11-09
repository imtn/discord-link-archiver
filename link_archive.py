import discord
from dotenv import load_dotenv
import logging
import os

logger = logging.getLogger(__name__)
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if '$tnt' in message.content:
        await message.channel.send('Bot says hello!')


def main():
    if client_token := os.getenv('CLIENT_TOKEN'):
        print(f"client token is >{client_token}< and str form is >{str(client_token)}<")
        client.run(str(client_token))
    else:
        logger.error("CLIENT_TOKEN not found in env file.")

if __name__ == '__main__':
    main()
