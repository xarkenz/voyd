#!/usr/bin/python

"""'''''''''''''''''''''''''''
| X A R K E N Z      2 0 1 9 |
|                            |
| |   |  /```\  \   /  |```\ |
| |   |  |   |   \ /   |   | |
|  \ /   |   |    Y    |   | |
|   V    \___/    |    |___/ |
|    r  e  w  r  i  t  e     |
|                            |
|Consider your server saved! |
'''''''''''''''''''''''''''"""

#611833175784-gfh8s12pjjm880ms799lj2b1lad5vjnv.apps.googleusercontent.com



try:
    import discord
    from discord.ext import commands
    import asyncio, os, datetime, traceback, sys, requests, shutil, praw, webp
    from math import floor
    from time import time
    from random import choice, randint, choices
    from PIL import Image, ImageDraw, ImageFont, ImageOps
    from io import BytesIO
except ImportError as e:
    print("Missing required modules. Error: ")
    raise



bot_token = ""
reddit_secret = ""
reddit_pswd = ""
errors = 0
starttime = time()
do_restart = False
err = 0xf04747
scs = 0x43b581
guildset = {} # guildid : ["prefix", "channelid", "nmm", Active, "roleid"]
userdata = {} # userid : [rank, plucks]
mmg = {} # userid : [Active, Ultimate, "answer", ["moves"], ["answeraslist"]]
reminders = {}
pluckwait = {}
activities = [
    [discord.ActivityType.playing, ["with the roles", "myself", "with the stars", "a game", "around", "with server stuff", "with ban reasons", "with my foot", "dead", "ping-pong", "table tennis", "alive", "Pong", "Minecraft", "Run 3", "with my food", "stupid", "Super Mario 64", "with you", "absolutely nothing", "music", "no Fortnite"]],
    [discord.ActivityType.watching, ["absolutely nothing", "a hockey game", "you", "grass grow", "your mouth", "TV", "over servers", "all messages", "for burglars", "music"]],
    [discord.ActivityType.listening, ["absolutely nothing", "you", "bad words", "your server", "a podcast", "bits and bytes", "some music"]]
]
yesno = {True: "yes", False: "no"}
confirms = ["y", "yes", "confirm", "t", "on", "true", "yep", "yeah", "ok", "okay", "active", "activate", "enable"]
denys = ["n", "no", "deny", "f", "off", "false", "nope", "nah", "non", "nein", "inactive", "deactivate", "disable"]
permlist = ["create_instant_invites",
            "kick_members",
            "ban_members",
            "administrator",
            "manage_channels",
            "manage_server",
            "add_reactions",
            "view_audit_logs",
            "read_messages",
            "send_messages",
            "send_tts_messages",
            "manage_messages",
            "embed_links",
            "attach_files",
            "read_message_history",
            "mention_everyone",
            "external_emojis",
            "connect",
            "speak",
            "mute_members",
            "deafen_members",
            "move_members",
            "use_voice_activation",
            "change_nickname",
            "manage_nicknames",
            "manage_roles",
            "manage_webhooks",
            "manage_emojis"]
months = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
mastermst = ["<:rd:600037948343320599>",
    "<:og:600037987056746529>",
    "<:yl:600038009458393108>",
    "<:gn:600038038281781249>",
    "<:bu:600038687962562591>",
    "<:wt:600038756820451365>"]
mastermul = {"r":"<:rd:600037948343320599>",
    "o":"<:og:600037987056746529>",
    "y":"<:yl:600038009458393108>",
    "g":"<:gn:600038038281781249>",
    "b":"<:bu:600038687962562591>",
    "p":"<:pr:600038715611414549>",
    "d":"<:bk:600038735471443983>",
    "w":"<:wt:600038756820451365>"}



stars = ["<:s_w:600061295613575237>",
    "<:s_r:600061319651000339>",
    "<:s_o:600061332557004810>",
    "<:s_y:600061352622686218>",
    "<:s_g:600061369802555422>",
    "<:s_t:600061384277098506>",
    "<:s_b:600061414941655060>",
    "<:s_v:600061451125915648>",
    "<:s_p:600061470595743771>",
    "<:s_br:600061530851115040>",
    "<:s_sv:600061554485886997>",
    "<:s_gd:600061574337658889>",
    "<:s_dm:600061608877621258>",
    "<:s_bk:600061656013209611>",
    "<:s_vd:600061674904616961>",
    "<:s_sc:600061706932060197>",
    "<:s_rb:600061735566835741>",
    "<:s_ed:600061795771875338>",
    "<:s_gw:600061818941210655>",
    "<:s_gb:600061836397641758>",
    "<:s_ge:600061850066878507>"]
starnames = ["White", "Red", "Orange", "Yellow", "Green", "Teal", "Blue", "Violet", "Pink", "Bronze", "Silver", "Gold", "Diamond", "Black", "Void", "Starception", "Rainbow", "Etched", "GLITCH White", "GLITCH Black", "GLITCH Etched"]
    


userjoinmsg = [
    "{0} is here!",
    "Hello there, {0}.",
    "Top of the morning to you, {0}!",
    "{0} clicks into battle!",
    "Quick! {0} is here! Hide!",
    "You're telling me that {0} is here to stay?",
    "The- oh, uh, er... yeah! {0} is here...!",
    "Please stay here, {0}. We need you!",
    "{0}, if I could shake your hand right now, I would.",
    "{0}, don't come near me. I'm a vacuum.",
    "Greetings, Professor {0}. Would you like to play a game?",
    "I tip my hat to you, {0}!",
    "{0} joined. This... does put a smile on my face.",
    "This crystal ball shows me that {0} just clicked an invite...",
    "Greetings, {0}. Would you like some tea?",
    "{0}, get ready for the adventure of your life!",
]
userleavemsg = [
    "Bye, {0}!",
    "I suppose this is goodbye, {0}.",
    "Where's my hanky? \*sniff\* {0} is leaving...",
    "No, {0}! Don't leave me!",
    "Where did {0} go?",
    "Aw! I thought we were having fun with {0}!",
    "I'll miss you, {0}!",
    "Argh, {0} is a quitter!",
    "{0} is missing all the fun!",
    "Just when I thought {0} was going to stay...",
    "{0} just poofed.",
    "But {0}, what about that hide & seek game we planned?",
]



def stringIn(string, line):
    for i in range(len(line) - (len(string) - 1)):
        teststr = ""
        for j in range(len(string)):
            teststr = teststr + line[i + j]
        if teststr == string:
            return i
    return False



def tuplestrcolor(tup):
    r = str(hex(int(tup[0])))[2:]
    g = str(hex(int(tup[1])))[2:]
    b = str(hex(int(tup[2])))[2:]
    if len(r) == 1: r = "0" + r
    if len(g) == 1: g = "0" + g
    if len(b) == 1: b = "0" + b
    return r+g+b



def strcolor(string):
    stringbreak = []
    for i in string:
        stringbreak.append(str(hex(i))[2:])
    r = (stringbreak[0] * 16) + stringbreak[1]
    g = (stringbreak[2] * 16) + stringbreak[3]
    b = (stringbreak[4] * 16) + stringbreak[5]
    return (r * (16 ** 4)) + (g * (16 ** 2)) + b



def getDC(guild: discord.Guild):
    if guild.default_channel is None:
        for ch in guild.channels:
            if ch.permissions_for(guild.me).send_messages and str(ch.type) not in ["category", "voice"]:
                return ch
    else:
        return guild.default_channel
    return None



def getStar():
    chances = [10000,5700,5600,5500,5400,5300,5200,5100,5000,100,90,80,70,50,30,20,10,10,4,2,1]
    item = choices(stars, chances)[0]
    return (item, stars.index(item))



def mmemoji(guess):
    result = ""
    for i in guess:
        result += mastermul[i]
    return result
    


def getDate(date:str):
    year = str(int(date[:4]))
    month = months[int(date[5:7])]
    day = str(int(date[8:10]))
    if day in ["11", "12", "13"]: day += "th"
    elif day[-1] == "1": day += "st"
    elif day[-1] == "2": day += "nd"
    elif day[-1] == "3": day += "rd"
    else: day += "th"
    return "%s %s, %s" % (month, day, year)



def search(iterable, string):
    matched = []
    matchedm = []
    for member in iterable:
        if string.lower() in member.name.lower():
            matched.append(member.mention)
            matchedm.append(member)
        elif member.nick is not None:
            if string.lower() in member.nick.lower():
                matched.append(member.mention)
                matchedm.append(member)
    if matched == []:
        box = discord.Embed(title="Your search returned no results. Make sure spelling is correct.", color=err)
        return box
    elif len(matched) > 1:
        if len(matched) <= 15:
            desc = ""
            for i in matched:
                desc += i + "\n"
            box = discord.Embed(title="Your search returned multiple results:", description=desc, color=0xfaa72f)
        else:
            box = discord.Embed(title="Your search was too broad. Please use more specific keywords.", color=0xfaa72f)
        return box
    else:
        return matchedm[0]



def permEmbed(perm):
    return discord.Embed(title="Hey! I need this permission:", description="`%s`\nI won't be able to function properly unless I get this permission." % perm, color=err)



def random_sub(ctx, subr, amt):
    subr = reddit.subreddit(subr)
    subs = []
    for sub in subr.hot(limit=amt):
        if not (sub.over_18 and not ctx.message.channel.is_nsfw):
            subs.append(sub)
    return choice(subs)



def permissionstr(string, permissions: discord.Permissions, active: bool):
    """if string == permlist[0]: permissions.create_instant_invites = active
    elif string == permlist[1]: permissions.kick_members = active
    elif string == permlist[2]: permissions.ban_members = active
    elif string == permlist[3]: permissions.administrator = active
    elif string == permlist[4]: permissions.manage_channels = active
    elif string == permlist[5]: permissions.manage_server = active
    elif string == permlist[6]: permissions.add_reactions = active
    elif string == permlist[7]: permissions.view_audit_logs = active
    elif string == permlist[8]: permissions.read_messages = active
    elif string == permlist[9]: permissions.send_messages = active
    elif string == permlist[10]: permissions.send_tts_messages = active
    elif string == permlist[11]: permissions.manage_messages = active
    elif string == permlist[12]: permissions.embed_links = active
    elif string == permlist[13]: permissions.attach_files = active
    elif string == permlist[14]: permissions.read_message_history = active
    elif string == permlist[15]: permissions.mention_everyone = active
    elif string == permlist[16]: permissions.external_emojis = active
    elif string == permlist[17]: permissions.connect = active
    elif string == permlist[18]: permissions.speak = active
    elif string == permlist[19]: permissions.mute_members = active
    elif string == permlist[20]: permissions.deafen_members = active
    elif string == permlist[21]: permissions.move_members = active
    elif string == permlist[22]: permissions.use_voice_activation = active
    elif string == permlist[23]: permissions.change_nickname = active
    elif string == permlist[24]: permissions.manage_nicknames = active
    elif string == permlist[25]: permissions.manage_roles = active
    elif string == permlist[26]: permissions.manage_webhooks = active
    elif string == permlist[27]: permissions.manage_emojis = active"""
    if string in permlist:
        exec("permissions.%s = active" % string)
    return permissions



