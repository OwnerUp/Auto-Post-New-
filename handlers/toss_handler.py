# =========================================
# handlers/toss_handler.py
# =========================================

from telethon import events

import config

from channels import CHANNELS

from memory.memory_manager import *

from utils import (
    send_media_safe,
    send_text_safe
)

from templates.toss_templates import (
    royal_toss,
    batman_toss,
    betting_toss,
    game_toss,
    guddu_toss,
    rocky_toss,
    jacky_toss,
    priyanshu_toss,
    tossking_toss,
    reddy_toss,
    shiva_toss,
    rahul_toss,
    angad_toss,
    king_toss,
)

toss_posts = []

def register_toss_handler(client):

    @client.on(events.NewMessage(pattern='/toss'))

    async def toss_handler(event):

        raw_input = event.raw_text.replace(
            '/toss',
            ''
        ).strip()

        if not raw_input:

            await event.reply(
                "USE:\n/toss INDIA ⚡"
            )

            return

        parts = raw_input.split(maxsplit=1)

        team_name = parts[0].upper()

        emoji = ""

        if len(parts) > 1:

            emoji = parts[1]

        team = f"{team_name} {emoji}".strip()

        if not event.reply_to_msg_id:

            await event.reply(
                "REPLY TO PHOTO"
            )

            return

        reply_msg = await event.get_reply_message()

        ids = []

        for channel_name, channel in CHANNELS.items():

            if channel_name == "ROYAL":

                caption, promo = royal_toss(team)

            elif channel_name == "BATMAN":

                caption, promo = batman_toss(team)

            elif channel_name == "BETTING":

                caption, promo = betting_toss(
                    team,
                    config.CURRENT_LEAGUE
                )

            elif channel_name == "GAME":

                caption, promo = game_toss(
                    team,
                    config.CURRENT_LEAGUE
                )

            elif channel_name == "GUDDU":

                caption, promo = guddu_toss(
                    team,
                    config.CURRENT_LEAGUE
                )

            elif channel_name == "ROCKY":

                caption, promo = rocky_toss(team)

            elif channel_name == "JACKY":

                caption, promo = jacky_toss(
                    team,
                    config.CURRENT_LEAGUE
                )

            elif channel_name == "PRIYANSHU":

                caption, promo = priyanshu_toss(team)

            elif channel_name == "TOSSKING":

                caption, promo = tossking_toss(team)

            elif channel_name == "REDDY":

                caption, promo = reddy_toss(
                    team,
                    config.CURRENT_LEAGUE
                )

            elif channel_name == "SHIVA":

                caption, promo = shiva_toss(
                    team,
                    config.CURRENT_LEAGUE
                )

            elif channel_name == "RAHUL":

                caption, promo = rahul_toss(
                    team,
                    config.CURRENT_LEAGUE
                )

            elif channel_name == "ANGAD":

                caption, promo = angad_toss(team)

            elif channel_name == "KING":

                caption, promo = king_toss(
                    team,
                    config.CURRENT_LEAGUE
                )

            else:

                caption = f"""✈️ OWNER UPDATE ✈️

TOSS 😬 {team}
TOSS 😬 {team}

NO LIMIT TOSS✔️
BIG LIMIT SE PLAY ✔️
1000% WIN THIS TOSS ✔️
PLAY YOUR MAX AMOUNT ✔️

OWNER UPDATE ✅"""

                promo = f"""{team} WIN THE TOSS ✔️

WAIT FOR BEST ENTRY 💸

OWNER UPDATE ✅"""

            msg = await send_media_safe(

                client,

                channel,

                reply_msg,

                caption,

                channel_name
            )

            await send_text_safe(

                client,

                channel,

                promo,

                msg.id,

                channel_name
            )

            ids.append({
    "channel_id": channel,
    "msg_id": msg.id,
    "channel_name": channel_name
})

        # =========================
        # SAVE TOSS TO MEMORY
        # =========================

        data = load_memory()

        new_toss = {
    "id": get_next_id("tosses"),
    "match": team,
    "winner": team,
    "status": "pending",
    "posts": ids
}

        data["tosses"].append(new_toss)

        save_memory(data)

        print(f"\n✅ TOSS SAVED : ID {new_toss['id']}\n")

        toss_posts.append(ids)

        await event.reply(
            f"✅ TOSS POSTED\n🆔 ID : {new_toss['id']}"
        )


print("✅ TOSS HANDLER LOADED")