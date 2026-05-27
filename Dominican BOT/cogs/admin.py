"""
⚙️ COG DE ADMINISTRACIÓN
Configuración del servidor, sueldos, etc.
"""

import discord
from discord.ext import commands
from discord import app_commands
from utils.database import (
    establecer_sueldo, obtener_config, actualizar_config,
    configurar_servidor, registrar_log
)
from utils.embeds import (
    embed_error, embed_exito, embed_config, embed_info
)
from utils.validar import convertir_a_segundos, MONEDA_DEFAULT

class Admin(commands.Cog):
    """Cog de administración"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="set_sueldo", description="[ADMIN] Establecer sueldo para un rol")
    @app_commands.describe(rol="Rol para establecer sueldo", cantidad="Cantidad del sueldo")
    async def set_sueldo(self, interaction: discord.Interaction, rol: discord.Role, cantidad: float):
        """Establecer sueldo de rol"""
        if not interaction.user.guild_permissions.administrator:
            embed = embed_error("Permiso denegado", "Solo administradores pueden usar este comando")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        if cantidad <= 0:
            embed = embed_error("Cantidad inválida", "El sueldo debe ser mayor a 0")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        guild_id = interaction.guild.id
        role_id = rol.id
        
        # Establecer sueldo
        establecer_sueldo(guild_id, role_id, cantidad)
        
        # Registrar log
        registrar_log(guild_id, "sueldo_establecido", interaction.user.id, 
                     f"Estableció sueldo de {rol.name} en {cantidad}")
        
        config = obtener_config(guild_id)
        moneda = config[5] if config else MONEDA_DEFAULT
        
        embed = embed_exito(
            "Sueldo establecido",
            f"Se estableció el sueldo de {rol.mention} en {moneda} **{cantidad:,.2f}**"
        )
        
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="config", description="[ADMIN] Configurar servidor")
    @app_commands.describe(
        opcion="Opción a configurar",
        valor="Valor para la opción"
    )
    async def config(self, interaction: discord.Interaction, opcion: str, valor: str):
        """Configurar servidor"""
        if not interaction.user.guild_permissions.administrator:
            embed = embed_error("Permiso denegado", "Solo administradores pueden usar este comando")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        guild_id = interaction.guild.id
        
        # Asegurar que exista configuración
        if not obtener_config(guild_id):
            configurar_servidor(guild_id)
        
        opcion = opcion.lower()
        
        try:
            if opcion == "logs":
                # Extraer ID del canal
                canal_id = int(valor.strip("<>#"))
                actualizar_config(guild_id, canal_logs=canal_id)
                embed = embed_exito("Configurado", f"Canal de logs establecido a <#{canal_id}>")
            
            elif opcion == "bienvenida":
                # Extraer ID del canal
                canal_id = int(valor.strip("<>#"))
                actualizar_config(guild_id, canal_bienvenida=canal_id)
                embed = embed_exito("Configurado", f"Canal de bienvenida establecido a <#{canal_id}>")
            
            elif opcion == "moneda":
                actualizar_config(guild_id, moneda=valor)
                embed = embed_exito("Configurado", f"Moneda establecida a: {valor}")
            
            elif opcion == "payday":
                # Convertir a segundos
                segundos = convertir_a_segundos(valor)
                if segundos is None:
                    embed = embed_error("Formato inválido", "Usa: 12h, 24h, 1d, etc.")
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                    return
                actualizar_config(guild_id, cooldown_payday=segundos)
                embed = embed_exito("Configurado", f"Cooldown de payday establecido a: {valor}")
            
            elif opcion == "work":
                # Convertir a segundos
                segundos = convertir_a_segundos(valor)
                if segundos is None:
                    embed = embed_error("Formato inválido", "Usa: 1h, 30m, 1d, etc.")
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                    return
                actualizar_config(guild_id, cooldown_work=segundos)
                embed = embed_exito("Configurado", f"Cooldown de work establecido a: {valor}")
            
            elif opcion == "daily":
                # Convertir a segundos
                segundos = convertir_a_segundos(valor)
                if segundos is None:
                    embed = embed_error("Formato inválido", "Usa: 24h, 1d, etc.")
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                    return
                actualizar_config(guild_id, cooldown_daily=segundos)
                embed = embed_exito("Configurado", f"Cooldown de daily establecido a: {valor}")
            
            else:
                embed = embed_error(
                    "Opción inválida",
                    "Opciones disponibles:\n`logs`, `bienvenida`, `moneda`, `payday`, `work`, `daily`"
                )
            
            # Registrar log
            registrar_log(guild_id, "config_actualizada", interaction.user.id, 
                         f"Configuró {opcion} a {valor}")
        
        except (ValueError, IndexError):
            embed = embed_error("Error", "Formato inválido para la opción")
        
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="mostrar_config", description="[ADMIN] Ver configuración del servidor")
    async def mostrar_config(self, interaction: discord.Interaction):
        """Mostrar configuración"""
        if not interaction.user.guild_permissions.administrator:
            embed = embed_error("Permiso denegado", "Solo administradores pueden usar este comando")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        guild_id = interaction.guild.id
        config = obtener_config(guild_id)
        
        if not config:
            configurar_servidor(guild_id)
            config = obtener_config(guild_id)
        
        embed = embed_config(guild_id, config)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Admin(bot))
