import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8739170453:AAEAiP7kdbAAIwYtRbFwMwtY3LVfdQ0Nhq0"
ADMIN = "@Brofa852"
bot = telebot.TeleBot(TOKEN)

def cours(youtube=None, drive=None):
    return {"youtube": youtube, "drive": drive}

def module_links(audio=None, video_prof=None, resume=None):
    return {"audio": audio, "video_prof": video_prof, "resume": resume}

UEI03_links = {
    "Anatomie": {
        "_module": module_links(
            audio      = None,
            video_prof = None,
            resume     = None,
        ),
        "REINS": cours(youtube="https://youtu.be/6c2ZxAkRk6Y?si=1FMqDlWFX9IM4K_G", drive=None),
        "uretères": cours(youtube="https://youtu.be/iuE40msqh1U?si=-FpXNbAXScRrMPGz", drive=None),
        "LA VESSIE": cours(youtube="https://youtu.be/RzykHoppmB4?si=yMx6sG7Z4vCY40J4", drive=None),
        "L'URÈTRE": cours(youtube="https://youtu.be/2q_MPgSz3sk?si=w39Q3wsQQP9FaUzq", drive=None),
        "appareil genital masculin": cours(youtube=None, drive=None),
        "App génital feminin": cours(youtube=None, drive=None),
    },
    "Physiologie": {
        "_module": module_links(
            audio      = None,
            video_prof = None,
            resume     = None,
        ),
        "fonctions du rein circulation": cours(youtube=None, drive=None),
        "filtration glomérulaire": cours(youtube=None, drive=None),
        "transfert tubulaire des solutés": cours(youtube=None, drive=None),
        "métabolisme rénale du sodium": cours(youtube=None, drive=None),
        "miction et fonction rénale": cours(youtube=None, drive=None),
        "Les diurétiques": cours(youtube=None, drive=None),
        "pouvoir dilution concentration": cours(youtube=None, drive=None),
    },
    "Histologie": {
        "_module": module_links(
            audio      = None,
            video_prof = None,
            resume     = None,
        ),
        "Embryo rénale": cours(youtube=None, drive=None),
        "L'appareil urinaire": cours(youtube=None, drive=None),
        "Histologie des voies urinaires": cours(youtube=None, drive=None),
        "APPAREIL GENITAL MASCULIN": cours(youtube=None, drive=None),
        "Glandes annexes de l'appareil génital": cours(youtube=None, drive=None),
        "VOIES GENITALES MASCULINES": cours(youtube=None, drive=None),
        "Spermogramme": cours(youtube=None, drive=None),
        "Organe de Copulation": cours(youtube=None, drive=None),
    },
    "Biochimie": {
        "_module": module_links(
            audio      = None,
            video_prof = None,
            resume     = None,
        ),
        "Exploration fonctionnelle rénale": cours(youtube=None, drive=None),
        "acide urique 2024": cours(youtube=None, drive=None),
    },
}

