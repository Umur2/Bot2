import discord
import os
import random
import requests
from sifre import gen_pass
from discord.ext import commands

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık.')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
        
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)





@bot.command()
async def mem(ctx):
    mems = os.listdir('images')
    choice = random.choice(mems)
    with open(f'images/{choice}','rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    
    
      

 

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    '''dog komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)


@bot.command()
async def geri(ctx, left:str):
    if left == 'plastik':
        await ctx.send('Bu çöpü sarı renkli kutuya atın.')
    elif left == 'metal':   
        await ctx.send('Bu çöpü gıri renkli kutuya atın.')
    elif left == 'cam':
        await ctx.send('Bu çöpü yeşil renkli kutuya atın.')
    elif left == 'kağıt':
        await ctx.send('Bu çöpü mavi renkli kutuya atın.')    
    elif left == 'pil':
        await ctx.send('Bu çöpü kırmızı renkli kutuya atın.')
    else:
        await ctx.send('Bu materyeli geri dönüştüremezsin.')

@bot.command()
async def geri_fikir(ctx):
    fikirler = ('Kartondan bir kalem kutusu','Kumaştan bir elbise','İlaç kutularından bir robot')
    fikir = random.choice(fikirler)
    await ctx.send(f'{fikir}, yapabilirsin.')

@bot.command()
async def geri_sure(ctx, left = str):
    if left == 'plastik şişe':
        await ctx.send('Bu atık doğada 450 yıl boyunca kalır.')







bot.run('Token')
