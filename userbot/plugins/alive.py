from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

name = str(ALIVE_NAME)
INDIANBOT_IS_ALIVE = (
    "**┏╋━━━━◥◣◆◢◤━━━━╋┓**\n\n"
    f"`Il mio capo`: {name}\n\n"
    "`Ha avviato l'userbot`\n"
    "`Stato:` **ONLINE**\n`"
    "┗╋━━━━◥◣◆◢◤━━━━╋┛"
)


@borg.on(admin_cmd(pattern="alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    await borg.send_message(chat, INDIANBOT_IS_ALIVE, link_preview=False)
