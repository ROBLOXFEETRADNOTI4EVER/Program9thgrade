import discord
import random

# Set your Discord bot token here directly
TOKEN = ''

# Set up intents
intents = discord.Intents.default()
intents.message_content = True  # Enable specific intents as needed

# Create a client instance with the defined intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

    # Get the user by their ID
    user = await client.fetch_user(444916321302478868)
    user1 = await client.fetch_user(1229436069821415446)
    # Send a DM to the user
    if user:
        try:
            await user.send("https://tenor.com/view/brusmala-cat-arabic-gif-21437623")
            await user1.send("https://tenor.com/view/brusmala-cat-arabic-gif-21437623")
            print(f"Sent a DM to {user.name}")
        except discord.Forbidden:
            print(f"Cannot send a DM to {user.name} - they might have DMs disabled.")
    else:
        print("User not found")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        'Cool. Cool cool cool cool cool cool cool, no doubt no doubt no doubt no doubt.'
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

    # Example: Send a DM when a certain user sends a message
    if message.author.id == 1229436069821415446:
        await message.channel.send('‎')

# Run the bot
client.run(TOKEN)
