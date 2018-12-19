"""
X A R K E N Z                2 0 1 8

█   █  ███  █   █ ████
█   █ █   █  █ █  █   █
 █ █  █   █   █   █   █
  █    ███    █   ████

Definitely not an Incredibles character...
"""

#611833175784-gfh8s12pjjm880ms799lj2b1lad5vjnv.apps.googleusercontent.com

try:
    import discord
    from discord.ext import commands
    from discord.ext.commands import Bot
    import asyncio
    import os
    from math import floor
    from time import time
    from random import choice, randint
    import datetime
except ImportError as e:
    print("Missing required modules. Error: " + str(e))

errors = 0
starttime = time()
err = 0xdd2200
scs = 0x22dd00
hexint = {"a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
serverset = {} # "serverid" : ["prefix", "channelid", "nmm", nmmactive, "roleid"]
games = ["with the roles", "myself", "with the stars", "a game", "gniyalp", "with server stuff", "with ban reasons", "with my foot"]
permlist = ["create_instant_invite",
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

def stripEnd(string, amount):
    result = ""
    for i in range(len(str(string)) - amount):
        result = result + str(string)[i]
    return result

def stripEndL(list, amount):
    result = []
    for i in range(len(list) - amount):
        result.append(list[i])
    return result

def stripBegin(string, amount):
    result = ""
    for i in range(len(str(string)) - amount):
        result += str(string)[i + amount]
    return result

def args_str(lst, sep=" "):
    string = ""
    for word in lst:
        string += word + sep
    return stripEnd(string, len(sep))

def tuplestrcolor(tup):
    r = stripBegin(str(hex(int(tup[0]))), 2)
    g = stripBegin(str(hex(int(tup[1]))), 2)
    b = stripBegin(str(hex(int(tup[2]))), 2)
    if len(r) == 1: r = "0" + r
    if len(g) == 1: g = "0" + g
    if len(b) == 1: b = "0" + b
    return r+g+b

def strcolor(string):
    stringbreak = []
    for i in string:
        if i.isalpha():
            stringbreak.append(hexint[i.lower()])
        else:
            stringbreak.append(int(i))
    r = (stringbreak[0] * 16) + stringbreak[1]
    g = (stringbreak[2] * 16) + stringbreak[3]
    b = (stringbreak[4] * 16) + stringbreak[5]
    return (r * (16 ** 4)) + (g * (16 ** 2)) + b

def getDC(server: discord.Server):
    if server.default_channel is None:
        for ch in server.channels:
            if ch.permissions_for(server.me).send_messages and str(ch.type) not in ["4", "voice"]:
                return ch
    else:
        return server.default_channel
    return None

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
        box = discord.Embed(title="Your search returned no results. Make sure spelling is correct.", color=0xdd2200)
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
    return discord.Embed(title="Hey! I need this permission:", description="`%s`\nI won't be able to function properly unless I get this permission." % perm, color=0xdd2200)

def permissionstr(string, permissions: discord.Permissions, active: bool):
    result = None
    if string == permlist[0]: permissions.create_instant_invites = active
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
    elif string == permlist[27]: permissions.manage_emojis = active
    return permissions

with open("info.txt", "r+") as voydinfo:
    j = -1
    for i in voydinfo.readlines():
        j += 1
        if j == 0:
            cmd_prefix = stripEnd(i, 1)
        elif j == 1:
            __version__ = stripEnd(i, 1)

with open("servers.txt", "r+") as voydservers:
    j = -1
    for i in voydservers.readlines():
        j += 1
        if j % 6 == 0:
            serverid = stripEnd(i, 1)
        elif j % 6 == 1:
            serverset[serverid] = [stripEnd(i, 1)]
        elif j % 6 in [2, 3, 5]:
            serverset[serverid].append(stripEnd(i, 1))
        elif j % 6 == 4:
            if i == "True\n":
                serverset[serverid].append(True)
            else:
                serverset[serverid].append(False)

def setupServer(serverid: str):
    if serverid not in serverset.keys():
        serverset[serverid] = ["{", "", "", False]

def updateSS():
    os.remove("servers.txt")
    newss = open("servers.txt", "w+")
    for i in serverset.items():
        newss.write(i + "\n")
    newss.close()

bot = commands.Bot(command_prefix=cmd_prefix)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("""Username: %s\nVersion: %s\nID: %s\nDefault prefix: %s\nStatus: ready""" % (bot.user.name, __version__, bot.user.id, bot.command_prefix))
    await bot.change_presence(game=discord.Game(name=choice(games)))

@bot.event
async def on_member_join(member):
    setupServer(member.server.id)
    if serverset[member.server.id][3]:
        if serverset[member.server.id][2] == "": box = None
        else: box = discord.Embed(description=serverset[member.server.id][2], color=0x43b581)
        chnchk = discord.utils.get(member.server.channels, id=serverset[member.server.id][1])
        if chnchk is None: await bot.send_message(getDC(member.server), choice(userjoinmsg).format(member.name), embed=box)
        else: await bot.send_message(chnchk, choice(userjoinmsg).format(member.name), embed=box)
    if serverset[member.server.id][4] != "":
        nmrole = discord.utils.get(member.server.roles, id=serverset[member.server.id][4])
        await bot.add_roles(member, nmrole)

@bot.event
async def on_member_remove(member):
    setupServer(member.server.id)
    if serverset[member.server.id][3] and member.id != "478945810378260490":
        chnchk = discord.utils.get(member.server.channels, id=serverset[member.server.id][1])
        if chnchk is None: await bot.send_message(getDC(member.server), "<:leavearrow:494153240389091328> **%s** has left the server." % member.name)
        else: await bot.send_message(chnchk, "<:leavearrow:494153240389091328> **%s** has left the server." % member.name)

@bot.event
async def on_server_join(server):
    await bot.send_message(discord.Object(id="480721130118971413"), embed=discord.Embed(title="Added to guild", description="Voyd has joined the server %s." % server.name, color=scs))
    await bot.send_message(getDC(server), embed=discord.Embed(title="Hey, thanks for inviting me!", description="My prefix here is `{0}`. To change it, type `{0}prefix <prefix>`. ;)".format(cmd_prefix), color=scs))

@bot.event
async def on_server_remove(server):
    await bot.send_message(discord.Object(id="480721130118971413"), embed=discord.Embed(title="Removed from guild", description="Voyd has been removed from the server %s." % server.name, color=err))

@bot.event
async def on_message(message):
    if type(stringIn("<@461646073769885697>", message.content)) == int:
        await bot.send_message(message.channel, "<:ping:459476736334364672>")
    if message.server != None and not message.author.bot:
        if message.server.id in serverset.keys():
            bot.command_prefix = serverset[message.server.id][0]
            await bot.process_commands(message)
            bot.command_prefix = cmd_prefix
        else:
            await bot.process_commands(message)

@bot.event
async def on_command_error(cmderror, ctx):
    global errors
    errors += 1

@bot.command(pass_context=True, aliases=["s", "stts", "runtime", "errors"])
async def status(ctx):
    box = discord.Embed(title="Status", description="Up and running!", color=scs)
    box.add_field(name="Start Time", value="`%s`" % str(starttime))
    box.add_field(name="Error Count", value=str(errors) + " error(s) during this run.")
    box.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    await bot.say(embed=box)

@bot.command(pass_context=True, aliases=["bot", "botinfo", "bot-info"])
async def voyd(ctx):
    servercount = 0
    for i in bot.servers:
        servercount += 1
    box = discord.Embed(title="Voyd#6046", description="The center of the Voyd.", color=0)
    box.add_field(name="ID", value=bot.user.id, inline=False)
    box.add_field(name="Creator", value="XarkenZ#6806", inline=False)
    box.add_field(name="Version", value=__version__, inline=False)
    box.add_field(name="Servers", value=servercount, inline=False)
    box.add_field(name="Language", value="`discord.py`, `asyncio`", inline=False)
    box.set_thumbnail(url=bot.user.avatar_url)
    await bot.send_message(ctx.message.channel, embed=box)

@bot.command(pass_context=True, aliases=["ping", "connection", "testconnection", "pong"])
async def speed(ctx):
    delta = datetime.datetime.utcnow() - ctx.message.timestamp
    delta = float(stripBegin(str(delta), 5))
    delta *= 100.0
    box = discord.Embed(title="Connection Speed", description=":control_knobs: %sms" % str(round(delta, 6)), color=0x2200dd) #(microseconds=1)
    box.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    box.set_footer(text="(one way)")
    hsend = await bot.say(embed=box)
    x = discord.utils.get(bot.get_all_emojis(), name="cross_mark")
    await bot.add_reaction(hsend, x)
    await bot.wait_for_reaction(emoji=x, user=ctx.message.author, message=hsend)
    await bot.delete_message(hsend)

@bot.command(pass_context=True, aliases=["h", "commands"])
async def help(ctx, category=None):
    if category is None:
        box = discord.Embed(title="Command Categories", description="Type `%shelp <category>` to view commands in a category." % cmd_prefix, color=0)
        box.add_field(name="Bot", value="Commands that pertain to Voyd itself.", inline=False)
        box.add_field(name="Server", value="Commands for roles, permissions, channels, and more.", inline=False)
        box.add_field(name="Member", value="Commands to manage your members.", inline=False)
        box.add_field(name="Chat", value="Commands to help with your chatting experience.", inline=False)
        box.add_field(name="Other", value="Absolutely random stuff.", inline=False)
    else:
        if category.lower() in ["b", "bot"]:
            box = discord.Embed(title="Bot Commands", description="Type `%shelp <category>` to view commands in a category." % cmd_prefix, color=0)
            box.add_field(name="Commands", value="""`help <item>`: You are here.
`change-prefix <prefix>`: Changes prefix.
`speed`: Show connection speed.
`invite`: Show invites for bot and official server.
`voyd`: Shows Voyd's info.
`say <message>`: Says a message as the bot.""")
        elif category.lower() in ["s", "server"]:
            box = discord.Embed(title="Server Commands", description="Type `%shelp <category>` to view commands in a category." % cmd_prefix, color=0)
            box.add_field(name="Commands", value="`roles <func> [args]`: Manage the server's roles. See `roles help` for more.")
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
            box = discord.Embed(title="Invalid category or command.", color=0xdd2200)
    box.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    hsend = await bot.send_message(ctx.message.channel, embed=box)
    x = discord.utils.get(bot.get_all_emojis(), name="cross_mark")
    await bot.add_reaction(hsend, x)
    await bot.wait_for_reaction(emoji=x, user=ctx.message.author, message=hsend)
    await bot.delete_message(hsend)

@bot.command(pass_context=True, aliases=["inv", "in", "iv", "voydinvite", "botinvite"])
async def invite(ctx):
    box = discord.Embed(title="Invite %s to your server!" % bot.user.name, description="https://discordapp.com/oauth2/authorize?client_id=478945810378260490&scope=bot", color=0)
    box.add_field(name="Join the official %s server!" % bot.user.name, value="https://discord.gg/5xgzh4r")
    box.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    await bot.send_message(ctx.message.channel, embed=box)
    await bot.send_message(ctx.message.channel, "https://discord.gg/5xgzh4r")

@bot.command(pass_context=True, aliases=["purge", "purgemessages", "purge-messages"])
async def p(ctx, messages, user=None):
    if messages.isdigit():
        messages = int(messages)
        if messages <= 500 and messages > 0:
            req = user
            if user is not None:
                user = discord.utils.get(ctx.message.server.members, name=user)
                if user is None:
                    user = discord.utils.get(ctx.message.server.members, id=user)
                    if user is None:
                        try:
                            if req[2] == "!": num = 3
                            else: num = 2
                            user = discord.utils.get(ctx.message.server.members, id=stripEnd(stripBegin(user, num), 1))
                        except discord.ext.commands.errors.CommandInvokeError: pass
                        if user is None:
                            user = search(ctx.message.server.members, req)
                            if type(user) == discord.Embed:
                                return await bot.say(embed=user)
            if ctx.message.author.server_permissions.manage_messages or user == ctx.message.author:
                if ctx.message.server.me.server_permissions:
                    if user is None:
                        await bot.purge_from(channel=ctx.message.channel, limit=messages+1)
                        box = discord.Embed(title="Purged %s messages." % str(messages), color=scs)
                    else:
                        def user_check(m):
                            return m.author == user
                        await bot.purge_from(channel=ctx.message.channel, limit=messages+1, check=user_check)
                        box = discord.Embed(title="Purged messages by %s in a range of %s messages." % (user.name, str(messages)), color=scs)
                else: box = discord.Embed(title="Woah, I don't have that permission.", color=err)
            else: box = discord.Embed(title="Missing permission: 'manage_messages'. (Purging your own messages also works!)", color=err)
        else: box = discord.Embed(title="Limit must be from 1 to 500.", color=err)
    else: box = discord.Embed(title="Limit is a required argument.", color=err)
    msg = await bot.say(embed=box)
    await asyncio.sleep(3)
    await bot.delete_message(msg)

@bot.command(pass_context=True, aliases=["q", "quotemessage", "quote-message", "retrieve"])
async def quote(ctx, messageid, *args):
    success = False
    if args == tuple():
        commented = False
    else:
        commented = True
    await bot.send_typing(ctx.message.channel)
    for i in ctx.message.server.channels:
        try:
            quotemessage = await bot.get_message(i, messageid)
            quotemember = quotemessage.author
            success = True
        except Exception as e:
            pass
    if success:
        if commented:
            comment = ""
            for word in args:
                comment = comment + word + " "
            comment = stripEnd(comment, 1)
        else: comment = ""
        if quotemember.nick == None:
            quotename = quotemember.name
        else:
            quotename = quotemember.nick
        quote = discord.Embed(description=quotemessage.content, color=0x36383e)
        quote.set_author(name=quotename, icon_url=quotemember.avatar_url)
        try: await bot.delete_message(ctx.message)
        except Exception as e: pass
        quote.set_footer(text=str(quotemessage.timestamp))
        await bot.send_message(ctx.message.channel, comment, embed=quote)
    else:
        await bot.say("That message doesn't exist in this server!")

@bot.command(pass_context=True, aliases=["pm", "message", "directmessage", "privatemessage"])
async def dm(ctx, usearch, *args):
    if ctx.message.author.server_permissions.manage_server:
        if ctx.message.server.me.server_permissions.manage_server:
            if len(args) == 0:
                await bot.send_message(ctx.message.channel, embed=discord.Embed(title="This command requires a message.", color=0xdd2200))
                return
            if len(usearch) > 1:
                if usearch[0] + usearch[1] == "<@":
                    get = ""
                    for i in usearch:
                        if i != " ":
                            get += i
                    if get[2] == "!":
                        user = ctx.message.server.get_member(stripEnd(stripBegin(get, 3), 1))
                    else:
                        user = ctx.message.server.get_member(stripEnd(stripBegin(get, 2), 1))
                else:
                    user = search(ctx.message.server.members, usearch)
            else:
                user = search(ctx.message.server.members, usearch)
            if type(user) == discord.Member:
                if user.bot:
                    box = discord.Embed(title="Bots are too powerful to send messages to!", description="Recipient: %s (%s)" % (user.mention, str(user.status)), color=0xdd2200)
                else:
                    await bot.send_message(user, args_str(args))
                    box = discord.Embed(title="Message sent.", color=0x22dd00)
                    box.add_field(name="Recipient:", value="%s (%s)" % (user.mention, str(user.status)))
                    box.add_field(name="Message:", value=args_str(args), inline=False)
            else:
                box = user
        else:
            box = discord.Embed(title="Woah, I don't have that permission.", color=err)
    else:
        box = discord.Embed(title="Forbidden: Missing permission `manage_server`.", color=0xdd2200)
    await bot.send_message(ctx.message.channel, embed=box)

@bot.command(pass_context=True, aliases=["commandprefix", "command-prefix", "commandp", "cprefix", "prefix", "set-prefix", "change-prefix", "sp", "setp", "changep"])
async def cp(ctx, prefixset=cmd_prefix):
    if len(prefixset) > 10:
        title = "Prefix cannot be longer than 10 characters."
    else:
        setupServer(ctx.message.server.id)
        if serverset[ctx.message.server.id] == prefixset:
            title = "That's the current prefix."
        else:
            serverset[ctx.message.server.id] = prefixset
            title = "Prefix set."
    updateSS()
    box = discord.Embed(title=title, color=0xdd2200)
    await bot.send_message(ctx.message.channel, embed=box)

@bot.command(pass_context=True, aliases=["nms", "new-member-settings", "nmsettings"])
async def newmembersettings(ctx, setting="l", *args):
    serverid = ctx.message.server.id
    setupServer(serverid)
    if setting.lower() in ["l", "li", "list"]:
        if serverset[serverid][3]:
            if serverset[serverid][1] == "": chn = "Not specified"
            else: chn = "<#" + serverset[serverid][1] + ">"
            if serverset[serverid][2] == "": msg = "None"
            else: msg = serverset[serverid][2]
            desc = None
        else:
            desc = "New member messages disabled for this server."
            chn = None
            msg = None
        box = discord.Embed(title="New Member Settings", description=desc, color=0x22dd00)
        box.set_author(name=ctx.message.server.name, icon_url=ctx.message.server.icon_url)
        if desc is None:
            box.add_field(name="Channel", value=chn, inline=False)
            box.add_field(name="Message", value=msg, inline=False)
    elif setting.lower() in ["c", "chn", "channel"]:
        if ctx.message.author.server_permissions.manage_server:
            if ctx.message.server.me.server_permissions.manage_server:
                if len(args) > 0:
                    channel = args[0]
                    if stripEnd(stripBegin(channel, 2), 1).isdigit() and len(channel) == 21 and discord.utils.get(ctx.message.server.channels, id=stripEnd(stripBegin(channel, 2), 1)) is not None:
                        serverset[serverid][1] = stripEnd(stripBegin(channel, 2), 1)
                        box = discord.Embed(title="Channel updated successfully.", description="New member channel: " + channel, color=scs)
                    else: box = discord.Embed(title="Invalid channel.", color=err)
                else: box = discord.Embed(title="Channel is a required argument.", color=err)
            else: box = discord.Embed(title="Woah, I don't have that permission.", color=err)
        else: box = discord.Embed(title="Forbidden: Missing permission 'manage_server'.", color=err)
    else: box = discord.Embed(title="Invalid setting.", color=0xdd2200)
    await bot.say(embed=box)

@bot.command(pass_context=True, aliases=["channel", "c", "chn", "ch"])
async def channels(ctx, function="l", channel=None):
    if function.lower() in ["l", "li", "list", "all"]:
        times = ""
        names = ""
        positions = ""
        sortchannels = {}
        channellist = []
        for i in ctx.message.server.channels:
            if str(i.type) != "4": sortchannels[i.position] = i
        for i in sorted(sortchannels.keys()):
            channellist.append(sortchannels[i])
        if len(channellist) > 15:
            stripEndL(channellist, len(channellist) - 15)
        for c in channellist:
            times += ":clock2: `" + stripEnd(str(c.created_at), 16) + "`\n"
            positions += ":pushpin: `" + str(c.position) + "`\n"
            if str(c.type) == "4":
                names += ":small_red_triangle_down: **%s**\n" % c.name.upper()
            elif str(c.type) == "voice":
                names += ":loud_sound: %s\n" % c.name
            else:
                names += ":page_facing_up: " + c.mention + "\n"
        box = discord.Embed(color=0x22dd00)
        box.set_author(name="%s Channels (%s)" % (ctx.message.server.name, str(len(channellist))), icon_url=ctx.message.server.icon_url)
        box.add_field(name="Channel", value=names)
        box.add_field(name="Position", value=positions)
        box.add_field(name="Created", value=times)
    elif function.lower() in ["i", "inf", "info"]:
        if channel is None:
            channel = ctx.message.channel
        else:
            chn = channel
            channel = discord.utils.get(ctx.message.server.channels, name=channel)
            if channel is None:
                channel = discord.utils.get(ctx.message.server.channels, id=stripBegin(stripEnd(chn, 1), 2))
                if channel is None:
                    box = discord.Embed(title="Channel not found.", color=0xdd2200)
                    return await bot.send_message(ctx.message.channel, embed=box)
        if str(channel.type) == "text": nm = channel.mention
        else: nm = channel.name
        box = discord.Embed(title="Channel Info", description=nm, color=0x22dd00)
        if channel.topic == "": topic = "None"
        else: topic = str(channel.topic)
        box.add_field(name="Topic", value=topic, inline=False)
        box.add_field(name="Information", value="**ID:** `%s`\n**Type:** %s\n**Created at:** `%s`\n**Private:** %s" % (channel.id, str(channel.type), str(channel.created_at), str(channel.is_private)), inline=False)
    else:
        box = discord.Embed(title="Invalid function.", color=0xdd2200)
    await bot.send_message(ctx.message.channel, embed=box)

@bot.command(pass_context=True, aliases=["em", "ems", "emote", "emotes", "emoji", "customemoji", "ce", "custom-emoji"])
async def emojis(ctx, function="l"):
    if function.lower() in ["l", "li", "list", "all"]:
        ems = ""
        names = ""
        ids = ""
        for i in ctx.message.server.emojis:
            ems += str(i) + "\n"
            names += "`:%s:`<:blank:498566453914501150>\n" % i.name
            ids += "`%s`<:blank:498566453914501150>\n" % i.id
        box = discord.Embed(color=0xbbcccc)
        box.add_field(name="Emoji", value=ems)
        box.add_field(name="Text", value=names)
        box.add_field(name="ID", value=ids)
        box.set_author(name=ctx.message.server.name + " Emojis", icon_url=ctx.message.server.icon_url)
    else:
        box = discord.Embed(title="Invalid function.", color=err)
    await bot.say(embed=box)

@bot.command(pass_context=True, aliases=["rl", "role", "rolelist", "serverroles", "rls"])
async def roles(ctx, function="l", arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
    if function in ["l", "li", "list", "all"]:
        names = ""
        pos = ""
        members = ""
        sortroles = {}
        rolelist = []
        roleamt = 0
        for i in ctx.message.server.roles:
            roleamt += 1
            sortroles[i.position] = i
        for i in sorted(sortroles.keys(), reverse=True):
            rolelist.append(sortroles[i])
        for role in rolelist:
            memberamt = 0
            if role.name == "@everyone": names += ":clipboard: @everyone\n"
            else: names += ":clipboard: " + role.mention + "\n"
            pos += ":pushpin: " + str(role.position) + "\n"
            for member in ctx.message.server.members:
                if role in member.roles:
                    memberamt += 1
            members += "<:members:479657677212090368> " + str(memberamt) + "\n"
        box = discord.Embed(color=0xaa00cc)
        box.add_field(name="Role", value=names)
        box.add_field(name="Position", value=pos)
        box.add_field(name="Members", value=members)
        box.set_author(name="%s Roles (%s)" % (ctx.message.server.name, str(roleamt)), icon_url=ctx.message.server.icon_url)
        if len(sortroles) >= 15:
            box.set_footer(text="You asked for it.")
    elif function in ["m", "me"]:
        names = ""
        pos = ""
        members = ""
        sortroles = {}
        rolelist = []
        for i in ctx.message.author.roles:
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
            for member in ctx.message.server.members:
                if role in member.roles:
                    memberamt += 1
            members += "<:members:479657677212090368> " + str(memberamt) + "\n"
        box = discord.Embed(color=0xaa00cc)
        box.add_field(name="Role", value=names)
        box.add_field(name="Position", value=pos)
        box.add_field(name="Members", value=members)
        box.set_author(name="%s's Roles" % ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
    elif function in ["f", "for", "o", "of"]:
        if arg1 == None:
            box = discord.Embed(title="This function requires a member.", color=0xdd2200)
        elif arg1[0] + arg1[1] == "<@":
            get = ""
            for i in arg1:
                if i != " ":
                    get += i
            if get[2] == "!":
                user = ctx.message.server.get_member(stripEnd(stripBegin(get, 3), 1))
            else:
                user = ctx.message.server.get_member(stripEnd(stripBegin(get, 2), 1))
        else:
            user = search(ctx.message.server.members, arg1)
        if type(user) == discord.Member:
            names = ""
            pos = ""
            members = ""
            sortroles = {}
            rolelist = []
            for i in user.roles:
                if i.name != "@everyone":
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
                for member in ctx.message.server.members:
                    if role in member.roles:
                        memberamt += 1
                members += "<:members:479657677212090368> " + str(memberamt) + "\n"
            box = discord.Embed(color=0xaa00cc)
            box.add_field(name="Role", value=names)
            box.add_field(name="Position", value=pos)
            box.add_field(name="Members", value=members)
            box.set_author(name="%s's Roles" % user.name, icon_url=user.avatar_url)
        else:
            box = user
    elif function.lower() in ["i", "inf", "info", "g", "get"]:
        role = arg1
        if role == None:
            box = discord.Embed(title="No role has been stated.", color=0xdd2200)
        else:
            if role[0] == "<":
                role = stripBegin(role, 3)
                role = stripEnd(role, 1)
                if discord.utils.get(ctx.message.server.roles, name=role) == None:
                    box = discord.Embed(title="That role doesn't exist.", color=0xdd2200)
                    await bot.send_message(ctx.message.channel, embed=box)
                    return
                else:
                    role = discord.utils.get(ctx.message.server.roles, id=role)
            elif role[0].isdigit():
                if discord.utils.get(ctx.message.server.roles, name=role) == None:
                    box = discord.Embed(title="That role doesn't exist.", color=0xdd2200)
                    await bot.send_message(ctx.message.channel, embed=box)
                    return
                else:
                    role = discord.utils.get(ctx.message.server.roles, id=role)
            else:
                if role[0] == "@":
                    role = stripBegin(role, 1)
                if discord.utils.get(ctx.message.server.roles, name=role) == None:
                    box = discord.Embed(title="That role doesn't exist.", color=0xdd2200)
                    await bot.send_message(ctx.message.channel, embed=box)
                    return
                else:
                    role = discord.utils.get(ctx.message.server.roles, name=role)
            membercount = 0
            for member in ctx.message.server.members:
                if role in member.roles:
                    membercount += 1
            box = discord.Embed(title="Role: " + role.name, description="**Mention:** %s\n**ID:** %s\n**Color:** %s %s\n**Mentionable:** %s\n**Displays separately:** %s\n**Members:** %s" % (role.mention, role.id, stripBegin(str(hex(role.color.value)), 2).upper(), str(role.color.to_tuple()), str(role.mentionable), str(role.hoist), membercount), color=role.color.value)
    elif function.lower() in ["create", "c"]:
        if ctx.message.author.server_permissions.manage_roles:
            if ctx.message.server.me.server_permissions.manage_roles:
                if arg1 is None:
                    box = discord.Embed(title="Role must have a name.", color=0xdd2200)
                else:
                    await bot.create_role(ctx.message.server, name=arg1)
                    box = discord.Embed(title="Role created.", description="Use `role edit <permission> <on|off>` to edit this role (and other roles!).", color=0x22dd00)
            else:
                box = discord.Embed(title="Woah, I don't have that permission.", color=0xdd2200)
                #await bot.send_message(ctx.message.server.owner, embed=permEmbed("manage_roles"))
        else:
            box = discord.Embed(title="Forbidden: Missing permission 'manage_roles'.", color=0xdd2200)
    elif function.lower() in ["d", "del", "delete"]:
        if ctx.message.author.server_permissions.manage_roles:
            if ctx.message.server.me.server_permissions.manage_roles:
                role = arg1
                if role[0] == "<":
                    role = stripBegin(role, 3)
                    role = stripEnd(role, 1)
                    if discord.utils.get(ctx.message.server.roles, name=role) == None:
                        box = discord.Embed(title="That role doesn't exist.", color=0xdd2200)
                        await bot.send_message(ctx.message.channel, embed=box)
                        return
                    else:
                        role = discord.utils.get(ctx.message.server.roles, id=role)
                elif role[0].isdigit():
                    if discord.utils.get(ctx.message.server.roles, name=role) == None:
                        box = discord.Embed(title="That role doesn't exist.", color=0xdd2200)
                        await bot.send_message(ctx.message.channel, embed=box)
                        return
                    else:
                        role = discord.utils.get(ctx.message.server.roles, id=role)
                else:
                    if role[0] == "@":
                        role = stripBegin(role, 1)
                    if discord.utils.get(ctx.message.server.roles, name=role) == None:
                        box = discord.Embed(title="That role doesn't exist.", color=0xdd2200)
                        await bot.send_message(ctx.message.channel, embed=box)
                        return
                    else:
                        role = discord.utils.get(ctx.message.server.roles, name=role)
                if ctx.message.author.server_permissions.manage_roles:
                    if ctx.message.server.me.server_permissions.manage_roles:
                        await bot.send_message(ctx.message.channel, embed=discord.Embed(title="Are you sure you want to delete '%s'?" % role.name, color=scs))
                        resp = await bot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
                        if resp.content.lower() in ["y", "yes", "confirm", "t", "true", "yep", "yeah", "ok", "okay"]:
                            await bot.delete_role(ctx.message.server, role)
                            box = discord.Embed(title="Role deleted.", color=scs)
                        else:
                            box = discord.Embed(title="Cancelled deletion.", color=err)
                    else:
                        box = discord.Embed(title="Woah, I don't have that permission.", color=err)
                else:
                    box = discord.Embed(title="Forbidden: Missing permission 'manage_roles'.", color=err)
            else:
                box = discord.Embed(title="Woah, I don't have that permission.", color=0xdd2200)
                #await bot.send_message(ctx.message.server.owner, embed=permEmbed("manage_roles"))
        else:
            box = discord.Embed(title="Forbidden: Missing permission 'manage_roles'.", color=0xdd2200)
    elif function.lower() in ["edit", "e", "change", "chg", "set", "s"]:
        if not ctx.message.author.server_permissions.manage_roles:
            box = discord.Embed(title="Forbidden: Missing permission 'manage_roles'.", color=err)
            await bot.send_message(ctx.message.channel, embed=box)
            return
        if not ctx.message.server.me.server_permissions.manage_roles:
            box = discord.Embed(title="Woah, I don't have that permission.", color=err)
            await bot.send_message(ctx.message.channel, embed=box)
            return
        role = arg1
        if role is None:
            box = discord.Embed(title="No role has been stated.", color=0xdd2200)
        else:
            if role[0] == "<":
                role = stripBegin(role, 3)
                role = stripEnd(role, 1)
                if discord.utils.get(ctx.message.server.roles, name=role) == None:
                    box = discord.Embed(title="That role doesn't exist.", color=0xdd2200)
                    await bot.send_message(ctx.message.channel, embed=box)
                    return
                else:
                    role = discord.utils.get(ctx.message.server.roles, id=role)
            elif role[0].isdigit():
                if discord.utils.get(ctx.message.server.roles, name=role) == None:
                    box = discord.Embed(title="That role doesn't exist.", color=0xdd2200)
                    await bot.send_message(ctx.message.channel, embed=box)
                    return
                else:
                    role = discord.utils.get(ctx.message.server.roles, id=role)
            else:
                if role[0] == "@":
                    role = stripBegin(role, 1)
                if discord.utils.get(ctx.message.server.roles, name=role) == None:
                    box = discord.Embed(title="That role doesn't exist.", color=0xdd2200)
                    await bot.send_message(ctx.message.channel, embed=box)
                    return
                else:
                    role = discord.utils.get(ctx.message.server.roles, name=role)
        perm = arg2
        if perm is None:
            box = discord.Embed(title="No permission has been stated.", color=err)
        else:
            if perm.lower() in permlist:
                perms = role.permissions
                perm = perm.lower()
                if arg3 is None:
                    box = discord.Embed(title="No bool has been stated.", color=err)
                else:
                    if arg3.lower() in ["y", "on", "t", "yes", "true", "active", "activate", "a"]:
                        perms = permissionstr(perm, perms, True)
                        await bot.edit_role(ctx.message.server, role, permissions=perms)
                        box = discord.Embed(title="Edited role '%s' to have '%s' permission on." % (role.name, perm), color=scs)
                    elif arg3.lower() in ["n", "off", "f", "no", "false", "inactive", "deactivate", "i", "d"]:
                        perms = permissionstr(perm, perms, False)
                        await bot.edit_role(ctx.message.server, role, permissions=perms)
                        box = discord.Embed(title="Edited role '%s' to have '%s' permission off." % (role.name, perm), color=scs)
                    else:
                        box = discord.Embed(title="Must be a valid boolean.", color=err)
            elif perm.lower() in ["color", "colour"]:
                if arg3 is None:
                    await bot.edit_role(ctx.message.server, role, color=discord.Color(value=0))
                    box = discord.Embed(title="Updated role color to default.", color=scs)
                else:
                    if len(arg3) == 6:
                        success = True
                        for i in arg3:
                            if not i.isdigit() and i.lower() not in ["a", "b", "c", "d", "e", "f"]: success = False
                        if success:
                            await bot.edit_role(ctx.message.server, role, color=discord.Color(value=strcolor(arg3)))
                            box = discord.Embed(title="Updated role color to `%s`." % arg3.lower(), color=scs)
                        else:
                            box = discord.Embed(title="Invalid color.", color=err)
                    else:
                        if not arg3.isdigit() or not arg4.isdigit() or not arg5.isdigit():
                            box = discord.Embed(title="Invalid color.", color=err)
                        elif int(arg3) > 255 or int(arg4) > 255 or int(arg5) > 255:
                            box = discord.Embed(title="Invalid color.", color=err)
                        else:
                            await bot.edit_role(ctx.message.server, role, color=discord.Color(value=strcolor(tuplestrcolor((arg3, arg4, arg5)))))
                            box = discord.Embed(title="Updated role color to `%s` (%s, %s, %s)." % (tuplestrcolor((arg3, arg4, arg5)), arg3, arg4, arg5), color=scs)
            else:
                box = discord.Embed(title="Invalid property. See role help for a list of valid permissions.", color=err)
    elif function.lower() in ["g", "give", "ap", "append", "a", "add"]:
        if arg1 is None or arg2 is None:
            box = discord.Embed(title="This function uses two arguments, <member> and <role>.", color=err)
        else:
            if not ctx.message.author.server_permissions.manage_roles:
                box = discord.Embed(title="Forbidden: Missing permission 'manage_roles'.", color=err)
            elif not ctx.message.server.me.server_permissions.manage_roles:
                box = discord.Embed(title="Woah, I don't have that permission.", color=err)
            else:
                role = arg1
                if role[0] == "<":
                    role = stripBegin(role, 3)
                    role = stripEnd(role, 1)
                    if discord.utils.get(ctx.message.server.roles, name=role) == None:
                        box = discord.Embed(title="That role doesn't exist.", color=0xdd2200)
                        await bot.send_message(ctx.message.channel, embed=box)
                        return
                    else:
                        role = discord.utils.get(ctx.message.server.roles, id=role)
                elif role[0].isdigit():
                    if discord.utils.get(ctx.message.server.roles, name=role) == None:
                        box = discord.Embed(title="That role doesn't exist.", color=0xdd2200)
                        await bot.send_message(ctx.message.channel, embed=box)
                        return
                    else:
                        role = discord.utils.get(ctx.message.server.roles, id=role)
                else:
                    if role[0] == "@":
                        role = stripBegin(role, 1)
                    if discord.utils.get(ctx.message.server.roles, name=role) == None:
                        box = discord.Embed(title="That role doesn't exist.", color=0xdd2200)
                        await bot.send_message(ctx.message.channel, embed=box)
                        return
                    else:
                        role = discord.utils.get(ctx.message.server.roles, name=role)
                if arg2[0] + arg2[1] == "<@":
                    get = ""
                    for i in arg2:
                        if i != " ":
                            get += i
                    if get[2] == "!":
                        user = ctx.message.server.get_member(stripEnd(stripBegin(get, 3), 1))
                    else:
                        user = ctx.message.server.get_member(stripEnd(stripBegin(get, 2), 1))
                else:
                    user = search(ctx.message.server.members, arg2)
                if type(user) == discord.Member:
                    await bot.add_roles(user, role)
                    if user.nick is None: uname = user.name
                    else: uname = user.nick
                    box = discord.Embed(title="Role %s has been given to user %s." % (role.name, uname), color=scs)
                else:
                    box = user
    #elif function.lower() in ["r", "rm", "rem", "remove"]:
    else:
        box = discord.Embed(title="Invalid function.", color=err)
    await bot.say(embed=box)

@bot.command(pass_context=True, aliases=["user", "us", "m"])
async def member(ctx, func="i", user=None):
    if func.lower() in ["i", "info", "information"]:
        if user is None:
            user = ctx.message.author
        else:
            user = search(ctx.message.server.members, user)
            if type(user) == discord.Embed:
                await bot.send_message(ctx.message.channel, embed=user)
                return
        joindate = stripEnd(str(user.joined_at), 16)
        jddate = stripEnd(str(user.created_at), 16)
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
        elif str(user.status) == "offline": status = "<:offline:486344317624123394> Offline/Invisible"
        else: status = ":grey_question: " + str(user.status).title()
        box.add_field(name="Status", value=status, inline=False)
        #box.add_field(name="")
        box.add_field(name="Joined %s" % ctx.message.server.name, value="%s %s, %s" % (months[joinstats[1]], joinday, joinstats[0]), inline=False)
        box.add_field(name="Joined Discord", value="%s %s, %s" % (months[jdstats[1]], jdday, jdstats[0]), inline=False)
        box.set_thumbnail(url=user.avatar_url)
        if user.id == "478945810378260490":
            box.set_footer(text="Use the 'voyd' command to learn more about me.")
        elif user.id == "451357826753888256":
            box.set_footer(text="Hey, I know that guy!")
    else:
        box = discord.Embed(title="Invalid function.", color=err)
    await bot.send_message(ctx.message.channel, embed=box)

@bot.command(pass_context=True)
async def say(ctx, *args):
    text = ""
    for word in args:
        text = text + word + " "
    text = stripEnd(text, 1)
    if ctx.message.author.id == "451357826753888256" or ctx.message.author.id == "451033390255439883" or ctx.message.author.id == "403193961562505216":
        foot = False
        try:
            await bot.delete_message(ctx.message)
        except Exception as e:
            foot = True
        if foot:
            box = discord.Embed(title="Unable to delete invoke.", color=0xdd2200)
            await bot.send_message(ctx.message.channel, text, embed=box)
        else:
            await bot.send_message(ctx.message.channel, text)
    else:
        await bot.say("Missing permissions for this command.")

@bot.command(pass_context=True, aliases=["vk", "voice-kick", "voicek", "vkick"])
async def voicekick(ctx, *, msearch):
    pass

@bot.command(pass_context=True, aliases=["vb", "voice-ban", "voiceb", "vban"])
async def voiceban(ctx, *, msearch):
    pass

@bot.command(pass_context=True, aliases=["k"])
async def kick(ctx, *args):
    perms = ctx.message.author.server_permissions
    if not perms.kick_members:
        box = discord.Embed(title="Forbidden: Missing permission 'kick_members'.", color=0xdd2200)
        await bot.send_message(ctx.message.channel, embed=box)
        return
    if not ctx.message.server.me.server_permissions.kick_members:
        box = discord.Embed(title="Woah, I don't have that permission.", color=0xdd2200)
        await bot.send_message(ctx.message.channel, embed=box)
        #await bot.send_message(ctx.message.server.owner, embed=permEmbed("kick_members"))
        return
    string = ""
    for word in args:
        string = string + word + " "
    string = stripEnd(string, 1)
    matched = []
    matchedm = []
    for member in ctx.message.server.members:
        if string.lower() in member.name.lower():
            matched.append(member.mention + " (%s)" % (member.status))
            matchedm.append(member)
        elif member.nick != None:
            if string.lower() in member.nick.lower():
                matched.append(member.mention + " (%s)" % (member.status))
                matchedm.append(member)
    if matched == []:
        box = discord.Embed(title="Your search returned no results. Make sure spelling is correct.", color=0xdd2200)
    elif len(matched) > 1:
        if len(matched) <= 15:
            desc = ""
            for i in matched:
                desc += i + "\n"
            box = discord.Embed(title="Your search returned multiple results:", description=desc, color=0xddcc11)
        else:
            box = discord.Embed(title="Your search was too broad. Please use more specific keywords.", color=0xff8100)
    else:
        if matchedm[0] == ctx.message.server.me:
            await bot.send_message(ctx.message.channel, embed=discord.Embed(title="I suppose this is goodbye. Are you sure you want to kick me?", color=0xdd2200))
            resp = await bot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            if resp.content.lower() in ["y", "yes", "confirm", "t", "true", "yep", "yeah", "ok", "okay"]:
                box = discord.Embed(title="Well, bye.", color=scs)
                await bot.say(embed=box)
                await bot.leave_server(ctx.message.server)
                return
            else:
                box = discord.Embed(title="Kicking cancelled.", color=err)
            return
        else:
            await bot.kick(matchedm[0])
            box = discord.Embed(title="Member kicked.", description=matched[0], color=0x22dd00)
    await bot.send_message(ctx.message.channel, embed=box)

@bot.command(pass_context=True, aliases="b")
async def ban(ctx, *args):
    perms = ctx.message.author.server_permissions
    if not perms.ban_members:
        box = discord.Embed(title="Forbidden: Missing permission 'ban_members'.", color=0xdd2200)
        await bot.send_message(ctx.message.channel, embed=box)
        return
    if not ctx.message.server.me.server_permissions.ban_members:
        box = discord.Embed(title="Woah, I don't have that permission.", color=0xdd2200)
        await bot.send_message(ctx.message.channel, embed=box)
        #await bot.send_message(ctx.message.server.owner, embed=permEmbed("kick_members"))
        return
    string = ""
    for word in args:
        string = string + word + " "
    string = stripEnd(string, 1)
    matched = []
    matchedm = []
    for member in ctx.message.server.members:
        if string.lower() in member.name.lower():
            matched.append(member.mention + " (%s)" % (member.status))
            matchedm.append(member)
        elif member.nick != None:
            if string.lower() in member.nick.lower():
                matched.append(member.mention + " (%s)" % (member.status))
                matchedm.append(member)
    if matched == []:
        box = discord.Embed(title="Your search returned no results. Make sure spelling is correct.", color=0xdd2200)
    elif len(matched) > 1:
        if len(matched) <= 15:
            desc = ""
            for i in matched:
                desc += i + "\n"
            box = discord.Embed(title="Your search returned multiple results:", description=desc, color=0xddcc11)
        else:
            box = discord.Embed(title="Your search was too broad. Please use more specific keywords.", color=0xff8100)
    else:
        await bot.ban(matchedm[0])
        box = discord.Embed(title="Member banned.", description=matched[0], color=0x22dd00)
    await bot.send_message(ctx.message.channel, embed=box)

@bot.command(pass_context=True, aliases=["ub"])
async def unban(ctx, *args):
    perms = ctx.message.author.server_permissions
    if not perms.ban_members:
        box = discord.Embed(title="Forbidden: Missing permission 'ban_members'.", color=0xdd2200)
        await bot.send_message(ctx.message.channel, embed=box)
        return
    if not ctx.message.server.me.server_permissions.ban_members:
        box = discord.Embed(title="Woah, I don't have that permission.", color=0xdd2200)
        await bot.send_message(ctx.message.channel, embed=box)
        #await bot.send_message(ctx.message.server.owner, embed=permEmbed("kick_members"))
        return
    string = ""
    for word in args:
        string = string + word + " "
    string = stripEnd(string, 1)
    matched = []
    matchedm = []
    for usr in await bot.get_bans(ctx.message.server):
        if string.lower() in usr.name.lower():
            matched.append(usr.name)
            matchedm.append(usr)
    if matched == []:
        box = discord.Embed(title="Your search returned no results. Make sure spelling is correct.", color=0xdd2200)
    elif len(matched) > 1:
        if len(matched) <= 15:
            desc = ""
            for i in matched:
                desc += i + "\n"
            box = discord.Embed(title="Your search returned multiple results:", description=desc, color=0xddcc11)
        else:
            box = discord.Embed(title="Your search was too broad. Please use more specific keywords.", color=0xff8100)
    else:
        await bot.unban(ctx.message.server, matchedm[0])
        box = discord.Embed(title="Member unbanned.", description=matched[0], color=0x22dd00)
    await bot.send_message(ctx.message.channel, embed=box)

"""@bot.command(pass_context=True, aliases=["voice-kick", "vk", "voicek", "vkick"])
async def voicekick(member=None):
    if member"""

bot.run("TOKEN")
