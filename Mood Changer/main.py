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
    
async def sendMessage(message,userMessage,isPrivate):
    if isPrivate:
        messageDestination = message.author
    else:
        messageDestination = message.channel
        
    if userMessage.startswith("hello") or userMessage.startswith("hi"):
        await messageDestination.send("Hi there!")
    
    elif userMessage.startswith("inspire"):
        quote =  randomQuote()
        await messageDestination.send(quote)
    
    elif any(word in userMessage for word in sadWords):
        joke = randomJoke()
        await messageDestination.send(joke)

    elif userMessage.startswith("commands"):
        await messageDestination.send("1. Hello or Hi\n2. Inspire\n3. Joke\n4. When you are feeling\n  1. sad\n  2. depressed\n  3. unhappy\n  4. miserable\n  5. gloomy\n  6. heartbroken\n  7. tearful\n  8. melancholy\n  9. despair\n  10. lonely\nBot will tell you a joke\n5. commands\n6. use '?' in start to get message in dm")

@client.event
async def on_ready():
    print("{0.user}".format(client) + " is running")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    userName = str(message.author)
    userMessage = str(message.content)
    channel = str(message.channel)

    userMessage = userMessage.lower()
    if userMessage[0] == "?":
        userMessage = userMessage[1:]
        await sendMessage(message,userMessage,isPrivate=True)
    else:
        await sendMessage(message,userMessage,isPrivate=False)

    

file = open("data.json","r")

data = json.load(file)

Token = data["Token"]

client.run(Token)