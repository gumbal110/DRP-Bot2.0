"""
🪪 COG DE CÉDULAS / IDENTIDAD
Sistema de cédulas de usuario
"""

import discord
from discord.ext import commands
from discord import app_commands
from utils.database import (
    crear_usuario, obtener_cedula, crear_cedula, obtener_usuario,
    eliminar_cedula, registrar_log, obtener_config
)
from utils.embeds import embed_cedula, embed_error, embed_exito, embed_advertencia
from utils.validar import (
    generar_cedula_id, format_fecha, obtener_roles_principales
)
from datetime import datetime

class Cedula(commands.Cog):
    """Cog de cédulas"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="cedula", description="Ver tu cédula de identidad")
    async def cedula(self, interaction: discord.Interaction):
        """Ver tu cédula"""
        user_id = interaction.user.id
        guild_id = interaction.guild.id
        
        # Crear usuario si no existe
        if not obtener_usuario(user_id):
            crear_usuario(user_id, interaction.user.name, int(datetime.now().timestamp()))
        
        cedula_data = obtener_cedula(user_id)
        
        if not cedula_data:
            # Crear cédula automáticamente
            cedula_id = generar_cedula_id()
            roles = obtener_roles_principales(interaction.user)
            fecha_creacion = interaction.user.created_at.strftime("%d/%m/%Y")
            fecha_ingreso = int(datetime.now().timestamp())
            
            crear_cedula(
                user_id,
                guild_id,
                interaction.user.name,
                cedula_id,
                [role.id for role in interaction.user.roles[1:]]
            )
            
            roles_str = " ".join(roles) if roles else "Sin roles"
            
            embed = embed_cedula(
                interaction.user,
                cedula_id,
                fecha_creacion,
                datetime.now().strftime("%d/%m/%Y"),
                roles_str,
                interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url
            )
        else:
            cedula_id, user_id_db, guild_id_db, nombre, fecha_creacion_str, roles_str = cedula_data
            fecha_ingreso = interaction.user.joined_at.strftime("%d/%m/%Y") if interaction.user.joined_at else "N/A"
            
            roles = obtener_roles_principales(interaction.user)
            roles_str = " ".join(roles) if roles else "Sin roles"
            
            embed = embed_cedula(
                interaction.user,
                cedula_id,
                interaction.user.created_at.strftime("%d/%m/%Y"),
                fecha_ingreso,
                roles_str,
                interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url
            )
        
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="ver_cedula", description="Ver cédula de otro usuario")
    @app_commands.describe(usuario="Usuario del que ver cédula")
    async def ver_cedula(self, interaction: discord.Interaction, usuario: discord.User):
        """Ver cédula de otro usuario"""
        user_id = usuario.id
        guild_id = interaction.guild.id
        
        # Crear usuario si no existe
        if not obtener_usuario(user_id):
            crear_usuario(user_id, usuario.name, int(datetime.now().timestamp()))
        
        cedula_data = obtener_cedula(user_id)
        
        if not cedula_data:
            # Crear cédula automáticamente
            cedula_id = generar_cedula_id()
            crear_cedula(
                user_id,
                guild_id,
                usuario.name,
                cedula_id,
                [role.id for role in usuario.roles[1:]]
            )
        else:
            cedula_id, _, _, _, _, _ = cedula_data
        
        roles = obtener_roles_principales(usuario)
        roles_str = " ".join(roles) if roles else "Sin roles"
        fecha_ingreso = usuario.joined_at.strftime("%d/%m/%Y") if usuario.joined_at else "N/A"
        
        embed = embed_cedula(
            usuario,
            cedula_id,
            usuario.created_at.strftime("%d/%m/%Y"),
            fecha_ingreso,
            roles_str,
            usuario.avatar.url if usuario.avatar else usuario.default_avatar.url
        )
        
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="crear_cedula", description="[ADMIN] Crear cédula para usuario")
    @app_commands.describe(usuario="Usuario para crear cédula")
    async def crear_cedula_cmd(self, interaction: discord.Interaction, usuario: discord.User):
        """Crear cédula [ADMIN]"""
        if not interaction.user.guild_permissions.administrator:
            embed = embed_error("Permiso denegado", "Solo administradores pueden usar este comando")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        user_id = usuario.id
        guild_id = interaction.guild.id
        
        # Crear usuario si no existe
        if not obtener_usuario(user_id):
            crear_usuario(user_id, usuario.name, int(datetime.now().timestamp()))
        
        # Verificar si ya existe
        cedula_data = obtener_cedula(user_id)
        
        if cedula_data:
            cedula_id, _, _, _, _, _ = cedula_data
            embed = embed_advertencia("Cédula existente", f"El usuario ya tiene cédula: `{cedula_id}`")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        # Crear cédula
        cedula_id = generar_cedula_id()
        crear_cedula(
            user_id,
            guild_id,
            usuario.name,
            cedula_id,
            [role.id for role in usuario.roles[1:]]
        )
        
        # Registrar log
        registrar_log(guild_id, "cedula_creada", interaction.user.id, f"Creó cédula para {usuario.name}")
        
        embed = embed_exito("Cédula creada", f"Se creó cédula para {usuario.mention}\nID: `{cedula_id}`")
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="editar_cedula", description="[ADMIN] Editar cédula de usuario")
    @app_commands.describe(usuario="Usuario a editar cédula")
    async def editar_cedula_cmd(self, interaction: discord.Interaction, usuario: discord.User):
        """Editar cédula [ADMIN]"""
        if not interaction.user.guild_permissions.administrator:
            embed = embed_error("Permiso denegado", "Solo administradores pueden usar este comando")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        user_id = usuario.id
        guild_id = interaction.guild.id
        
        cedula_data = obtener_cedula(user_id)
        
        if not cedula_data:
            embed = embed_error("Sin cédula", f"{usuario.mention} no tiene cédula creada")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        # Eliminar y recrear
        eliminar_cedula(user_id)
        cedula_id = generar_cedula_id()
        crear_cedula(
            user_id,
            guild_id,
            usuario.name,
            cedula_id,
            [role.id for role in usuario.roles[1:]]
        )
        
        # Registrar log
        registrar_log(guild_id, "cedula_editada", interaction.user.id, f"Editó cédula de {usuario.name}")
        
        embed = embed_exito("Cédula actualizada", f"Cédula de {usuario.mention} fue actualizada\nNuevo ID: `{cedula_id}`")
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="eliminar_cedula", description="[ADMIN] Eliminar cédula de usuario")
    @app_commands.describe(usuario="Usuario para eliminar cédula")
    async def eliminar_cedula_cmd(self, interaction: discord.Interaction, usuario: discord.User):
        """Eliminar cédula [ADMIN]"""
        if not interaction.user.guild_permissions.administrator:
            embed = embed_error("Permiso denegado", "Solo administradores pueden usar este comando")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        user_id = usuario.id
        guild_id = interaction.guild.id
        
        cedula_data = obtener_cedula(user_id)
        
        if not cedula_data:
            embed = embed_error("Sin cédula", f"{usuario.mention} no tiene cédula creada")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        eliminar_cedula(user_id)
        
        # Registrar log
        registrar_log(guild_id, "cedula_eliminada", interaction.user.id, f"Eliminó cédula de {usuario.name}")
        
        embed = embed_exito("Cédula eliminada", f"Cédula de {usuario.mention} fue eliminada")
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Cedula(bot))
