"""
📚 COG DE AYUDA
Comando help y información general
"""

import discord
from discord.ext import commands
from discord import app_commands
from utils.embeds import embed_help

class Help(commands.Cog):
    """Cog de ayuda"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="help", description="Ver todos los comandos disponibles")
    async def help(self, interaction: discord.Interaction):
        """Mostrar ayuda"""
        embed = embed_help()
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))
