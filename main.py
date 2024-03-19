
from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return '''<body style="margin: 0; padding: 0;">
    <iframe width="100%" height="100%" src="https://axocoder.vercel.app/" frameborder="0" allowfullscreen></iframe>
  </body>'''

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()

keep_alive()
print("Server Running Because of Axo")




#-------------------------
import asyncio
import disnake.ext.commands as commands
import disnake
from disnake.ext import commands
import random



# -------------------


# Your bot token here
TOKEN = 'MTIxOTIwMTIwNjA3MzgyMzI0Mw.GCTF7v.XS0TYXirYal3imv0If23hPXfUtNVwC-HH2Ef3Y'

# Initialize the Disnake bot
bot = commands.Bot(command_prefix='!')
intents = disnake.Intents.default()
intents.bans = True
# Function to update activities every 10 seconds


# ------------------------------

intents = disnake.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("Bot is ready and waiting for chaos!")


@bot.slash_command(description="Bans a member ")
@commands.has_permissions(administrator=True)
async def ban_member(ctx, member: disnake.Member):
    await member.ban()
    await ctx.send("Member has been banned.<:Verified:1219595134279221348>", ephemeral=True)


@bot.slash_command(description="Unbans a member ")
@commands.has_permissions(administrator=True)
async def unban_member(ctx, user: disnake.User):
    await ctx.guild.unban(user)
    await ctx.send("Member has been unbanned.<:Verified:1219595134279221348>", ephemeral=True)


@bot.slash_command(description="Kicks a member ")
@commands.has_permissions(administrator=True)
async def kick_member(ctx, member: disnake.Member):
    await member.kick()
    await ctx.send("Member has been kicked.", ephemeral=True)


@bot.slash_command(description="Mutes a member in text channels ")
@commands.has_permissions(administrator=True)
async def mute_text(ctx, member: disnake.Member):
    # Code for muting the member in text channels
    await ctx.send("Member has been muted in text channels.<:Verified:1219595134279221348>", ephemeral=True)


@bot.slash_command(description="Unmutes a member in text channels")
@commands.has_permissions(administrator=True)
async def unmute_text(ctx, member: disnake.Member):
    # Code for unmuting the member in text channels
    await ctx.send("Member has been unmuted in text channels.<:Verified:1219595134279221348>", ephemeral=True)


@bot.slash_command(description="Mutes a member in voice channels ")
@commands.has_permissions(administrator=True)
async def mute_voice(ctx, member: disnake.Member):
    # Code for muting the member in voice channels
    await ctx.send("Member has been muted in voice channels.<:Verified:1219595134279221348>", ephemeral=True)


@bot.slash_command(description="Unmutes a member in voice channels ")
@commands.has_permissions(administrator=True)
async def unmute_voice(ctx, member: disnake.Member):
    # Code for unmuting the member in voice channels
    await ctx.send("Member has been unmuted in voice channels.<:Verified:1219595134279221348>", ephemeral=True)


@bot.slash_command(description="Times out a member ")
@commands.has_permissions(administrator=True)
async def timeout_member(ctx, member: disnake.Member):
    # Code for timing out the member
    await ctx.send("Member has been timed out.<:Verified:1219595134279221348>", ephemeral=True)


@bot.slash_command(description="Untimes out a member ")
@commands.has_permissions(administrator=True)
async def untimeout_member(ctx, member: disnake.Member):
    # Code for untiming out the member
    await ctx.send("Member has been untimed out.<:Verified:1219595134279221348>", ephemeral=True)


@bot.slash_command(description="pong!")
async def ping(ctx):
    latency = bot.latency * 1000  # Convert to milliseconds
    embed = disnake.Embed(title="Bot Latency", color=disnake.Color.blurple())
    embed.add_field(
        name="Pong!", value=f"{latency:.2f}ms <:ping:1217931762160631899>")
    await ctx.send(embed=embed, ephemeral=True)


@bot.slash_command(description="Enables anti-spam to block every spam message")
@commands.has_permissions(administrator=True)
async def enable_anti_spam(ctx):
    # Code for enabling anti-spam
    await ctx.send("Anti-spam has been enabled.<:Verified:1219595134279221348>", ephemeral=True)