def setupguild(guildid: str):
    if guildid not in guildset.keys():
        guildset[guildid] = ["{", "", "", False, None]

def setupuser(userid: str):
    if userid not in userdata.keys():
        userdata[userid] = [0, [0]*21]



def create_rank_card(member: discord.Member, percent: int, filename="latest.gif"):
    color = member.top_role.color.to_rgb()
    disccolor = (90,100,110)
    textcolor = (194,196,197)
    darkcolor = (40,45,50)
    level, percent = divmod(percent, 100)
    level += 1
    print(member.avatar_url)
    response = requests.get(member.avatar_url, stream=True)
    #pfp = Image.open(response.raw)
    pfp = Image.new("RGB", (180,180), color=(0,200,0))
    raw = Image.new("RGB", (900,450), color=(73,76,83))
    mask = Image.new("L", (180,180), 0)

    drawmask = ImageDraw.Draw(mask)
    drawmask.ellipse([0,0,180,180], fill=255)

    image = ImageDraw.Draw(raw)
    namefont = ImageFont.truetype("regular.ttf", 45)
    discfont = ImageFont.truetype("light.ttf", 36)
    percfont = ImageFont.truetype("bold.ttf", 42)
    levlfont = ImageFont.truetype("bold.ttf", 60)
    image.rectangle((15,15,885,435), fill=(57,60,65))
    image.text((300,60), member.display_name, font=namefont, fill=color)
    image.text((300,120), "#"+str(member.discriminator), font=discfont, fill=disccolor)

    pfp.thumbnail((180,180))#, Image.ANTIALIAS)
    finalpfp = ImageOps.fit(pfp, (180,180), centering=(0.5,0.5))
    finalpfp.putalpha(mask)
    
    image.ellipse((51,51,249,249), fill=darkcolor)
    image.rectangle((45,350,855,405), fill=darkcolor)
    image.text((774,300), "/100", font=discfont, fill=textcolor)
    image.text((714,297), str(percent), font=percfont, fill=color)
    image.text((45,300), "LEVEL", font=discfont, fill=textcolor)
    image.text((152,280), str(level), font=levlfont, fill=color)
    
    # animations
    frames = []
    currentval = 0
    for i in range(20):
        frames.append(raw.copy())
        currentval += (percent - currentval) / 5
        if i == 19: currentval = percent
        frameedit = ImageDraw.Draw(frames[i])
        if percent: frameedit.rectangle((45,350,(7.5*currentval)+45,405), fill=color)
        if percent: frameedit.pieslice((45,45,258,258), 90, (3.6*currentval)+90, fill=color)
        frames[i].paste(finalpfp, (60,60), mask=mask)
        frames[i].thumbnail((300,150), Image.ANTIALIAS)
    
    frames[0].save(filename, "GIF", save_all=True, append_images=frames[1:], duration=50)



def writeFiles():
    os.remove("guilds.txt")
    with open("guilds.txt", "w+") as newss:
        for guildid, lst in guildset.items():
            newss.write(str(guildid)+"\n")
            for item in lst:
                newss.write(str(item) + "\n")
    os.remove("botusers.txt")
    with open("botusers.txt", "w+") as newud:
        for userid, data in userdata.items():
            newud.write("%d\n%d\n%s\n" % (userid, data[0], " ".join([str(i) for i in data[1]])))
            #for item in data[2:]:
            #    newud.write(str(item)+"\n")



def readFiles():
    global bot_token, reddit_secret, reddit_pswd, cmd_prefix, version
    with open("info.txt", "r+") as voydinfo:
        for i in enumerate(voydinfo.readlines()):
            j = i[0]; i = i[1][:-1]
            if j == 0: bot_token = i
            elif j == 1: reddit_secret = i
            elif j == 2: reddit_pswd = i
            elif j == 3: cmd_prefix = i
            elif j == 4: version = i
    with open("guilds.txt", "r+") as voydguilds:
        for i in enumerate(voydguilds.readlines()):
            j = i[0]; i = i[1][:-1]
            if j % 6 == 0: guildid = int(i)
            elif j % 6 == 1: guildset[guildid] = [i]
            elif j % 6 in [3]: guildset[guildid].append(i)
            elif j % 6 in [4]: guildset[guildid].append(i == "True")
            elif j % 6 in [2,5]: guildset[guildid].append(int(i) if i != "None" else None)
    with open("botusers.txt") as voydusers:
        for i in enumerate(voydusers.readlines()):
            j = i[0]; i = i[1][:-1]
            if j % 3 == 0: userid = int(i)
            elif j % 3 == 1: userdata[userid] = [int(i)]
            elif j % 3 == 2:
                userdata[userid].append([int(s) for s in i.split(" ")])
                userdata[userid][1] += [0]*(len(stars)-len(userdata[userid][1]))



readFiles()
bot = commands.Bot(command_prefix=cmd_prefix)
bot.remove_command("help")
reddit = praw.Reddit(client_id="Sqd5-jtoWZ62mw", client_secret=reddit_secret, username="XarkenZ", password=reddit_pswd, user_agent="xretreivev1")



@bot.event
async def on_ready():
    print("Username: %s\nVersion: %s\nID: %s\nDefault prefix: %s\nStatus: ready" % (bot.user.name, version, bot.user.id, bot.command_prefix))
    status = choice(activities)
    await bot.change_presence(activity=discord.Activity(type=status[0], name=choice(status[1])))
    
    

@bot.event
async def on_member_join(member):
    setupguild(member.guild.id)
    if guildset[member.guild.id][3]:
        if guildset[member.guild.id][2] == "": box = None
        else: box = discord.Embed(description=guildset[member.guild.id][2].replace("{{user}}", member.mention), color=scs)
        chnchk = discord.utils.get(member.guild.channels, id=guildset[member.guild.id][1])
        text = "<:joinarrow:494141514872520714> "+choice(userjoinmsg).format(member.mention)
        if chnchk is None: await getDC(member.guild).send(text, embed=box)
        else: await chnchk.send(text, embed=box)
    if guildset[member.guild.id][4] != "None":
        nmrole = discord.utils.get(member.guild.roles, id=guildset[member.guild.id][4])
        if nmrole is not None: await member.add_roles(nmrole)



@bot.event
async def on_member_remove(member):
    setupguild(member.guild.id)
    if guildset[member.guild.id][3] and member.id != 478945810378260490:
        #if guildset[member.guild.id][2] == "": box = None
        #else: box = discord.Embed(description=guildset[member.guild.id][2].replace("{{user}}", member.mention), color=scs)
        chnchk = discord.utils.get(member.guild.channels, id=guildset[member.guild.id][1])
        text = "<:leavearrow:494153240389091328> "+choice(userleavemsg).format(member.mention)
        if chnchk is None: await getDC(member.guild).send(text)
        else: await chnchk.send(text)



@bot.event
async def on_guild_join(guild):
    await discord.Object(id=480721130118971413).send(embed=discord.Embed(title="Added to server", description="Voyd has joined the server %s." % guild.name, color=scs))
    await getDC(guild).send(embed=discord.Embed(title="Hey, thanks for inviting me!", description="My prefix here is `{0}`. To change it, type `{0}prefix <prefix>`. ;)".format(cmd_prefix), color=scs))



@bot.event
async def on_guild_remove(guild):
    await discord.Object(id=480721130118971413).send(embed=discord.Embed(title="Removed from server", description="Voyd has been removed from the server %s." % guild.name, color=err))



