import datetime

import discord
from discord.ext import commands
import urllib
import re
from urllib import parse, request
from discord.utils import get
import requests
import sys

client= commands.Bot(command_prefix='>',description='Bot de Tincho',intents=discord.Intents.all())
#@client.command(name='info')
#async def informacion(ctx):
 #embed= discord.Embed(title=)

@client.command(name='suma')
async def sumar(ctx,num1,num2):
    total= int(num1) + int(num2)
    await ctx.send(total)
@client.command(name='mult')
async def multiplicar(ctx,num1,num2):
    total= int(num1) * int(num2)
    if total > 1000000:
        await ctx.send("Resultado demasiado alto")
    else:
        await ctx.send(f"{total} ")

@client.command(name='youtube')
async def busquedaYou(ctx, *, serch):
    query=parse.urlencode({'search_query':serch})
    html_content=request.urlopen('http://www.youtube.com/results?' + query)
    resultados=re.findall('watch\?v=(.{11})',html_content.read().decode('utf-8'))
    for i in range(0,3):
        await ctx.send('https://www.youtube.com/watch?v=' + resultados[i])

@client.command(name='clima')
async def clima(ctx,ciudad):
    url="{URL}"
    response= requests.get(url + "/" + sys.argv[0].replace(" ", "+"))
    print(response.content)

@client.command(name='dia')
async def dia (ctx):
    parameter = {
        "lat": -37.996971,
        "lng": -57.549099,
    }
    response = requests.get('Url API', params=parameter)
    data = response.json()
    amanecer = data["results"]["sunrise"]
    anochecer = data["results"]["sunset"]
    duracion = data["results"]["day_length"]
    embed= discord.Embed(title=f"{ctx.guild.name}", description="Bienvenido",timestamp=datetime.datetime.utcnow(),color=discord.Color.dark_red())
    embed.add_field(name="Server Owner",value=f"{ctx.guild.owner}")
    embed.add_field(name="Region",value=f"Mar Del Plata")
    embed.add_field(name="Salida del sol",value=f"{amanecer}")
    embed.add_field(name="Puesta del sol",value=f"{anochecer}")
    embed.add_field(name="Duracion del dia",value=f"{duracion}")
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/a/a4/Sol_de_Mayo_Bandera_Argentina.png')
    await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member, *, razon=None):
    if razon==None:
        razon="No se proporciono una razon para este kick"
    await ctx.guild.kick(member)
    embed = discord.Embed(title='Reporte de kick',description='-------------------------------------------*----------------------------------------',timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_theme())
    embed.add_field(name=f'Razon', value=f'{razon}', inline=True)
    embed.add_field(name=f'Usuario Kickeado:', value=f'{member.mention}', inline=True)
    embed.set_author(name=ctx.message.author)
    embed.add_field(name=f'El autor del Kickeo fue:', value=f'{embed.author.name}', inline=True)
    await ctx.send(embed=embed)


@client.command(name='ban')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member, *, razon=None):
    if razon==None:
        razon="No se proporciono una razon para este ban"
    await ctx.guild.ban(member)
    embed = discord.Embed(title='Reporte de Ban',description='-------------------------------------------*----------------------------------------',timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_theme())
    embed.add_field(name=f'Razon', value=f'{razon}', inline=True)
    embed.add_field(name=f'Usuario baneado:', value=f'{member.mention}', inline=True)
    embed.set_author(name=ctx.message.author)
    embed.add_field(name=f'El autor del ban fue:', value=f'{embed.author.name}', inline=True)

    await ctx.send(embed=embed)

@client.command(name='temp')
async def temperatura(ctx,ciudad):
    url='{Clave API}'.format(ciudad)
    response=requests.get(url=url)
    print(response)
    data= response.json()
    embed = discord.Embed(title='Reporte del Clima para hoy', description='-------------------------------------------*----------------------------------------', timestamp=datetime.datetime.utcnow(), color=discord.Color.purple())
    embed.add_field(name=f'Temperatura Maxima:', value=f'{data["main"]["temp_max"]} °C ', inline=True)
    embed.add_field(name=f'Temperatura Minima::', value=f'{data["main"]["temp_min"]} °C ', inline=True)
    embed.set_author(name=ctx.message.author)
    embed.add_field(name=f'Sensacion Termica:', value=f'{data["main"]["feels_like"]} °C ', inline=True)
    embed.add_field(name=f'Descripcion:', value=f'{data["weather"][0]["description"]}', inline=True)
    embed.add_field(name=f'Humedad:', value=f'{data["main"]["humidity"]} %', inline=True)
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/a/a4/Sol_de_Mayo_Bandera_Argentina.png')
    await ctx.send(embed=embed)
client.run('{Clave}')