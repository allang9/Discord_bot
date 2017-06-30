import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def bitch(*target : str):
	members = bot.get_all_members();
	member_name = ' '.join(target)
	target_mem = None
	for member in members:
		if (not str(member).find(member_name)):
			target_mem = member

	if (target_mem is not None):
		await bot.send_message(target_mem, "you a bitch")
	else:
		await bot.say('no member found by the name of ' + str(member_name))



bot.run('MzI4Mjc3OTExMzIzMDE3MjE3.DDBkLA.-g1gqxBhl_EGicQMr2VsJfL3T34')