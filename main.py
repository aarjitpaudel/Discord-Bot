import discord
import asyncio
import json
import os
from webserver import keep_alive
from discord.ext import commands, tasks
from itertools import *
import random
import aiohttp
import string
from discord.utils import get
import urllib.parse, urllib.request, re
import wikipedia
import datetime
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import io
from io import BytesIO
import requests

run = True
intents = discord.Intents.default()
intents.members = True



owner_id = 778819230815748118
prefixes="y."
#prefix is '+'
client = commands.Bot(command_prefix = prefixes, intents = intents)

    
    
client.remove_command('help')
     
    
@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game())
    

@client.command()
async def load(ctx, extension):
      client.load_extension(f'cogs.{extension}')
      return

@client.command()
async def unload(ctx, extension):
        client.unload_extension(f'cogs.{extension}')
        return

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
#rules commands



#welcomming member command
@client.command(aliases=['wel'])
async def welcome(ctx, member : discord.Member):
    wel_embed = discord.Embed(
    	title = f'yay you made it to this server {member}',
        description = f'Welcome to this server {member} , Have an amazing time here!',
        colour = discord.Colour.green()
    )
    
    await ctx.send(embed=wel_embed)


#MODERNATION COMMANDS

#purging and clearing message

my_secret = os.environ['DISCORD_BOT_SECRET']

my_secret = os.environ['DISCORD_BOT_SECRET']
@client.command(aliases=['purge'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
    if amount < 100:
        await ctx.channel.purge(limit = amount)
        await ctx.send(f'```{amount} messages were purged```')
    else:
        await ctx.send('100 is max purge limit :)')


#kicking command
@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *,reason=None):
    if reason == None:
        reason = 'no reason'
    else:
        reason = reason
    await member.kick(reason=reason)
    await ctx.send(f'```Relif!!! {member} is kicked for {reason} wow server seems clean! ```')

    
#baning member 
@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *,reason = "No reason"):
    await member.ban(reason = reason)
    await ctx.send(f'```Relif!!! {member} is banded for {reason} wow server seems clean! ```')

#muteing member

@client.command(aliases=['inv'])
async def invite(ctx):
    await ctx.send("http://bit.ly/yantra_Bot")
    


@client.command()
async def kiss(ctx, member : discord.Member):
    embed = discord.Embed(
    	title = f'you are kissing! {member}',
        discription = 'this is discription',
        colour = discord.Colour.blue()
    )
    
    embed.set_footer(text='congluration you kissed someone!')
    embed.set_image(url='https://media1.giphy.com/media/Chv54N5jOjeog/giphy.gif')
    
    await ctx.send(embed=embed)

    
@client.command()
async def hug(ctx, member : discord.Member):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/animu/hug") as r:
                data = await r.json()
                emb3 = discord.Embed(description = f"{ctx.author.mention} hugs {member.mention}")
                emb3.set_image(url=data['link'])
                emb3.set_footer(text = "Powered By - some-random-api.ml")

                await ctx.send(embed = emb3)

@client.command()
async def kill(ctx, member : discord.Member):
    embed = discord.Embed(
    	title = f'yay succesfully killed {member}',
        discription = 'kiled ;-;',
        colour = discord.Colour.blue()
    )
    
    embed.set_footer(text='congluration you killed some one but police are comming run!')
    embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIcgG6YQriOCSGamul38Vf97MVwP0Qus-IgA&usqp=CAU')
    
    await ctx.send(embed=embed)

@client.command()
async def punch(ctx, member : discord.Member):
    embed = discord.Embed(
    	title = f'yay succesfully punched {member}',
        description = 'punched yay',
        colour = discord.Colour.blue()
    )
    
    embed.set_footer(text='congluration you punched but that person is back to take revenge run!')
    embed.set_image(url='https://media1.giphy.com/media/SsUev4H3S7k7HZ5OI4/giphy.gif')
   
    
    await ctx.send(embed=embed)

@client.command()
async def cry(ctx):
    embed = discord.Embed(
    	title = 'sad moment you are crying',
        discription = ';-;',
        colour = discord.Colour.blue()
    )
    
    embed.set_footer(text='sad you are crying be happy!')
    embed.set_image(url='https://i.pinimg.com/originals/b2/79/66/b27966140db68d0621628f2309f8a443.gif')
    
    await ctx.send(embed=embed)
      
@client.command()
async def say(ctx, *, question):
    if ctx.author.id == owner_id:
        await ctx.send(f'{question}')
        await ctx.message.delete()
    else:
        await ctx.send("**This Command Is Bot Owner Only Command For Some Days Sorry You Cannot Use It**")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! my ping is `{(client.latency * 1000)}` ms')
        
        
