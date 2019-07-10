
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
    import asyncio, os, datetime, traceback, sys
    from math import floor
    from time import time
    from random import choice, randint
except ImportError as e:
    print("Missing required modules. Error: " + str(e))

errors = 0
starttime = time()
err = 0xdd2200
scs = 0x22dd00
guildset = {} # "guildid" : ["prefix", "channelid", "nmm", nmmactive, "roleid"]
activities = [
    [discord.ActivityType.playing, ["with the roles", "myself", "with the stars", "a game", "around", "with server stuff", "with ban reasons", "with my foot", "dead", "ping-pong", "alive", "Pong", "Minecraft", "Run 3", "with my food", "stupid", "Super Mario 64", "with you", "absolutely nothing", "music", "no Fortnite"]],
    [discord.ActivityType.watching, ["absolutely nothing", "a hockey game", "you", "grass grow", "your mouth", "TV", "over servers", "all messages", "for burglars", "music"]],
    [discord.ActivityType.listening, ["absolutely nothing", "you", "bad words", "your server", "a podcast", "bits and bytes", "some music"]]
]
yesno = {True: "yes", False: "no"}
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
userjoinmsg = [
    "<:joinarrow:494141514872520714> **{0}** just joined the server - glhf!",
    "<:joinarrow:494141514872520714> **{0}** just joined. Everyone, look busy!",
    "<:joinarrow:494141514872520714> **{0}** just joined. Can I get a heal?",
    "<:joinarrow:494141514872520714> **{0}** joined your party.",
    "<:joinarrow:494141514872520714> **{0}** joined. You must construct additional pylons.",
    "<:joinarrow:494141514872520714> Ermagherd. **{0}** is here.",
    "<:joinarrow:494141514872520714> Welcome, **{0}**. Stay awhile and listen.",
    "<:joinarrow:494141514872520714> Welcome, **{0}**. We were expecting you \u0361\u00B0 \u035C\u0296 \u0361\u00B0",
    "<:joinarrow:494141514872520714> Welcome, **{0}**. We hope you brought pizza.",
    "<:joinarrow:494141514872520714> Welcome **{0}**. Leave your weapons by the door.",
    "<:joinarrow:494141514872520714> A wild **{0}** appeared.",
    "<:joinarrow:494141514872520714> Swoooosh. **{0}** just landed.",
    "<:joinarrow:494141514872520714> Brace yourselves. **{0}** just joined the server.",
    "<:joinarrow:494141514872520714> **{0}** just joined. Hide your bananas.",
    "<:joinarrow:494141514872520714> **{0}** just arrived. Seems OP - please nerf.",
    "<:joinarrow:494141514872520714> **{0}** just slid into the server.",
    "<:joinarrow:494141514872520714> A **{0}** has spawned in the server.",
    "<:joinarrow:494141514872520714> Big **{0}** showed up!",
    "<:joinarrow:494141514872520714> Where’s **{0}**? In the server!",
    "<:joinarrow:494141514872520714> **{0}** hopped into the server. Kangaroo!!",
    "<:joinarrow:494141514872520714> **{0}** just showed up. Hold my beer.",
    "<:joinarrow:494141514872520714> Challenger approaching - **{0}** has appeared!",
    "<:joinarrow:494141514872520714> It's a bird! It's a plane! Nevermind, it's just **{0}**.",
    "<:joinarrow:494141514872520714> It's **{0}**! Praise the sun! \u005C[T]/",
    "<:joinarrow:494141514872520714> Never gonna give **{0}** up. Never gonna let **{0}** down.",
    "<:joinarrow:494141514872520714> Ha! **{0}** has joined! You activated my trap card!",
    "<:joinarrow:494141514872520714> Cheers, love! **{0}**'s here!",
    "<:joinarrow:494141514872520714> Hey! Listen! **{0}** has joined!",
    "<:joinarrow:494141514872520714> We've been expecting you **{0}**",
    "<:joinarrow:494141514872520714> It's dangerous to go alone, take **{0}**!",
    "<:joinarrow:494141514872520714> **{0}** has joined the server! It's super effective!",
    "<:joinarrow:494141514872520714> Cheers, love! **{0}** is here!",
    "<:joinarrow:494141514872520714> **{0}** is here, as the prophecy foretold.",
    "<:joinarrow:494141514872520714> **{0}** has arrived. Party's over.",
    "<:joinarrow:494141514872520714> Ready player **{0}**",
    "<:joinarrow:494141514872520714> **{0}** is here to kick butt and chew bubblegum. And **{0}** is all out of gum.",
    "<:joinarrow:494141514872520714> Hello. Is it **{0}** you're looking for?",
    "<:joinarrow:494141514872520714> **{0}** has joined. Stay a while and listen!",
    "<:joinarrow:494141514872520714> Roses are red, violets are blue, **{0}** joined this server with you"
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
            if ch.permissions_for(guild.me).send_messages and str(ch.type) not in ["4", "voice"]:
                return ch
    else:
        return guild.default_channel
    return None

def getDate(date:str):
    year = str(int(date[:4]))
    month = months[int(date[5:7])]
    day = str(int(date[8:10]))
    if day == "1": day = "1st"
    elif day == "2": day = "2nd"
    elif day == "3": day = "3rd"
    elif len(day) == 1: day += "th"
    elif day[1] == "1": day += "st"
    elif day[1] == "2": day += "nd"
    elif day[1] == "3": day += "rd"
    else: day += "th"
    return "%s %s, %s" % (month, day, year)

def search(iterable, string):
    matched = []
    matchedm = []
    for member in iterable:
        if string.lower() in member.name.lower():
            matched.append(member.mention)
            matchedm.append(member)
        elif member.nick != None:
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
            box = discord.Embed(title="Your search returned multiple results:", description=desc, color=0xddcc11)
        else:
            box = discord.Embed(title="Your search was too broad. Please use more specific keywords.", color=0xff8100)
        return box
    else:
        return matchedm[0]

def permEmbed(perm):
    return discord.Embed(title="Hey! I need this permission:", description="`%s`\nI won't be able to function properly unless I get this permission." % perm, color=err)

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

with open("info.txt", "r+") as voydinfo:
    j = -1
    for i in voydinfo.readlines():
        j += 1
        if j == 0:
            cmd_prefix = i[:-1]
        elif j == 1:
            version = i[:-1]

with open("guilds.txt", "r+") as voydguilds:
    j = -1
    for i in voydguilds.readlines():
        j += 1
        if j % 6 == 0:
            guildid = i[:-1]
        elif j % 6 == 1:
            guildset[guildid] = [i[:-1]]
        elif j % 6 in [2, 3, 5]:
            guildset[guildid].append(i[:-1])
        elif j % 6 == 4:
            guildset[guildid].append(i == "True\n")

def setupguild(guildid: str):
    if guildid not in guildset.keys():
        guildset[guildid] = ["{", "", "", False]

def updateSS():
    os.remove("guilds.txt")
    newss = open("guilds.txt", "w+")
    for guildid, lst in guildset.items():
        newss.write(str(guildid)+"\n")
        for item in lst:
            newss.write(str(item) + "\n")
    newss.close()

bot = commands.Bot(command_prefix=cmd_prefix)
bot.remove_command("help")

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
        else: box = discord.Embed(description=guildset[member.guild.id][2], color=0x43b581)
        chnchk = discord.utils.get(member.guild.channels, id=guildset[member.guild.id][1])
        if chnchk is None: await getDC(member.guild).send(choice(userjoinmsg).format(member.name), embed=box)
        else: await chnchk.send(choice(userjoinmsg).format(member.name), embed=box)
    if guildset[member.guild.id][4] != "":
        nmrole = discord.utils.get(member.guild.roles, id=guildset[member.guild.id][4])
        await bot.add_roles(member, nmrole)

@bot.event
async def on_member_remove(member):
    setupguild(member.guild.id)
    if guildset[member.guild.id][3] and member.id != 478945810378260490:
        chnchk = discord.utils.get(member.guild.channels, id=guildset[member.guild.id][1])
        if chnchk is None: await getDC(member.guild).send("<:leavearrow:494153240389091328> **%s** has left the guild." % member.name)
        else: await chnchk.send("<:leavearrow:494153240389091328> **%s** has left the guild." % member.name)

@bot.event
async def on_guild_join(guild):
    await discord.Object(id=480721130118971413).send(embed=discord.Embed(title="Added to guild", description="Voyd has joined the guild %s." % guild.name, color=scs))
    await getDC(guild).send(embed=discord.Embed(title="Hey, thanks for inviting me!", description="My prefix here is `{0}`. To change it, type `{0}prefix <prefix>`. ;)".format(cmd_prefix), color=scs))

@bot.event
async def on_guild_remove(guild):
    await discord.Object(id=480721130118971413).send(embed=discord.Embed(title="Removed from guild", description="Voyd has been removed from the guild %s." % guild.name, color=err))

@bot.event
async def on_message(message):
    if "<@461646073769885697>" in message.content:
        await message.channel.send("hi dere")
    if message.guild is not None and not message.author.bot:
        if message.guild.id in guildset.keys():
            bot.command_prefix = guildset[message.guild.id][0]
            await bot.process_commands(message)
            bot.command_prefix = cmd_prefix
        else:
            setupguild(message.guild.id)
            await bot.process_commands(message)

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
        box = discord.Embed(title="Command Categories", description="Type `%shelp <category>` to view commands in a category." % cmd_prefix, color=0)
        box.add_field(name="Bot", value="Commands that pertain to Voyd itself.", inline=False)
        box.add_field(name="Guild", value="Commands for roles, permissions, channels, and more.", inline=False)
        box.add_field(name="Member", value="Commands to manage your members.", inline=False)
        box.add_field(name="Chat", value="Commands to help with your chatting experience.", inline=False)
        box.add_field(name="Other", value="Absolutely random stuff.", inline=False)
    else:
        if category.lower() in ["b", "bot"]:
            box = discord.Embed(title="Bot Commands", description="Type `%shelp <category>` to view commands in a category." % cmd_prefix, color=0)
            box.add_field(name="Commands", value="""`help <item>`: You are here.
`change-prefix <prefix>`: Changes prefix.
`speed`: Show connection speed.
`invite`: Show invites for bot and official guild.
`voyd`: Shows Voyd's info.
`say <message>`: Says a message as the bot.""")
        elif category.lower() in ["s", "guild"]:
            box = discord.Embed(title="Guild Commands", description="Type `%shelp <category>` to view commands in a category." % cmd_prefix, color=0)
            box.add_field(name="Commands", value="`roles <func> [etc]`: Manage the guild's roles. See `roles help` for more.")
        elif category.lower() in ["m", "member"]:
            box = discord.Embed(title="Member Commands", description="Type `%shelp <category>` to view commands in a category." % cmd_prefix, color=0)
            box.add_field(name="Commands", value="""`member <func> [user]`: Manage users. See `member help` for more.
`warn <user> <message>`: Messages a user.
`kick <user>`: Kicks a user.
`ban <user>`: Bans a user.
`unban <user>`: Unbans a user.""")
        elif category.lower() in ["c", "chat"]:
            box = discord.Embed(title="Chat Commands", description="Type `%shelp <category>` to view commands in a category." % cmd_prefix, color=0)
            box.add_field(name="Commands", value="""`quote <msgid> [comment]`: Quote a message.""")
        elif category.lower() in ["o", "other"]:
            box = discord.Embed(title="Other Commands", description="Type `%shelp <category>` to view commands in a category." % cmd_prefix, color=0)
            box.add_field(name="Commands", value="None yet!")
        else:
            box = discord.Embed(title="Invalid category or command.", color=err)
    box.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    await ctx.send(embed=box)

@bot.command(aliases=["inv", "in", "iv", "voydinvite", "botinvite"])
async def invite(ctx):
    box = discord.Embed(title="Invite %s to your guild!" % bot.user.name, description="https://discordapp.com/oauth2/authorize?client_id=478945810378260490&scope=bot", color=0)
    box.add_field(name="Join the official %s guild!" % bot.user.name, value="https://discord.gg/5xgzh4r")
    box.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    await ctx.send(embed=box)
    await ctx.send("https://discord.gg/5xgzh4r")

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
    if len(etc) == 0:
        commented = False
    else:
        commented = True
    await ctx.channel.trigger_typing()
    for i in ctx.guild.channels:
        try:
            quotemessage = await i.get_message(messageid)
            quotemember = quotemessage.author
            success = True
        except Exception as e:
            pass
    if success:
        comment = "".join(etc) if commented else ""
        if quotemember.nick is None: quotename = quotemember.name
        else: quotename = quotemember.nick
        quotebox = discord.Embed(description=quotemessage.content, color=0x36383e)
        quotebox.set_author(name=quotename, icon_url=quotemember.avatar_url)
        try: await ctx.message.delete()
        except Exception as e: pass
        quotebox.set_footer(text=str(quotemessage.timestamp))
        await ctx.send(comment, embed=quotebox)
    else:
        await ctx.send("That message doesn't exist in this guild!")

@bot.command(aliases=["pm", "message", "directmessage", "privatemessage"])
async def dm(ctx, usearch, *etc):
    if ctx.message.author.guild_permissions.manage_guild:
        if ctx.message.guild.me.guild_permissions.manage_guild:
            if len(etc) == 0:
                await ctx.send(embed=discord.Embed(title="This command requires a message.", color=err))
                return
            if len(usearch) > 1:
                if usearch[0] + usearch[1] == "<@":
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

@bot.command(aliases=["commandprefix", "command-prefix", "commandp", "cprefix", "prefix", "set-prefix", "change-prefix", "sp", "setp", "changep"])
async def cp(ctx, prefixset=cmd_prefix):
    color = err
    guildid = ctx.message.guild.id
    setupguild(guildid)
    if ctx.message.author.guild_permissions.manage_guild:
        if len(prefixset) > 10:
            title = "Prefix cannot be longer than 10 characters."
        else:
            if guildset[guildid][0] == prefixset:
                title = "That's the current prefix."
            else:
                guildset[guildid][0] = prefixset
                title = "Prefix set."
                color = scs
        updateSS()
    else:
        color = err
        title = "Forbidden: Missing permission `manage_guild`."
    box = discord.Embed(title=title, color=color)
    await ctx.send(embed=box)

@bot.command(aliases=["nms", "new-member-settings", "nmsettings"])
async def newmembersettings(ctx, setting="l", *etc):
    guildid = ctx.message.guild.id
    setupguild(guildid)
    if setting.lower() in ["l", "li", "list"]:
        if guildset[guildid][3]:
            if guildset[guildid][1] == "": chn = "Not specified"
            else: chn = "<#" + guildset[guildid][1] + ">"
            if guildset[guildid][2] == "": msg = "None"
            else: msg = guildset[guildid][2]
            desc = None
        else:
            desc = "New member messages disabled for this guild."
            chn = None
            msg = None
        box = discord.Embed(title="New Member Settings", description=desc, color=scs)
        box.set_author(name=ctx.message.guild.name, icon_url=ctx.message.guild.icon_url)
        if desc is None:
            box.add_field(name="Channel", value=chn, inline=False)
            box.add_field(name="Message", value=msg, inline=False)
    elif setting.lower() in ["c", "chn", "channel"]:
        if ctx.message.author.guild_permissions.manage_guild:
            if ctx.message.guild.me.guild_permissions.manage_guild:
                if len(etc) > 0:
                    channel = etc[0]
                    if channel[2:-1].isdigit() and len(channel) == 21 and discord.utils.get(ctx.message.guild.channels, id=channel[2:-1]) is not None:
                        guildset[guildid][1] = channel[2:-1]
                        box = discord.Embed(title="Channel updated successfully.", description="New member channel: " + channel, color=scs)
                    else: box = discord.Embed(title="Invalid channel.", color=err)
                else: box = discord.Embed(title="Channel is a required argument.", color=err)
            else: box = discord.Embed(title="Woah, I don't have that permission.", color=err)
        else: box = discord.Embed(title="Forbidden: Missing permission 'manage_guild'.", color=err)
    else: box = discord.Embed(title="Invalid setting.", color=err)
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
    else:
        box = discord.Embed(title="Invalid function.", color=err)
    await ctx.send(embed=box)

@bot.command(aliases=["em", "ems", "emote", "emotes", "emoji", "customemoji", "ce", "custom-emoji"])
async def emojis(ctx, function="l"):
    if function.lower() in ["l", "li", "list", "all"]:
        ems = ""
        names = ""
        ids = ""
        for i in ctx.message.guild.emojis:
            ems += str(i) + "\n"
            names += "`:%s:`<:blank:498566453914501150>\n" % i.name
            ids += "`%s`<:blank:498566453914501150>\n" % i.id
        box = discord.Embed(color=0xbbcccc)
        box.add_field(name="Emoji", value=ems)
        box.add_field(name="Text", value=names)
        box.add_field(name="ID", value=ids)
        box.set_author(name=ctx.message.guild.name + " Emojis", icon_url=ctx.message.guild.icon_url)
    else:
        box = discord.Embed(title="Invalid function.", color=err)
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
                        if resp.content.lower() in ["y", "yes", "confirm", "t", "true", "yep", "yeah", "ok", "okay"]:
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
                    if args[2].lower() in ["y", "on", "t", "yes", "true", "active", "activate", "a"]:
                        perms = permissionstr(perm, perms, True)
                        await bot.edit_role(ctx.message.guild, role, permissions=perms)
                        box = discord.Embed(title="Edited role '%s' to have '%s' permission on." % (role.name, perm), color=scs)
                    elif args[2].lower() in ["n", "off", "f", "no", "false", "inactive", "deactivate", "i", "d"]:
                        perms = permissionstr(perm, perms, False)
                        await bot.edit_role(ctx.message.guild, role, permissions=perms)
                        box = discord.Embed(title="Edited role '%s' to have '%s' permission off." % (role.name, perm), color=scs)
                    else:
                        box = discord.Embed(title="Must be a valid boolean.", color=err)
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
                    box = discord.Embed(title="Role '%s' has been given to user %s." % (role.name, user.name if user.nick is None else user.nick), color=scs)
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
                    box = discord.Embed(title="Role '%s' has been taken from user %s." % (role.name, user.name if user.nick is None else user.nick), color=scs)
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
async def voicekick(ctx, *, msearch):
    pass

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
        elif member.nick != None:
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
    string = "".join(etc)
    matched = []
    matchedm = []
    for usr in await ctx.guild.bans():
        usr, reason = usr
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
        await matchedm[0].unban()
        box = discord.Embed(title="Member unbanned.", description="Unbanned: "+matched[0], color=scs)
    await ctx.send(embed=box)

"""@bot.command(aliases=["voice-kick", "vk", "voicek", "vkick"])
async def voicekick(member=None):
    if member"""

@bot.command()
async def shutdown(ctx):
    if ctx.author.id == "451357826753888256":
        await bot.close()

bot.run("TOKEN")
