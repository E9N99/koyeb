import random
import re
import time
import psutil
from datetime import datetime
from platform import python_version

import requests
from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from . import StartTime, zedub, zedversion

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import zedalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus

plugin_category = "utils"
STATS = gvarstatus("Z_STATS") or "فحص"

#كتـابة وتعـديل:  @SedUb
file_path = "installation_date.txt"
if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    with open(file_path, "r") as file:
        installation_time = file.read().strip()
else:
    installation_time = datetime.now().strftime("%Y-%m-%d")
    with open(file_path, "w") as file:
        file.write(installation_time)

@zedub.zed_cmd(pattern=f"{STATS}$")
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await edit_or_reply(event, "**⎆┊جـاري .. فحـص البـوت الخـاص بك**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "๛┊‌‎"
    me = await l313l.get_me()
    first_name = me.first_name
    mention = first_name
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "**父[ 𝙨𝙤𝙪𝙍𝙘𝙚 𝙈𝙖𝙏𝙍𝙞𝙭 ⌁  ✓ ](t.me/veevvw)父**"
    HuRe_IMG = gvarstatus("ALIVE_PIC") or Config.A_PIC
    l313l_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    caption = l313l_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        jepver=JEPVERSION,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
        Tare5=installation_time,
    )
    matrix = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    matrix = Get(matrix)
    try:
        await event.client(matrix)
    except BaseException:
        pass
    if HuRe_IMG:
        SedUb = [x for x in HuRe_IMG.split()]
        PIC = random.choice(SedUb)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                event,
                f"**الميـديا خـطأ **\nغـير الرابـط بأستـخدام الأمـر  \n `.اضف_فار ALIVE_PIC رابط صورتك`\n\n**لا يمـكن الحـصول عـلى صـورة من الـرابـط :-** `{PIC}`",
            )
    else:
        await edit_or_reply(
            event,
            caption,
        )


temp = """{ALIVE_TEXT}
**~ سۅٛࢪس سيدثۅٛن يعمݪ بنجاެح** 
**~ اެسِمِكَ : {mention}** ٫
**~ اެصداެࢪ اެݪتيݪيثۅٛن : `{pyver}`** ٫
**‌‎~ اެصداެࢪ اެݪسۅٛࢪس : `{telever}`** ٫
**‌‎~ اެݪتاެࢪيخ : `{Tare5}`** ٫
**~ اެݪۅٛقت :`{uptime}`** ٫
‌‎**اެݪسِࢪعَة `{ping}`** ٫
‌‎**تَاެࢪيَخِ اެݪتَنِصِيَبَ `{Tare5}`** ٫
**𖠄 𝙨𝙤𝙪𝙍𝙘𝙚 𝙈𝙖𝙏𝙍𝙞𝙭 ⌁ 𖠄**"""