@client.command(aliases=['w'])
@commands.has_permissions(manage_messages = True)
async def warn(ctx, member : discord.Member, *,reason = "No reason"):
    await ctx.send(f'```member was dangerously warned by dangerous moderator for {reason} ```')
    await member.send(f'```member was dangerously warned by dangerous moderator for {reason} :) dont be bad suggestion from me :)```')

@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")
    
    
@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await member.send(f" you have unmutedd from: - {ctx.guild.name}")
    embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
    await member.send(embed=embed)
    await ctx.send(embed=embed)
    
  
@client.command()
async def help(ctx, args=None):
    help_embed = discord.Embed(title='**Yantramanav** Commands Center')
    help_embed.add_field(
        name="My prefix is ```y.``` *Total 50 Commands*",
        value='```All Commands With Catogary: ```',
        inline=False
    )
    help_embed.add_field(
        name="》Staff Mod 9 Commands",
        value="```ban, kick, mute, unban, unmute, clear, warn, nick, slowmode.```",
        inline=False
    )
    help_embed.add_field(
        name='》Fun 7 Commands',
        value='```kiss, hug, cry, kill, punch, givenitro, snipe.```',
        inline=False
    )
    help_embed.add_field(
        name='》Informative 13 Commands',
        value='```add, subtract, multiplication, divide, about, invite, help, about, ping, avatar, serverinfo, servers, yt. ```',
        inline=False
        )
    help_embed.add_field(
        name='》Facts 7 Commands',
        value='```dog, cat, panda, fox, bird, koala, 8ball```',
        inline=False
    )
    help_embed.add_field(
        name='》Images 9 Commands',
        value='```wanted, rip, dogimage, catimage, pandaimage, redpanda, birdimage, foximage, koalaimage```',
        inline=False
    )
    help_embed.add_field(
        name = '》Others 3 Commands and more comming',
        value='```welcome, say, motivate.```',
        inline = False
    )
    help_embed.add_field(
        name = '》Bot Owner Only 2 Commands :)',
        value='```dm, logout```',
        inline = False
    )
    help_embed.add_field(
        name = '》Bot`s Invite Link And Support Server',
        value='http://bit.ly/yantra_bot\n https://aarjit.ml',
        inline = False
    )

    await ctx.message.add_reaction('✔')
    try:
        await ctx.send(embed=help_embed)
    except:
        await ctx.author.send(embed=help_embed)
    
@client.command()
async def add(ctx, a: int, b:int):
    await ctx.send(f'```result is {a+b}```')
    
@client.command(aliases=['sub'])
async def subtract(ctx, a: int, b:int):
    await ctx.send(f'```result is {a-b}```')
    
@client.command(aliases=['multi'])
async def multiply(ctx, a: int, b:int):
    await ctx.send(f'```result is {a*b}```')
    
@client.command(aliases=['div'])
async def divide(ctx, a: int, b:int):
    await ctx.send(f'```result is {a/b}```')
    
@client.command(aliases=['av'])
async def avatar(ctx, user : discord.Member=None):
    if user == None:
        user = ctx.message.author
    userAvatarUrl = user.avatar_url
    await ctx.send('`Take it `')
    await ctx.send(userAvatarUrl)


@client.command(aliases=['info', 'version'])
async def about(ctx):
    info_embed = discord.Embed(title="Yantramanav Info")
    info_embed.add_field(
        name = '》Bot Info:',
        value = '`This Bot Is Made By` **Aarjit Paudel** `do y.help for seeing whole`',
        inline = False
    )
    info_embed.add_field(
        name = '》Last Update:',
        value = '`Yt command made nsfw channel only for some days/working on NEPSE command`',
        inline = False
    )
    info_embed.add_field(
        name = '》Version:',
        value = '`1.0.6`',
        inline = False
    )
    info_embed.add_field(
        name = '》links:',
        value = "\n `bot invite:` https://bit.ly/yantrabot\n `devloper's Protfolio:` https://aarjit.ml",
        inline = False
    )
    await ctx.send(embed=info_embed)

@client.command()
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")

