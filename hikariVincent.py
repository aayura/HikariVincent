import hikari
import lightbulb
import random
from webserver import keep_alive

bot = lightbulb.BotApp(token='OTI4MzI1NDMzMjE5NTA2MjA3.YdXIbg.aQ76mc74LLk3xWhCbr_SQm5FDUU', default_enabled_guilds = (733198740348731442))

@bot.listen(hikari.StartedEvent)
async def on_started(event):
  print("Bot is ready, go get them tiger!")


@bot.command
@lightbulb.command('test', 'Testing commands.')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def testing_commands(ctx):
  pass

@testing_commands.child
@lightbulb.command('ping', 'Says Pong!')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def ping(ctx):
  await ctx.respond("Pong!")

@bot.command
@lightbulb.command('gamble', 'Gambling commands.')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def gambling_commands(ctx):
  pass

@gambling_commands.child
@lightbulb.command('toss', 'toss a coin!')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def toss(ctx):
  outputs = ('Heads', 'Tails')
  outputs = random.choice(outputs)
  await ctx.respond(f'{ctx.author.mention}, The call is {outputs}.')

keep_alive()
bot.run()
