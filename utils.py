# =========================================
# utils.py
# =========================================

from io import BytesIO

from telethon.errors.rpcerrorlist import (

    DocumentInvalidError

)

from emoji_engine import premium_entities


# =========================================
# SAFE MEDIA SEND
# =========================================

async def send_media_safe(

    client,
    channel,
    reply_msg,
    caption,
    channel_name

):

    entities = premium_entities(

        caption,
        channel_name
    )

    try:

        return await client.send_file(

            channel,

            file=reply_msg.media,

            caption=caption,

            formatting_entities=entities,

            parse_mode=None
        )

    except DocumentInvalidError:

        media_stream = BytesIO()

        await reply_msg.download_media(
            file=media_stream
        )

        media_stream.seek(0)

        return await client.send_file(

            channel,

            file=media_stream,

            caption=caption,

            formatting_entities=entities,

            parse_mode=None
        )


# =========================================
# SAFE TEXT SEND
# =========================================

async def send_text_safe(

    client,
    channel,
    text,
    reply_to,
    channel_name

):

    entities = premium_entities(

        text,
        channel_name
    )

    return await client.send_message(

        channel,

        text,

        reply_to=reply_to,

        formatting_entities=entities,

        parse_mode=None,

        link_preview=False
    )


print("✅ UTILS LOADED")