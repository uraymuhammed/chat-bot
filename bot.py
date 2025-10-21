import discord

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Sen kimsın,nerden geldin?")
    elif message.content.startswith('$sakin ol sana bir şey sorcam'):
        await message.channel.send("hee tamam sor")
    elif message.content.startswith('$bana sınav tarihlerini verebilir misin?'):
        await message.channel.send("hmm,hayır e okul a baksana")
    elif message.content.startswith('$çok kaba bir botsun'):
        await message.channel.send("zaten ismim öyle.")
    elif message.content.startswith('$ben gidiyorum'):
        await message.channel.send("tamam yürü başka bir bota git.")
    elif message.content.startswith('$yee hu çıktım'):
        await message.channel.send("hmm sanırım çıkmdın çıksana yav")
    else:
        await message.channel.send(message.content)

client.run("BOTUNUZUN TOKEN BURADA OLMALIDIR!")