@bot.event
async def on_message(message):
    if message.guild is not None and not message.author.bot:
        if "<@461646073769885697>" in message.content: await message.channel.send("hi dere")
        aid = message.author.id
        gid = message.guild.id
        setupuser(aid)
        userdata[aid][0] += 1
        if userdata[aid][0] % 100 == 0:
            await message.channel.send(embed=discord.Embed(title="%s leveled up to level %d!" % (message.author.display_name, userdata[aid][0]//100+1), color=message.author.top_role.color))
        setupguild(gid)
        bot.command_prefix = guildset[gid][0]
        message.content = message.content.replace(bot.command_prefix+"r/",bot.command_prefix+"sr ")
        await bot.process_commands(message)
        bot.command_prefix = cmd_prefix



@bot.event
async def on_command_error(ctx, error):
    global errors
    errors += 1
    if hasattr(ctx.command, "on_error"): return
    
    print("Ignoring exception in command %s:" % ctx.command, file=sys.stderr)
    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)



@bot.command(aliases=["s", "stts", "runtime", "errors"])
async def status(ctx):
    box = discord.Embed(title="Status", description="Up and running!", color=scs)
    box.add_field(name="Start Time", value="`%s`" % str(starttime))
    box.add_field(name="Error Count", value=str(errors) + " error%s during this run." % ("" if errors == 1 else "s"))
    box.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    await ctx.send(embed=box)



@bot.command(aliases=["bot", "botinfo", "bot-info"])
async def voyd(ctx):
    guildcount = sum([1 for i in bot.guilds])
    box = discord.Embed(title="Voyd#6046", description="The center of the Voyd.", color=0)
    box.add_field(name="Creator", value="XarkenZ#6806", inline=False)
    box.add_field(name="Version", value=version, inline=False)
    box.add_field(name="guilds", value=guildcount, inline=False)
    box.add_field(name="Language", value="Python (discord.py)", inline=False)
    box.add_field(name="User ID", value=bot.user.id, inline=False)
    box.set_thumbnail(url=bot.user.avatar_url)
    await ctx.send(embed=box)



@bot.command(aliases=["ping", "connection", "testconnection", "pong"])
async def speed(ctx):
    box = discord.Embed(title="Connection Speed", description=":control_knobs: %ss" % str(round(bot.latency,6)), color=0x2200dd)
    box.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    box.set_footer(text="Measured with Discord Heartbeat")
    await ctx.send(embed=box)



@bot.command(aliases=["h", "commands"])
async def help(ctx, category=None):
    if category is None:
        box = discord.Embed(title="Help Categories", description="Type `help <category>` to view commands in a category.", color=0)
        box.add_field(name="Bot", value="Make the bot your own.", inline=False)
        box.add_field(name="Chat", value="Enhance your chatting experience.", inline=False)
        box.add_field(name="Games", value="Fun things to pass the time.", inline=False)
        box.add_field(name="Member", value="Know all there is to know about the humans.", inline=False)
        box.add_field(name="Server", value="Control the server without lifting a finger.", inline=False)
    else:
    
    
        if category.lower() in ["b", "bot"]:
            box = discord.Embed(title="Bot Commands", description="Type `help <command>` to view help for a command.", color=0)
            box.add_field(name="Commands", value="""[MS] `changeprefix <prefix>`: Changes prefix.
`help <item>`: You are here.
`invite`: Show invites for bot and official server.
`ping`: Show connection speed.
`voyd`: Shows Voyd's info.""")


        elif category.lower() in ["s", "server", "guild"]:
            box = discord.Embed(title="Server Commands", description="Type `help <command>` to view help for a command.", color=0)
            box.add_field(name="Commands", value="""[D] `roles [func] [etc]`: Manage the server's roles. See `role help` for more.
[D] `channels [func] [etc]`: Manage the server's channels. See `channel help` for more.
[D] `server [func] [etc]`: Manage the server. See `server help` for more.
[D] `emojis [func] [etc]`: Manage the server's emojis. See `emoji help` for more.
[MS] `newmembersettings [func] [etc]`: Manage the new member settings. (custom join messages, roles, etc.) See `nms help` for more.
[MS] `purge <limit> [user]`: Delete `limit` number of messages above. You can use `user` as a filter to determine which messages to delete.""")


        elif category.lower() in ["m", "member", "members"]:
            box = discord.Embed(title="Member Commands", description="Type `help <command>` to view help for a command.", color=0)
            box.add_field(name="Commands", value="""[MS] `ban <user>`: Bans a user.
[MS] `kick <user>`: Kicks a user.
[D] `member [func] [user]`: Manage users. See `member help` for more.
[MS] `unban <user>`: Unbans a user.
[MS] `warn <user> <message>`: Messages a user.
[VM] `voicekick <user>`: Kick a user from their voice channel.""")


        elif category.lower() in ["c", "chat", "chatting"]:
            box = discord.Embed(title="Chat Commands", description="Type `help <command>` to view help for a command.", color=0)
            box.add_field(name="Commands", value="""`quote <msgid> [comment]`: Quote a message.
`subreddit <name> [limit]`: Display a random post from a given subreddit. (`r/<name>` is also a valid command.)
`meme`: Take a random meme from r/memes, r/dankmemes, or r/deepfriedmemes, for when you can't decide.
`showerthought`: Take a showerthought from r/showerthoughts. How insightful.
`dog`: Take a cute lil' puppy from r/dogpictures.
`cat`: Take a cat photo from r/cats and r/russianblue.
`tilt <text>`: Make your message look LiKe ThiS.
`rank [user]`: View the chat rank of you or someone else.""")
            
            
        elif category.lower() in ["g", "games", "fun"]:
            box = discord.Embed(title="Other Commands", description="Type `help <command>` to view help for a command.", color=0)
            box.add_field(name="Commands", value="""`mastermind [etc1] [etc2]`: See `mm help` for more. A version of Mastermind in Discord.""")
            
        
        elif category.lower() == "me": box = discord.Embed(title="I can try...", description="No promises, sorry.", color=0)
        else: box = discord.Embed(title="Invalid category or command.", color=err)
        box.set_footer(text="KEY: [M*]: Manage * [VM]: Move Members [D] Depends")
    box.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    await ctx.send(embed=box)



@bot.command(aliases=["inv", "in", "iv", "voydinvite", "botinvite"])
async def invite(ctx):
    box = discord.Embed(title="Invite %s to your server!" % bot.user.name, description="https://discordapp.com/oauth2/authorize?client_id=478945810378260490&scope=bot", color=0)
    box.add_field(name="Join the official %s guild!" % bot.user.name, value="https://discord.gg/5xgzh4r")
    box.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    await ctx.send(embed=box)
    await ctx.send("https://discord.gg/5xgzh4r")



@bot.command(pass_context=True, aliases=["dogpic", "doggo", "puppy", "pupper", "doggy", "pup"])
async def dog(ctx):
    await ctx.channel.trigger_typing()
    sub = random_sub(ctx, "dogpictures", 100)
    box = discord.Embed(title=sub.title, color=0x36383e)
    box.set_image(url=sub.url)
    box.set_footer(text="r/dogpictures · %s upvote%s" % (sub.score, "" if sub.score == 1 else "s"))
    try: await ctx.send(embed=box)
    except commands.errors.CommandInvokeError: await ctx.send(embed=discord.Embed(title="An error occurred.", color=err))



@bot.command(pass_context=True, aliases=["catto", "kitty", "kitten", "catty", "kit"])
async def cat(ctx):
    await ctx.channel.trigger_typing()
    sub = random_sub(ctx, "cats+russianblue", 100)
    box = discord.Embed(title=sub.title, color=0x36383e)
    box.set_image(url=sub.url)
    box.set_footer(text="r/%s · %s upvote%s" % (sub.subreddit.display_name, sub.score, "" if sub.score == 1 else "s"))
    try: await ctx.send(embed=box)
    except commands.errors.CommandInvokeError: await ctx.send(embed=discord.Embed(title="An error occurred.", color=err))



@bot.command(pass_context=True, aliases=["mem", "memz", "memez", "memes", "dankmeme", "dankmemes", "dank", "deepfriedmemes", "deepfriedmeme"])
async def meme(ctx):
    await ctx.channel.trigger_typing()
    sub = random_sub(ctx, "memes+dankmemes+deepfriedmemes", 200)
    box = discord.Embed(title=sub.title, color=0x36383e)
    box.set_image(url=sub.url)
    box.set_footer(text="r/%s · %s upvote%s" % (sub.subreddit.display_name, sub.score, "" if sub.score == 1 else "s"))
    try: await ctx.send(embed=box)
    except commands.errors.CommandInvokeError: await ctx.send(embed=discord.Embed(title="An error occurred.", color=err))



@bot.command(pass_context=True, aliases=["showerthoughts", "showert", "sthought", "sthoughts", "showerts", "st"])
async def showerthought(ctx):
    await ctx.channel.trigger_typing()
    sub = random_sub(ctx, "showerthoughts", 200)
    box = discord.Embed(title=sub.title, color=0x36383e)
    box.set_image(url=sub.url)
    box.set_footer(text="r/showerthoughts · %s upvote%s" % (sub.score, "" if sub.score == 1 else "s"))
    try: await ctx.send(embed=box)
    except commands.errors.CommandInvokeError: await ctx.send(embed=discord.Embed(title="An error occurred.", color=err))



@bot.command(pass_context=True, aliases=["subr", "sreddit", "reddit", "rdt", "srdt", "sbrdt", "sr"])
async def subreddit(ctx, sr, num="50"):
    if sr.startswith("r/"): sr = sr[2:]
    if num.isdigit():
        num = int(num)
        if int(num) <= 200:
            try:
                sr = reddit.subreddit(sr)
                await ctx.channel.trigger_typing()
                subs = []
                for sub in sr.hot(limit=num):
                    if not (sub.over_18 and not ctx.message.channel.is_nsfw):
                        subs.append(sub)
            except: await ctx.send(embed=discord.Embed(title="'%s' isn't a valid subreddit." % sr, color=err))
            else:
                rsub = choice(subs)
                if len(rsub.selftext) > 2000:
                    text = rsub.selftext[:1997] + "..."
                else: text = rsub.selftext
                box = discord.Embed(title=rsub.title, description=text, color=0x36383e)
                if rsub.url.split(".")[-1].lower() in ["png", "jpg", "jpeg", "tif", "tiff", "gif"]:
                    box.set_image(url=rsub.url)
                else:
                    box.set_author(name="[View on Reddit]", url=rsub.url)
                box.set_footer(text="#%d on r/%s · %s upvote%s" % (subs.index(rsub)+1, sr, rsub.score, "" if sub.score == 1 else "s"))
                try: await ctx.send(embed=box)
                except commands.errors.CommandInvokeError: await ctx.send(embed=discord.Embed(title="An error occurred.", color=err))
        else: await ctx.send(embed=discord.Embed(title="That's too many posts!", color=err))
    else: await ctx.send(embed=discord.Embed(title="That's not a valid number.", color=err))



@bot.command(aliases=["tilt", "tiktok", "alt", "wobble"])
async def weird(ctx, *etc):
    string = " ".join(etc)
    result = ""
    for i in range(len(string)):
        if i % 2 or string[i].lower() == "l": result += string[i].upper()
        else: result += string[i].lower()
    box = discord.Embed(description=result, color=0x0033aa)
    box.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    box.set_footer(text="'tilt' command")
    await ctx.message.delete()
    await ctx.send(embed=box)



@bot.command(pass_context=True, aliases=["mastermind", "masterm", "mmind", "master", "mind"])
async def mm(ctx, arg1="h", arg2=""):
    userid = ctx.author.id
    help = False
    if arg1.lower() in ["h", "help"]:
        help = True
        box = discord.Embed(title="Help", color=0x11ccaa)
        box.add_field(name="Objective:", value="""The computer will generate a random sequence of colors. Your job is to guess the colors. Every time you make a guess, the computer will grade your submission. If one correct color is in its correct spot, you will receive a <:red_small_circle:475001526872702977>. If one color is correct, but not in the correct spot, you will receive a <:white_small_circle:475001540676157451>.""", inline=False)
        box.add_field(name="Functions:", value="""`'h'elp`: You are here.
`'s'tandard`: Start a standard game. (4 spaces, 6 colors)
`'u'ltimate`: Start an ultimate game. (5 spaces, 8 colors)
`'q'uit`: Quit the current game.
`'r'estart`, `'r'eset`: Restart the current game, whilst saving the answer.
`'g'uess`: Make a guess, using the guide below.""", inline=False)
        box.add_field(name="Guessing:", value="""`r` for red
`o` for orange
`y` for yellow
`g` for green
`b` for blue
`p` for purple (Ultimate only)
`d` for black (Ultimate only)
`w` for white""", inline=False)
        box.add_field(name="Example usage:", value="`mm guess rygb` (in Standard mode)", inline=False)
        box.set_author(name="MasterMind", icon_url="https://media.discordapp.net/attachments/474939004366749696/475330712157814824/mm_icon.png")
    elif arg1.lower() in ["s", "st", "stand", "standard"]:
        combination = ""
        comblst = []
        for i in range(4):
            item = choice(mastermst)
            combination += item
            comblst.append(item)
        mmg[userid] = [True, False, combination, [], comblst, []]
        box = discord.Embed(title="Mastermind: New standard game", color=0x88cc11)
    elif arg1.lower() in ["u", "ul", "ult", "ultimate"]:
        combination = ""
        comblst = []
        mmvalues = []
        for i in mastermul.values():
            mmvalues.append(i)
        for i in range(5):
            item = choice(mmvalues)
            combination += item
            comblst.append(item)
        mmg[userid] = [True, True, combination, [], comblst, []]
        box = discord.Embed(title="Mastermind: New ultimate game", color=0x11ccaa)
    elif arg1.lower() in ["q", "quit"]:
        if userid in mmg.keys():
            if mmg[userid][0]:
                mmg[userid][0] = False
                box = discord.Embed(title="Quit game.", description="Answer: %s" % mmg[userid][2], color=0x3345dc)
            else:
                box = discord.Embed(title="No game is in progress.", color=0xdc3345)
        else:
            box = discord.Embed(title="No game is in progress.", color=0xdc3345)
    elif arg1.lower() in ["r", "restart", "reset"]:
        if userid in mmg.keys():
            if mmg[userid][0]:
                mmg[userid][3] = []
                mmg[userid][5] = []
                box = discord.Embed(title="Reset game. (Answer saved)", color=0x3345dc)
            else:
                box = discord.Embed(title="No game is in progress.", color=0xdc3345)
        else:
            box = discord.Embed(title="No game is in progress.", color=0xdc3345)

    elif arg1.lower() in ["g", "guess"]:
        guess = []
        if userid not in mmg.keys():
            await ctx.send("No Mastermind games are in progress.")
            return
        if not mmg[userid][0]:
            await ctx.send("No Mastermind games are in progress.")
            return
        if mmg[userid][1] and len(arg2) != 5:
            await ctx.send("Invalid guess format.")
            return
        if not mmg[userid][1] and len(arg2) != 4:
            await ctx.send("Invalid guess format.")
            return
        for i in arg2:
            if i.lower() not in ["r", "o", "y", "g", "b", "p", "d", "w"]:
                await ctx.send("Your guess contains invalid characters.")
                return
            if i.lower() in ["p", "d"] and not mmg[userid][1]:
                await ctx.send("Your guess contains invalid characters.")
                return
            guess.append(i.lower())
        move = mmemoji(guess)
        anstemp = []
        for i in mmg[userid][4]:
            anstemp.append(i)
        j = -1
        rcount = 0
        wcount = 0
        for i in guess:
            j += 1
            if mastermul[i] == mmg[userid][4][j]:
                rcount += 1
                anstemp[j] = ""
        j = -1
        for i in guess:
            j += 1
            if mastermul[i] in anstemp:
                wcount += 1
                anstemp[j] = ""
        grade = ""
        for i in range(rcount):
            grade += "<:rs:600037874930548760>"
        for i in range(wcount):
            grade += "<:ws:600037899840258049>"
        ogmove = move
        move += "|"+grade
        mmg[userid][3].append(move)
        print(mmg[userid][2])
        if mmg[userid][2] == ogmove:
            mmg[userid][0] = False
            if mmg[userid][1]: descr = "Customizations may be coming soon!"
            else: descr = "Now try Ultimate mode!"
            box = discord.Embed(title=":tada: Congratulations! You solved the puzzle! :tada:", description=descr, color=scs)
        elif (len(mmg[userid][3]) >= 10 and not mmg[userid][1]) or (len(mmg[userid][3]) >= 12 and mmg[userid][1]):
            mmg[userid][0] = False
            box = discord.Embed(title="You ran out of moves...", description="Answer: " + mmg[userid][2], color=err)
        if mmg[userid][0]:
            desc = value="\n".join(mmg[userid][3])
            if not mmg[userid][1]: box = discord.Embed(title="Standard game (Most recent last)", description=desc, color=0x88cc11)
            else: box = discord.Embed(title="Ultimate game (Most recent last)", description=desc, color=0x11ccaa)
    else: box = discord.Embed(title="Invalid command.", color=err)
    if not help: box.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=box)
    
    
    
@bot.command(pass_context=True, aliases=["pull", "pl"])
async def pluck(ctx):
    mem = ctx.author.id
    current = time()
    time_wait = 5
    if mem not in pluckwait.keys(): pluckwait[mem] = current - time_wait
    if current - pluckwait[mem] >= time_wait:
        earned, starnum = getStar()
        box = discord.Embed(title="You earned:", description=earned+" "+starnames[starnum], color=scs)
        #box.set_footer(text=choice(pluckresponses))
        box.set_author(name="Pluck")#, icon_url="https://cdn.discordapp.com/emojis/461002409658023986.png?v=1")
        await ctx.send(embed=box)
        userdata[mem][1][starnum] += 1
        pluckwait[mem] = current
    else:
        box = discord.Embed(title=ctx.author.display_name+":", description="You have to wait for %d more second(s) before plucking again." % floor(time_wait-(current-pluckwait[mem])), color=err)
        box.set_author(name="Pluck")#, icon_url="https://cdn.discordapp.com/emojis/461002409658023986.png?v=1")
        await ctx.send(embed=box, delete_after=3)



@bot.command(pass_context=True, aliases=["ps", "pullscore", "plucks", "pulls"])
async def pluckscore(ctx, *args):
    if len(args) == 0: user = ctx.author
    else:
        user = " ".join(args)
        if len(user) > 1:
            if user[:2] == "<@":
                get = user.replace(" ","")
                if get[2] == "!": user = ctx.guild.get_member(int(get[3:-1]))
                else: user = ctx.guild.get_member(int(get[2:-1]))
            else: user = search(ctx.guild.members, user)
        else: user = search(ctx.guild.members, user)
        if isinstance(user, discord.Embed):
            await ctx.send(embed=user)
            return
    setupuser(user.id)
    box = discord.Embed(title=user.display_name, color=0xdc3345)
    box.set_author(name="Pluck")#, icon_url="https://cdn.discordapp.com/emojis/461002409658023986.png?v=1")
    starshow = []
    for i in range(21):
        if userdata[user.id][1][i] > 0: starshow.append("%s%d"%(stars[i],userdata[user.id][1][i]))
    box.add_field(name="Score:", value="\n".join(starshow))
    box.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=box)



