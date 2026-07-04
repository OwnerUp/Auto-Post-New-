# =========================================
# handlers/match_handler.py
# =========================================

from telethon import events

import config

from memory.memory_manager import *

from channels import CHANNELS

from utils import (

    send_media_safe,
    send_text_safe

)

from templates.match_templates import (

    royal_match,
    batman_match,
    betting_match,
    game_match,
    guddu_match,
    rocky_match,
    jacky_match,
    priyanshu_match,
    tossking_match,
    reddy_match,
    shiva_match,
    rahul_match,
    angad_match,
    king_match,
)

# =========================================
# MEMORY
# =========================================

match_posts = []


# =========================================
# REGISTER
# =========================================

def register_match_handler(client):

    @client.on(events.NewMessage(pattern='/match'))

    async def match_handler(event):

        raw = event.raw_text.replace(

            '/match',
            ''

        ).strip()

        try:

            parts = raw.split(" w ")

            teams = parts[0]

            winner = parts[1]

            team1 = teams.split(" vs ")[0].upper()

            team2 = teams.split(" vs ")[1].upper()

        except:

            await event.reply(

                "USE:\n/match CSK vs MI w CSK"
            )

            return

        if not event.reply_to_msg_id:

            await event.reply(
                "REPLY TO PHOTO"
            )

            return

        reply_msg = await event.get_reply_message()

        ids = []

        # =====================================
        # LOOP CHANNELS
        # =====================================

        for channel_name, channel in CHANNELS.items():

            # =================================
            # ROYAL
            # =================================

            if channel_name == "ROYAL":

                text, promo1, promo2 = royal_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # BATMAN
            # =================================

            elif channel_name == "BATMAN":

                text, promo1, promo2 = batman_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # BETTING
            # =================================

            elif channel_name == "BETTING":

                text, promo1, promo2 = betting_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # GAME
            # =================================

            elif channel_name == "GAME":

                text, promo1, promo2 = game_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # GUDDU
            # =================================

            elif channel_name == "GUDDU":

                text, promo1, promo2 = guddu_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # ROCKY
            # =================================

            elif channel_name == "ROCKY":

                text, promo1, promo2 = rocky_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # JACKY
            # =================================

            elif channel_name == "JACKY":

                text, promo1, promo2 = jacky_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # PRIYANSHU
            # =================================

            elif channel_name == "PRIYANSHU":

                text, promo1, promo2 = priyanshu_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # TOSSKING
            # =================================

            elif channel_name == "TOSSKING":

                text, promo1, promo2 = tossking_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # REDDY
            # =================================

            elif channel_name == "REDDY":

                text, promo1, promo2 = reddy_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # SHIVA
            # =================================

            elif channel_name == "SHIVA":

                text, promo1, promo2 = shiva_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )
                            # =================================
            # RAHUL
            # =================================

            elif channel_name == "RAHUL":

                text, promo1, promo2 = rahul_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # ANGAD
            # =================================

            elif channel_name == "ANGAD":

                text, promo1, promo2 = angad_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # KING
            # =================================

            elif channel_name == "KING":

                text, promo1, promo2 = king_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # OWNER CHANNELS
            # =================================

            else:

                text = f"""✈️ OWNER UPDATE ✈️

🆘 {config.CURRENT_LEAGUE} 🆘

{team1} 🆚 {team2}

TV BAND REPORT....
TELEGRAM TOD REPORT.....

Winner ➡️ {winner}

Loss Cut Book Set At 10P 💸

WAIT FOR BEST TRAINING ENTRY

OWNER UPDATE ✅"""

                promo1 = f"""Jitna Khel Sakte Ho Khelo....

With Max Amount...

{winner} Will Win This MATCH..!! 🤑✔️

OWNER UPDATE ✅"""

                promo2 = None

            # =================================
            # SEND MEDIA
            # =================================

            msg = await send_media_safe(

                client,

                channel,

                reply_msg,

                text,

                channel_name
            )

            # =================================
            # SEND PROMO 1
            # =================================

            await send_text_safe(

                client,

                channel,

                promo1,

                msg.id,

                channel_name
            )

                        # =================================
            # SEND PROMO 2
            # =================================

            if promo2:

                await send_text_safe(

                    client,

                    channel,

                    promo2,

                    msg.id,

                    channel_name
                )

            ids.append({

                "channel_id": channel,

                "msg_id": msg.id,

                "channel_name": channel_name

            })

        # =========================
        # SAVE MATCH TO MEMORY
        # =========================

        data = load_memory()

        new_match = {
        "id": get_next_id("matches"),
        "team1": team1,
        "team2": team2,
        "winner": winner,
        "status": "pending",
        "posts": ids
}

        data["matches"].append(new_match)

        save_memory(data)

        print(f"\n✅ MATCH SAVED : ID {new_match['id']}\n")

        match_posts.append(ids)

        await event.reply(

            f"✅ MATCH POSTED\n🆔 ID : {new_match['id']}"
        )

print("✅ MATCH HANDLER LOADED")