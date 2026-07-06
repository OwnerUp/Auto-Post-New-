# =========================================

# templates/session_templates.py

# =========================================

def session_call_emoji(call):
    if call == "YES":
        return "✅"
    return "❌"

# =========================================

# ROYAL

# =========================================

def royal_session(over, run, call):
    emoji = session_call_emoji(call)
    return f"{over} OVER 🌐 {call} KARO {emoji}\n\n{run} RUN 🛡"

def royal_session_pass(over, result):
    return f"{result} 🅿️🅰️💲💲✔️\n\n{over} OVER 👑\n\nSESSIONS PASS 💸❤️"

def royal_session_loss():
    return " SESSION APNA LOSS RAHA ❌ 
    KOI BAAT NHI ABHI COVAR HO JAYEGA "

# =========================================

# BETTING

# =========================================

def betting_session(over, run, call):
    emoji = session_call_emoji(call)
    return f"{run} RUN 🤔 {over} OVER\n\n{call} KARO {emoji}\n\n20K LIMIT SE PLAY 🥳"

def betting_session_pass(result):
    return f"{result} 🅿️🅰️💵💵✔️✔️\n\nSESSIONS PASS 💰🔥\n\n💫 🅱𝗢𝗢Ⓜ️ 💫 🅱𝗢𝗢Ⓜ"

def betting_session_loss():
    return "LOSS ❌"

# =========================================

# BATMAN

# =========================================

def batman_session(over, run, call):
    emoji = session_call_emoji(call)
    return f"{over} OVER 👉 {run} RUN\n\nBINDASS 👍\n\n{call} KARO 👉 {emoji}\n\n20K LIMIT SE PLAY 💰"

def batman_session_pass(result):
    return f"{result} 🅿️🅰️💵💵✔️\n\nSESSIONS PASS ✊"

def batman_session_loss():
    return "LOSS ❌"

# =========================================

# GAME

# =========================================

def game_session(over, run, call):
    emoji = session_call_emoji(call)
    return f"🎯 TARGET LOCK\n\n{run} RUN\n\n{over} OVER\n\n{call} KARO {emoji}"

def game_session_pass(result):
    return f"{result} 💸💸✔️\n\nSESSIONS PASS 🎯\n\nTARGET HIT 🔥"

def game_session_loss():
    return "LOSS ❌"

# =========================================

# GUDDU

# =========================================

def guddu_session(over, run, call):
    emoji = session_call_emoji(call)
    return f"🔱 MAHADEV KRIPA 🔱\n\n{run} RUN\n\n{call} KARO {emoji}\n\n{over} OVER"

def guddu_session_pass(result):
    return f"{result} 💰💰✔️\n\nSESSIONS PASS 🔱\n\nHAR HAR MAHADEV ❤️"

def guddu_session_loss():
    return "LOSS ❌"

# =========================================

# ROCKY

# =========================================

def rocky_session(over, run, call):
    emoji = session_call_emoji(call)
    return f"KGF SPECIAL 👑\n\n{over} OVER\n\n{call} KARO {emoji}\n\n{run} RUN"

def rocky_session_pass(result):
    return f"{result} 🅿️🅰️💵💵✔️\n\nSESSIONS PASS 👑\n\nROCKY BOOM 💥"

def rocky_session_loss():
    return "LOSS ❌"

# =========================================

# PRIYANSHU

# =========================================

def priyanshu_session(over, run, call):
    emoji = session_call_emoji(call)
    return f"🚀 ROCKET ENTRY\n\n{call} KARO {emoji}\n\n{run} RUN\n\n{over} OVER"

def priyanshu_session_pass(result):
    return f"{result} 💸✔️\n\nSESSIONS PASS 🚀\n\nFULL CONFIDENCE ❤️"

def priyanshu_session_loss():
    return "LOSS ❌"

# =========================================

# JACKY

# =========================================

def jacky_session(over, run, call):
    emoji = session_call_emoji(call)
    return f"🛠 FIX MARKET\n\n{over} OVER\n\n{run} RUN\n\n{call} KARO {emoji}"

def jacky_session_pass(result):
    return f"{result} ✔️✔️\n\nSESSIONS PASS 🛠\n\nFIX CONFIRM 💣🔥"

def jacky_session_loss():
    return "LOSS ❌"

# =========================================

# KING

# =========================================

def king_session(over, run, call):
    emoji = session_call_emoji(call)
    return f"👑 KING ORDER 👑\n\n{run} RUN\n\n{call} KARO {emoji}\n\n{over} OVER"

def king_session_pass(result):
    return f"{result} 💲💲✔️\n\nSESSIONS PASS 👑\n\nKING ENTRY ❤️"

def king_session_loss():
    return "LOSS ❌"

# =========================================

# ANGAD

# =========================================

def angad_session(over, run, call):
    emoji = session_call_emoji(call)
    return f"⚔️ DADA ENTRY ⚔️\n\n{call} KARO {emoji}\n\n{over} OVER\n\n{run} RUN"

def angad_session_pass(result):
    return f"{result} ✔️\n\nSESSIONS PASS ⚔️\n\nDADA POWER 🔥"

def angad_session_loss():
    return "LOSS ❌"

# =========================================

# RAHUL

# =========================================

def rahul_session(over, run, call):
    emoji = session_call_emoji(call)
    return f"💎 PREMIUM CALL\n\n{run} RUN\n\n{over} OVER\n\n{call} KARO {emoji}"

def rahul_session_pass(result):
    return f"{result} 💎✔️\n\nSESSIONS PASS 💎\n\nPREMIUM ENTRY ❤️"

def rahul_session_loss():
    return "LOSS ❌"

# =========================================

# SHIVA

# =========================================

def shiva_session(over, run, call):
    emoji = session_call_emoji(call)
    return f"🔥 REDDY MARKET 🔥\n\n{over} OVER\n\nFULL SUPPORT ❤️\n\n{run} RUN\n\n{call} KARO {emoji}"

def shiva_session_pass(result):
    return f"{result} 💵💵✔️\n\nSESSIONS PASS 🔥\n\nREDDY PASS ❤️"

def shiva_session_loss():
    return "LOSS ❌"

# =========================================

# REDDY

# =========================================

def reddy_session(over, run, call):
    emoji = session_call_emoji(call)
    return f"🌶 ANNA SPECIAL\n\n{run} RUN\n\n{over} OVER\n\n{call} KARO {emoji}"

def reddy_session_pass(result):
    return f"{result} 💲💲✔️\n\nSESSIONS PASS 🌶\n\nANNA BOOM 💥"

def reddy_session_loss():
    return "LOSS ❌"

# =========================================

# TOSSKING

# =========================================

def tossking_session(over, run, call):
    emoji = session_call_emoji(call)
    return f"🏆 CHAMPION SESSION\n\n{call} KARO {emoji}\n\n{over} OVER\n\n{run} RUN"

def tossking_session_pass(result):
    return f"{result} 💰💰✔️\n\nSESSIONS PASS 🏆\n\nADITYA PASS ❤️"

def tossking_session_loss():
    return "LOSS ❌"

print("✅ SESSION TEMPLATES LOADED")
