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
        "_module": module_links(audio=None, video_prof=None, resume=None),
        "REINS": cours(youtube="https://youtu.be/6c2ZxAkRk6Y?si=1FMqDlWFX9IM4K_G", drive=None),
        "uretères": cours(youtube="https://youtu.be/iuE40msqh1U?si=-FpXNbAXScRrMPGz", drive=None),
        "LA VESSIE": cours(youtube="https://youtu.be/RzykHoppmB4?si=yMx6sG7Z4vCY40J4", drive=None),
        "L'URÈTRE": cours(youtube="https://youtu.be/2q_MPgSz3sk?si=w39Q3wsQQP9FaUzq", drive=None),
        "appareil genital masculin": cours(youtube=None, drive=None),
        "App génital feminin": cours(youtube=None, drive=None),
    },
    "Physiologie": {
        "_module": module_links(audio=None, video_prof=None, resume=None),
        "fonctions du rein circulation": cours(youtube=None, drive=None),
        "filtration glomérulaire": cours(youtube=None, drive=None),
        "transfert tubulaire des solutés": cours(youtube=None, drive=None),
        "métabolisme rénale du sodium": cours(youtube=None, drive=None),
        "miction et fonction rénale": cours(youtube=None, drive=None),
        "Les diurétiques": cours(youtube=None, drive=None),
        "pouvoir dilution concentration": cours(youtube=None, drive=None),
    },
    "Histologie": {
        "_module": module_links(audio=None, video_prof=None, resume=None),
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
        "_module": module_links(audio=None, video_prof=None, resume=None),
        "Exploration fonctionnelle rénale": cours(youtube=None, drive=None),
        "acide urique 2024": cours(youtube=None, drive=None),
    },
}

