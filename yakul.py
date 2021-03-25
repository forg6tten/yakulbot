import random
import json 
import requests
import aiohttp
import discord
from discord import Game, Embed, Color, Status, ChannelType
from discord.ext import commands
from discord.ext.commands import Bot
from bs4 import BeautifulSoup
with open("config.json", "r") as h:
    config = json.load(h)

client = Bot(command_prefix=commands.when_mentioned_or(config['prefix']))
client.remove_command('help')
reddit = praw.Reddit(client_id='REDACTED', 
                     client_secret='REDACTED',
                     user_agent='used for discord')


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.command(pass_context= True)
async def marco(ctx):
    t = await client.say('Polo!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await client.edit_message(t, new_content='Polo! It took me {}ms to recieve t"\
                              "hat but other than that it seems the castle is up"\
                              "and running :smile: :fire:'.format(int(ms)))

@client.command(pass_context=True)
async def saveme(ctx):
    await client.say(embed=Embed(description="**HAVE NO FEAR!! CAUSE I AM HERE**",
                                 set_image="https://bit.ly/2GenQV2",
                                 color=Color.gold()))

@client.command(pass_context=True)
async def zr(ctx):
    await client.say(embed=Embed(description="**DO A BARRELL ROLL**",
                                 set_image="https://bit.ly/2Io2aHz",
                                 color=Color.gold()))

@client.command(pass_context=True, aliases=['em', 'e'])
async def embd(ctx, *args):
    colors = {
       "red": Color.red(),
        "green": Color.green(),
        "gold": Color.gold(),
        "orange": Color.orange(),
        "blue": Color.blue(),
        "purple": Color.purple(),
        "teal": Color.teal(),
        "magenta": Color.magenta(),
        "grey": Color.lighter_grey()
    }
    if args:
        argstr = " ".join(args)
        if "-c " in argstr:
            text = argstr.split("-c ")[0]
            color_str = argstr.split("-c ")[1]
            color = colors[color_str] if color_str in colors else Color.default()
        else:
            text = argstr
            color = Color.default()

            await client.say(embed=Embed(color=color, description=text))
            await client.delete_message(ctx.message)

@client.command(pass_context=True, aliases=['google'])
async def lmgtfy(ctx, *args):
    if args:
        url = "http://lmgtfy.com/?q=" + "+".join(args)
        await client.say(embed=Embed(description="**[Look here!](%s)**" % url,
                                     color=Color.gold()))
    await client.delete_message(ctx.message)

@client.command(pass_context=True, aliases=['ip', 'i'])
async def ifconfig(ctx, arg1):
    url = f"http://ip-api.com/json/{arg1}"
    ip = discord.Embed(
        color=discord.Colour.purple()
    )
    async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            ip.set_author(name="IP Reconnasaince")
            ip.add_field(name="IP", value=response['query'])
            ip.add_field(name="ISP", value=response['isp'])
            ip.add_field(name="Country", value=response['country'])
            ip.add_field(name="State", value=response['region'])
            ip.add_field(name="Area Code", value=response['zip'])
            ip.add_field(name="ASN", value=response['as'])
            await client.say(embed=ip)

@client.command(pass_context=True, aliases=['alphabet'])
async def g(ctx, *args):
    if args:
        url = "https://www.google.com/search?q=" + "+".join(args)
        await client.say(embed=Embed(description="**[Google Search](%s)**" % url,
                                     color=Color.gold()))
    await client.delete_message(ctx.message)

@client.command(aliases=['urba'])
async def ud(*args):
  word = ' '.join(args)
  r = requests.get(f"http://www.urbandictionary.com/define.php?term={word}")
  soup = BeautifulSoup(r.content, features="html.parser")
  x = soup.find("div",attrs={"class":"meaning"}).text
  y = ("*"+x+"*")
  await client.say(y)

@client.command(aliases=['blowjob'])
async def bj():
    nsf = discord.Embed(
        color=discord.Colour.red()
    )
    memes_submissions = reddit.subreddit('BlowjobGifs').hot()
    post_to_pick = random.randint(1, 9999)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
        nsf.set_image(url=submission.url)
    await client.say(embed=nsf)

@client.command(aliases=['bbs'])
async def boobs():
    nsf = discord.Embed(
        color=discord.Colour.red()
    )
    memes_submissions = reddit.subreddit('BoobGifs').hot()
    post_to_pick = random.randint(1, 9999)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
        nsf.set_image(url=submission.url)
    await client.say(embed=nsf)

@client.command(aliases=['cumshot'])
async def cs():
    nsf = discord.Embed(
        color=discord.Colour.red()
    )
    memes_submissions = reddit.subreddit('CumShotGifs').hot()
    post_to_pick = random.randint(1, 9999)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
        nsf.set_image(url=submission.url)
    await client.say(embed=nsf)

@client.command(aliases=['b'])
async def nsfw():
    nsf = discord.Embed(
        color=discord.Colour.red()
    )
    memes_submissions = reddit.subreddit('NSFW_Gifs').hot()
    post_to_pick = random.randint(1, 9999)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)
        nsf.set_image(url=submission.url)
    await client.say(embed=nsf)

