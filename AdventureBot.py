import discord
import asyncio

TOKEN = 'NDg5MTEzOTE1MTYzMjc5Mzcx.DnmM2A.8np5scfrdhim91QCseqj1sp3pLk'
CHANNEL = 'land-of-adventure'

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
	print('message detected:\n- message channel: "{}"\n- message content: "{}"'.format(message.channel.name, message.content))

	if message.channel.name == CHANNEL:
		await client.send_message(message.channel, 'Detected message in channel {}: {}'.format(message.channel.name, message.content))

#	if message.content.startswith('_test'):
#		counter = 0
#		tmp = await client.send_message(message.channel, 'Calculating messages...')
#		async for log in client.logs_from(message.channel, limit=100):
#			if log.author == message.author:
#				counter += 1
#
#		await client.edit_message(tmp, 'You have {} messages.'.format(counter))
#	elif message.content.startswith('_sleep'):
#		await client.send_message(message.channel, 'Sleeping...')
#		await asyncio.sleep(5)
#		await client.send_message(message.channel, 'Done sleeping')

client.run(TOKEN)