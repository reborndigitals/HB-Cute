import asyncio
import datetime
from VIPMUSIC import app
from pyrogram import Client
from VIPMUSIC.utils.database import get_served_chats
from config import START_IMG_URL, AUTO_GCAST_MSG, AUTO_GCAST, LOGGER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

AUTO_GCASTS = f"{AUTO_GCAST}" if AUTO_GCAST else False

START_IMG_URLS = "https://graph.org/file/ffdb1be822436121cf5fd.png"

MESSAGES = f"""  **𝐻𝑒𝑎𝑟𝑡 𝐵𝑒𝑎𝑡 𝐷𝑟𝑢𝑔𝑧𝑠 🖤✨ 𝐼𝑠 𝐴𝑑𝑣𝑎𝑛𝑐𝑒 𝑀𝑢𝑠𝑖𝑐 𝐵𝑜𝑡  😎🙂‍↔✨

𝑁𝑒𝑤 𝐹𝑒𝑎𝑡𝑢𝑟𝑒 📩✨

𝑁𝑜𝑤 𝑌𝑜𝑢 𝐶𝑎𝑛 𝑃𝑙𝑎𝑦 𝑊𝑖𝑡ℎ𝑜𝑢𝑡 [ / ] 🙅🏻

𝐸𝑥 : 𝑃𝑙𝑎𝑦 𝑆𝑜𝑛𝑔 𝑁𝑎𝑚𝑒 𝑂𝑅 𝑌𝑡 𝐿𝑖𝑛𝑘 🪶

𝑃𝑖𝑐𝑘𝑢𝑝 𝑙𝑖𝑛𝑒 💙✨, 𝐿𝑒𝑓𝑡 𝑁𝑜𝑡𝑖𝑐𝑒 😑✨ , 𝑇𝑎𝑔𝑎𝑙𝑙 🥳✨, 𝑉𝑐𝑇𝑎𝑔 🎥✨, 𝑉𝑖𝑑𝑒𝑜 𝐷𝑜𝑤𝑛𝑙𝑜𝑎𝑑 🔽✨, 𝐵𝑎𝑛 🚫✨, 𝑊𝑒𝑙𝑐𝑜𝑚𝑒 𝑁𝑜𝑡𝑖𝑐𝑒 😇✨

𝐻𝑒𝑎𝑟𝑡 𝐵𝑒𝑎𝑡 𝐷𝑟𝑢𝑔𝑧 🖤✨ 𝑆𝑝𝑙 𝐹𝑒𝑎𝑡𝑢𝑟𝑒 🦋✨

𝑃𝑖𝑐𝑘 𝑈𝑝 𝐿𝑖𝑛𝑒 🔐✨

𝐶𝑚𝑑 📲✨

/lifeline

/lovebeats

/heartbeat

𝑃𝑜𝑤𝑒𝑟 𝐵𝑦 - [𝞖𝘌𝘈𝘙𝘛𝂬♡𝂬𝞑𝘌𝘈𝘛▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ ](https://t.me/HeartBeat_Muzic) 😎✨

𝑂𝑤𝑛𝑒𝑟 - [𑫏ⳢⅬᤌໍᤌ᭄ᰈⅬᤌໍᤌ𑂞ⳣവᰈᮀ།ໍᴮᴬᵀ🦇](https://t.me/rajeshrakis) ❤🖤✨ 

𝑁𝑒𝑡𝑤𝑜𝑟𝑘 - [𝞖𝘌𝘈𝘙𝘛𝂬♡𝂬𝞑𝘌𝘈𝘛▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ](https://t.me/HeartBeat_Offi) 😎✨**"""


BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🦋‌𝞖𝘌𝘈𝘙𝘛𝂬♡𝂬‌𝞑𝘌𝘈𝘛▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ ‌𝆺𝅥🦋⤍🖤", url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
    ]
)

