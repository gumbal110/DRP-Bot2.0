"""
💰 COG DE ECONOMÍA
Sistema completo de dinero, work, daily, payday, etc.
"""

import discord
from discord.ext import commands
from discord import app_commands
import random
from utils.database import (
    crear_usuario, obtener_saldo, agregar_dinero, restar_dinero,
    depositar, retirar, transferir, actualizar_cooldown, obtener_cooldown,
    obtener_top, obtener_config, registrar_log, obtener_sueldo_mas_alto,
    obtener_usuario
)
from utils.embeds import (
    embed_balance, embed_dinero_recibido, embed_transferencia, embed_payday,
    embed_top, embed_error, embed_exito, embed_cooldown, embed_advertencia
)
from utils.validar import (
    verificar_cooldown, formato_tiempo, obtener_roles_principales,
    generar_sueldo_trabajo, generar_sueldo_daily, MONEDA_DEFAULT
)
from datetime import datetime

class Economia(commands.Cog):
    """Cog de economía"""
    
    def __init__(self, bot):
        self.bot = bot
    
    def obtener_moneda(self, guild_id):
        """Obtener moneda del servidor"""
        config = obtener_config(guild_id)
        if config:
            return config[5]  # moneda
        return MONEDA_DEFAULT
    
    @app_commands.command(name="balance", description="Ver tu balance de dinero")
    @app_commands.describe(usuario="Usuario para ver balance")
    async def balance(self, interaction: discord.Interaction, usuario: discord.User = None):
        """Ver balance de dinero"""
        usuario = usuario or interaction.user
        
        # Crear usuario si no existe
        if not obtener_usuario(usuario.id):
            crear_usuario(usuario.id, usuario.name, int(datetime.now().timestamp()))
        
        saldo, banco = obtener_saldo(usuario.id)
        moneda = self.obtener_moneda(interaction.guild.id)
        
        embed = embed_balance(usuario, saldo, banco, moneda)
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="work", description="Trabajar y ganar dinero")
    async def work(self, interaction: discord.Interaction):
        """Trabajar y ganar dinero"""
        user_id = interaction.user.id
        guild_id = interaction.guild.id
        
        # Crear usuario si no existe
        if not obtener_usuario(user_id):
            crear_usuario(user_id, interaction.user.name, int(datetime.now().timestamp()))
        
        # Obtener config
        config = obtener_config(guild_id)
        cooldown_work = config[7] if config else 3600
        
        # Verificar cooldown
        ultima_work = obtener_cooldown(user_id, "work")
        puede, tiempo = verificar_cooldown(ultima_work, cooldown_work)
        
        if not puede:
            embed = embed_cooldown("work", formato_tiempo(tiempo))
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        # Generar dinero
        cantidad = generar_sueldo_trabajo()
        agregar_dinero(user_id, cantidad)
        actualizar_cooldown(user_id, "work")
        moneda = self.obtener_moneda(guild_id)
        
        # Obtener nuevo saldo
        nuevo_saldo, _ = obtener_saldo(user_id)
        
        # Registrar log
        registrar_log(guild_id, "work", user_id, f"Ganó {moneda} {cantidad}")
        
        embed = embed_dinero_recibido(interaction.user, cantidad, nuevo_saldo, moneda, "Work")
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="daily", description="Recompensa diaria")
    async def daily(self, interaction: discord.Interaction):
        """Obtener recompensa diaria"""
        user_id = interaction.user.id
        guild_id = interaction.guild.id
        
        # Crear usuario si no existe
        if not obtener_usuario(user_id):
            crear_usuario(user_id, interaction.user.name, int(datetime.now().timestamp()))
        
        # Obtener config
        config = obtener_config(guild_id)
        cooldown_daily = config[8] if config else 86400
        
        # Verificar cooldown
        ultima_daily = obtener_cooldown(user_id, "daily")
        puede, tiempo = verificar_cooldown(ultima_daily, cooldown_daily)
        
        if not puede:
            embed = embed_cooldown("daily", formato_tiempo(tiempo))
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        # Generar dinero
        cantidad = generar_sueldo_daily()
        agregar_dinero(user_id, cantidad)
        actualizar_cooldown(user_id, "daily")
        moneda = self.obtener_moneda(guild_id)
        
        # Obtener nuevo saldo
        nuevo_saldo, _ = obtener_saldo(user_id)
        
        # Registrar log
        registrar_log(guild_id, "daily", user_id, f"Recibió {moneda} {cantidad}")
        
        embed = embed_dinero_recibido(interaction.user, cantidad, nuevo_saldo, moneda, "Daily")
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="payday", description="Cobrar sueldo por rol")
    async def payday(self, interaction: discord.Interaction):
        """Cobrar sueldo por rol"""
        user_id = interaction.user.id
        guild_id = interaction.guild.id
        member = interaction.user
        
        # Crear usuario si no existe
        if not obtener_usuario(user_id):
            crear_usuario(user_id, interaction.user.name, int(datetime.now().timestamp()))
        
        # Obtener config
        config = obtener_config(guild_id)
        cooldown_payday = config[6] if config else 43200
        
        # Verificar cooldown
        ultima_payday = obtener_cooldown(user_id, "payday")
        puede, tiempo = verificar_cooldown(ultima_payday, cooldown_payday)
        
        if not puede:
            embed = embed_cooldown("payday", formato_tiempo(tiempo))
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        # Obtener role IDs del usuario
        role_ids = [role.id for role in member.roles[1:]]
        
        if not role_ids:
            embed = embed_error("Sin roles", "Necesitas tener al menos un rol para cobrar sueldo")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        # Obtener sueldo más alto
        cantidad = obtener_sueldo_mas_alto(guild_id, role_ids)
        
        if cantidad == 0:
            embed = embed_advertencia("Sin sueldo", "Tu rol no tiene sueldo configurado")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        # Agregar dinero
        agregar_dinero(user_id, cantidad)
        actualizar_cooldown(user_id, "payday")
        moneda = self.obtener_moneda(guild_id)
        
        # Obtener nuevo saldo
        nuevo_saldo, _ = obtener_saldo(user_id)
        
        # Obtener rol principal
        rol_principal = member.roles[-1].mention if len(member.roles) > 1 else "Miembro"
        
        # Registrar log
        registrar_log(guild_id, "payday", user_id, f"Cobró {moneda} {cantidad} como {rol_principal}")
        
        embed = embed_payday(interaction.user, rol_principal, cantidad, nuevo_saldo, moneda)
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="depositar", description="Depositar dinero en el banco")
    @app_commands.describe(cantidad="Cantidad a depositar")
    async def depositar(self, interaction: discord.Interaction, cantidad: float):
        """Depositar dinero"""
        user_id = interaction.user.id
        guild_id = interaction.guild.id
        
        # Crear usuario si no existe
        if not obtener_usuario(user_id):
            crear_usuario(user_id, interaction.user.name, int(datetime.now().timestamp()))
        
        if cantidad <= 0:
            embed = embed_error("Cantidad inválida", "Debes depositar una cantidad mayor a 0")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        if not depositar(user_id, cantidad):
            embed = embed_error("Saldo insuficiente", f"No tienes {cantidad} para depositar")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        moneda = self.obtener_moneda(guild_id)
        nuevo_saldo, _ = obtener_saldo(user_id)
        
        # Registrar log
        registrar_log(guild_id, "deposito", user_id, f"Depositó {moneda} {cantidad}")
        
        embed = embed_exito("Depósito realizado", f"Depositaste {moneda} **{cantidad:,.2f}**")
        embed.add_field(name="Saldo en mano", value=f"{moneda} **{nuevo_saldo:,.2f}**", inline=True)
        embed.set_thumbnail(url=interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url)
        
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="retirar", description="Retirar dinero del banco")
    @app_commands.describe(cantidad="Cantidad a retirar")
    async def retirar(self, interaction: discord.Interaction, cantidad: float):
        """Retirar dinero del banco"""
        user_id = interaction.user.id
        guild_id = interaction.guild.id
        
        # Crear usuario si no existe
        if not obtener_usuario(user_id):
            crear_usuario(user_id, interaction.user.name, int(datetime.now().timestamp()))
        
        if cantidad <= 0:
            embed = embed_error("Cantidad inválida", "Debes retirar una cantidad mayor a 0")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        if not retirar(user_id, cantidad):
            embed = embed_error("Saldo insuficiente", f"No tienes {cantidad} en el banco")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        moneda = self.obtener_moneda(guild_id)
        nuevo_saldo, _ = obtener_saldo(user_id)
        
        # Registrar log
        registrar_log(guild_id, "retiro", user_id, f"Retiró {moneda} {cantidad}")
        
        embed = embed_exito("Retiro realizado", f"Retiraste {moneda} **{cantidad:,.2f}**")
        embed.add_field(name="Saldo en mano", value=f"{moneda} **{nuevo_saldo:,.2f}**", inline=True)
        embed.set_thumbnail(url=interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url)
        
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="transferir", description="Transferir dinero a otro usuario")
    @app_commands.describe(usuario="Usuario a recibir", cantidad="Cantidad a transferir")
    async def transferir(self, interaction: discord.Interaction, usuario: discord.User, cantidad: float):
        """Transferir dinero"""
        user_id = interaction.user.id
        user_destino = usuario.id
        guild_id = interaction.guild.id
        
        # Crear usuarios si no existen
        if not obtener_usuario(user_id):
            crear_usuario(user_id, interaction.user.name, int(datetime.now().timestamp()))
        
        if not obtener_usuario(user_destino):
            crear_usuario(user_destino, usuario.name, int(datetime.now().timestamp()))
        
        if cantidad <= 0:
            embed = embed_error("Cantidad inválida", "Debes transferir una cantidad mayor a 0")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        if user_id == user_destino:
            embed = embed_error("Transferencia inválida", "No puedes transferirte dinero a ti mismo")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        if not transferir(user_id, user_destino, cantidad):
            embed = embed_error("Saldo insuficiente", f"No tienes {cantidad} para transferir")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        moneda = self.obtener_moneda(guild_id)
        
        # Registrar log
        registrar_log(guild_id, "transferencia", user_id, f"Transferió {moneda} {cantidad} a {usuario.name}")
        
        embed = embed_transferencia(interaction.user, usuario, cantidad, moneda)
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="top", description="Ver ranking de usuarios")
    async def top(self, interaction: discord.Interaction):
        """Ver top 10 usuarios"""
        guild_id = interaction.guild.id
        usuarios = obtener_top(guild_id, 10)
        
        if not usuarios:
            embed = embed_error("Sin datos", "No hay usuarios con dinero aún")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        moneda = self.obtener_moneda(guild_id)
        embed = embed_top(usuarios, moneda)
        
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Economia(bot))