UEI05_links = {
    "Anatomie": {
        "_module": module_links(audio="https://t.me/+AzpSeklQa3k1MTZk", video_prof="https://t.me/+1otd224wtI80M2M8", resume=None),
        "ostéologie du crane": cours(youtube="https://youtu.be/PeUNKwD59E0?si=76QTGqHoYySmzyXx", drive="https://drive.google.com/file/d/1OJyu1uOr-LXx7C6oFFDxEeDHahPLLWZP/view?usp=drive_open"),
        "ostéologie de la face 2": cours(youtube="https://youtu.be/Jpg38T16g0Q?si=y2-xqkOT7e3yTKuP", drive="https://drive.google.com/open?id=1P5KZg_94xURCcmFHWQ0j0TvqX5fDrSil&authuser=0"),
        "ARTICULATION TEMPORO-MANDIBULAIRE (ATM)": cours(youtube="https://youtu.be/P44_lXHRMjU?si=f9vnc3sDtHgK4Lbf", drive="https://drive.google.com/file/d/1jmBKrOTnVPcMpoiL9i1ett2dr3pDYjoO/view"),
        "Morphologie de la moelle épinière": cours(youtube="https://youtu.be/AmHJIdkRKJ0?si=j5QBOx9cqmyfjU-f", drive="https://drive.google.com/file/d/1fJcIQGcxnoOTaWfeApJPX3vSiwYLngHC/view"),
        "Cervelet et méninges": cours(youtube="https://youtu.be/4AUbq9CkbaY?si=n-yvjBN7BMvbxDhg", drive="https://drive.google.com/file/d/1wODzghAVWRultAXmgfOp80IS9XoMnS5e/view?usp=drive_open"),
        "TRONC CÉRÉBRAL": cours(youtube="https://youtu.be/36DhHT9lWPA?si=zKadv_6gKBM7hv8A", drive="https://drive.google.com/file/d/1wRWqoxD-v5lTRSioZ53BJPFIc9vlUr6-/view"),
        "Diencéphale": cours(youtube="https://youtu.be/36DhHT9lWPA?si=zKadv_6gKBM7hv8A", drive="https://drive.google.com/file/d/1xyMpLCF0fko7s1S0I2wIH8C0-Z1HXE4W/view"),
        "CONFIGURATION INTERNE": cours(youtube="https://youtu.be/84y05tkjDqM?si=AzQM3sQKlYRzE3-w", drive="https://drive.google.com/file/d/1ybDnR99cxu0jtfsIQmlqPsblhZxboCsd/view?usp=drive_open"),
        "morphologie du télencéphale": cours(youtube="https://youtu.be/peXTOEWdaoA?si=gbcQ6T7eSQxcVBjz", drive="https://drive.google.com/open?id=1yrJtsoKYRKcyQZXXG_KnXRKgNeQFRb6l&authuser=0"),
        "vascularisation du cerveau": cours(youtube="https://youtu.be/hbS7TllcdEw?si=Fq_lRFDXRdes3oqn", drive="https://drive.google.com/open?id=1yt65aVPb_Ownx9YtoOLYl--Yzsy9CMB7&authuser=0"),
        "oreille": cours(youtube="https://youtu.be/6q1rp0pBLzg?si=JAw5LpBJrzSmIhNE", drive="https://drive.google.com/file/d/1zpIBb_styHjWG8YJ9xcY6FWPx5Mi88-B/view?usp=drive_open"),
        "oeil et cavité orbitaire": cours(youtube="https://youtu.be/7zT1AtqgEX0?si=OnGlpFv9fo-gkh5a", drive="https://drive.google.com/open?id=1vNy2tKzTas_i-cTVoWZdKQlKcOcTEkTA&authuser=0"),
    },
    "Biophysique": {
        "_module": module_links(audio=None, video_prof=None, resume=None),
        "Introduction UEI5": cours(youtube="https://youtu.be/QmhbgmtFy5M?si=SRPdcBvaNHAWbeiF", drive="https://drive.google.com/drive/folders/1hu_vmVWjgpGkQfNhDjk-3ec2ioN2xdQC"),
        "Vision": cours(youtube="https://youtu.be/QmhbgmtFy5M?si=ZDN7F5uXjAp3uqBx", drive="https://drive.google.com/drive/folders/1hu_vmVWjgpGkQfNhDjk-3ec2ioN2xdQC"),
        "Propagation des ondes": cours(youtube="https://youtu.be/cE_LBKxxEu8?si=tUgPMixun25QbPXn", drive="https://drive.google.com/file/d/1xltqhlJFmZ94pDajSYgHVGFaducnhqUn/view"),
        "Audition": cours(youtube="https://youtu.be/r-cIEvhDaIU?si=sfWWZE2Iiw639rWK", drive="https://drive.google.com/file/d/15MwJnNNvrNOHRc-24ih4lYXBLUB0QsAg/view"),
    },
    "Histologie": {
        "_module": module_links(audio="https://t.me/+jvguo0PAxxc0M2I0", video_prof="https://t.me/+_cQMtbzAwRRhYzk0", resume=None),
        "Développement embryologique": cours(youtube="https://youtu.be/ULJNMSrmNLI?si=Wn9kNdOZi2nDwb5B", drive="https://drive.google.com/open?id=18D5tb5YWtsoWciDS037LpmURqIf0BuYk&authuser=0"),
        "Cortex cérébral (Dr. Daksi)": cours(youtube="https://youtu.be/oC_qcfZBcLQ?si=zUS2tiHD6G2tTsCO", drive="https://drive.google.com/file/d/1Ofwr7qVj2xBPR7pUAkk8W4SEzZP4Tvm_/view"),
        "HISTOLOGIE DU CORTEX CÉRÉBRAL": cours(youtube="https://youtu.be/Sp09jHLp6iI?si=CB7shMPRZ8Hz-pxm", drive="https://drive.google.com/file/d/1hgLuosSO13SK84HR1LGrrUpdZiQ35wYd/view"),
        "La moelle épinière (Dr. Aouati)": cours(youtube="https://youtu.be/Z0WEsnEMyJE?si=XbcP-LpexR8bz44t", drive="https://drive.google.com/file/d/1iLD5IQ-NRC2-0cFbLcDU4_IiREdAT2Nl/view"),
        "Ganglion rachidien": cours(youtube="https://youtu.be/iwMQ8kgw-ro?si=97GuvupMgO9sY069", drive="https://drive.google.com/open?id=1kJPqxYvpD2V4p7SQXvSwyqmcfPVnAD8Y&authuser=0"),
        "Méninges et plexus choroïde": cours(youtube="https://youtu.be/gNi-hl9LVgc?si=oIZDbJE7NAAqEfzE", drive="https://drive.google.com/file/d/1kOvxLEmeuquwnp9s31uP5uN0a8p5RoaW/view?usp=drive_open"),
        "Les ganglions végétatifs": cours(youtube="https://youtu.be/bmBg4tB4QdA?si=fAU-zm3sVQIuZmQz", drive="https://drive.google.com/file/d/1Hs-6UIcGYqH_FV2ouYwlL5jRLfo4ab9b/view"),
        "Nerf, fibres et terminaisons nerveuses": cours(youtube="https://youtu.be/iVcJD1N0bRA?si=X7a2yaIMZ41CNoxa", drive="https://drive.google.com/file/d/1YsatPES1TresXWP2nmyaZYvctnh856tk/view"),
        "Bourgeons du Goût (Dr. Adjissi)": cours(youtube="https://youtu.be/y8dBpe9DEfA?si=GfNYdRVDcE147QX8", drive="https://drive.google.com/file/d/1YsatPES1TresXWP2nmyaZYvctnh856tk/view"),
        "Classification des organes de sens": cours(youtube="https://youtu.be/nAPzixeludI?si=nosgFtTRGiTioFOb", drive="https://drive.google.com/file/d/1qesSfA9M4Lh_jfjadykgu6uPjQZ6XydU/view"),
        "La muqueuse olfactive": cours(youtube="https://youtu.be/R2JI6Z5UpG4?si=80bVxNVFpOMOgOOp", drive="https://drive.google.com/file/d/1qfhH-D4nP97Lqv40ygKa5ihuOSmeMR51/view?usp=drive_open"),
        "L'oreille": cours(youtube="https://youtu.be/dtMXWVAbSR8?si=PMGwqDNZbYFKlMNa", drive="https://drive.google.com/file/d/1wONqJQ0Qo1vmtmkilhL7mlRAJYn6nmRN/view"),
        "L'oeil et la rétine visuelle": cours(youtube="https://youtu.be/jecTxdsV4Jk?si=TgjAWJMMUbbSxWBT", drive="https://drive.google.com/file/d/1Pq7V4LrFdD9hnAEbZx67GfWBYo5AZcGe/view"),
        "Les terminaisons nerveuses de la peau": cours(youtube="https://youtu.be/nAPzixeludI?si=-SaI7fuLYAYUJcfB", drive="https://drive.google.com/file/d/12VKFRTIKEEEPnYaglGxeNVzF4pBUhsVp/view"),
    },
    "Physiologie": {
        "_module": module_links(audio="https://t.me/+Ds45rnXkPLM1MDdk", video_prof="https://t.me/+FR2KCqQ6cwA4MTBk", resume=None),
        "Récepteurs sensoriels": cours(youtube="https://youtu.be/wCjUdBDJGG4?si=mGriPyv-Axw5u6e1", drive="https://drive.google.com/file/d/1qCL6FxmUtvsGfvyd83bJaC-yv61kfHup/view"),
        "Racines rachidiennes": cours(youtube="https://youtu.be/fw9DaKNuQl8?si=HGnHRFRKbq-CJOAk", drive="https://drive.google.com/file/d/1ArFIe3gC3t7iZbCcHtGeZAusb2z9aL5U/view"),
        "ME Conduction": cours(youtube="https://youtu.be/yb4ckpRP5JA?si=ZV_sRHcTEg90oCTi", drive="https://drive.google.com/file/d/1hHMHZ4VAsWzE1pe7hzgwwCF12FAHIq02/view"),
        "Réflexes médullaires": cours(youtube="https://youtu.be/jMiW2AeDrMo?si=nY16zCbDGwtO1Yb8", drive="https://drive.google.com/file/d/1kYImnLm34jqNZppjTqMfkZ2m2-euauyJ/view"),
        "Somesthésie": cours(youtube="https://youtu.be/8bVO9w5WakA?si=ZpexzxgLaMonygwF", drive="https://drive.google.com/file/d/1nTPiA_0fTGRz51bTR9IKCj4zyIRsqiV3/view"),
        "Régulation supraspinale des réflexes": cours(youtube="https://youtu.be/Xz_gCpnJnRE?si=yJ2KweqjywBpmEXe", drive="https://drive.google.com/file/d/1rpJIvzpDga9rZp74HFITS1lB9qE4Ilk-/view"),
        "La formation réticulée": cours(youtube="https://youtu.be/SM6vTpjxH1Y?si=sv9rCL3CoUyXCvkK", drive="https://drive.google.com/file/d/1rwlCl41aDODlOCb4RyivG_A1EyCU1Qy4/view"),
        "Cervelet": cours(youtube="https://youtu.be/lAIN_W1UIug?si=VQoxM1NpoFGgIxIF", drive="https://drive.google.com/open?id=1sFfc7PDABtZBD86SvwHFeZHhKSOO67Dp&authuser=0"),
        "Physiologie de la douleur": cours(youtube="https://youtu.be/lz0zXiAYs5U?si=x5HWdLLyaZMXLaTa", drive="https://drive.google.com/file/d/1aEia4hzL_qXMyXmBdRqbS8jIZZnFH8zi/view"),
        "Sommeil normal (Pr. Adjiri)": cours(youtube="https://youtu.be/BTPvGUP_6h0?si=vlXJDWaPWiwvYvPD", drive="https://drive.google.com/file/d/1cHTyY0Zwk8JQ0K8JeX8X67nCfJCNB1I6/view"),
        "Régulation Veille-Sommeil": cours(youtube="https://youtu.be/-sHLb_PY4cY?si=nwPd-Iz74fiGBAuS", drive="https://drive.google.com/file/d/1JmtQOFb-2HGtKBmsjNykBj3lv8BsBZs0/view"),
        "Cortex Moteur": cours(youtube="https://youtu.be/ThhnxSVUMZQ?si=iEgg5sOd4q1GAFCf", drive="https://drive.google.com/file/d/1yR0VpauTyX4DaiNkHgCUPjYzWXR1zYhS/view"),
        "NGB": cours(youtube="https://youtu.be/Li-1G6WJVOo?si=1IeBU3vFf4aLz0HO", drive="https://drive.google.com/file/d/1yJ69px3TWbdzWwWCjyqksVp9lO3903Rg/view"),
        "Physiologie de la Vision": cours(youtube="https://youtu.be/Tb6p1rpsx0Y?si=rEH3XoDgipLd9gyV", drive="https://drive.google.com/file/d/1bSne96xgTVPnShvKFjKwB-twBQUkx5C7/view?usp=drive_open"),
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
    audio=mod.get("audio"); video_prof=mod.get("video_prof"); resume=mod.get("resume")
    if any([audio, video_prof, resume]):
        keyboard.add(InlineKeyboardButton("─────────────────", callback_data="noop"))
        row_m=[]
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
    chat_id=call.message.chat.id; message_id=call.message.message_id; data=call.data
    if data=="back_main": main_menu(chat_id,message_id)
    elif data.startswith("back_subject|"): subject_menu(chat_id,message_id,data.split("|")[1])
    elif data.startswith("unit_"):
        unit=data[5:]
        if unit in ACTIVE_UNITS: subject_menu(chat_id,message_id,unit)
        else: bot.answer_callback_query(call.id,"هذه الوحدة قريباً 😅")
    elif data in ("placeholder","noop"): bot.answer_callback_query(call.id)
    elif data.startswith("subj|"):
        _,unit,subject=data.split("|",2); lessons_menu(chat_id,message_id,unit,subject)

print("✅ BOT STARTED")
bot.infinity_polling(skip_pending=True)
