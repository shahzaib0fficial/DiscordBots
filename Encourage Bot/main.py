import discord
import requests
import json

intents = discord.Intents.all()

client = discord.Client(intents=intents)

sadWords = ['joke', 'sad', 'depressed', 'unhappy', 'miserable', 'gloomy', 'heartbroken', 'tearful', 'melancholy', 'despair', 'lonely']

def randomJoke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        jsonData = json.loads(response.text)
        joke = jsonData["setup"] + "\n" + jsonData["punchline"]
        return joke
    else:
        return "Sorry there is a bit issue with fetching joke we'll fix soon"

def randomQuote():
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        jsonData = json.loads(response.text)
        quote = jsonData[0]["q"] + "\n-" + jsonData[0]["a"]
        return quote
    else:
        return "Sorry there is a bit issue with fetching quote we'll fix soon"

@client.event
async def on_ready():
    print("{0.user}".format(client) + " is running")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.lower().startswith("hello") or message.content.lower().startswith("hi"):
        await message.channel.send("Hi there!")
    
    elif message.content.lower().startswith("inspire"):
        quote =  randomQuote()
        await message.channel.send(quote)
    
    elif any(word in message.content.lower() for word in sadWords):
        joke = randomJoke()
        await message.channel.send(joke)

    

file = open("data.json","r")

data = json.load(file)

Token = data["Token"]

client.run(Token)