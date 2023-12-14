import discord
import responses
import json

def readHidden(file_path="hidden.json"):
    with open(file_path, "r") as file:
        hidden = json.load(file)
    return hidden

hidden = readHidden()
botToken = hidden["botToken"]

async def sendMessage(message,userMessage,isPrivate):
    try:
        response = responses.handleUserResponse(userMessage)
        await message.author.send(response) if isPrivate else await message.channel.send(response)
    except Exception as e:
        print(e)

def runDiscordBot():

    # Create an instance of Intents
    intents = discord.Intents.all()
    
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        userName = str(message.author)
        userMessage = str(message.content)
        channel = str(message.channel)

        print(f"{userName} said : '{userMessage}' in '{channel}' channel")
        
        if userMessage[0] == "?":
            userMessage = userMessage[1:]
            await sendMessage(message, userMessage,isPrivate=True)
        else:
            await sendMessage(message, userMessage,isPrivate=False)

    client.run(botToken)