@client.command(pass_context=True, aliases=['h'])
async def help(ctx):
    m = discord.Embed(
        colour = discord.Colour.teal()
    )
    m.set_author(name="Help")
    m.add_field(name="square/sq",value="*Squares a number*", inline=False)
    m.add_field(name="marco/p", value="*Polo!!!*", inline=False)
    m.add_field(name="embd/e", value="*Embeds given text*", inline=False)
    m.add_field(name="lmgtfy/l", value="*Generates a lmgtfy link*",
                inline=False)
    m.add_field(name="ifconfig/ip", value="*Gives Info on given IP*",
                inline=False)
    m.add_field(name="g/google", value="*Creates google search link*",
                inline=False)
    m.add_field(name="ud/urban", value="*Searches UrbanDictionary*",
                inline=False)
    m.add_field(name="suggestion/sg",
                value="*Send Your Suggestions to help make the bot better*",
                inline=False)
    m.add_field(name="aes/a",
                value="*Generates a random ａｅｓｔｈｅｔｉｃ image*",
                inline=False)
    m.add_field(name="yums/y",
                value="*Generates a random ａｅｓｔｈｅｔｉｃ food image*",
                inline=False)
    m.add_field(name="finger/u", value="*Displays given users info*")
    m.add_field(name="marry/m", value="*marry your lover*", inline=False)
    m.add_field(name="kill/kl", value="*kill someone*", inline=False)
    m.add_field(name="punch/pn", value="*punch someone*", inline=False)
    m.add_field(name="kiss/ks", value="*Kiss your lover*", inline=False)
    m.add_field(name="clear/c", value="*Clears the bots messages*")
    m.add_field(name="fuck/f", value="*reproduce*", inline=False)
    m.add_field(name="btc/s", value="*Gives current price for bitcoin*",
                inline=False)
    m.add_field(name="adv/aa", value="*Gives Random Bits Advice*", inline=False)
    m.add_field(name="bj/blowjob", value="*Random Blowjob Gifs*", inline=False)
    m.add_field(name="boobs/bbs", value="*Random Boob Gifs*", inline=False)
    m.add_field(name="cs/cumshot", value="*Random Cumshot Gifs*", inline=False)
    m.add_field(name="nsfw/b", value="*Random NSFW Gifs*", inline=False)
    await client.say(ctx.message.author, embed=m)

@client.command(pass_context=True, aliases=['sg'])
async def suggestion(ctx, *args):
    argstr = " ".join(args)
    text = argstr
    suggestionsFile = open("suggestions.txt", "a+")
    suggestionsFile.write(text + "\n")
    msg = f"{ctx.author.mention} Added your suggestion! It will be processed and m"\
    "ay be added soon! Thanks for the help!"
    await client.say(msg)

@client.command(pass_context=True, aliases=['aa'])
async def adv(ctx):
  await client.say(random.choice(tuple(config['advice'])))
  await client.delete_message(ctx.message)

@client.command(pass_context=True, aliases=['a'])
async def aes(ctx):
    inbed = discord.Embed(
        colour=discord.Colour.purple()
    )
    inbed.set_image(url=random.choice(tuple(config['aes'])))
    await client.say(embed=inbed)
    await client.delete_message(ctx.message)

@client.command(pass_context=True, aliases=['y'])
async def yums(ctx):
    yummy = discord.Embed(
        colour=discord.Colour.dark_green()
    )
    yummy.set_image(url=random.choice(tuple(config['yum'])))
    yummy.set_footer(text="images thanks to ***cami the marshmallow***")
    await client.say(embed=yummy)
    await client.delete_message(ctx.message)

