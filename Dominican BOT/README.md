# 🤖 BOT DOMINICANO AVANZADO PARA DISCORD

Bot avanzado y profesional para Discord con sistema de economía, cédulas de identidad, sueldos por rol y más.

## ✨ Características

### 💰 Sistema de Economía
- `balance` - Ver balance de dinero
- `work` - Trabajar y ganar dinero (cooldown configurable)
- `daily` - Recompensa diaria (24h)
- `payday` - Cobrar sueldo por rol
- `depositar <cantidad>` - Depositar en banco
- `retirar <cantidad>` - Retirar del banco
- `transferir @usuario <cantidad>` - Transferir dinero
- `top` - Ver ranking de usuarios

### 🪪 Sistema de Cédulas
- `cedula` - Ver tu cédula de identidad
- `ver_cedula @usuario` - Ver cédula de otro usuario
- `crear_cedula @usuario` - [ADMIN] Crear cédula
- `editar_cedula @usuario` - [ADMIN] Editar cédula
- `eliminar_cedula @usuario` - [ADMIN] Eliminar cédula

### 💼 Sistema de Sueldos
- `set_sueldo @rol <cantidad>` - [ADMIN] Establecer sueldo
- Cobro automático con `/payday`
- Se cobra el sueldo más alto si tienes múltiples roles

### ⚙️ Configuración
- `config logs #canal` - Establecer canal de logs
- `config bienvenida #canal` - Establecer canal de bienvenida
- `config moneda <emoji>` - Cambiar moneda
- `config payday 12h` - Cooldown de payday
- `config work 1h` - Cooldown de work
- `config daily 24h` - Cooldown de daily
- `mostrar_config` - Ver configuración actual

### 📚 Otros
- `help` - Ver todos los comandos
- Bienvenida automática por DM
- Sistema completo de logs
- Base de datos SQLite

## 📋 Requisitos

- Python 3.8+
- discord.py 2.3.2+
- SQLite3 (incluido en Python)

## 🚀 Instalación

### Local

1. Clona o descarga el proyecto
2. Abre la carpeta en una terminal
3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. En Replit o como variable de entorno, configura tu token:
```bash
export DISCORD_TOKEN="tu_token_aqui"
```

5. Ejecuta el bot:
```bash
python main.py
```

### Replit

1. Crea un nuevo Replit project
2. Importa los archivos del repositorio
3. Ve a "Secrets" (🔒 ícono) y agrega:
   - **Key**: `DISCORD_TOKEN`
   - **Value**: Tu token de Discord
4. Ejecuta el bot:
```bash
python main.py
```

## 🔑 Obtener Token de Discord

1. Ve a [Discord Developer Portal](https://discord.com/developers/applications)
2. Crea una nueva aplicación
3. Ve a "Bot" > "Add Bot"
4. Copia el token bajo el nombre del bot
5. Habilita los Intents necesarios:
   - Message Content Intent ✅
   - Server Members Intent ✅
   - Presence Intent ✅

## 📱 Invitar el Bot

1. En Developer Portal, ve a "OAuth2" > "URL Generator"
2. Selecciona estos scopes:
   - `bot`
3. Selecciona estos permisos:
   - Send Messages ✅
   - Embed Links ✅
   - Read Messages ✅
   - Manage Messages ✅
4. Copia la URL generada y abre en navegador

## 💾 Base de Datos

El bot crea automáticamente `bot_database.db` con estas tablas:

- **usuarios** - Datos de usuarios
- **economia** - Saldos y dinero
- **salarios_roles** - Sueldos por rol
- **cedulas** - Cédulas de identidad
- **config** - Configuración del servidor
- **logs** - Registro de eventos

## 📁 Estructura del Proyecto

```
Dominican BOT/
├── main.py                 # Archivo principal
├── requirements.txt        # Dependencias
├── .gitignore             # Archivos ignorados
├── bot_database.db        # Base de datos (se crea automáticamente)
├── utils/
│   ├── __init__.py
│   ├── database.py        # Sistema de BD
│   ├── embeds.py          # Diseños de embeds
│   └── validar.py         # Funciones de validación
└── cogs/
    ├── __init__.py
    ├── economia.py        # Comandos de economía
    ├── cedula.py          # Comandos de cédulas
    ├── admin.py           # Comandos de admin
    ├── eventos.py         # Eventos del bot
    └── help.py            # Comando de ayuda
```

## ⚙️ Configuración Recomendada

Al agregar el bot a tu servidor, configura:

```
/config logs #📋-logs
/config bienvenida #👋-bienvenida
/config moneda 💵
/config payday 12h
/config work 1h
/config daily 24h
```

Luego establece sueldos:

```
/set_sueldo @Miembro 500
/set_sueldo @VIP 2000
/set_sueldo @Moderador 3000
```

## 🎨 Diseño

- Embeds modernos y elegantes
- Colores: Azul, Verde, Rojo
- Footers personalizados
- Thumbnails de usuarios
- Timestamps automáticos

## 🔒 Seguridad

- Validación de permisos en comandos admin
- Cooldowns para evitar spam
- Verificación de saldos antes de operaciones
- Logs de todas las operaciones

## 📝 Notas

- Las cédulas se generan automáticamente si no existen
- El dinero se guarda en SQLite
- Los logs se registran automáticamente
- Los embeds se adaptan al servidor
- Bienvenida automática (sin error si falla)

## 🐛 Troubleshooting

**El bot no responde**
- Verifica que el token sea correcto
- Asegúrate de que los Intents estén habilitados
- Revisa los permisos en el servidor

**Comando no funciona**
- Usa `/help` para ver comandos disponibles
- Verifica que tengas permisos suficientes
- Algunos comandos son solo para admin

**Base de datos corrupta**
- Elimina `bot_database.db`
- Reinicia el bot (se creará automáticamente)

## 📞 Soporte

Para preguntas o problemas, abre un issue o pregunta en tu servidor Discord.

## 📄 Licencia

Uso libre para servidores Discord personales.

---

**Hecho con ❤️ para la comunidad dominicana** 🇩🇴
