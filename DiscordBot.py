import discord
import logging
from discord.ext import commands
from urllib.request import urlopen
import pyttsx3

TOKEN = "!! your token!!"  #insert your Token that you copied from Discord

# Key Variable declarations
handler= logging.FileHandler(filename='discord.log', encoding = 'utf-8', mode = 'w')

# What are intents? intents involve what the bot can and can't do 
intent = discord.Intents.default() # Default intants set
intent.message_content = True

# Creating a Client/Command Instance (prefix +Function Name)
Bot = commands.Bot(command_prefix=' !!put your prefix of choice here!! ', intents= " !!put the intent variable here!! ")
#Fill in the Blanks above 
engine = pyttsx3.init() #constructor for the Voice Output


# Challenge 1: Booting up the DiscordBot
'''
Description: called when Bot is ready (you can choose what the program to print)
Parameters:no parameters
Returns: no return value
'''
@Bot.event
async def on_ready():
    print("!!put your print statement!!")
    # insert the print statement of your choice

'''
Description: called when a command is called (you can choose the command that calls the bot)
Parameters: ctx (context) : Represents the context in which a command is being invoked under.
Returns: no return value
'''    
@Bot.command(name="!! put your command !!", pass_context = True)
async def Call(ctx):
    await ctx.send("Function Call works!")
    
# Challenge 2 : Functions 
'''
We are going to let Discord-Bot tell 
us the temperature of any city we give it.
In doing so, we are going to use the function
declared below
'''

#Helper Function
'''
Description: obtains the temperature (in Celsius) for a designated city
Parametrs:
    (1) city: city name (with no spaces in between: ex: LosAngeles)
Returns:
    (1) tempC: a string consisting of the city's temperature

'''
def get_temperature(city):
    # We will be using the urllib functions
    url = "http://wttr.in/"+"!!Put in the argument!!"+"?format=%t"
    # We are going to use the urlopen(url) function to obtain the url
    URLPage = "!! put the function here !!"
    # We wll use the .read() on the URLPage 
    page = "!! put the read method here !!" 
    tempC = page.decode("utf-8")
    return tempC

#Bot Function
'''
Description: called when particular discord messages are seen
Parametrs:
    (1)message: the user input creating event
Returns: no return value
'''

@Bot.event
async def on_message(message):
    ''' !! Create an if-statement where if message.author'
    is equal to Bot.user, it returns nothing '''
    
    # check if the command for temperature is called
    if(message.content.startswith == "!! fill in your desired command !!"):
        daily_forecast = get_temperature(message.content.split("!! same command here!! ", 1)[1])
        await message.channel.send(message.content.split("!! and here!!  ", 1)[1]+":"+ daily_forecast) #Bot-output statement
    # Must be the same command in the if-statement
    
    ''' !! Extra: based on the previous if-statement, see if you can write an if statement where
        the bot replies to you when you say thank you !!
        
    '''
    
    # This is the command allows the bot to continue receiving messages ; DO NOT TOUCH IT
    await Bot.process_commands(message)

# Challenge 3: Bot Commands
'''
We are going to let our Bot be capable of getting 
in and out of voice channels at our command
'''  

'''
Description: allows Geno to join a Voice Channel
Parametrs:
    (1)ctx: short for context
Returns: no return value
'''
@Bot.command(name="!! fill in your desired command !!", pass_context = True)
async def VoiceOn(ctx):
    # check if the ctx.author.voice is true (that you are in the voice channel)
    if("!!Fill in the blanks!!"):
        channel = ctx.author.voice.channel
        await channel.connect() #connects to the voice channel
        #Use the ctx.send() to let the bot say something when it gets in
    else:
        #use the ctx.send() to let the bot say an error message
        return "DELETE ME when you when in the blanks"   

'''
Description: allows Geno to leave a Voice Channel
Parametrs:
    (1)ctx: short for conetxt
Returns: no return value
'''
@Bot.command(name="!! fill in your desired command !!",pass_context = True)
async def VoiceOff(ctx):
    # check if the ctx.author.voice is true (that you are in the voice channel)
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect() #disconnects from the voice channel
         #Use the ctx.send() to let the bot say something when it gets out
    else:
       #use the ctx.send() to let the bot say an error message   
       return "DELETE ME when you when in the blanks"

# Challenge 4: Adding Voice Output
'''
Using the pyttsx3 library, we will let the Bot produce a voice 
output.The following lines will be used:
    engine = pyttsx3.init() #constructor(Already done for you)
    engine.say("text the Bot will say) #outputs the text as voice
    engine.runAndWait() # Blocks while processing all currently queued commands(should be at the end).
 
'''
@Bot.command(name="!! fill in your desired command !!",pass_context = True)
async def VoiceCommand(ctx):
    #Fill in the with the voice commands from above
    return "DELETE ME when you when in the blanks"



''' 
!! Extra: Try implementing these voice commands to the previous commands such 
    that it would give both a tetx and voice output!!        
'''
    
# This is the command that starts the bot; DO NOT TOUCH IT
# There is also a DiscordBot Debugger that is opened as well
Bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)
