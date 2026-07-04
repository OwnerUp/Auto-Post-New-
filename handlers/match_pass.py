# =========================================
# handlers/match_pass.py
# FINAL FULLY FIXED WORKING VERSION
# =========================================

import cmd
from re import match

from telethon import events

from utils import send_text_safe

from handlers.match_handler import match_posts

from memory.memory_manager import *


# =========================================
# REGISTER
# =========================================

def register_match_pass_handler(client):

    @client.on(events.NewMessage(pattern='/mpass'))

    async def match_pass_handler(event):

        cmd = event.raw_text.split(maxsplit=3)

        if len(cmd) < 4:

            await event.reply(

                "USE:\n/mpass CSK 10 WICKETS"
            )

            return

        match_id = int(cmd[1])

        team = cmd[2].upper()

        result = cmd[3].upper()
    
        data = load_memory()

        selected = None

        for match in data["matches"]:
            if match["id"] == match_id:
                if match["status"] == "passed":
                    await event.reply(
                        "❌ MATCH ALREADY PASSED"
                    )
                    return

                selected = match["posts"]
                break

        if not selected:
            await event.reply(
                "MATCH ID NOT FOUND"
            )
            return

        # =====================================
        # LOOP
        # =====================================

        for post in selected:
                        
            channel = post["channel_id"]

            msg_id = post["msg_id"]

            channel_name = post["channel_name"]

            ctype = channel_name

            # =====================================
            # ROYAL
            # =====================================

            if ctype == "ROYAL":

                text = f"""{team} WIN BY {result} 🏆

🤜 B O O M B O O M 🤜

ROYALS WIN KE SATH ONLY PROFIT 🏆

AGEN FUCK ALL MARKET 🤑

ROYALS WIN 💠"""

            # =====================================
            # BATMAN
            # =====================================

            elif ctype == "BATMAN":

                text = f"""{team} WON BY {result} ✅

AGEN FUCK ALL MARKET🥳

💥 Back to Back Pass 💥

🏆🏆Jeet Mubarak 🏆🏆

BATMAN (Official) 💠"""

            # =====================================
            # GAME
            # =====================================

            elif ctype == "GAME":

                text = f"""{team} WON BY {result} 🏆

🤜B O O M B O O M🤜

GAME CHANGER ABHI KE SATH

 ONLY ON PROFIT 🏆

AGEN FUCK ALL MARKET 🤑

GAME CHANGER ABHI 💠"""

            # =====================================
            # GUDDU
            # =====================================

            elif ctype == "GUDDU":

                text = f"""{team} won by {result}

ONLY ON PROFIT 🏆

AGEN FUCK ALL MARKET🥳

💥 Back to Back Pass 💥

GUDDU PANDIT ✅"""

            # =====================================
            # ROCKY
            # =====================================

            elif ctype == "ROCKY":

                text = f"""{team} WIN BY {result} ✅

Back-to-Back Match PASS 💥🔥

Market mein sirf naam hi nahi… kaam bhi bolta hai 💯

Poora market ek taraf…
Apka bhai Akele 😎👑

Kyon pade ho chakkaron mein?
Koi nahi hai takkar mein! 💪🔥

Rocky bhai (Trending King) 💠"""

            # =====================================
            # JACKY
            # =====================================

            elif ctype == "JACKY":

                text = f"""{team} WON BY {result} ✅

🎯 Exact Match Prediction Passed 💯

🔥 Another Successful Call 🔥

💵 Profit Done For Premium Members 💵

Only 🔻 JACKY FIXER 💠"""

            # =====================================
            # PRIYANSHU
            # =====================================

            elif ctype == "PRIYANSHU":

                text = f"""{team} WIN BY {result}

🤜B O O M B O O M🤜

PRIYANSHU BHAI KE SATH ONLY PROFIT 🏆

SUPRE SURE MATCH
ONLY ONE IN MARKET
AGEN FUCK ALL MARKET 🤑

PRIYANSHU BHAI 💠"""

            # =====================================
            # TOSS KING
            # =====================================

            elif ctype == "TOSSKING":

                text = f"""🏏 {team} WON BY {result} ✅️

Match Passed 💯

Another Successful Call 🔥

Profit Done For Premium Members 💵

CALL ➡️TOSS KING(Aditya)💠"""

            # =====================================
            # REDDY
            # =====================================

            elif ctype == "REDDY":

                text = f"""{team} WIN BY {result}

🤜B O O M B O O M🤜

SUPRE SURE MATCH
ONLY ONE IN MARKET
AGEN FUCK ALL MARKET 🤑

REDDY ANNA 💠"""

            # =====================================
            # SHIVA
            # =====================================

            elif ctype == "SHIVA":

                text = f"""{team} WON BY {result}🏆

AGEN FUCK ALL MARKET🥳

💥 Back to Back Pass 💥

Happy for Win

✅ All Market Fail
✅ Bane raho aur profit karo.....

ONLY🔻SHIVA REDDY 💠"""

            # =====================================
            # RAHUL
            # =====================================

            elif ctype == "RAHUL":

                text = f"""{team} WIN BY {result}

ONLY PROFIT 🏆

AGEN FUCK ALL MARKET🥳

💥 Back to Back Pass 💥

🏆🏆Jeet Mubarak 🏆🏆

✅ Boom Boom Boom…
✅ Full Market Fail…
✅ Always Profit With Me.....

ONLY ➡️ RAHUL DADA 💠"""

            # =====================================
            # ANGAD
            # =====================================

            elif ctype == "ANGAD":

                text = f"""{team} WON BY {result} 🏆

AGEN FUCK ALL MARKET🥳

💥 Back to Back Pass 💥

🏆🏆Jeet Mubarak 🏆🏆

✔️ Boom Boom Boom…
✔️ Full Market Fail…
✔️ Always Profit With Me.....

ONLY 🔻ANGAD DADA 💠"""

            # =====================================
            # KING
            # =====================================

            elif ctype == "KING":

                text = f"""{team} WIN BY {result}

ONLY PROFIT 🏆

AGEN FUCK ALL MARKET🥳

💥 Back to Back Pass 💥

🏆🏆Jeet Mubarak 🏆🏆

✅ Boom Boom Boom…
✅ Full Market Fail…
✅ Always Profit With Me.....

𝐎𝐍𝐋𝐘 👉 THE KING 💠"""

             # =====================================
            # BETTING
            # =====================================

            elif ctype == "BETTING":

                text = f"""{team} WIN BY {result} 🏆

BETTING KING KE SATH ONLY PROFIT 🏆

AGEN FUCK ALL MARKET🥳

💥 Back to Back Pass 💥

🏆🏆Jeet Mubarak 🏆🏆

✅ Boom Boom Boom…
✅ Full Market Fail…
✅ Always Profit With Me.....

BETTING KING 💠"""

            # =====================================
            # OWNER UPDATE
            # =====================================

            else:

                text = f"""{team} WON BY {result} ✅

💥 MATCH PASS CONFIRM 💥

🏆 PREMIUM ENTRY PASSED 🏆

🤑 CLIENTS IN HUGE PROFIT 🤑

OWNER UPDATE ✅"""

            # =====================================
            # SEND
            # =====================================

            await send_text_safe(
             client,
             channel,
            text,
            msg_id,
           channel_name
)

            for match in data["matches"]:

                if match["id"] == match_id:

                 match["status"] = "passed"

                 break

                save_memory(data)

        await event.reply(

           "✅ MATCH PASS POSTED"
)

print("✅ MATCH PASS HANDLER LOADED")