@bot.command(aliases=["purge", "purgemessages", "purge-messages"])
async def p(ctx, messages, user=None):
    if messages.isdigit():
        messages = int(messages)
        if messages <= 500 and messages > 0:
            req = user
            if user is not None:
                user = discord.utils.get(ctx.message.guild.members, name=user)
                if user is None:
                    user = discord.utils.get(ctx.message.guild.members, id=user)
                    if user is None:
                        try:
                            if req[2] == "!": num = 3
                            else: num = 2
                            user = discord.utils.get(ctx.message.guild.members, id=user[num:-1])
                        except commands.errors.CommandInvokeError: pass
                        if user is None:
                            user = search(ctx.message.guild.members, req)
                            if type(user) == discord.Embed:
                                return await ctx.send(embed=user)
            if ctx.author.guild_permissions.manage_messages or user == ctx.author:
                if ctx.guild.me.guild_permissions:
                    if user is None:
                        await ctx.channel.purge(limit=messages+1)
                        box = discord.Embed(title="Purged %s messages." % str(messages), color=scs)
                    else:
                        await ctx.channel.purge(limit=messages+1, check=lambda m: m.author == user)
                        box = discord.Embed(title="Purged messages by %s in a range of %s messages." % (user.name, str(messages)), color=scs)
                else: box = discord.Embed(title="Woah, I don't have that permission.", color=err)
            else: box = discord.Embed(title="Missing permission: 'manage_messages'. (Purging your own messages also works!)", color=err)
        else: box = discord.Embed(title="Limit must be from 1 to 500.", color=err)
    else: box = discord.Embed(title="Limit is a required argument.", color=err)
    await ctx.send(embed=box, delete_after=3)



@bot.command(aliases=["q", "quotemessage", "quote-message", "retrieve"])
async def quote(ctx, messageid, *etc):
    success = False
    commented = len(etc) > 0
    await ctx.channel.trigger_typing()
    for i in ctx.guild.channels:
        try:
            quotemessage = await i.fetch_message(int(messageid))
            quotemember = quotemessage.author
            success = True
        except:
            pass
    if success:
        comment = " ".join(etc) if commented else ""
        quotebox = discord.Embed(description=quotemessage.content, color=0x36383e)
        quotebox.set_author(name=quotemember.display_name, icon_url=quotemember.avatar_url)
        try: await ctx.message.delete()
        except: pass
        quotebox.timestamp = quotemessage.created_at
        await ctx.send(comment, embed=quotebox)
    else: await ctx.send(embed=discord.Embed(title="That message doesn't exist in this guild!", color=err))



@bot.command(aliases=["rankcard", "card"])
async def rank(ctx, mem=None):
    if mem is None: user = ctx.author
    elif len(mem) > 1:
        if mem[:2] == "<@":
            get = mem.replace(" ","")
            if get[2] == "!": user = ctx.guild.get_member(int(get[3:-1]))
            else: user = ctx.guild.get_member(int(get[2:-1]))
        else: user = search(ctx.guild.members, mem)
    else: user = search(ctx.guild.members, mem)
    if isinstance(user, discord.Member):
        setupuser(user.id)
        create_rank_card(user, userdata[user.id][0])
        await ctx.send(file=discord.File("latest.gif", "card.gif"))
        return
    else: box = user
    await ctx.send(embed=box)



@bot.command(aliases=["warn", "pm", "message", "directmessage", "privatemessage"])
async def dm(ctx, usearch, *etc):
    if ctx.message.author.guild_permissions.manage_guild:
        if ctx.message.guild.me.guild_permissions.manage_guild:
            if len(etc) == 0:
                await ctx.send(embed=discord.Embed(title="This command requires a message.", color=err))
                return
            if len(usearch) > 1:
                if usearch[:2] == "<@":
                    get = ""
                    for i in usearch:
                        if i != " ":
                            get += i
                    if get[2] == "!":
                        user = ctx.message.guild.get_member(get[3:-1])
                    else:
                        user = ctx.message.guild.get_member(get[2:-1])
                else:
                    user = search(ctx.message.guild.members, usearch)
            else:
                user = search(ctx.message.guild.members, usearch)
            if type(user) == discord.Member:
                if user.bot:
                    box = discord.Embed(title="Bots are too powerful to send messages to!", description="Recipient: %s (%s)" % (user.mention, str(user.status)), color=err)
                else:
                    await user.send(" ".join(etc))
                    box = discord.Embed(title="Message sent.", color=scs)
                    box.add_field(name="Recipient:", value="%s (%s)" % (user.mention, str(user.status)))
                    box.add_field(name="Message:", value=" ".join(etc), inline=False)
            else:
                box = user
        else:
            box = discord.Embed(title="Woah, I don't have that permission.", color=err)
    else:
        box = discord.Embed(title="Forbidden: Missing permission `manage_guild`.", color=err)
    await ctx.send(embed=box)