@client.command(pass_context=True, aliases=['pn'])
async def punch(ctx, member: discord.Member):
    if member.mention == ctx.message.author.mention:
        pnc = discord.Embed(
          colour=discord.Colour.blue()
        )
        pnc.set_image(url=config['punch'])
        await client.say(ctx.message.author.mention, embed=pnc)
        await client.delete_message(ctx.message)
    else:
        await client.say(f"{member.mention} got knocked the fuck out \
                         by {ctx.message.author.mention}")
    await client.delete_message(ctx.message)

@client.command(pass_context=True, aliases=['kl'])
async def kill(ctx, member: discord.Member):
    if member.mention == ctx.message.author.mention:
        await client.say(f"{ctx.message.author.mention} Committed seppuku")
        await client.delete_message(ctx.message)
    else:
        await client.say(f"{member.mention} was killed \
                         by {ctx.message.author.mention}"
    await client.delete_message(ctx.message)

@client.command(pass_context=True, aliases=['ks'])
async def kiss(ctx, member: discord.Member):
    await client.say(f"{member.mention} was kissed \
                     by {ctx.message.author.mention}")
    await client.delete_message(ctx.message)

@client.command(pass_context=True, aliases=['f'])
async def fuck(ctx, member: discord.Member):
    if member.mention == ctx.message.author.mention:
        await client.say("You cant fuck yourself...your dicks too small")
        await client.delete_message(ctx.message)
    else:
        await client.say(f"{member.mention} got their pussy filled, \
                         screws loosened, with cum \
                         by {ctx.message.author.mention}, the sex god")
    await client.delete_message(ctx.message)

client.marriage_active = False
@client.command(pass_context=True, aliases=['m'])
async def marry(ctx, member: discord.Member):
    mg = discord.Embed(
        colour=discord.Colour.dark_green()
    )
    mg.set_image(url="https://bit.ly/2OZ16eD")
    if client.marriage_active:
        return  
    client.marriage_active = True
    await client.say(f"{member.mention} wanna get married \
                     to {ctx.message.author.mention}?")
    reply = await client.wait_for_message(author=member,
                                          channel=ctx.message.channel,
                                          timeout=30)
    if not reply or reply.content.lower() not in ("y", "yes", "yeah"):
        await client.say("Too bad, you lose man", embed=mg)
    else:
        await client.say("Mazel Tov!")

    client.marriage_active = False
@client.command(pass_context=True, aliases=['cls', 'c'])
async def clear(ctx):
    async for msg in client.logs_from(ctx.message.channel):
        if msg.author.id == client.user.id:
            try:
                await client.delete_message (msg)
            except:
                pass
    embed = discord.Embed(description="Chat Cleaned! :fire:", color=0x00ff00)
    await client.say (embed=embed)
    await client.delete_message(ctx.message)

@client.command(pass_context=True, aliases=['u'])
async def finger(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.message.author
    roles = [r.name for r in user.roles if r.name != "@everyone"]
    if roles:
        roles = sorted(roles, key=[x.name for x in ctx.message.server.role_hierarchy if x.name != "@everyone"].index)
    else:
        roles = "None"
    print(len(roles))
    if len(roles) > 16:
        roles = "Too much info to show."
    else:
        roles = "   ".join(roles)
    fg = discord.Embed(description=f"finger {ctx.message.author.mention} :", 
                       title="User Info", color=0X008CFF)
    if user.avatar_url:
        fg.set_thumbnail(url=user.avatar_url)
    else:
        fg.set_thumbnail(url=user.default_avatar_url)
    fg.add_field(name="User", value=user.name)
    fg.add_field(name="Discrim", value=user.discriminator)
    if user.nick:
        fg.add_field(name="Nick", value=user.nick)
    else:
        fg.add_field(name="Nick", value="None")
    fg.add_field(name="UserID", value=user.id)
    fg.add_field(name="Stats", value=user.status)
    if user.game:
        fg.add_field(name="Currently Playing", value=user.game)
    else:
        fg.add_field(name="Currently Playing", value="Nothing")
    fg.add_field(name="AFK?", value=user.is_afk)
    fg.add_field(name="Bot?", value=user.bot)
    fg.add_field(name="Muted in the server?", value=user.mute)
    fg.add_field(name="Deafened in the server?", value=user.deaf)
    fg.add_field(name="Joined Discord On", value=user.created_at.strftime("%d %b"\
                                                                          " %Y %H:%M"))
    fg.add_field(name="Joined Server On", value=user.joined_at.strftime("%d %b"\
                                                                        " %Y %H:%M"))
    fg.add_field(name="Highest role color", value=user.color)
    fg.add_field(name="Roles", value=roles)
    await client.say(embed=fg)
client.run(config['token'])
