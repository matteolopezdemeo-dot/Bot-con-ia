import discord
from discord.ext import commands
from settings import TOKEN
from funciones import tabla
from funciones import gemeni
#permisos para recibir y enviar mensajes
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='', intents=intents)
@bot.command()  
async def hola(ctx):
    await ctx.send(f"Hola! Soy un bot de discor y me llamo {bot.user}")

@bot.command()
async def suma(ctx, a: int, b: int):
    c = a + b
    await ctx.send(f"La suma de {a} y {b} es {c}")

@bot.command()
async def resta(ctx, a: int, b: int):
    c = a - b
    await ctx.send(f"La resta de {a} y {b} es {c}")
    
@bot.command()
async def multiplicacion(ctx, a: int, b: int):
    c = a * b
    await ctx.send(f"La multiplicación de {a} y {b} es {c}")

@bot.command()
async def division(ctx, a: int, b: int):
    if b == 0:
        await ctx.send("No se puede dividir entre cero.")
    else:
        c = a / b
        await ctx.send(f"La división de {a} y {b} es {c}")
@bot.command()
async def tabla_m(ctx, num: int):
    resultado = tabla(num)
    await ctx.send(f" La tabla de multiplicar del {num} es:\n{resultado}")
@bot.command()
async def archivo(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{file_name}")
            await ctx.send(f"Guarde la imagen como ./{file_name} en {file_url}")
    else:
        await ctx.send("No me enviaste el archivo, envialo por favor")
@bot.command()  
async def IA(ctx, *, pregunta: str):
     await ctx.send("estoy pensando...⏳")
     await ctx.send(f"{gemeni(pregunta)}")

bot.run(TOKEN)