@bot.command()
async def writedata(ctx):
    if ctx.author.id == 451357826753888256:
        writeFiles()
        await ctx.send("i remember now")



@bot.command()
async def readdata(ctx):
    if ctx.author.id == 451357826753888256:
        readFiles()
        await ctx.send("i understand everything")



@bot.command(aliases=["commandprefix", "command-prefix", "commandp", "cprefix", "prefix", "set-prefix", "change-prefix", "sp", "setp", "changep"])
async def cp(ctx, prefixset=cmd_prefix):
    color = err
    guildid = ctx.guild.id
    setupguild(guildid)
    if ctx.author.guild_permissions.manage_guild:
        if len(prefixset) > 10:
            title = "Prefix cannot be longer than 10 characters."
        else:
            if guildset[guildid][0] == prefixset:
                title = "That's the current prefix."
            else:
                guildset[guildid][0] = prefixset
                title = "Prefix set."
                color = scs
        writeFiles()
    else:
        color = err
        title = "Forbidden: Missing permission `manage_guild`."
    box = discord.Embed(title=title, color=color)
    await ctx.send(embed=box)



@bot.command(aliases=["nms", "new-member-settings", "nmsettings"])
async def newmembersettings(ctx, setting="l", *etc):
    guildid = ctx.guild.id
    setupguild(guildid)
    
    
    if setting.lower() in ["l", "li", "list"]:
        if guildset[guildid][3]:
            if guildset[guildid][1] == "": chn = "Not specified"
            else: chn = "<#%d>" % guildset[guildid][1]
            if guildset[guildid][2] == "": msg = "No extra message"
            else: msg = guildset[guildid][2]
            desc = None
        else:
            desc = "New member messages disabled for this server."
            chn = None
            msg = None
        box = discord.Embed(title="New Member Settings", description=desc, color=scs)
        box.set_author(name=ctx.message.guild.name, icon_url=ctx.message.guild.icon_url)
        if desc is None:
            box.add_field(name="Channel", value=chn, inline=False)
            box.add_field(name="Message", value=msg, inline=False)
    
    
    elif setting.lower() in ["h", "help", "commands"]: pass
    
    
    elif setting.lower() in ["c", "chn", "channel"]:
        try:
            assert ctx.message.author.guild_permissions.manage_guild, "fb" # forbidden
            assert len(etc) > 0, "rq" # channel required
            channel = etc[0]
            assert channel[2:-1].isdigit() and len(channel) == 21 and discord.utils.get(ctx.message.guild.channels, id=int(channel[2:-1])) is not None, "ic" # invalid channel
            guildset[guildid][1] = int(channel[2:-1])
            box = discord.Embed(title="Channel updated successfully.", description="**New member channel:** " + channel, color=scs)
        except Exception as ex:
            e = str(ex)
            if e == "ic": box = discord.Embed(title="Invalid channel.", color=err)
            elif e == "rq": box = discord.Embed(title="Channel is a required argument.", color=err)
            elif e == "fb": box = discord.Embed(title="Forbidden: Missing permission 'Manage Server'.", color=err)
            else:
                box = discord.Embed(title="An unknown error occurred.", color=err)
                traceback.print_exception(type(ex), ex, ex.__traceback__, file=sys.stderr)
    
    
    elif setting.lower() in ["m", "msg", "message"]:
        try:
            assert ctx.message.author.guild_permissions.manage_guild, "fb" # forbidden
            assert len(etc) > 0, "rq" # message required
            guildset[guildid][2] = " ".join(etc)
            box = discord.Embed(title="Message updated successfully.", description="**New member message:**\n" + guildset[guildid][2], color=scs)
        except Exception as ex:
            e = str(ex)
            if e == "rq": box = discord.Embed(title="Message is a required argument.", color=err)
            elif e == "fb": box = discord.Embed(title="Forbidden: Missing permission 'Manage Server'.", color=err)
            else:
                box = discord.Embed(title="An unknown error occurred.", color=err)
                traceback.print_exception(type(ex), ex, ex.__traceback__, file=sys.stderr)
    
    
    elif setting.lower() in confirms:
        try:
            assert ctx.message.author.guild_permissions.manage_guild, "fb" # forbidden
            guildset[guildid][3] = True
            box = discord.Embed(title="New member messages enabled.", color=scs)
        except Exception as ex:
            e = str(ex)
            if e == "fb": box = discord.Embed(title="Forbidden: Missing permission 'Manage Server'.", color=err)
            else:
                box = discord.Embed(title="An unknown error occurred.", color=err)
                traceback.print_exception(type(ex), ex, ex.__traceback__, file=sys.stderr)
    
    
    elif setting.lower() in denys:
        guildset[guildid][3] = False
        box = discord.Embed(title="New member messages disabled.", color=scs)
    
    
    elif setting.lower() in ["test", "sample", "t"]:
        setupguild(ctx.guild.id)
        if guildset[ctx.guild.id][3]:
            if guildset[ctx.guild.id][2] == "": box = None
            else: box = discord.Embed(description=guildset[ctx.guild.id][2].replace("{{user}}", ctx.author.mention), color=scs)
            await ctx.send(choice(userjoinmsg).format(ctx.author.mention), embed=box)
            return
        else: box = discord.Embed(title="New member messages are not enabled on your server.", color=err)
    
    
    else: box = discord.Embed(title="Invalid setting.", color=err)
    await ctx.send(embed=box)



@bot.command(aliases=["serverinfo", "ser", "server-info"])
async def server(ctx, function="i", *args):

    if function.lower() in ["i", "info", "about"]:
        s = ctx.guild
        schannels = sum([1 for i in s.channels])
        smembers = sum([1 for i in s.members])
        box = discord.Embed(title="About Server", description="**Created on:** %s\n**ID:** `%d`\n**Owner:** %s\n**Region:** `%s`\n**Roles:** %d\n**Custom emojis:** %d\n**Channels:** %d\n**Members:** %d" % (getDate(str(s.created_at)), s.id, s.owner.mention, str(s.region), len(s.roles), len(s.emojis), schannels, smembers), color=0xcccccc)
        box.set_author(name=s.name, icon_url=s.icon_url)
        
        
    else: box = discord.Embed(title="Invalid function.", color=err)
    await ctx.send(embed=box)



@bot.command(aliases=["channel", "c", "chn", "ch"])
async def channels(ctx, function="l", channel=None):
    if function.lower() in ["l", "li", "list", "all"]:
        times = ""
        names = ""
        positions = ""
        categories = {}
        bycat = [[i[0],i[1]] for i in ctx.guild.by_category()]
        more = False
        numchn = sum([len(i[1]) for i in bycat])
        if numchn > 10:
            more = True
            testnum = 0
            for i in range(len(bycat)):
                ogtest = testnum
                testnum += len(bycat[i][1])
                if testnum > 10:
                    bycat[i][1] = bycat[i][1][:10-ogtest]
                    bycat = bycat[:i+1]
                    break
        for cat in bycat:
            times += ":clock2: " + getDate(str(cat[0].created_at)) + "\n"
            positions += "<:green_pin:598200778569809940> `" + str(cat[0].position) + "`\n"
            names += "<:category:511998393938214912> **%s**\n" % cat[0].name.upper()
            for c in cat[1]:
                times += ":clock2: " + getDate(str(c.created_at)) + "\n"
                positions += ":pushpin: `" + str(c.position) + "`\n"
                if str(c.type) == "voice":
                    names += "<:voice_channel:511998451274481694> %s\n" % c.name
                elif str(c.type) == "text":
                    names += "<:text_channel:511998432345587723> " + c.mention + "\n"
        box = discord.Embed(color=scs)
        box.set_author(name="%s Channels (%d)" % (ctx.message.guild.name, numchn), icon_url=ctx.message.guild.icon_url)
        if more: box.set_footer(text="%d more..." % (numchn-10))
        box.add_field(name="Channel", value=names)
        box.add_field(name="Position", value=positions)
        box.add_field(name="Created", value=times)
    elif function.lower() in ["i", "inf", "info"]:
        if channel is None:
            channel = ctx.channel
        else:
            chn = channel
            channel = discord.utils.get(ctx.guild.channels, name=channel)
            if channel is None:
                channel = discord.utils.get(ctx.guild.channels, id=chn[2:-1])
                if channel is None:
                    box = discord.Embed(title="Channel not found.", color=err)
                    return await ctx.send(embed=box)
        if str(channel.type) == "text": nm = channel.mention
        else: nm = channel.name
        box = discord.Embed(title="Channel Info", description=nm, color=scs)
        if channel.topic == "": topic = "No topic"
        else: topic = str(channel.topic)
        box.add_field(name="Topic", value=topic, inline=False)
        box.add_field(name="Information", value="**ID:** `%s`\n**Type:** %s\n**Created on:** %s" % (channel.id, str(channel.type), getDate(str(channel.created_at))), inline=False)
    else: box = discord.Embed(title="Invalid function.", color=err)
    await ctx.send(embed=box)



