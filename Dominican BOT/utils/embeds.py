"""
🎨 SISTEMA DE EMBEDS MODERNOS
Diseños elegantes y profesionales para el bot
"""

import discord
from datetime import datetime

# Colores
AZUL = discord.Color.from_rgb(52, 152, 219)       # Azul principal
VERDE = discord.Color.from_rgb(46, 204, 113)      # Verde éxito
ROJO = discord.Color.from_rgb(231, 76, 60)        # Rojo error
NARANJA = discord.Color.from_rgb(230, 126, 34)    # Naranja advertencia
MORADO = discord.Color.from_rgb(155, 89, 182)     # Morado información

def crear_embed(titulo="", descripcion="", color=AZUL, imagen=None, thumbnail=None):
    """Crear un embed base"""
    embed = discord.Embed(
        title=titulo,
        description=descripcion,
        color=color,
        timestamp=datetime.now()
    )
    
    if imagen:
        embed.set_image(url=imagen)
    
    if thumbnail:
        embed.set_thumbnail(url=thumbnail)
    
    embed.set_footer(text="🇩🇴 Dominican Bot", icon_url="https://cdn.discordapp.com/emojis/1081664993644347522.png")
    
    return embed

# ==================== CÉDULAS ====================

def embed_cedula(usuario, cedula_id, fecha_creacion_cuenta, fecha_ingreso, roles_str, avatar_url):
    """Embed de cédula de usuario"""
    embed = discord.Embed(
        title="🪪 CÉDULA DE IDENTIDAD",
        color=AZUL,
        timestamp=datetime.now()
    )
    
    embed.add_field(
        name="👤 Nombre",
        value=f"**{usuario.name}**",
        inline=False
    )
    
    embed.add_field(
        name="🆔 ID de Discord",
        value=f"`{usuario.id}`",
        inline=True
    )
    
    embed.add_field(
        name="📛 Número de Cédula",
        value=f"`{cedula_id}`",
        inline=True
    )
    
    embed.add_field(
        name="📅 Cuenta Creada",
        value=fecha_creacion_cuenta,
        inline=True
    )
    
    embed.add_field(
        name="📍 Miembro desde",
        value=fecha_ingreso,
        inline=True
    )
    
    embed.add_field(
        name="🎭 Roles",
        value=roles_str if roles_str else "Sin roles",
        inline=False
    )
    
    embed.set_thumbnail(url=avatar_url)
    embed.set_footer(text="🇩🇴 Dominican Bot | Documento de Identidad", icon_url=avatar_url)
    
    return embed

# ==================== ECONOMÍA ====================

def embed_balance(usuario, saldo, banco, moneda="💵"):
    """Embed de balance"""
    total = saldo + banco
    
    embed = crear_embed(
        titulo=f"💰 Balance de {usuario.name}",
        color=VERDE
    )
    
    embed.add_field(
        name="Dinero en Mano",
        value=f"{moneda} **{saldo:,.2f}**",
        inline=True
    )
    
    embed.add_field(
        name="Dinero en Banco",
        value=f"{moneda} **{banco:,.2f}**",
        inline=True
    )
    
    embed.add_field(
        name="Total",
        value=f"{moneda} **{total:,.2f}**",
        inline=False
    )
    
    embed.set_thumbnail(url=usuario.avatar.url if usuario.avatar else usuario.default_avatar.url)
    
    return embed

def embed_dinero_recibido(usuario, cantidad, nuevo_saldo, moneda="💵", tipo="dinero"):
    """Embed de dinero recibido"""
    embed = crear_embed(
        titulo=f"✅ {tipo.upper()} RECIBIDO",
        color=VERDE
    )
    
    embed.add_field(
        name="Cantidad",
        value=f"{moneda} **{cantidad:,.2f}**",
        inline=True
    )
    
    embed.add_field(
        name="Nuevo Saldo",
        value=f"{moneda} **{nuevo_saldo:,.2f}**",
        inline=True
    )
    
    embed.set_thumbnail(url=usuario.avatar.url if usuario.avatar else usuario.default_avatar.url)
    
    return embed

def embed_transferencia(usuario_desde, usuario_hacia, cantidad, moneda="💵"):
    """Embed de transferencia"""
    embed = crear_embed(
        titulo="💸 TRANSFERENCIA REALIZADA",
        color=AZUL
    )
    
    embed.add_field(
        name="De",
        value=usuario_desde.mention,
        inline=True
    )
    
    embed.add_field(
        name="Para",
        value=usuario_hacia.mention,
        inline=True
    )
    
    embed.add_field(
        name="Cantidad",
        value=f"{moneda} **{cantidad:,.2f}**",
        inline=False
    )
    
    return embed

def embed_payday(usuario, rol, cantidad, nuevo_saldo, moneda="💵"):
    """Embed de payday"""
    embed = crear_embed(
        titulo="✅ PAYDAY RECIBIDO",
        color=VERDE
    )
    
    embed.add_field(
        name="Rol",
        value=rol,
        inline=True
    )
    
    embed.add_field(
        name="Monto Cobrado",
        value=f"{moneda} **{cantidad:,.2f}**",
        inline=True
    )
    
    embed.add_field(
        name="Saldo Actual",
        value=f"{moneda} **{nuevo_saldo:,.2f}**",
        inline=False
    )
    
    embed.set_thumbnail(url=usuario.avatar.url if usuario.avatar else usuario.default_avatar.url)
    
    return embed

