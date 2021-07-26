import os
import pickle
import discord
from dotenv import load_dotenv
import requests
import json
import random
# from neuralintents import GenericAssistant


# bot = GenericAssistant('intents.json')
# bot.train_model()
# bot.save_model()
bot = pickle.load(open("assistant_model_words.pkl", 'rb'))

client = discord.Client()
load_dotenv()
TOKEN = os.getenv("TOKEN")

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


@client.event
async def on_messages(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("$bot"):
        response = bot.request(message.content[4:])
        await message.channel.send(response)
    
    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)


print("Bot is running ... ")
client.run(TOKEN)