@bot.command(aliases=["em", "ems", "emote", "emotes", "emoji", "customemoji", "ce", "custom-emoji"])
async def emojis(ctx, function="l", *etc):
    if function.lower() in ["l", "list", "all"]:
        ems = ""
        names = ""
        ids = ""
        for i in ctx.guild.emojis:
            ems += str(i) + "\n"
            names += "`:%s:`<:blank:498566453914501150>\n" % i.name
            ids += "`%s`<:blank:498566453914501150>\n" % i.id
        box = discord.Embed(color=0xbbcccc)
        box.add_field(name="Emoji", value=ems)
        box.add_field(name="Text", value=names)
        box.add_field(name="ID", value=ids)
        box.set_author(name=ctx.message.guild.name + " Emojis", icon_url=ctx.message.guild.icon_url)
    elif function.lower() in ["a", "add", "c", "create", "n", "new"]:
        try:
            assert ctx.author.guild_permissions.manage_emojis, "fb" # forbidden
            assert ctx.guild.me.guild_permissions.manage_emojis, "np" # no permission
            assert len(etc) > 0, "ne" # not enough arguments
            image = etc[0]
            if len(etc) > 1: name = etc[1]
            else: name = image.split(".")[0]
            assert len(name) >= 2, "ts" # too short
            assert name.isalnum, "na" # not alphanumeric
            image = requests.get(image, stream=True).content
            em = await ctx.guild.create_custom_emoji(name=name, image=image, reason="Created by"+str(ctx.author))
            await ctx.message.add_reaction(em)
            return
        except Exception as e:
            e = str(e)
            if e == "fb": title = "Forbidden: Missing permission 'Manage Emojis'."
            elif e == "np": title = "Woah, I don't have that permission."
            elif e == "ne": title = "This command requires an image (in URL form)."
            elif e == "ts": title = "The emoji name must be more than 2 letters long."
            elif e == "na": title = "The emoji name contains invalid characters."
            else: title = "An unknown error occurred."
            await ctx.send(embed=discord.Embed(title=title, color=err))
            return
            
    else: box = discord.Embed(title="Invalid function.", color=err)
    await ctx.send(embed=box)