UEI05_links = {
    "Anatomie": {
        "_module": module_links(
            audio      = "https://t.me/+AzpSeklQa3k1MTZk",
            video_prof = "https://t.me/+1otd224wtI80M2M8",
            resume     = None,
        ),
        "ostéologie du crane": cours(youtube="https://youtu.be/PeUNKwD59E0?si=76QTGqHoYySmzyXx", drive="https://drive.google.com/drive/folders/19ghFVAH2QZVmMjxzGLNZ9cWujekZMeUv"),
        "ostéologie de la face 2": cours(youtube="https://youtu.be/Jpg38T16g0Q?si=y2-xqkOT7e3yTKuP", drive="https://drive.google.com/drive/folders/1WEi6-TMdwCuFw1ZCIrh1g68dzQS4m2ng"),
        "ARTICULATION TEMPORO-MANDIBULAIRE (ATM)": cours(youtube="https://youtu.be/P44_lXHRMjU?si=f9vnc3sDtHgK4Lbf", drive="https://drive.google.com/drive/folders/1WEi6-TMdwCuFw1ZCIrh1g68dzQS4m2ng"),
        "Morphologie de la moelle épinière": cours(youtube="https://youtu.be/AmHJIdkRKJ0?si=j5QBOx9cqmyfjU-f", drive="https://drive.google.com/drive/folders/1WEi6-TMdwCuFw1ZCIrh1g68dzQS4m2ng"),
        "Cervelet et méninges": cours(youtube="https://youtu.be/4AUbq9CkbaY?si=n-yvjBN7BMvbxDhg", drive="https://drive.google.com/drive/folders/1WEi6-TMdwCuFw1ZCIrh1g68dzQS4m2ng"),
        "TRONC CÉRÉBRAL": cours(youtube="https://youtu.be/36DhHT9lWPA?si=zKadv_6gKBM7hv8A", drive="https://drive.google.com/drive/folders/1WEi6-TMdwCuFw1ZCIrh1g68dzQS4m2ng"),
        "Diencéphale": cours(youtube="https://youtu.be/36DhHT9lWPA?si=zKadv_6gKBM7hv8A", drive="https://drive.google.com/drive/folders/1WEi6-TMdwCuFw1ZCIrh1g68dzQS4m2ng"),
        "CONFIGURATION INTERNE": cours(youtube="https://youtu.be/84y05tkjDqM?si=AzQM3sQKlYRzE3-w", drive="https://drive.google.com/drive/folders/1WEi6-TMdwCuFw1ZCIrh1g68dzQS4m2ng"),
        "morphologie du télencéphale": cours(youtube="https://youtu.be/peXTOEWdaoA?si=gbcQ6T7eSQxcVBjz", drive="https://drive.google.com/drive/folders/1WEi6-TMdwCuFw1ZCIrh1g68dzQS4m2ng"),
        "vascularisation du cerveau": cours(youtube="https://youtu.be/hbS7TllcdEw?si=Fq_lRFDXRdes3oqn", drive="https://drive.google.com/drive/folders/1WEi6-TMdwCuFw1ZCIrh1g68dzQS4m2ng"),
        "oreille": cours(youtube="https://youtu.be/6q1rp0pBLzg?si=JAw5LpBJrzSmIhNE", drive="https://drive.google.com/drive/folders/1WEi6-TMdwCuFw1ZCIrh1g68dzQS4m2ng"),
        "oeil et cavité orbitaire": cours(youtube="https://youtu.be/7zT1AtqgEX0?si=OnGlpFv9fo-gkh5a", drive="https://drive.google.com/drive/folders/1WEi6-TMdwCuFw1ZCIrh1g68dzQS4m2ng"),
    },
    "Biophysique": {
        "_module": module_links(
            audio      = None,
            video_prof = None,
            resume     = None,
        ),
        "Introduction UEI5": cours(youtube=None, drive=None),
        "Vision": cours(youtube=None, drive=None),
        "Propagation des ondes": cours(youtube=None, drive=None),
        "Audition": cours(youtube=None, drive=None),
    },
    "Histologie": {
        "_module": module_links(
            audio      = None,
            video_prof = None,
            resume     = None,
        ),
        "Développement embryologique": cours(youtube=None, drive=None),
        "Cortex cérébral (Dr. Daksi)": cours(youtube=None, drive=None),
        "HISTOLOGIE DU CORTEX CÉRÉBRAL": cours(youtube=None, drive=None),
        "La moelle épinière (Dr. Aouati)": cours(youtube=None, drive=None),
        "Ganglion rachidien": cours(youtube=None, drive=None),
        "Méninges et plexus choroïde": cours(youtube=None, drive=None),
        "Les ganglions végétatifs": cours(youtube=None, drive=None),
        "Nerf, fibres et terminaisons nerveuses": cours(youtube=None, drive=None),
        "Bourgeons du Goût (Dr. Adjissi)": cours(youtube=None, drive=None),
        "Classification des organes de sens": cours(youtube=None, drive=None),
        "La muqueuse olfactive": cours(youtube=None, drive=None),
        "L'oreille": cours(youtube=None, drive=None),
        "L'oeil et la rétine visuelle": cours(youtube=None, drive=None),
        "Les terminaisons nerveuses de la peau": cours(youtube=None, drive=None),
    },
    "Physiologie": {
        "_module": module_links(
            audio      = None,
            video_prof = None,
            resume     = None,
        ),
        "Récepteurs sensoriels": cours(youtube=None, drive=None),
        "Racines rachidiennes": cours(youtube=None, drive=None),
        "ME Conduction": cours(youtube=None, drive=None),
        "Réflexes médullaires": cours(youtube=None, drive=None),
        "Somesthésie": cours(youtube=None, drive=None),
        "Régulation supraspinale des réflexes": cours(youtube=None, drive=None),
        "La formation réticulée": cours(youtube=None, drive=None),
        "Cervelet": cours(youtube=None, drive=None),
        "Physiologie de la douleur": cours(youtube=None, drive=None),
        "Sommeil normal (Pr. Adjiri)": cours(youtube=None, drive=None),
        "Régulation Veille-Sommeil": cours(youtube=None, drive=None),
        "Cortex Moteur": cours(youtube=None, drive=None),
        "NGB": cours(youtube=None, drive=None),
        "Physiologie de la Vision": cours(youtube=None, drive=None),
    },
}