def embed_top(usuarios, moneda="💵"):
    """Embed de ranking de usuarios"""
    embed = crear_embed(
        titulo="🏆 TOP 10 USUARIOS",
        color=NARANJA
    )
    
    descripcion = ""
    for idx, (user_id, total) in enumerate(usuarios, 1):
        descripcion += f"`{idx}`. <@{user_id}> - {moneda} **{total:,.2f}**\n"
    
    embed.description = descripcion
    
    return embed

# ==================== GENERAL ====================

def embed_error(titulo="Error", descripcion=""):
    """Embed de error"""
    embed = crear_embed(
        titulo=f"❌ {titulo}",
        descripcion=descripcion,
        color=ROJO
    )
    return embed

def embed_exito(titulo="Éxito", descripcion=""):
    """Embed de éxito"""
    embed = crear_embed(
        titulo=f"✅ {titulo}",
        descripcion=descripcion,
        color=VERDE
    )
    return embed

def embed_info(titulo="Información", descripcion=""):
    """Embed de información"""
    embed = crear_embed(
        titulo=f"ℹ️ {titulo}",
        descripcion=descripcion,
        color=AZUL
    )
    return embed

def embed_advertencia(titulo="Advertencia", descripcion=""):
    """Embed de advertencia"""
    embed = crear_embed(
        titulo=f"⚠️ {titulo}",
        descripcion=descripcion,
        color=NARANJA
    )
    return embed

def embed_cooldown(tipo, tiempo_restante):
    """Embed de cooldown"""
    embed = crear_embed(
        titulo=f"⏳ Espera un poco",
        descripcion=f"Debes esperar **{tiempo_restante}** antes de usar {tipo} nuevamente",
        color=NARANJA
    )
    return embed

def embed_config(guild_id, config):
    """Embed de configuración"""
    embed = crear_embed(
        titulo="⚙️ CONFIGURACIÓN DEL SERVIDOR",
        color=MORADO
    )
    
    if config:
        guild_id, canal_logs, canal_bienvenida, msg_bienvenida, color, moneda, cooldown_payday, cooldown_work, cooldown_daily = config
        
        embed.add_field(
            name="📋 Canal de Logs",
            value=f"<#{canal_logs}>" if canal_logs else "No configurado",
            inline=True
        )
        
        embed.add_field(
            name="👋 Canal de Bienvenida",
            value=f"<#{canal_bienvenida}>" if canal_bienvenida else "No configurado",
            inline=True
        )
        
        embed.add_field(
            name="💰 Moneda",
            value=moneda,
            inline=True
        )
        
        embed.add_field(
            name="⏱️ Cooldown Payday",
            value=f"{cooldown_payday // 3600} horas",
            inline=True
        )
        
        embed.add_field(
            name="⏱️ Cooldown Work",
            value=f"{cooldown_work // 60} minutos",
            inline=True
        )
        
        embed.add_field(
            name="⏱️ Cooldown Daily",
            value=f"{cooldown_daily // 3600} horas",
            inline=True
        )
    
    return embed

def embed_help():
    """Embed de ayuda"""
    embed = crear_embed(
        titulo="📚 AYUDA - COMANDOS DISPONIBLES",
        color=MORADO
    )
    
    embed.add_field(
        name="💰 ECONOMÍA",
        value="`/balance` - Ver tu balance\n`/work` - Trabajar y ganar dinero\n`/daily` - Recompensa diaria\n`/payday` - Cobrar sueldo\n`/depositar <cantidad>` - Depositar en banco\n`/retirar <cantidad>` - Retirar del banco\n`/transferir @usuario <cantidad>` - Transferir dinero\n`/top` - Ver ranking",
        inline=False
    )
    
    embed.add_field(
        name="🪪 IDENTIDAD",
        value="`/cedula` - Ver tu cédula\n`/ver_cedula @usuario` - Ver cédula de alguien",
        inline=False
    )
    
    embed.add_field(
        name="⚙️ CONFIGURACIÓN",
        value="`/config` - Configurar servidor (Admin)",
        inline=False
    )
    
    embed.add_field(
        name="👨‍💼 ADMIN",
        value="`/set_sueldo @rol <cantidad>` - Establecer sueldo\n`/crear_cedula @usuario` - Crear cédula\n`/editar_cedula @usuario` - Editar cédula\n`/eliminar_cedula @usuario` - Eliminar cédula",
        inline=False
    )
    
    return embed

def embed_bienvenida(usuario, servidor):
    """Embed de bienvenida por DM"""
    embed = crear_embed(
        titulo=f"👋 ¡BIENVENIDO A {servidor.name.upper()}!",
        color=VERDE
    )
    
    embed.description = f"Hola **{usuario.mention}**, nos alegra que te hayas unido a nuestra comunidad. Aquí encontrarás una experiencia única con múltiples características.\n\n"
    
    embed.add_field(
        name="💰 Economía",
        value="`/balance` - Ver tu balance\n`/work` - Trabajar\n`/daily` - Recompensa diaria\n`/payday` - Cobrar sueldo",
        inline=False
    )
    
    embed.add_field(
        name="🪪 Identidad",
        value="`/cedula` - Tu cédula de identidad",
        inline=False
    )
    
    embed.add_field(
        name="⚙️ Configuración",
        value="`/config` - Configuración del servidor",
        inline=False
    )
    
    embed.add_field(
        name="📊 Ranking",
        value="`/top` - Usuarios con más dinero",
        inline=False
    )
    
    embed.add_field(
        name="📞 Soporte",
        value="¿Dudas? Pregunta en el servidor, estamos para ayudarte.",
        inline=False
    )
    
    embed.set_thumbnail(url=usuario.avatar.url if usuario.avatar else usuario.default_avatar.url)
    
    return embed