@client.command(pass_context=True)
@commands.has_permissions(manage_nicknames=True)
async def nick(ctx, member: discord.Member,* ,nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')



@client.command()
async def givenitro(ctx):
  await ctx.send("Take! No Need To Thank Me!")
  await ctx.send("https://media.discordapp.net/attachments/767628261999509544/811917108911800350/fuckoff.png")

@client.command()
async def serverinfo(ctx):

    role_count = len(ctx.guild.roles)
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
    staff_roles = ["Owner", "Head Dev", "Dev", "Head Admin", "Admins", "Moderators", "Community Helpers", "Members"]
        
    embed2 = discord.Embed(timestamp=ctx.message.created_at, color=ctx.author.color)
    embed2.add_field(name='Name', value=f"{ctx.guild.name}", inline=False)
    embed2.add_field(name='Owner', value=f"{ctx.guild.owner}", inline=False)
    embed2.add_field(name='Verification Level', value=str(ctx.guild.verification_level), inline=False)
    embed2.add_field(name='Highest role', value=ctx.guild.roles[-2], inline=False)
    embed2.add_field(name='Contributers:', value="None")

    for r in staff_roles:
        role = discord.utils.get(ctx.guild.roles, name=r)
        if role:
            members = '\n'.join([member.name for member in role.members]) or "None"
            embed2.add_field(name=role.name, value=members)

    embed2.add_field(name='Number of roles', value=str(role_count), inline=False)
    embed2.add_field(name='Number Of Members', value=ctx.guild.member_count, inline=False)
    embed2.add_field(name='Bots:', value=(', '.join(list_of_bots)))
    embed2.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
    embed2.set_thumbnail(url=ctx.guild.icon_url)
    embed2.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed2.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed2)

@client.command()
async def motivate(ctx):
    variable = [
        "“The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty.” – Winston Churchill",
        "“The Best Way To Get Started Is To Quit Talking And Begin Doing.” – Walt Disney",
        '“Don’t Let Yesterday Take Up Too Much Of Today.” – Will Rogers',
        '“You Learn More From Failure Than From Success. Don’t Let It Stop You. Failure Builds Character.” – Unknown',
        '“It’s Not Whether You Get Knocked Down, It’s Whether You Get Up.” – Inspirational Quote By Vince Lombardi',
        '“If You Are Working On Something That You Really Care About, You Don’t Have To Be Pushed. The Vision Pulls You.” – Steve Jobs',
        '“Failure Will Never Overtake Me If My Determination To Succeed Is Strong Enough.” – Og Mandino',
        '“Entrepreneurs Are Great At Dealing With Uncertainty And Also Very Good At Minimizing Risk. That’s The Classic Entrepreneur.” – Mohnish Pabrai',
        '“We May Encounter Many Defeats But We Must Not Be Defeated.” – Maya Angelou',
        '“Knowing Is Not Enough; We Must Apply. Wishing Is Not Enough; We Must Do.” – Johann Wolfgang Von Goethe',
        '“Imagine Your Life Is Perfect In Every Respect; What Would It Look Like?” – Brian Tracy',
        '“We Generate Fears While We Sit. We Overcome Them By Action.” – Dr. Henry Link',
        '“Whether You Think You Can Or Think You Can’t, You’re Right.” – Quote By Henry Ford',
        '“Security Is Mostly A Superstition. Life Is Either A Daring Adventure Or Nothing.” – Life Quote By Helen Keller',
        '“The Man Who Has Confidence In Himself Gains The Confidence Of Others.” – Hasidic Proverb',
        '“The Only Limit To Our Realization Of Tomorrow Will Be Our Doubts Of Today.” – Motivational Quote By Franklin D. Roosevelt',
        '“Creativity Is Intelligence Having Fun.” – Albert Einstein',
        '“What You Lack In Talent Can Be Made Up With Desire, Hustle And Giving 110% All The Time.” – Don Zimmer',
        '“Do What You Can With All You Have, Wherever You Are.” – Theodore Roosevelt'
        ]
    await ctx.send("{}".format(random.choice(variable)))

@client.command()
async def dog(ctx):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/facts/dog") as r:
                data = await r.json()
                await ctx.send(data['fact'] )

@client.command()
async def cat(ctx):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/facts/cat") as r:
                data = await r.json()
                await ctx.send(data['fact'] )

@client.command()
async def panda(ctx):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/facts/panda") as r:
                data = await r.json()
                await ctx.send(data['fact'] )

@client.command()
async def fox(ctx):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/facts/fox") as r:
                data = await r.json()
                await ctx.send(data['fact'] )

@client.command()
async def bird(ctx):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/facts/bird") as r:
                data = await r.json()
                await ctx.send(data['fact'] )

@client.command()
async def koala(ctx):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/facts/koala") as r:
                data = await r.json()
                await ctx.send(data['fact'] )

@client.command()
async def logout(ctx):
    if ctx.message.author.id == 778819230815748118:
        await ctx.send('Shutting down')
        await client.logout()
    else:
        await ctx.send('**Shut Up You Are Not My Owner!!! Owner Is Aarjit This Is Bot Owner Only Command**')

