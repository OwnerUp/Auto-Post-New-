# =========================================
# handlers/toss_pass.py
# =========================================

# removed unused import 'cmd' to avoid shadowing the local variable 'cmd'

from telethon import events

from utils import send_text_safe

from handlers.toss_handler import toss_posts

from channels import CHANNELS

from memory.memory_manager import *


# =========================================
# REGISTER
# =========================================

def register_toss_pass_handler(client):

    @client.on(events.NewMessage(pattern='/tpass'))

    async def toss_pass_handler(event):

        cmd = event.raw_text.split()

        if len(cmd) < 4:
            await event.reply(
                "USE:\n/tpass 1 INDIA BAT"
            )
            return

        toss_id = int(cmd[1])
        team = cmd[2].upper()
        choice = cmd[3].upper()

        data = load_memory()
        selected = None

        # find toss by id
        for toss in data["tosses"]:
            if toss["id"] == toss_id:
                # if already passed
                if toss.get("status") == "passed":
                    await event.reply("❌ TOSS ALREADY PASSED")
                    return

                selected = toss.get("posts")
                break

        if not selected:
            await event.reply("TOSS ID NOT FOUND")
            return

        # =====================================
        # LOOP
        # =====================================

        for post in selected:

            channel = post["channel_id"]

            msg_id = post["msg_id"]

            channel_name = post["channel_name"]

            # =================================
            # ROYAL
            # =================================

            if channel_name == "ROYAL":

                text = f"""{team} WON THE TOSS AND CALLED TO {choice} ✔️✔️

💥 BOOM 💥 BOOM 💥

TOSS PASS...✅️
PUNTER KHUS...✅️
HUM KHUS...✅️

ROYAL WIN 💠"""

            # =================================
            # BATMAN
            # =================================

            elif channel_name == "BATMAN":

                text = f"""{team} WON THE TOSS AND CALLED TO {choice} ✔️✔️

💥 BOOM 💥 BOOM 💥

PREMIUM PASS CONFIRM 🔥

BATMAN (Official) 💠"""

            # =================================
            # BETTING
            # =================================

            elif channel_name == "BETTING":

                text = f"""{team} WON THE TOSS AND DECIDED TO {choice} ✔️✔️

💰 BACK TO BACK PASS 💰
     BETTING KING
  HAIN TO PROFIT HAIN 

BETTING KING  💠"""

            # =================================
            # GAME
            # =================================

            elif channel_name == "GAME":

                text = f"""{team} WON THE TOSS AND DECIDED TO {choice} ✔️✔️

💥 BOOM 💥👊💥 BOOM 💥

FIX TOSS PASS
SURE TOSS PASS
LIFE TIME TOSS PASS

OPEN WORK TOSS PASS ✅✅

👉 GAME CHANGER ( Abhi ) 💠"""

            # =================================
            # GUDDU
            # =================================

            elif channel_name == "GUDDU":

                text = f"""{team} WON THE TOSS AND DECIDED TO {choice} ✔️✔️

Back To Back pass 🔻

Back To Back pass 🔻

Play With :- GUDDU PANDIT✅"""

            # =================================
            # ROCKY
            # =================================

            elif channel_name == "ROCKY":

                text = f"""{team} WON THE TOSS AND CALLED TO {choice} ✔️✔️

💥 BOOM 💥 BOOM 💥

FIX TOSS PASS
SURE TOSS PASS
LIFE TIME TOSS PASS

OPEN WORK TOSS PASS ✅

Rocky bhai (Trending King) 💠"""

            # =================================
            # JACKY
            # =================================

            elif channel_name == "JACKY":

                text = f"""{team} WON THE TOSS AND TO {choice} ✔️✔️

💣 BOOM 💣👍💣 BOOM 💣

FIX TOSS PASS
SURE TOSS PASS
LIFE TIME TOSS PASS

OPEN WORK TOSS PASS ✅️✅️

𝐎𝐍𝐋𝐘 👉 JACKY FIXER 💠"""

            # =================================
            # PRIYANSHU
            # =================================

            elif channel_name == "PRIYANSHU":

                text = f"""{team} HAVE WON THE TOSS & ELECTED TO 🏏 {choice} FIRST ✔️

𝐓𝐎𝐒𝐒 𝐏𝐀𝐒𝐒

𝐁𝐎𝐎𝐌 💥 𝐁𝐎𝐎𝐌 💥 𝐁𝐎𝐎𝐌✔️

ONLY 👉 PRIYANSHU BHAI 🏏 💠"""

            # =================================
            # TOSSKING
            # =================================

            elif channel_name == "TOSSKING":

                text = f"""{team} WON THE TOSS AND TO {choice} FIRST ✔️✔️

💥 BOOM 💥👊💥 BOOM 💥
💥 BOOM 💥👊💥 BOOM 💥

FIX TOSS PASS
SURE TOSS PASS
LIFE TIME TOSS PASS

CALL ➡️TOSS KING(Aditya)💠"""
                

            # =================================
            # REDDY
            # =================================

            elif channel_name == "REDDY":

                text = f"""{team} WON THE TOSS AND TO {choice} FIRST ✔️✔️

FIX TOSS PASS 
SURE TOSS PASS 
LIFE TIME TOSS PASS ✔️

CALL ➡️REDDY ANNA 💠"""
                
            # =================================
            # ANGAD
            # =================================

            elif channel_name == "ANGAD":

                text = f"""{team} WON THE TOSS AND TO {choice} FIRST ✔️✔️

    ONLY ONE IN MARKET
    JACKPOT KA BAAP KOUN 👇

FIX TOSS PASS 
SURE TOSS PASS 
LIFE TIME TOSS PASS ✔️

CALL ➡️ANGAD DADA 💠"""

            # =================================
            # RAHUL
            # =================================

            elif channel_name == "RAHUL":

                text = f"""{team} WON THE TOSS AND TO {choice} FIRST ✔️✔️

    JACKPOT KA BAAP KOUN 👇

FIX TOSS PASS 
SURE TOSS PASS 
LIFE TIME TOSS PASS ✔️

CALL ➡️RAHUL DADA 💠"""
                
            # =================================
            # SHIVA
            # =================================

            elif channel_name == "SHIVA":

                text = f"""{team} WON THE TOSS AND TO {choice} FIRST ✔️✔️

    💥 BOOM 💥👊💥 BOOM 💥 

FIX TOSS PASS
SURE TOSS PASS
LIFE TIME TOSS PASS

OPEN WORK TOSS PASS ✅
➡️Play Double Limit Toss ✔️

ONLY🔻SHIVA REDDY 💠"""
                
            # =================================
            # KING
            # =================================

            elif channel_name == "KING":

                text = f"""{team} WON THE TOSS AND TO {choice} ✔️✔️

💣 BOOM 💣👍💣 BOOM 💣

FIX TOSS PASS
SURE TOSS PASS
LIFE TIME TOSS PASS

OPEN WORK TOSS PASS ✅️✅️

𝐎𝐍𝐋𝐘 👉 THE KING 💠"""

            # =================================
            # OWNER CHANNELS
            # =================================

            else:

                text = f"""{team} HAVE WON THE TOSS & ELECTED TO 🏏 {choice} FIRST ✔️

𝐓𝐎𝐒𝐒 𝐏𝐀𝐒𝐒

𝐁𝐎𝐎𝐌 💥 𝐁𝐎𝐎𝐌 💥 𝐁𝐎𝐎𝐌✔️

OWNER UPDATE ✅"""

            # =================================
            # SEND
            # =================================

            await send_text_safe(

                client,

                channel,

                text,

                msg_id,

                channel_name
            )
        
        for toss in data["tosses"]:

            if toss["id"] == toss_id:

                toss["status"] = "passed"

                break

        save_memory(data)

        await event.reply(
          "✅ TOSS PASS POSTED"
)


print("✅ TOSS PASS HANDLER LOADED")