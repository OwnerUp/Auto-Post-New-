# =========================================
# main.py
# =========================================

from telethon import TelegramClient

from config import (

    API_ID,
    API_HASH,
    PHONE,
    SESSION_NAME

)

# =========================================
# HANDLERS
# =========================================

from handlers.league_handler import (
    register_league_handler
)

from handlers.toss_handler import (
    register_toss_handler
)

from handlers.toss_pass import (
    register_toss_pass_handler
)

from handlers.match_handler import (
    register_match_handler
)

from handlers.match_pass import (
    register_match_pass_handler
)

from handlers.session_handler import (
    register_session_handler
)

from handlers.session_pass import (
    register_session_pass_handler
)

from handlers.session_loss import (
    register_session_loss_handler
)

# =========================================
# CLIENT
# =========================================

client = TelegramClient(

    SESSION_NAME,

    API_ID,

    API_HASH
)

# =========================================
# REGISTER ALL
# =========================================

register_league_handler(client)

register_toss_handler(client)

register_toss_pass_handler(client)

register_match_handler(client)

register_match_pass_handler(client)

register_session_handler(client)

register_session_pass_handler(client)

register_session_loss_handler(client)

# =========================================
# START
# =========================================

async def main():

    await client.start(
        phone=PHONE
    )

    me = await client.get_me()

    print(
        f"✅ LOGGED IN: {me.first_name}"
    )

    print("🚀 PREMIUM MULTI BOT STARTED")

    await client.run_until_disconnected()


# =========================================
# RUN
# =========================================

if __name__ == "__main__":

    with client:

        client.loop.run_until_complete(
            main()
        )