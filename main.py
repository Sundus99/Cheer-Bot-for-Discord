#-------------------------------------------------------------------------------
# Name:        Cheer Bot for Discord
# Purpose:     Detect signs of despair by checking if any of the sad words are contained in the message received from the user
#              and cheer user up via jokes, relevant quotes, cat videos, and provide resources for suicide prevention
# Author:      Sundus Yawar
# Student #:   215-028-574
# Created:     2021-06-30
#-----------------------------------------------------------------------------
import discord
import os
import requests
import json
import random
#===========variables============================
client = discord.Client()
sad_words = ["sad","upset","depressed","depressing","anxiety","anxious","hopeless","failed","fail","failure","lost","unhappy","angry","miserable"]
funny_videos = ["https://www.youtube.com/watch?v=ByH9LuSILxU", "https://www.youtube.com/watch?v=vLDcCvCJ8bM","https://www.youtube.com/watch?v=pOmu0LtcI6Y"]
hope_quotes = ["Hope can be a powerful force. Maybe there's no actual magic in it, but when you know what you hope for most and hold it like a light within you, you can make things happen, almost like magic. - Laini Taylor", "When things go wrong, don't go with them. - Elvis Presley", "The bravest thing I ever did was continuing my life when I wanted to die. - Juliette Lewis", "Even in the grave, all is not lost. - Edgar Allan Poe", "One should . . . be able to see things as hopeless and yet be determined to make them otherwise. - F.Scott Fitzgerald", "Don't lose hope. You never know what tomorrow might change. - Laura Chouette", "Sad is not the land with no hero. Sad is the land that needs a hero. - Bertolt Brecht", "Sometimes its hard to see the light at the end of a tunnel. Sometimes you don't even know its there - Campbell Thompson", "When you pray and hope for a change. Don't expect a change to come. Expect the opportunity for a change to come. - Jonathon Anthony Burkett","Never be defined by what has happened to you in the past, it was just a life lesson, not a life sentence. ~ Donald Pillai" , "No matter what happens, as long as you think positively, hopelessness can never touch you! - Mehmet Murat ildan"]
failure_quotes = ["Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill", "There is only one thing that makes a dream impossible to achieve: the fear of failure. - Paulo Coelho", "Failure is the condiment that gives success its flavor. - Truman Capote", "It is hard to fail, but it is worse never to have tried to succeed. - Theodore Roosevelt", "All of old. Nothing else ever. Ever tried. Ever failed. No matter. Try again. Fail again. Fail better. - Samuel Beckett", "Do not let arrogance go to your head and despair to your heart; do not let compliments go to your head and criticisms to your heart; do not let success go to your head and failure to your heart. - Roy T. Bennett", "Only those who dare to fail greatly can ever achieve greatly. - Robert F. Kennedy", "You may be disappointed if you fail, but you are doomed if you don’t try. - Beverly Sills", "You make mistakes, mistakes don't make you - Maxwell Maltz", "Sometimes, when we want something so badly, we fear failure more than we fear being without that thing. - Matthew J. Kirby", "When we give ourselves permission to fail..we at the same time, give ourselves permission to excel. - Eloise Ristad","How much you can learn when you fail determines how far you will go into achieving your goals. - Roy Bennett","I have failed many times, and that's why I am a success. - Michael Jordon", "The man who has done his level best…is a success, even though the world write him down a failure. - B. Forbes", "Failure is the sourness that makes success All the more sweeter. - Joshua Wisenbaker", "The moment you believe you will fail, you have already lost the battle. - Bianca Frazier"]
#===========requests=============================
def get_quote():
	response = requests.get("https://zenquotes.io/api/random")#zenquotes is a quotes api
	#converting response into json
	json_data = json.loads(response.text)
	print(json_data)
	quote = json_data[0]['q'] + " -" + json_data[0]['a']# key q contains quote from the api and key a contains the name of the author
	return(quote)

def get_joke():
	response2 = requests.get("https://official-joke-api.appspot.com/random_joke")
	json_data2 = json.loads(response2.text)
	print(json_data2)
	joke = "Setup: "+ json_data2['setup'] + "\nPunchline: " + json_data2['punchline']
	return(joke)
#============Discord=============================
@client.event

async def on_ready():#when the bot is ready
	print('we have logged in as {0.user}'.format(client))


@client.event

async def on_message(message):#these func are from the discord library
	if message.author == client.user:#if the message is from the bot do nothing
		return

	if message.content.startswith('hello') or message.content.startswith('hi') or message.content.startswith('Hello') or message.content.startswith('Hi'):
		await message.channel.send('Hello! How are you feeling today?')

	if message.content.startswith('inspire'):
		quote = get_quote()
		await message.channel.send(quote)

	if sad_words[0] in message.content or sad_words[1] in message.content:
		await message.channel.send("Allow me to cheer you up with a joke!")
		joke = get_joke()
		await message.channel.send(joke)

	if sad_words[2] in message.content or sad_words[3] in message.content or sad_words[4] in message.content or sad_words[5] in message.content:
		await message.channel.send("You're not alone. I may not understand exactly how you feel, but you're not alone")
		e = discord.Embed(title="There there")
		e.set_image(url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/0e44ab3f-a9dc-4693-86b5-cba1ff8a9ef8/d863gzq-71e41b18-1df5-4d2b-b09b-b1d20179f67e.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvMGU0NGFiM2YtYTlkYy00NjkzLTg2YjUtY2JhMWZmOGE5ZWY4XC9kODYzZ3pxLTcxZTQxYjE4LTFkZjUtNGQyYi1iMDliLWIxZDIwMTc5ZjY3ZS5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.HIyNCC7QhFON8w6dlUl2sg4u87zg6_cenA_xO4jrSkQ")
		e.set_thumbnail(url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/0e44ab3f-a9dc-4693-86b5-cba1ff8a9ef8/d863gzq-71e41b18-1df5-4d2b-b09b-b1d20179f67e.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvMGU0NGFiM2YtYTlkYy00NjkzLTg2YjUtY2JhMWZmOGE5ZWY4XC9kODYzZ3pxLTcxZTQxYjE4LTFkZjUtNGQyYi1iMDliLWIxZDIwMTc5ZjY3ZS5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.HIyNCC7QhFON8w6dlUl2sg4u87zg6_cenA_xO4jrSkQ")
		await message.channel.send(embed=e)
		await message.channel.send("Please allow me to distract you with cute and funny cat videos. Hope it makes you feel better.")
		await message.channel.send(random.choice(funny_videos))

	if sad_words[6] in message.content:
		await message.channel.send(random.choice(hope_quotes))

	if sad_words[7] in message.content or sad_words[8] in message.content or sad_words[9] in message.content or sad_words[10] in message.content:
		await message.channel.send(random.choice(failure_quotes))	

	if "suicide" in message.content or "take my life" in message.content or "don't want to live" in message.content:
		await message.channel.send("https://www.crisisservicescanada.ca/en/share-your-story/")
		await message.channel.send("https://www.crisisservicescanada.ca/en/thinking-about-suicide/")
		await message.channel.send("Even if you may not think so at this moment, your life IS precious. \nPlease call 1-833-456-4566 they are available 24/7 to hear you out. \n You can also send a text to 45645 between 4PM to Midnight ET. \n See their website for Stories of hope under Resources. \nThis help line has saved many lives and it will save yours. \n They are there for you! \n Talking to them will help reduce stress and bring you relief.")

#run the bot
#client.run(os.getenv('TOKEN'))#put bot token
client.run('TOKEN')