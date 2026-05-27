"""
📢 COG DE EVENTOS
Eventos del bot: bienvenida, miembro entra/sale, etc.
"""

import discord
from discord.ext import commands
from utils.database import crear_usuario, registrar_log, obtener_config
from utils.embeds import embed_bienvenida, embed_error
from datetime import datetime

class Eventos(commands.Cog):
    """Cog de eventos"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """Evento cuando un miembro entra al servidor"""
        guild = member.guild
        guild_id = guild.id
        user_id = member.id
        
        # Crear usuario en BD
        crear_usuario(user_id, member.name, int(datetime.now().timestamp()))
        
        # Registrar en logs
        registrar_log(guild_id, "miembro_entra", user_id, f"{member.name} entró al servidor")
        
        # Enviar DM de bienvenida
        try:
            embed = embed_bienvenida(member, guild)
            await member.send(embed=embed)
        except discord.Forbidden:
            # No se pudo enviar DM, solo registrar
            pass
        
        # Enviar mensaje en canal de bienvenida si está configurado
        config = obtener_config(guild_id)
        if config and config[2]:  # canal_bienvenida
            try:
                canal = guild.get_channel(config[2])
                if canal:
                    embed = discord.Embed(
                        title=f"👋 Bienvenido {member.name}",
                        description=f"Nos alegra que te unas a **{guild.name}**",
                        color=discord.Color.green()
                    )
                    embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
                    await canal.send(embed=embed)
            except:
                pass
    
    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        """Evento cuando un miembro sale del servidor"""
        guild = member.guild
        guild_id = guild.id
        user_id = member.id
        
        # Registrar en logs
        registrar_log(guild_id, "miembro_sale", user_id, f"{member.name} salió del servidor")

async def setup(bot):
    await bot.add_cog(Eventos(bot))
