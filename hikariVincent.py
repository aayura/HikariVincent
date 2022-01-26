import hikari
import lightbulb
import random
import os
from webserver import keep_alive

my_secret = os.environ['DISCORD_BOT_TOKEN']
bot = lightbulb.BotApp(
    token=my_secret, default_enabled_guilds=(733198740348731442))


@bot.listen(hikari.StartedEvent)
async def on_started(event):
  print("Bot is ready, go get them tiger!")


@bot.listen(hikari.MessageCreateEvent)
async def on_message(event):
  await event.message.respond(f"{event.message.author.mention} You typed a message!")


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