@bot.slash_command(description="Gives a role to a member ")
@commands.has_permissions(administrator=True)
async def give_role(ctx, member: disnake.Member, role: disnake.Role):
    await member.add_roles(role)
    await ctx.send(f"{member.mention} has been given the {role.name} role.<:Verified:1219595134279221348>", ephemeral=True)


@bot.slash_command(description="Removes a role from a member ")
@commands.has_permissions(administrator=True)
async def remove_role(ctx, member: disnake.Member, role: disnake.Role):
    await member.remove_roles(role)
    await ctx.send(f"{role.name} role has been removed from {member.mention}.<:Verified:1219595134279221348>", ephemeral=True)


@bot.slash_command(description="Deletes a specific number of messages")
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    channel = ctx.channel

    try:
        # Delete the specified number of messages
        await channel.purge(limit=amount + 1)

        # Success message (ephemeral)
        success_embed = disnake.Embed(
            title="Clear", description=f"{amount} messages have been deleted.<:Verified:1219595134279221348>", color=disnake.Color.blue())
        await ctx.send(embed=success_embed, ephemeral=True)

    except disnake.NotFound:
        await ctx.send("Not found")
    except TimeoutError:
        await ctx.send("Timeout")


@bot.slash_command(description="love sang")
async def lovesanj(ctx, member1: disnake.Member, member2: disnake.Member):
    love_percentage = random.randint(0, 100)
    love_embed = disnake.Embed(
        title="Love Calculator", color=disnake.Color.blue())
    love_embed.description = f"{member1.name} 💖 {member2.name}\n\nYou are {love_percentage}% in love.\n\nDon't give up!"
    await ctx.send(embed=love_embed)


@bot.slash_command(description="bache sal sanj")
async def bachesalsanj(ctx, member1: disnake.Member):
    bachesalsanj_percentage = random.randint(0, 100)
    bachesalsanj_embed = disnake.Embed(
        title="Bache Sal Sanj", color=disnake.Color.blue())
    bachesalsanj_embed.description = f"{member1.name}\n\nYou are {bachesalsanj_percentage}% bachesal.!"
    await ctx.send(embed=bachesalsanj_embed)


@bot.slash_command(description="Show member invites")
async def show_invites(ctx):
    member = ctx.author
    guild = ctx.guild

    # Get member's invite information
    invites = await guild.invites()

    total_invites = 0
    total_leaves = 0
    total_fake_invites = 0

    # Calculate invite information
    for invite in invites:
        if invite.inviter == member:
            total_invites += invite.uses
        if invite.inviter != member and invite.inviter is not None and invite.inviter.bot:
            total_fake_invites += invite.uses
        if invite.inviter != member and invite.inviter is None:
            total_leaves += invite.uses

    # Build the embed
    embed = disnake.Embed(title="Member Invites", color=disnake.Color.blue())
    embed.add_field(
        name="Invites", value=f"{member.mention} has {total_invites} invites <:Verified:1219595134279221348>")
    embed.add_field(name="All Invites",
                    value=f"Total Invites: {total_invites} 🔥\nLeaves: {total_leaves}\nFakes: {total_fake_invites}")

    await ctx.send(embed=embed)

    # -------------------------------


async def update_activities():
    while True:
        # Get total members and total servers
        total_members = sum(guild.member_count for guild in bot.guilds)
        total_servers = len(bot.guilds)

        # Update the activities
        await bot.change_presence(
            activity=disnake.Activity(
                type=disnake.ActivityType.playing,
                name=f'with {total_members} in {total_servers} servers'
            )
        )
        await asyncio.sleep(10)  # Change every 10 seconds

        await bot.change_presence(
            activity=disnake.Activity(
                type=disnake.ActivityType.watching,
                name='beta version'
            )
        )
        await asyncio.sleep(10)  # Change every 10 seconds

# Event handler for bot ready


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    bot.loop.create_task(update_activities())

bot.run(TOKEN)
