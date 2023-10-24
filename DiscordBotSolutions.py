import discord
from discord.ext import commands
from urllib.request import urlopen
import pyttsx3

TOKEN = "TOKEN"  #insert your Token that you copied from Discord

# Key Variable declarations
# What are intents? intents involve what the bot can and can't do 
intent = discord.Intents.default() # Default intants set
intent.message_content = True

# Creating a Client/Command Instance (prefix +Function Name)
Bot = commands.Bot(command_prefix="%", intents= intent)
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
    print("!!BLANK print statement!!")
    # insert the print statement of your choice

'''
Description: called when a command is called (you can choose the command that calls the bot)
Parameters: ctx (context) : Represents the context in which a command is being invoked under.
Returns: no return value
'''    
@Bot.command(name="TEST", pass_context = True)
async def Call(ctx):
    await ctx.send("Function Call works!")
    

# Challenge 2: Bot Commands
'''
We are going to let our Bot be capable of getting 
in and out of voice channels at our command
'''  

'''
Description: allows Bot to join a Voice Channel
Parametrs:
    (1)ctx: short for context
Returns: no return value
'''
@Bot.command(name="VON", pass_context = True)
async def VoiceOn(ctx):
    # check if the ctx.author.voice is true (that you are in the voice channel)
    if(ctx.author.voice):
        # check if Bot is already in the channel
        voice = discord.utils.get(Bot.voice_clients, guild=ctx.guild) #Obtain Voice Object
        #A Bot with no channel will have None as its object (by default)
        if(voice == None):
            channel = ctx.author.voice.channel #Name of the Channel 
            #Use the ctx.send() to let the bot say something when it gets in
            await ctx.send("Voice ON")
            await channel.connect() #connects to the voice channel
        else:
            #use the ctx.send() to let the bot say an error message
            await ctx.send("Error!")
            #return "DELETE ME when you when in the blanks" 
            
        
    else:
        #use the ctx.send() to let the bot say an error message
        await ctx.send("Error!")
        return "DELETE ME when you when in the blanks"   

'''
Description: allows Bot to leave a Voice Channel
Parametrs:
    (1)ctx: short for conetxt
Returns: no return value
'''
@Bot.command(name="VOFF",pass_context = True)
async def VoiceOff(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect() #disconnects from the voice channel
         #Use the await ctx.send() to let the bot say something when it gets out
        await ctx.send("Voice OFF")
    else:
        #use the await ctx.send() to let the bot say an error message   
        await ctx.send("Error!")
        #return "DELETE this line when you fill in the blanks"

# Challenge 3: Adding Voice Output
'''
Using the pyttsx3 library, we will let the Bot produce a voice 
output.The following lines will be used:
    engine = pyttsx3.init() #constructor(Already done for you above)
    engine.say("text the Bot will say) #outputs the text as voice
    engine.runAndWait() # Blocks while processing all currently queued commands(should be at the end).
'''
@Bot.command(name="TALK",pass_context = True)
async def VoiceCommand(ctx):
    #Fill in the with the voice commands from above
    engine.say("say soemthing")
    engine.runAndWait()
    #return "DELETE ME when you when in the blanks"

'''
Description: allows Bot to say something
Parametrs:
    (1)ctx: short for conetxt
    (2)message: words the Bot will say
Returns: no return value
'''
@Bot.command(name="MESSAGE",pass_context = True)
async def VoiceCommand2(ctx, message):
    #Fill in the with the voice commands from above
    
    engine.say(message)
    engine.runAndWait()
    return "DELETE ME when you when in the blanks"      
    
    return "DELETE this line when you fill in the blanks"



''' 
!! Extra: Try implementing these voice commands to the previous commands such 
    that it would give both a tetx and voice output!!        
'''

# Challenge 4 : Functions 
'''
We are going to let Discord-Bot tell 
us the temperature of any city we give it.
In doing so, we are going to use the function
declared below
'''

#Helper Function
'''
Description: obtains the temperature (in Fahrenheit) for a designated city
Parametrs:
    (1) city: city name (with no spaces in between: ex: LosAngeles)
Returns:
    (1) tempC: a string consisting of the city's temperature

'''
def get_temperature(city):
    # We will be using the urllib functions
    url = "http://wttr.in/"+city+"?format=%t"
    # We are going to use the urlopen(url) function to obtain the url
    URLPage = urlopen(url)
    # We wll use the .read() on the URLPage 
    page = URLPage.read() 
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
    if message.author == Bot.user:
        return
    
    # check if the command for temperature is called
    if(message.content.startswith("TEMP")):
        if(message.content == "TEMP"):
            await message.channel.send("Please input a city")
            return 
        daily_forecast = get_temperature(message.content.split("TEMP ", 1)[1])
        await message.channel.send(message.content.split("TEMP ", 1)[1]+":"+ daily_forecast) #Bot-output statement
    # Must be the same command in the if-statement
    
    ''' !! Extra: based on the previous if-statement, see if you can write an if statement where
        the bot replies to you when you say thank you !!
        
    '''
    
    # This is the command allows the bot to continue receiving messages ; DO NOT TOUCH IT
    await Bot.process_commands(message)


    
# This is the command that starts the bot; DO NOT TOUCH IT
# There is also a DiscordBot Debugger that is opened as well
Bot.run(TOKEN)
