  @bot.on(dev_cmd(pattern=r"ridi"))
async def ridi(event):
    if event.fwd_from:
        return
    await event.edit("AHAHAHAHAHAAHAHAHAHAHAHAHAHAHAAHAHAHAHAHAAHAHAHAH")
