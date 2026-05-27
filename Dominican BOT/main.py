"""
🤖 BOT AVANZADO DOMINICANO PARA DISCORD
Desenvolvedor por: TU NOMBRE
Características: Sistema de Cédula, Economía, Roles, Logs y más
"""

import discord
from discord.ext import commands
import os
from utils.database import crear_base_datos
from dotenv import load_dotenv
load_dotenv()

# Configuración del bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Crear base de datos
crear_base_datos()

@bot.event
async def on_ready():
    """Evento cuando el bot está listo"""
    print(f"✅ Bot conectado como: {bot.user}")
    print(f"📊 Servidores: {len(bot.guilds)}")
    
    try:
        synced = await bot.tree.sync()
        print(f"✔️ {len(synced)} slash commands sincronizados")
    except Exception as e:
        print(f"❌ Error sincronizando comandos: {e}")
    
    # Cambiar estado del bot
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="a los dominicanos 🇩🇴"
        )
    )

@bot.event
async def on_guild_join(guild):
    """Evento cuando el bot entra a un servidor"""
    from utils.database import configurar_servidor
    configurar_servidor(guild.id)
    print(f"📍 Bot agregado a: {guild.name}")

# Cargar cogs
async def cargar_cogs():
    """Cargar todos los cogs del bot"""
    cogs_path = "cogs"
    
    if not os.path.exists(cogs_path):
        os.makedirs(cogs_path)
    
    for filename in os.listdir(cogs_path):
        if filename.endswith(".py") and not filename.startswith("_"):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"✔️ Cog cargado: {filename}")
            except Exception as e:
                print(f"❌ Error cargando {filename}: {e}")

async def main():
    async with bot:
        await cargar_cogs()
        
        # Token desde variable de entorno (Replit)
        TOKEN = os.getenv("DISCORD_TOKEN")
        if not TOKEN:
            print("❌ Error: No se encontró DISCORD_TOKEN en variables de entorno")
            return
        
        await bot.start(TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