MESSAGE = f"""**𝐻𝑒𝑎𝑟𝑡 𝐵𝑒𝑎𝑡 𝐷𝑟𝑢𝑔𝑧 🖤✨ 𝐼𝑠 𝐴𝑑𝑣𝑎𝑛𝑐𝑒 𝑀𝑢𝑠𝑖𝑐 𝐵𝑜𝑡  😎🙂‍↔✨

𝑁𝑒𝑤 𝐹𝑒𝑎𝑡𝑢𝑟𝑒 📩✨

𝑁𝑜𝑤 𝑌𝑜𝑢 𝐶𝑎𝑛 𝑃𝑙𝑎𝑦 𝑊𝑖𝑡ℎ𝑜𝑢𝑡 [ / ] 🙅🏻

𝐸𝑥 : 𝑃𝑙𝑎𝑦 𝑆𝑜𝑛𝑔 𝑁𝑎𝑚𝑒 𝑂𝑅 𝑌𝑡 𝐿𝑖𝑛𝑘 🪶

𝑃𝑖𝑐𝑘𝑢𝑝 𝑙𝑖𝑛𝑒 💙✨, 𝐿𝑒𝑓𝑡 𝑁𝑜𝑡𝑖𝑐𝑒 😑✨ , 𝑇𝑎𝑔𝑎𝑙𝑙 🥳✨, 𝑉𝑐𝑇𝑎𝑔 🎥✨, 𝑉𝑖𝑑𝑒𝑜 𝐷𝑜𝑤𝑛𝑙𝑜𝑎𝑑 🔽✨, 𝐵𝑎𝑛 🚫✨, 𝑊𝑒𝑙𝑐𝑜𝑚𝑒 𝑁𝑜𝑡𝑖𝑐𝑒 😇✨

𝐻𝑒𝑎𝑟𝑡 𝐵𝑒𝑎𝑡 𝐷𝑟𝑢𝑔𝑧 🖤✨ 𝑆𝑝𝑙 𝐹𝑒𝑎𝑡𝑢𝑟𝑒 🦋✨

𝑃𝑖𝑐𝑘 𝑈𝑝 𝐿𝑖𝑛𝑒 🔐✨

𝐶𝑚𝑑 📲✨

/uruttu 

/pickup 

/love

𝑃𝑜𝑤𝑒𝑟 𝐵𝑦 - [𝞖𝘌𝘈𝘙𝘛𝂬♡𝂬𝞑𝘌𝘈𝘛▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ](https://t.me/HeartBeat_Muzic)😎✨

𝑂𝑤𝑛𝑒𝑟 - [𑫏ⳢⅬᤌໍᤌ᭄ᰈⅬᤌໍᤌ𑂞ⳣവᰈᮀ།ໍᴮᴬᵀ🦇](https://t.me/rajeshrakis) ❤🖤✨ 

𝑁𝑒𝑡𝑤𝑜𝑟𝑘 - [𝞖𝘌𝘈𝘙𝘛𝂬♡𝂬𝞑𝘌𝘈𝘛▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ](https://t.me/HeartBeat_Offi) 😎✨

🔐ᴜꜱᴇ » [/start](https://t.me/{app.username}?start=help) ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ

➲ ʙᴏᴛ :** @{app.username}"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("💕 𝐊𖽹𖽴𖽡𖽖𖽳 𝐌𖽞 🦋", url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
    ]
)

caption = f"""{AUTO_GCAST_MSG}""" if AUTO_GCAST_MSG else MESSAGES

TEXT = """**ᴀᴜᴛᴏ ɢᴄᴀsᴛ ɪs ᴇɴᴀʙʟᴇᴅ sᴏ ᴀᴜᴛᴏ ɢᴄᴀsᴛ/ʙʀᴏᴀᴅᴄᴀsᴛ ɪs ᴅᴏɪɴ ɪɴ ᴀʟʟ ᴄʜᴀᴛs ᴄᴏɴᴛɪɴᴜᴏᴜsʟʏ. **\n**ɪᴛ ᴄᴀɴ ʙᴇ sᴛᴏᴘᴘᴇᴅ ʙʏ ᴘᴜᴛ ᴠᴀʀɪᴀʙʟᴇ [ᴀᴜᴛᴏ_ɢᴄᴀsᴛ = (ᴋᴇᴇᴘ ʙʟᴀɴᴋ & ᴅᴏɴᴛ ᴡʀɪᴛᴇ ᴀɴʏᴛʜɪɴɢ)]**"""

async def send_text_once():
    try:
        await app.send_message(LOGGER_ID, TEXT)
    except Exception as e:
        pass

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URLS, caption=caption, reply_markup=BUTTONS)
                    await asyncio.sleep(20)  # Sleep for 100 second between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats

async def continuous_broadcast():
    await send_text_once()  # Send TEXT once when bot starts

    while True:
        if AUTO_GCAST:
            try:
                await send_message_to_chats()
            except Exception as e:
                pass

        # Wait for 100000 seconds before next broadcast
        await asyncio.sleep(100000)

# Start the continuous broadcast loop if AUTO_GCAST is True
if AUTO_GCAST:  
    asyncio.create_task(continuous_broadcast())
