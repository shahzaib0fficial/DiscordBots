import random

data = {}

def handleUserResponse(message):
    
    #converting user message to lower case

    userMessage = message.lower()

    if userMessage == "hello":
        return "Hello I am a Bot created by shahzaibofficial!"
    
    if userMessage == "random":
        return str(random.randint(1,6))
    
    if userMessage == "commands":
        return "1. hello\n2. random\n3. commands\n4. use '?' to get private messages"