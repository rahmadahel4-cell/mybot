import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# ---------------- CONFIG ----------------
TOKEN = "8739170453:AAEAiP7kdbAAIwYtRbFwMwtY3LVfdQ0Nhq0"
ADMIN = "@Brofa852"
bot = telebot.TeleBot(TOKEN)

def cours(youtube=None, drive=None, resume=None, qcm=None, audio=None):
    return {"youtube": youtube, "drive": drive,
            "resume": resume,  "qcm": qcm, "audio": audio}

# ================================================================
#  UEI03
# ================================================================
UEI03_links = {
    "Anatomie": {
        "REINS": cours(
            youtube = "https://youtu.be/6c2ZxAkRk6Y?si=1FMqDlWFX9IM4K_G",
            drive   = None,  # https://drive.google.com/file/d/XXXXX
            resume  = None,  # https://drive.google.com/file/d/XXXXX
            qcm     = None,  # https://drive.google.com/file/d/XXXXX
            audio   = None,  # https://t.me/c/XXXXXXX/XX
        ),
        "uretères": cours(
            youtube = "https://youtu.be/iuE40msqh1U?si=-FpXNbAXScRrMPGz",
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "LA VESSIE": cours(
            youtube = "https://youtu.be/RzykHoppmB4?si=yMx6sG7Z4vCY40J4",
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "L'URÈTRE": cours(
            youtube = "https://youtu.be/2q_MPgSz3sk?si=w39Q3wsQQP9FaUzq",
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "appareil genital masculin": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "App génital feminin": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
    },
    "Physiologie": {
        "fonctions du rein circulation": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "filtration glomérulaire": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "transfert tubulaire des solutés": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "métabolisme rénale du sodium": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "miction et fonction rénale": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Les diurétiques": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "pouvoir dilution concentration": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
    },
    "Histologie": {
        "Embryo rénale": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "L'appareil urinaire": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Histologie des voies urinaires": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "APPAREIL GENITAL MASCULIN": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Glandes annexes de l'appareil génital": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "VOIES GENITALES MASCULINES": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Spermogramme": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Organe de Copulation": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
    },
    "Biochimie": {
        "Exploration fonctionnelle rénale": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "acide urique 2024": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
    },
}

# ================================================================
#  UEI05
# ================================================================
UEI05_links = {
    "Anatomie": {
        "ostéologie du crane": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "ostéologie de la face 2": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "ARTICULATION TEMPORO-MANDIBULAIRE (ATM)": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Morphologie de la moelle épinière": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Cervelet et méninges": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "TRONC CÉRÉBRAL": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Diencéphale": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "CONFIGURATION INTERNE": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "morphologie du télencéphale": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "vascularisation du cerveau": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "oreille": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "oeil et cavité orbitaire": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
    },
    "Biophysique": {
        "Introduction UEI5": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Vision": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Propagation des ondes": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Audition": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
    },
    "Histologie": {
        "Développement embryologique": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Cortex cérébral (Dr. Daksi)": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "HISTOLOGIE DU CORTEX CÉRÉBRAL": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "La moelle épinière (Dr. Aouati)": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Ganglion rachidien": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Méninges et plexus choroïde": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Les ganglions végétatifs": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Nerf, fibres et terminaisons nerveuses": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Bourgeons du Goût (Dr. Adjissi)": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Classification des organes de sens": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "La muqueuse olfactive": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "L'oreille": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "L'oeil et la rétine visuelle": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Les terminaisons nerveuses de la peau": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
    },
    "Physiologie": {
        "Récepteurs sensoriels": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Racines rachidiennes": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "ME Conduction": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Réflexes médullaires": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Somesthésie": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Régulation supraspinale des réflexes": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "La formation réticulée": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Cervelet": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Physiologie de la douleur": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Sommeil normal (Pr. Adjiri)": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Régulation Veille-Sommeil": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Cortex Moteur": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "NGB": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
        "Physiologie de la Vision": cours(
            youtube = None,
            drive   = None,
            resume  = None,
            qcm     = None,
            audio   = None,
        ),
    },
}

# ================================================================
#  UNITS REGISTRY
# ================================================================
UNITS_LINKS  = {"UEI03": UEI03_links, "UEI05": UEI05_links}
ACTIVE_UNITS = {"UEI03", "UEI05"}

# ================================================================
#  MENUS
# ================================================================
def main_menu(chat_id, message_id=None):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(
        "🌐 Drive Médecine Sétif 2024-2025",
        url="https://drive.google.com/drive/folders/1E1Tky9BJsYKngBVTQM11V3zd834v_DVM"
    ))
    for i in range(1, 6):
        unit = f"UEI0{i}"
        if unit in ACTIVE_UNITS:
            keyboard.add(InlineKeyboardButton(f"📚 {unit}", callback_data=f"unit_{unit}"))
        else:
            keyboard.add(InlineKeyboardButton(f"📚 {unit} (قريباً)", callback_data="placeholder"))
    keyboard.add(InlineKeyboardButton("🌐 مواقع مفيدة", url="https://example.com/your_sources"))
    keyboard.add(InlineKeyboardButton(
        f"📩 Contact Admin: {ADMIN}", url=f"https://t.me/{ADMIN[1:]}"
    ))
    text = "📌 القائمة الرئيسية:"
    if message_id:
        bot.edit_message_text(text, chat_id, message_id, reply_markup=keyboard)
    else:
        bot.send_message(chat_id, text, reply_markup=keyboard)


def subject_menu(chat_id, message_id, unit):
    links = UNITS_LINKS.get(unit, {})
    keyboard = InlineKeyboardMarkup()
    for subject in links:
        keyboard.add(InlineKeyboardButton(subject, callback_data=f"subj|{unit}|{subject}"))
    keyboard.add(InlineKeyboardButton("⬅️ Retour", callback_data="back_main"))
    bot.edit_message_text(
        f"📘 الوحدة: {unit}\nاختر المادة:", chat_id, message_id, reply_markup=keyboard
    )


def lessons_menu(chat_id, message_id, unit, subject):
    subject_data = UNITS_LINKS.get(unit, {}).get(subject, {})
    keyboard = InlineKeyboardMarkup()

    for lesson, urls in subject_data.items():
        yt    = urls.get("youtube")
        drv   = urls.get("drive")
        res   = urls.get("resume")
        qcm   = urls.get("qcm")
        audio = urls.get("audio")
        has_any = any([yt, drv, res, qcm, audio])

        keyboard.add(InlineKeyboardButton(f"📖 {lesson}", callback_data="noop"))

        if not has_any:
            keyboard.add(InlineKeyboardButton("🔒 قريباً", callback_data="placeholder"))
            continue

        row1 = []
        if yt:  row1.append(InlineKeyboardButton("▶️ YouTube",  url=yt))
        if drv: row1.append(InlineKeyboardButton("📁 Drive",    url=drv))
        if row1: keyboard.add(*row1)

        row2 = []
        if res: row2.append(InlineKeyboardButton("📄 Résumé",   url=res))
        if qcm: row2.append(InlineKeyboardButton("❓ QCM",      url=qcm))
        if row2: keyboard.add(*row2)

        if audio:
            keyboard.add(InlineKeyboardButton("🎙️ Enregistrement", url=audio))

        keyboard.add(InlineKeyboardButton("· · ·", callback_data="noop"))

    keyboard.add(InlineKeyboardButton("⬅️ Retour", callback_data=f"back_subject|{unit}"))
    bot.edit_message_text(
        f"📚 {unit} › {subject}\nاختر الدرس:", chat_id, message_id, reply_markup=keyboard
    )


# ================================================================
#  HANDLERS
# ================================================================
@bot.message_handler(commands=['start'])
def start(message):
    main_menu(message.chat.id)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    chat_id    = call.message.chat.id
    message_id = call.message.message_id
    data = call.data

    if data == "back_main":
        main_menu(chat_id, message_id)
    elif data.startswith("back_subject|"):
        unit = data.split("|")[1]
        subject_menu(chat_id, message_id, unit)
    elif data.startswith("unit_"):
        unit = data[5:]
        if unit in ACTIVE_UNITS:
            subject_menu(chat_id, message_id, unit)
        else:
            bot.answer_callback_query(call.id, "هذه الوحدة قريباً 😅")
    elif data in ("placeholder", "noop"):
        bot.answer_callback_query(call.id)
    elif data.startswith("subj|"):
        _, unit, subject = data.split("|", 2)
        lessons_menu(chat_id, message_id, unit, subject)
    elif data == "retours":
        bot.send_message(chat_id, f"✍️ أرسل اقتراحاتك\n📩 {ADMIN}")


# ================================================================
print("✅ BOT STARTED")
bot.infinity_polling(skip_pending=True)