UNITS_LINKS  = {"UEI03": UEI03_links, "UEI05": UEI05_links}
ACTIVE_UNITS = {"UEI03", "UEI05"}

def main_menu(chat_id, message_id=None):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🌐 Drive Médecine Sétif 2024-2025", url="https://drive.google.com/drive/folders/1E1Tky9BJsYKngBVTQM11V3zd834v_DVM"))
    for i in range(1, 6):
        unit = f"UEI0{i}"
        if unit in ACTIVE_UNITS:
            keyboard.add(InlineKeyboardButton(f"📚 {unit}", callback_data=f"unit_{unit}"))
        else:
            keyboard.add(InlineKeyboardButton(f"📚 {unit} (قريباً)", callback_data="placeholder"))
    keyboard.add(InlineKeyboardButton("🌐 مواقع مفيدة", url="https://example.com/your_sources"))
    keyboard.add(InlineKeyboardButton(f"📩 Contact Admin: {ADMIN}", url=f"https://t.me/{ADMIN[1:]}"))
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
    bot.edit_message_text(f"📘 الوحدة: {unit}\nاختر المادة:", chat_id, message_id, reply_markup=keyboard)

def lessons_menu(chat_id, message_id, unit, subject):
    subject_data = UNITS_LINKS.get(unit, {}).get(subject, {})
    keyboard = InlineKeyboardMarkup()
    for lesson, urls in subject_data.items():
        if lesson == "_module":
            continue
        yt  = urls.get("youtube")
        drv = urls.get("drive")
        keyboard.add(InlineKeyboardButton(f"📖 {lesson}", callback_data="noop"))
        row = []
        if yt:  row.append(InlineKeyboardButton("▶️ YouTube", url=yt))
        if drv: row.append(InlineKeyboardButton("📁 Drive",   url=drv))
        if row:
            keyboard.add(*row)
        else:
            keyboard.add(InlineKeyboardButton("🔒 قريباً", callback_data="placeholder"))
    mod = subject_data.get("_module", {})
    audio      = mod.get("audio")
    video_prof = mod.get("video_prof")
    resume     = mod.get("resume")
    if any([audio, video_prof, resume]):
        keyboard.add(InlineKeyboardButton("─────────────────", callback_data="noop"))
        row_m = []
        if audio:      row_m.append(InlineKeyboardButton("🎙️ Audio",      url=audio))
        if video_prof: row_m.append(InlineKeyboardButton("🎬 Vidéo Prof", url=video_prof))
        if resume:     row_m.append(InlineKeyboardButton("📄 Résumé",     url=resume))
        if row_m: keyboard.add(*row_m)
    keyboard.add(InlineKeyboardButton("⬅️ Retour", callback_data=f"back_subject|{unit}"))
    bot.edit_message_text(f"📚 {unit} › {subject}\nاختر الدرس:", chat_id, message_id, reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def start(message):
    main_menu(message.chat.id)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    chat_id = call.message.chat.id
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

print("✅ BOT STARTED")
bot.infinity_polling(skip_pending=True)