@bot.command(aliases=["rl", "role", "rolelist", "guildroles", "rls"])
async def roles(ctx, function="l", *args):

    if function in ["l", "li", "list", "all"]:
        names = ""
        pos = ""
        members = ""
        sortroles = {}
        rolelist = []
        roleamt = 0
        for i in ctx.guild.roles:
            roleamt += 1
            sortroles[i.position] = i
        for i in sorted(sortroles.keys(), reverse=True):
            rolelist.append(sortroles[i])
        for role in rolelist:
            memberamt = 0
            if role.name == "@everyone": names += ":clipboard: @everyone\n"
            else: names += ":clipboard: " + role.mention + "\n"
            pos += ":pushpin: " + str(role.position) + "\n"
            for member in ctx.message.guild.members:
                if role in member.roles:
                    memberamt += 1
            members += "<:members:479657677212090368> " + str(memberamt) + "\n"
        box = discord.Embed(color=0xaa00cc)
        box.add_field(name="Role", value=names)
        box.add_field(name="Position", value=pos)
        box.add_field(name="Members", value=members)
        box.set_author(name="%s Roles (%s)" % (ctx.guild.name, str(roleamt)), icon_url=ctx.message.guild.icon_url)
        if more: box.set_footer(text="%d more..." % (numchn-10))
    elif function in ["m", "me"]:
        names = ""
        pos = ""
        members = ""
        sortroles = {}
        rolelist = []
        for i in ctx.author.roles:
            sortroles[i.position] = i
        for i in sorted(sortroles.keys(), reverse=True):
            rolelist.append(sortroles[i])
        for role in rolelist:
            memberamt = 0
            if role.name == "@everyone":
                names += ":clipboard: @everyone\n"
            else:
                names += ":clipboard: " + role.mention + "\n"
            pos += ":pushpin: " + str(role.position) + "\n"
            for member in ctx.message.guild.members:
                if role in member.roles:
                    memberamt += 1
            members += "<:members:479657677212090368> " + str(memberamt) + "\n"
        box = discord.Embed(color=0xaa00cc)
        box.add_field(name="Role", value=names)
        box.add_field(name="Position", value=pos)
        box.add_field(name="Members", value=members)
        box.set_author(name="%s's Roles" % ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        
        
    elif function in ["f", "for", "o", "of"]:
        if args[0] is None:
            box = discord.Embed(title="This function requires a member.", color=err)
        elif args[0][:2] == "<@":
            args[0] = args[0].replace(" ","")
            if get[2] == "!":
                user = ctx.guild.get_member(get[3:-1])
            else:
                user = ctx.guild.get_member(get[2:-1])
        else:
            user = search(ctx.guild.members, args[0])
        if isinstance(user, discord.Member):
            names = ""
            pos = ""
            members = ""
            sortroles = {}
            rolelist = []
            for i in user.roles:
                if i.name != "@everyone":
                    sortroles[i.position] = i
            if len(sortroles) > 0:
                for i in sorted(sortroles.keys(), reverse=True):
                    rolelist.append(sortroles[i])
                for role in rolelist:
                    memberamt = 0
                    if role.name == "@everyone":
                        names += ":clipboard: @everyone\n"
                    else:
                        names += ":clipboard: " + role.mention + "\n"
                    pos += ":pushpin: " + str(role.position) + "\n"
                    for member in ctx.message.guild.members:
                        if role in member.roles:
                            memberamt += 1
                    members += "<:members:479657677212090368> " + str(memberamt) + "\n"
                box = discord.Embed(color=0xaa00cc)
                box.add_field(name="Role", value=names)
                box.add_field(name="Position", value=pos)
                box.add_field(name="Members", value=members)
            else:
                box = discord.Embed(description="This user has no roles.", color=0xaa00cc)
            box.set_author(name="%s's Roles" % user.name, icon_url=user.avatar_url)
        else:
            box = user
            
            
    elif function.lower() in ["i", "inf", "info", "g", "get"]:
        role = " ".join(args)
        if role == None:
            box = discord.Embed(title="No role has been stated.", color=err)
        else:
            if role[0] == "<":
                role = role[3:-1]
                if discord.utils.get(ctx.message.guild.roles, name=role) is None:
                    box = discord.Embed(title="That role doesn't exist.", color=err)
                    await ctx.send(embed=box)
                    return
                else:
                    role = discord.utils.get(ctx.message.guild.roles, id=role)
            elif role[0].isdigit():
                if discord.utils.get(ctx.message.guild.roles, name=role) is None:
                    box = discord.Embed(title="That role doesn't exist.", color=err)
                    await ctx.send(embed=box)
                    return
                else:
                    role = discord.utils.get(ctx.message.guild.roles, id=role)
            else:
                if role[0] == "@":
                    role = role[1:]
                if discord.utils.get(ctx.message.guild.roles, name=role) is None:
                    box = discord.Embed(title="That role doesn't exist.", color=err)
                    await ctx.send(embed=box)
                    return
                else:
                    role = discord.utils.get(ctx.message.guild.roles, name=role)
            membercount = 0
            for member in ctx.guild.members:
                if role in member.roles:
                    membercount += 1
            box = discord.Embed(title="Role: " + role.name, description="**Mention:** %s\n**ID:** %s\n**Color:** %s %s\n**Mentionable:** %s\n**Displays separately:** %s\n**Members:** %s" % (role.mention, role.id, "#"+str(hex(role.color.value))[2:].lower(), str(role.color.to_tuple()), yesno[role.mentionable], yesno[role.hoist], membercount), color=role.color.value)
    elif function.lower() in ["create", "c"]:
        if ctx.message.author.guild_permissions.manage_roles:
            if ctx.message.guild.me.guild_permissions.manage_roles:
                if args[0] is None:
                    box = discord.Embed(title="Role must have a name.", color=err)
                else:
                    await bot.create_role(ctx.message.guild, name=args[0])
                    box = discord.Embed(title="Role created.", description="Use `role edit <permission> <on|off>` to edit this role (and other roles!).", color=scs)
            else:
                box = discord.Embed(title="Woah, I don't have that permission.", color=err)
        else:
            box = discord.Embed(title="Forbidden: Missing permission 'manage_roles'.", color=err)
            
            
    elif function.lower() in ["d", "del", "delete"]:
        if ctx.message.author.guild_permissions.manage_roles:
            if ctx.message.guild.me.guild_permissions.manage_roles:
                role = args[0]
                if role[0] == "<":
                    role = role[3:-1]
                    if discord.utils.get(ctx.message.guild.roles, name=role) == None:
                        box = discord.Embed(title="That role doesn't exist.", color=err)
                        await ctx.send(embed=box)
                        return
                    else:
                        role = discord.utils.get(ctx.message.guild.roles, id=role)
                elif role[0].isdigit():
                    if discord.utils.get(ctx.message.guild.roles, name=role) == None:
                        box = discord.Embed(title="That role doesn't exist.", color=err)
                        await ctx.send(embed=box)
                        return
                    else:
                        role = discord.utils.get(ctx.message.guild.roles, id=role)
                else:
                    if role[0] == "@":
                        role = role[1:]
                    if discord.utils.get(ctx.message.guild.roles, name=role) == None:
                        box = discord.Embed(title="That role doesn't exist.", color=err)
                        await ctx.send(embed=box)
                        return
                    else:
                        role = discord.utils.get(ctx.message.guild.roles, name=role)
                if ctx.message.author.guild_permissions.manage_roles:
                    if ctx.message.guild.me.guild_permissions.manage_roles:
                        await ctx.send(embed=discord.Embed(title="Are you sure you want to delete '%s'?" % role.name, color=scs))
                        resp = await bot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
                        if resp.content.lower() in confirms:
                            await role.delete()
                            box = discord.Embed(title="Role deleted.", color=scs)
                        else: box = discord.Embed(title="Cancelled deletion.", color=err)
                    else: box = discord.Embed(title="Woah, I don't have that permission.", color=err)
                else: box = discord.Embed(title="Forbidden: Missing permission 'manage_roles'.", color=err)
            else: box = discord.Embed(title="Woah, I don't have that permission.", color=err)
        else: box = discord.Embed(title="Forbidden: Missing permission 'manage_roles'.", color=err)
            
            
    elif function.lower() in ["edit", "e", "change", "chg", "set", "s"]:
        if not ctx.message.author.guild_permissions.manage_roles:
            box = discord.Embed(title="Forbidden: Missing permission 'manage_roles'.", color=err)
            await ctx.send(embed=box)
            return
        if not ctx.message.guild.me.guild_permissions.manage_roles:
            box = discord.Embed(title="Woah, I don't have that permission.", color=err)
            await ctx.send(embed=box)
            return
        role = args[0]
        if role is None:
            box = discord.Embed(title="No role has been stated.", color=err)
        else:
            if role[0] == "<":
                role = role[3:-1]
                if discord.utils.get(ctx.message.guild.roles, name=role) == None:
                    box = discord.Embed(title="That role doesn't exist.", color=err)
                    await ctx.send(embed=box)
                    return
                else:
                    role = discord.utils.get(ctx.message.guild.roles, id=role)
            elif role[0].isdigit():
                if discord.utils.get(ctx.message.guild.roles, name=role) == None:
                    box = discord.Embed(title="That role doesn't exist.", color=err)
                    await ctx.send(embed=box)
                    return
                else:
                    role = discord.utils.get(ctx.message.guild.roles, id=role)
            else:
                if role[0] == "@":
                    role = role[1:]
                if discord.utils.get(ctx.message.guild.roles, name=role) == None:
                    box = discord.Embed(title="That role doesn't exist.", color=err)
                    await ctx.send(embed=box)
                    return
                else:
                    role = discord.utils.get(ctx.message.guild.roles, name=role)
        perm = args[1]
        if perm is None:
            box = discord.Embed(title="No permission has been stated.", color=err)
        else:
            if perm.lower() in permlist:
                perms = role.permissions
                perm = perm.lower()
                if args[2] is None:
                    box = discord.Embed(title="No bool has been stated.", color=err)
                else:
                    if args[2].lower() in confirms:
                        perms = permissionstr(perm, perms, True)
                        await bot.edit_role(ctx.message.guild, role, permissions=perms)
                        box = discord.Embed(title="Edited role '%s' to have '%s' permission on." % (role.name, perm), color=scs)
                    elif args[2].lower() in denys:
                        perms = permissionstr(perm, perms, False)
                        await bot.edit_role(ctx.message.guild, role, permissions=perms)
                        box = discord.Embed(title="Edited role '%s' to have '%s' permission off." % (role.name, perm), color=scs)
                    else:
                        box = discord.Embed(title="Must be a yes or no answer.", color=err)
            elif perm.lower() in ["color", "colour"]:
                if args[2] is None:
                    await bot.edit_role(ctx.message.guild, role, color=discord.Color(value=0))
                    box = discord.Embed(title="Updated role color to default.", color=scs)
                else:
                    if len(args[2]) == 6:
                        success = True
                        for i in args[2]:
                            if not i.isdigit() and i.lower() not in ["a", "b", "c", "d", "e", "f"]: success = False
                        if success:
                            await bot.edit_role(ctx.message.guild, role, color=discord.Color(value=strcolor(args[2])))
                            box = discord.Embed(title="Updated role color to `%s`." % args[2].lower(), color=scs)
                        else:
                            box = discord.Embed(title="Invalid color.", color=err)
                    else:
                        if not args[2].isdigit() or not args[3].isdigit() or not args[4].isdigit():
                            box = discord.Embed(title="Invalid color.", color=err)
                        elif int(args[2]) > 255 or int(args[3]) > 255 or int(args[4]) > 255:
                            box = discord.Embed(title="Invalid color.", color=err)
                        else:
                            await bot.edit_role(ctx.message.guild, role, color=discord.Color(value=strcolor(tuplestrcolor(args[2:5]))))
                            box = discord.Embed(title="Updated role color to `%s` %s." % (tuplestrcolor(args[2:5]), (*args[2:5])), color=scs)
            else:
                box = discord.Embed(title="Invalid property. See role help for a list of valid permissions.", color=err)
                
                
    elif function.lower() in ["g", "give", "ap", "append", "a", "add"]:
        if None in args[:2]:
            box = discord.Embed(title="This function uses two arguments, <member> and <role>.", color=err)
        else:
            if not ctx.message.author.guild_permissions.manage_roles:
                box = discord.Embed(title="Forbidden: Missing permission 'manage_roles'.", color=err)
            elif not ctx.message.guild.me.guild_permissions.manage_roles:
                box = discord.Embed(title="Woah, I don't have that permission.", color=err)
            else:
                rolest = args[1]
                if rolest[1] == "<": rolest = rolest[3:-1]
                elif rolest[1] == "@": rolest = rolest[1:]
                role = discord.utils.get(ctx.message.guild.roles, name=rolest)
                if role is None:
                    role = discord.utils.get(ctx.message.guild.roles, id=role)
                    if role is None:
                        box = discord.Embed(title="That role doesn't exist.", color=err)
                        await ctx.send(embed=box)
                        return
                if args[0][:2] == "<@":
                    get = args[0].replace(" ", "")
                    if get[2] == "!": user = ctx.message.guild.get_member(get[3:-1])
                    else: user = ctx.message.guild.get_member(get[2:-1])
                else: user = search(ctx.message.guild.members, args[0])
                if isinstance(user, discord.Member):
                    await user.add_roles(role)
                    box = discord.Embed(title="Role '%s' has been given to user %s." % (role.name, user.display_name), color=scs)
                else: box = user
                
                
    elif function.lower() in ["r", "rm", "rem", "remove", "take"]:
        if None in args[:2]:
            box = discord.Embed(title="This function uses two arguments, <member> and <role>.", color=err)
        else:
            if not ctx.message.author.guild_permissions.manage_roles:
                box = discord.Embed(title="Forbidden: Missing permission 'manage_roles'.", color=err)
            elif not ctx.message.guild.me.guild_permissions.manage_roles:
                box = discord.Embed(title="Woah, I don't have that permission.", color=err)
            else:
                rolest = args[1]
                if rolest[1] == "<": rolest = rolest[3:-1]
                elif rolest[1] == "@": rolest = rolest[1:]
                role = discord.utils.get(ctx.message.guild.roles, name=rolest)
                if role is None:
                    role = discord.utils.get(ctx.message.guild.roles, id=role)
                    if role is None:
                        box = discord.Embed(title="That role doesn't exist.", color=err)
                        await ctx.send(embed=box)
                        return
                if args[0][:2] == "<@":
                    get = args[0].replace(" ", "")
                    if get[2] == "!": user = ctx.message.guild.get_member(get[3:-1])
                    else: user = ctx.message.guild.get_member(get[2:-1])
                else: user = search(ctx.message.guild.members, args[0])
                if isinstance(user, discord.Member):
                    await user.remove_roles(role)
                    box = discord.Embed(title="Role '%s' has been taken from user %s." % (role.name, user.display_name), color=scs)
                else: box = user
                
                
    else: box = discord.Embed(title="Invalid function.", color=err)
    await ctx.send(embed=box)



@bot.command(aliases=["user", "us", "m"])
async def member(ctx, func="i", user=None):
    if func.lower() in ["i", "info", "information"]:
        if user is None:
            user = ctx.message.author
        else:
            user = search(ctx.message.guild.members, user)
            if type(user) == discord.Embed:
                await ctx.send(embed=user)
                return
        joindate = str(user.joined_at)[:-16]
        jddate = str(user.created_at)[:-16]
        joinstats = joindate.split("-")
        jdstats = jddate.split("-")
        for i in range(len(joinstats)):
            joinstats[i] = int(joinstats[i])
        joinday = str(joinstats[2])
        if joinday == "1":
            joinday = "1st"
        elif joinday == "2":
            joinday = "2nd"
        elif joinday == "3":
            joinday = "3rd"
        elif len(joinday) == 1:
            joinday += "th"
        elif joinday[1] == "1":
            joinday += "st"
        elif joinday[1] == "2":
            joinday += "nd"
        elif joinday[1] == "3":
            joinday += "rd"
        else:
            joinday += "th"
        for i in range(len(jdstats)):
            jdstats[i] = int(jdstats[i])
        jdday = str(jdstats[2])
        if jdday == "1":
            jdday = "1st"
        elif jdday == "2":
            jdday = "2nd"
        elif jdday == "3":
            jdday = "3rd"
        elif len(jdday) == 1:
            jdday += "th"
        elif jdday[1] == "1":
            jdday += "st"
        elif jdday[1] == "2":
            jdday += "nd"
        elif jdday[1] == "3":
            jdday += "rd"
        else:
            jdday += "th"
        if user.nick is None:
            ttl = "Info: %s" % str(user)
        else:
            ttl = "Info: %s (aka %s)" % (str(user), user.nick)
        box = discord.Embed(title=ttl, description="ID: `%s`" % user.id, color=user.top_role.color.value)
        if str(user.status) == "online": status = "<:online:486344135209385987> Online"
        elif str(user.status) == "idle": status = "<:idle:486344204629573697> Idle"
        elif str(user.status) == "dnd": status = "<:dnd:486344262191939624> Do Not Disturb"
        elif str(user.status) == "offline": status = "<:offline:486344317624123394> Offline"
        else: status = ":grey_question: " + str(user.status).title()
        box.add_field(name="Status", value=status, inline=False)
        #box.add_field(name="")
        box.add_field(name="Joined %s" % ctx.message.guild.name, value="%s %s, %s" % (months[joinstats[1]], joinday, joinstats[0]), inline=False)
        box.add_field(name="Joined Discord", value="%s %s, %s" % (months[jdstats[1]], jdday, jdstats[0]), inline=False)
        box.set_thumbnail(url=user.avatar_url)
        if user.id == 478945810378260490:
            box.set_footer(text="Use the 'voyd' command to learn more about me.")
        elif user.id == 451357826753888256:
            box.set_footer(text="Hey, I know that guy!")
    else:
        box = discord.Embed(title="Invalid function.", color=err)
    await ctx.send(embed=box)



@bot.command(pass_context=True, aliases=["rem", "r", "reminder", "reminders", "calendarreminders"])
async def remind(ctx, func="l", arg0="", arg1="", arg2="", arg3="", arg4="", *args):
    global reminders
    
    
    if func.lower() in ["h", "help"]:
        box = discord.Embed(title="Functions (default is 'list')", description="`'cl'ear, 'w'ipe`: Wipes all reminders for this server.\n`'e'nable <id>`: Enables a reminder.\n`'d'isable <id>`: Disables a reminder.\n`'a'dd, 'c'reate <name> <channel> <interval> <starts> <tts> <message>`: Creates a new reminder.\n`'l'ist, 'a'll`: Shows all reminders for this server.", color=0xdd7700)
        box.set_author(name="Reminder Help", icon_url="https://media.discordapp.net/attachments/480721365826273283/599007771844673548/reminders.png")
        
        
    elif func.lower() in ["cl", "clear", "w", "wipe"]:
        if len(reminders) == 0:
            box = discord.Embed(title="There are no reminders to clear.", color=0xdd2200)
        else:
            reminders = {}
            box = discord.Embed(title="Cleared reminders.", color=0x22dd00)
            
            
    elif func.lower() in ["e", "en", "enable"]:
        try:
            sch = reminders[int(arg0)]
            if sch[0]:
                box = discord.Embed(title="This reminder is already enabled.", color=0xdd2200)
            else:
                sch[0] = True
                box = discord.Embed(title="Reminder `%s` enabled." % int(arg0), color=0x22dd00)
        except Exception as e:
            box = discord.Embed(title="ID needs to be in integer form.", color=0xdd2200)
            
            
    elif func.lower() in ["d", "dis", "disable"]:
        try:
            sch = reminders[int(arg0)]
            if not sch[0]:
                box = discord.Embed(title="This reminder is already disabled.", color=0xdd2200)
            else:
                sch[0] = False
                box = discord.Embed(title="Reminder `%s` disabled." % int(arg0), color=0x22dd00)
        except ValueError:
            box = discord.Embed(title="ID needs to be in integer form.", color=0xdd2200)
        except KeyError:
            box = discord.Embed(title="ID is not valid.", color=0xdd2200)
            
            
    elif func.lower() in ["a", "add", "c", "create"]:
        arg5 = "".join(args)
        if arg1[:2] != "<#" or arg1[-1] != ">":
            box = discord.Embed(title="Mention the channel to set it.", color=0xdd2200)
        elif arg2[-1].lower() not in ["m", "h", "d", "w"]:
            await bot.say(arg2[-1].lower())
            box = discord.Embed(title="The interval unit must be valid.", color=0xdd2200)
        elif not arg2[:-1].isdigit():
            box = discord.Embed(title="The interval number must be valid.", color=0xdd2200)
        elif arg3[2] != ":":
            box = discord.Embed(title="The start time format must be HH:MM.", color=0xdd2200)
        elif arg4.lower() not in ["true", "false", "yes", "no", "t", "f", "y", "n", "on", "off"]:
            box = discord.Embed(title="The TTS argument must be valid.", color=0xdd2200)
        else:
            schid = len(reminders)
            tts = ""
            if arg4.lower() in ["true", "yes", "t", "y", "on"]:
                arg4 = True
                tts = "<:voice_channel:511998451274481694> "
            else: arg4 = False
            reminders[schid] = [True, ctx.guild.id, arg0, arg1, arg2, arg3, arg5, arg4]
            box = discord.Embed(title="Reminder set.", description="**ID:** `%s`\n**Name:** %s\n**Channel:** %s\n**Starts:** `%s`\n**Interval:** `%s`\n**Message:** %s%s" % (schid, arg0, arg1, arg3, arg2, tts, arg5), color=0x22dd00)
            
            
    elif func.lower() in ["l", "li", "list"]:
        guildcount = 0
        for i in reminders.values():
            if i[1] == ctx.guild.id:
                guildcount += 1
        if guildcount == 0:
            box = discord.Embed(title="Reminders", description="Your server doesn't have any reminders.", color=0xdd7700)
            box.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        else:
            ids = ""
            names = ""
            channelms = ""
            for schid, info in reminders.items():
                if info[1] == ctx.guild.id:
                    active = "<:check_mark:478929263815557166> `" if info[0] else "<:cross_mark:478929280538116097> `"
                    ids += active + str(schid) + "`\n"
                    names += ":pencil2: " + info[2] + "\n"
                    channelms += "<:text_channel:511998432345587723> " + info[3] + "\n"
            box = discord.Embed(title="Reminders", color=0xdd7700)
            box.add_field(name="ID", value=ids)
            box.add_field(name="Name", value=names)
            box.add_field(name="Channel", value=channelms)
            box.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
            
            
    else: box = discord.Embed(title="That's not a valid function.", color=0xdd2200)
    await ctx.send(embed=box)



@bot.command(pass_context=True)
async def say(ctx, *etc):
    text = "".join(etc)
    print(type(ctx.author.id))
    if ctx.author.id in [451357826753888256]:
        foot = False
        try:
            await ctx.message.delete()
        except Exception as e:
            foot = True
        if foot:
            box = discord.Embed(title="Unable to delete invoke.", color=err)
            await ctx.send(text, embed=box)
        else:
            await ctx.send(text)
    else:
        await ctx.send("Command only permitted by owner.")



@bot.command(aliases=["vk", "voice-kick", "voicek", "vkick"])
async def voicekick(ctx, mem, reason=None):
    try:
        assert ctx.author.guild_permissions.move_members, "fb" # forbidden
        assert ctx.guild.me.guild_permissions.move_members, "np" # not enough permission
        assert ctx.author.voice is not None, "av" # author not using voice channel
        if len(mem) > 1:
            if mem[:2] == "<@":
                get = mem.replace(" ","")
                if get[2] == "!": user = ctx.guild.get_member(int(get[3:-1]))
                else: user = ctx.guild.get_member(int(get[2:-1]))
            else: user = search(ctx.guild.members, mem)
        else: user = search(ctx.guild.members, mem)
        if isinstance(user, discord.Member):
            assert user.voice is not None, "tv" # target not using voice channel
            user.move_to(None, reason=reason)
            box = discord.Embed(title="Member kicked from current voice channel.", color=scs)
        else: box = user
        await ctx.send(embed=box)
    except Exception as e:
        e = str(e)
        desc = ""
        if e == "fb": title = "Forbidden: Missing permission 'Move Members'."
        elif e == "np": title = "I don't have the required permissions to use this command."; desc = "I need:\nMove Members"
        elif e == "av": title = "You need to be using a voice channel to use this command."
        elif e == "tv": title = user.display_name + " isn't using any voice channels."
        await ctx.send(embed=discord.Embed(title=title, description=desc, color=err))



@bot.command(aliases=["vb", "voice-ban", "voiceb", "vban"])
async def voiceban(ctx, *, msearch):
    pass



@bot.command(aliases=["k"])
async def kick(ctx, *etc):
    perms = ctx.message.author.guild_permissions
    if not perms.kick_members:
        box = discord.Embed(title="Forbidden: Missing permission 'kick_members'.", color=err)
        await ctx.send(embed=box)
        return
    if not ctx.message.guild.me.guild_permissions.kick_members:
        box = discord.Embed(title="Woah, I don't have that permission.", color=err)
        await ctx.send(embed=box)
        return
    string = "".join(etc)
    matched = []
    matchedm = []
    for member in ctx.message.guild.members:
        if string.lower() in member.name.lower():
            matched.append(member.mention + " (%s)" % str(member.status))
            matchedm.append(member)
        elif member.nick is not None:
            if string.lower() in member.nick.lower():
                matched.append(member.mention + " (%s)" % str(member.status))
                matchedm.append(member)
    if matched == []:
        box = discord.Embed(title="Your search returned no results. Make sure spelling is correct.", color=err)
    elif len(matched) > 1:
        if len(matched) <= 15:
            box = discord.Embed(title="Your search returned multiple results:", description="\n".join(matched), color=0xddcc11)
        else:
            box = discord.Embed(title="Your search was too broad. Please use more specific keywords.", color=0xff8100)
    else:
        if matchedm[0] == ctx.message.guild.me:
            await ctx.send(embed=discord.Embed(title="I suppose this is goodbye. Are you sure you want to kick me?", color=err))
            try:
                resp = await bot.wait_for("message", check=lambda m: m.author == ctx.message.author and m.channel == ctx.message.channel, timeout=60.0)
            except asyncio.TimeoutError:
                box = discord.Embed(title="Automatically timed out after 1 minute of inactivity.", color=err)
                await ctx.send(embed=box)
                return
            if resp.content.lower() in ["y", "yes", "confirm", "t", "true", "yep", "yeah", "ok", "okay", "k"]:
                box = discord.Embed(title="Well, bye.", color=scs)
                await ctx.send(embed=box)
                await ctx.guild.leave()
                return
            else:
                box = discord.Embed(title="Kicking cancelled.", color=err)
            return
        else:
            await matchedm[0].kick()
            box = discord.Embed(title="Member kicked.", description=matched[0], color=scs)
    await ctx.send(embed=box)



@bot.command(aliases=["b"])
async def ban(ctx, *etc):
    perms = ctx.message.author.guild_permissions
    if not perms.ban_members:
        box = discord.Embed(title="Forbidden: Missing permission 'ban_members'.", color=err)
        await ctx.send(embed=box)
        return
    if not ctx.message.guild.me.guild_permissions.ban_members:
        box = discord.Embed(title="Woah, I don't have that permission.", color=err)
        await ctx.send(embed=box)
        return
    string = "".join(etc)
    matched = []
    matchedm = []
    for member in ctx.message.guild.members:
        if string.lower() in member.name.lower():
            matched.append(member.mention + " (%s)" % str(member.status))
            matchedm.append(member)
        elif member.nick is not None:
            if string.lower() in member.nick.lower():
                matched.append(member.mention + " (%s)" % str(member.status))
                matchedm.append(member)
    if matched == []:
        box = discord.Embed(title="Your search returned no results. Make sure spelling is correct.", color=err)
    elif len(matched) > 1:
        if len(matched) <= 15:
            box = discord.Embed(title="Your search returned multiple results:", description="\n".join(matched), color=0xddcc11)
        else:
            box = discord.Embed(title="Your search was too broad. Please use more specific keywords.", color=0xff8100)
    else:
        await matchedm[0].ban()
        box = discord.Embed(title="Member banned.", description=matched[0], color=scs)
    await ctx.send(embed=box)



@bot.command(aliases=["ub"])
async def unban(ctx, *etc):
    perms = ctx.message.author.guild_permissions
    if not perms.ban_members:
        box = discord.Embed(title="Forbidden: Missing permission 'ban_members'.", color=err)
        await ctx.send(embed=box)
        return
    if not ctx.message.guild.me.guild_permissions.ban_members:
        box = discord.Embed(title="Woah, I don't have that permission.", color=err)
        await ctx.send(embed=box)
        return
    string = " ".join(etc)
    matched = []
    matchedm = []
    for usr in await ctx.guild.bans():
        reason, usr = usr
        if usr is not None:
            if string.lower() in usr.name.lower():
                matched.append(usr.name+("" if reason is None else " (%s)"%reason))
                matchedm.append(usr)
    if matched == []:
        box = discord.Embed(title="Your search returned no results. Make sure spelling is correct.", color=err)
    elif len(matched) > 1:
        if len(matched) <= 15:
            box = discord.Embed(title="Your search returned multiple results:", description="\n".join(matched), color=0xddcc11)
        else:
            box = discord.Embed(title="Your search was too broad. Please use more specific keywords.", color=0xff8100)
    else:
        await ctx.guild.unban(matchedm[0])
        box = discord.Embed(title="Member unbanned.", description="Unbanned: "+matched[0], color=scs)
    await ctx.send(embed=box)



@bot.command()
async def shutdown(ctx):
    if ctx.author.id == 451357826753888256:
        await ctx.send("cya bye")
        await bot.logout()
        print("Ended via bot command.")
        
        

@bot.command()
async def restart(ctx):
    global do_restart
    if ctx.author.id == 451357826753888256:
        await ctx.send("ok im restarting")
        do_restart = True
        await bot.close()



if __name__ == "__main__":
    try: bot.run(bot_token)
    except: print("Ended via KeyboardInterrupt.")
    writeFiles()
    print("Files updated.")