@client.command()
async def dm(ctx, user: discord.User, *, message=None):
    if ctx.message.author.id == 778819230815748118:
        message = message or "This Message is sent via DM"
        await ctx.message.delete()
        await user.send(message)
    else:
        await ctx.send('**Shut Up You Are Not My Owner!!! Owner Is Aarjit This Is Bot Owner Only Command**')

@client.command(pass_context=True)
async def servers(ctx):
    await ctx.send("I'm in `" + str(len(client.guilds)) + "` servers")


@client.command()
async def yt(ctx, *, search):
    if ctx.channel.is_nsfw():
        try:
            query_string = urllib.parse.urlencode({'search_query': search})
            htm_content = urllib.request.urlopen(
                'http://www.youtube.com/results?' + query_string)
            search_results = re.findall(r'/watch\?v=(.{11})',
                                        htm_content.read().decode())
            await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])
        except:
            await ctx.send('sorry, i cannot found resuld for this :( try with another title to get correct answer :)')
    else:
        await ctx.send('`This Command Can Be Only Used In NSFW Channel For Now`')

@client.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)

@client.command()
async def wanted(ctx, user: discord.Member = None):
    async with ctx.channel.typing():
        if user == None:
            user = ctx.author
      
        wanted = Image.open("wanted.jpg")
        asset = user.avatar_url_as(size=513)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((330,330))
        wanted.paste(pfp,(86, 185))
        wanted.save("wanted-export.jpg")
        await ctx.send(file = discord.File("wanted-export.jpg"))


@client.command(aliases=['RIP'])
async def rip(ctx, user: discord.Member = None):
    async with ctx.channel.typing():
        if user == None:
            user = ctx.author
      
        wanted = Image.open("rip.jpg")
        asset = user.avatar_url_as(size=256)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((200,200))
        wanted.paste(pfp,(70, 189))
        wanted.save("rip-export.jpg")
        await ctx.send(file = discord.File("rip-export.jpg"))

@client.command()
async def meme(ctx):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/meme") as r:
                data = await r.json()
                await ctx.send(data['caption'])
                await ctx.send(data['image'])

@client.command()
async def dogimage(ctx):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/img/dog") as r:
                data = await r.json()
                await ctx.send(data['link'])

@client.command()
async def catimage(ctx):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/img/cat") as r:
                data = await r.json()
                await ctx.send(data['link'])

@client.command()
async def pandaimage(ctx):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/img/panda") as r:
                data = await r.json()
                await ctx.send(data['link'])

@client.command()
async def redpanda(ctx):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/img/red_panda") as r:
                data = await r.json()
                await ctx.send(data['link'])

@client.command()
async def birdimage(ctx):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/img/birb") as r:
                data = await r.json()
                await ctx.send(data['link'])

@client.command()
async def foximage(ctx):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/img/fox") as r:
                data = await r.json()
                await ctx.send(data['link'])


@client.command()
async def koalaimage(ctx):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/img/koala") as r:
                data = await r.json()
                await ctx.send(data['link'])



@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
  responses = [
  discord.Embed(title='It is certain.'),
  discord.Embed(title='It is decidedly so.'),
  discord.Embed(title='Without a doubt.'),
  discord.Embed(title='Yes - definitely.'),
  discord.Embed(title='You may rely on it.'),
  discord.Embed(title='Most likely.'),
  discord.Embed(title='Outlook good.'),
  discord.Embed(title='Yes.'),
  discord.Embed(title='Signs point to yes.'),
  discord.Embed(title='Reply hazy, try again.'),
  discord.Embed(title='Ask again later.'),
  discord.Embed(title='Better not tell you now.'),
  discord.Embed(title='Cannot predict now.'),
  discord.Embed(title='Concentrate and ask again.'),
  discord.Embed(title="Don't count on it."),
  discord.Embed(title='My reply is no.'),
  discord.Embed(title='My sources say no.'),
  discord.Embed(title='Outlook not very good.'),
  discord.Embed(title='Very doubtful.')
    ]
  responses = random.choice(responses)
  await ctx.send(content=f'Question: {question}\nAnswer:', embed=responses)



#@client.command(aliases=['nepse'])
#async def NEPSE(ctx, *,question):
    #async with ctx.channel.typing():
        #async with aiohttp.ClientSession() as cs:
            #async with cs.get("https://nepse-data-api.herokuapp.com/data/todaysprice") as r:
                #data = await r.json()
                #for company in data:
                    #if company['companyName'] == question:
                        #for nepse in data:
                            #everything = ['companyName', 'noOfTransactions', 'maxPrice', 'minPrice', 'closingPrice', 'tradedShares', 'amount', 'previousClosing', 'difference']
                            #await ctx.send(everything)


@client.command()
async def oks(ctx):
    await ctx.send('OKS')

#code to connect to discord
keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
