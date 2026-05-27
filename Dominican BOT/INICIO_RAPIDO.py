#!/usr/bin/env python3
"""
🚀 GUÍA RÁPIDA DE INICIO
Ejecuta este script para ayuda rápida
"""

print("""
╔════════════════════════════════════════════════════════════╗
║    🤖 BOT DOMINICANO AVANZADO PARA DISCORD 🇩🇴            ║
║           ¡Bienvenido! Aquí está tu guía rápida           ║
╚════════════════════════════════════════════════════════════╝

📋 PASOS INICIALES:

1️⃣  CREAR BOT EN DISCORD
   ➜ Ve a: https://discord.com/developers/applications
   ➜ Click "New Application"
   ➜ Ve a "Bot" y click "Add Bot"
   ➜ Copia el TOKEN

2️⃣  HABILITAR INTENTS
   ➜ En Discord Developer Portal
   ➜ Bot > Intents
   ➜ Habilita:
      ✓ Message Content Intent
      ✓ Server Members Intent
      ✓ Presence Intent

3️⃣  GENERAR LINK DE INVITACIÓN
   ➜ OAuth2 > URL Generator
   ➜ Scope: bot
   ➜ Permissions: Send Messages, Embed Links, etc.
   ➜ Copia el link y abre en navegador

4️⃣  INSTALAR DEPENDENCIAS
   python -m pip install -r requirements.txt

5️⃣  CONFIGURAR TOKEN
   
   🔹 OPCIÓN A - LOCAL:
      export DISCORD_TOKEN="tu_token_aqui"
      python main.py
   
   🔹 OPCIÓN B - REPLIT:
      ➜ Click 🔒 Secrets
      ➜ Agrega: DISCORD_TOKEN = tu_token_aqui
      ➜ Run: python main.py

6️⃣  CONFIGURAR EN DISCORD
   Una vez el bot esté en tu servidor (como ADMIN):
   
   /config logs #📋-logs
   /config bienvenida #👋-bienvenida
   /config moneda 💵
   /config payday 12h
   /config work 1h
   /config daily 24h

7️⃣  ESTABLECER SUELDOS
   /set_sueldo @Miembro 500
   /set_sueldo @VIP 2000
   /set_sueldo @Moderador 3000

═══════════════════════════════════════════════════════════════

📚 COMANDOS DISPONIBLES:

💰 ECONOMÍA:
   /balance - Tu balance
   /work - Trabajar
   /daily - Recompensa diaria
   /payday - Cobrar sueldo
   /depositar <cantidad> - Depositar
   /retirar <cantidad> - Retirar
   /transferir @usuario <cantidad> - Enviar dinero
   /top - Ranking

🪪 IDENTIDAD:
   /cedula - Tu cédula
   /ver_cedula @usuario - Ver cédula de alguien

⚙️ ADMIN:
   /set_sueldo @rol <cantidad> - Establecer sueldo
   /config <opcion> <valor> - Configurar servidor
   /crear_cedula @usuario - Crear cédula
   /editar_cedula @usuario - Editar cédula
   /eliminar_cedula @usuario - Eliminar cédula

📚 OTROS:
   /help - Ver todos los comandos

═══════════════════════════════════════════════════════════════

🔧 TROUBLESHOOTING:

❌ El bot no inicia
   ✓ Verifica el token en variables de entorno
   ✓ Asegúrate que Python 3.8+ está instalado
   ✓ Ejecuta: pip install -r requirements.txt

❌ El bot no responde en Discord
   ✓ Verifica que el token sea correcto
   ✓ Comprueba permisos en el servidor
   ✓ Habilita los Intents necesarios

❌ Comando no funciona
   ✓ Usa /help para ver comandos
   ✓ Algunos comandos requieren admin
   ✓ Espera a que se sincronic en los slash commands

═══════════════════════════════════════════════════════════════

📁 ESTRUCTURA DEL PROYECTO:

Dominican BOT/
├── main.py ..................... Archivo principal
├── requirements.txt ............. Dependencias
├── README.md .................... Documentación
├── CONFIGURACION.md ............. Guía de configuración
├── bot_database.db .............. Base de datos (se crea automáticamente)
├── utils/
│   ├── database.py .............. Sistema de BD
│   ├── embeds.py ................ Diseños
│   └── validar.py ............... Validaciones
└── cogs/
    ├── economia.py .............. Dinero
    ├── cedula.py ................ Cédulas
    ├── admin.py ................. Admin
    ├── eventos.py ............... Eventos
    └── help.py .................. Ayuda

═══════════════════════════════════════════════════════════════

💡 TIPS IMPORTANTES:

✓ El bot crea automáticamente la base de datos
✓ Los embeds son completamente personalizables
✓ Los logs se guardan automáticamente
✓ Los cooldowns son configurables por servidor
✓ Compatible 100% con Replit
✓ Sin errores, código limpio y profesional

═══════════════════════════════════════════════════════════════

📝 PRÓXIMOS PASOS:

1. Lee README.md para más detalles
2. Lee CONFIGURACION.md para todas las opciones
3. Revisa el código en cogs/ para entender la estructura
4. Personaliza colors, textos y comportamientos
5. ¡Disfruta tu bot!

═══════════════════════════════════════════════════════════════

❓ ¿NECESITAS AYUDA?

📖 Documentación: Lee README.md y CONFIGURACION.md
🔍 Código: Revisa los comentarios en cada archivo
💬 Comunidad: Pregunta en tu servidor Discord
📧 Issues: Abre un ticket si encuentras problemas

═══════════════════════════════════════════════════════════════

¡Gracias por usar el Bot Dominicano! 🇩🇴 ❤️

Hecho con 💜 para la comunidad Discord dominicana
""")
