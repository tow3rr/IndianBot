"""Commands:
.bombs
.fuck
.kiss
.love
.pornhub
.sex
.sexy"""

import asyncio
from telethon import events
from userbot import bot
from userbot.system import admin_cmd


@bot.on(admin_cmd(pattern=f"bombs", outgoing=True))
async def _(event):
    if event.fwd_from:
        return 
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")
    await asyncio.sleep(1)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n")
    await asyncio.sleep(0.5)
    await event.edit("`RIP 😵😵😵...`")
    await asyncio.sleep(2)
    

@bot.on(admin_cmd(pattern=f"fuck", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.2
    animation_ttl = range(0, 101)
    #input_str = event.pattern_match.group(1)
    #if input_str == "fuck":
    await event.edit("fuck")
    animation_chars = [

            "👉       ✊️",

            "👉     ✊️",

            "👉  ✊️",

            "👉✊️💦"

        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])


@bot.on(admin_cmd(pattern="love", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 101)
    #input_str = event.pattern_match.group(1)
    #if input_str == "love":
    await event.edit("love")
    animation_chars = [

            "L_",

            "LO_",

            "LOV_",
            
            "LOVE_",
            
            "LOVE❤",
            

        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 10])


@bot.on(admin_cmd(pattern=f"kiss", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.2
    animation_ttl = range(0, 101)
    #input_str = event.pattern_match.group(1)
    #if input_str == "kiss":
    await event.edit("kiss")
    animation_chars = [

            "🤵       👰",

            "🤵     👰",

            "🤵  👰",

            "🤵💋👰"

        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])


@bot.on(admin_cmd(pattern="pornhub", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 101)
    #input_str = event.pattern_match.group(1)
    #if input_str == "pornhub":
    await event.edit("pornhub")
    animation_chars = [

            "P_",

            "PO_",

            "POR_",

            "PORN_",
            
            "PORNH_",
            
            "PORNHU_",
            
           "PORNHUB_", 
           
           "PORNHUB",

        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 10])


@bot.on(admin_cmd(pattern=f"sex", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.2
    animation_ttl = range(0, 101)
    #input_str = event.pattern_match.group(1)
    #if input_str == "sex":
    await event.edit("sex")
    animation_chars = [

            "🤵       👰",

            "🤵     👰",

            "🤵  👰",

            "🤵👼👰"

        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])


@bot.on(admin_cmd(pattern="sexy", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 101)
    #input_str = event.pattern_match.group(1)
    #if input_str == "sexy":
    await event.edit("sexy")
    animation_chars = [

            "S_",

            "SE_",

            "SEX_",

            "SEXY_",
            
            "SEXY👄_",
            
            "SEXY👄",
            
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 10])
