import discord
import __token__

# Client
# Necessario para o Bot ler as mensagens
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Pronto")

@client.event
async def on_disconnect():
    print("Desconectado")

# Message events
@client.event
async def on_message(message):
    content = message.content
    channel = message.channel
    author = message.author

# Bot run and token

if __name__ == '__main__':
    client.run(__senha__.BOT_TOKEN)