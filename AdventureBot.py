import discord
import asyncio

TOKEN = open('.advtoken').readline()
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

	if message.channel.name == CHANNEL and message.author.id != client.user.id:
	
		print('message detected:\n- message channel name: "{}"\n- message channel id: "{}"\n- author account name: "{}"\n- author display name: "{}"\n- author ID: "{}"\n- message content: "{}"'.format(
				message.channel.name, message.channel.id, message.author.name, message.author.display_name, message.author.id, message.content))

		if message.content == 'advbot_clean':

			print('deleting...')

			async for log in client.logs_from(message.channel):
				if log.author.id == client.user.id:
					print('- found message: {}'.format(log.content))
					await client.delete_message(log)

		elif message.content == 'advbot_nuke':

			await client.send_message(message.channel, 'Are you sure? (y/n)')
		
			ans = await client.wait_for_message(timeout=10, author=message.author, channel=message.channel)
			if ans != None and ans.content == 'y':
				
				messages = []
				async for log in client.logs_from(message.channel):
					messages.append(log)
				print('deleting all messages')
				await client.delete_messages(messages)

				# Run a second time to clear older messages
				asyncio.sleep(3)
				async for log in client.logs_from(message.channel):
					if log != None:
						print('clearing additional messages')
						await client.delete_message(log)

			else:
				await client.send_message(message.channel, 'Nuke cancelled.')

		else:

			await client.send_message(message.channel, 'message detected:\n- message channel name: "{}"\n- message channel id: "{}"\n- author account name: "{}"\n- author display name: "{}"\n- author ID: "{}"\n- message content: "{}"'.format(
			message.channel.name, message.channel.id, message.author.name, message.author.display_name, message.author.id, message.content))

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