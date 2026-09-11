TRANSLATIONS = {
    "en": {
        "welcome": "👋 Welcome! 🌟\n\nThis bot animates your photos using AI.\nChoose a language:",
        "animate": "✨ Animate Photo",
        "about": "ℹ️ About",
        "app_caption": "📱 For the full experience, download our app\n\nIf you have any problems with the installation, please contact our technical support team and we'll help you right away\n\n@premium_assistent ⬇️",
        "app_not_found": "❌ Application not found",
        "back": "⬅️ Back to Menu",
    },
    "de": {
        "welcome": "👋 Willkommen! 🌟\n\nDieser Bot belebt Ihre Fotos mit KI.\nWählen Sie eine Sprache:",
        "animate": "✨ Foto animieren",
        "about": "ℹ️ Über uns",
        "app_caption": "📱 Laden Sie unsere App herunter, um voll und ganz in die Welt einzutauchen\n\nSollten bei der Installation Probleme auftreten, wenden Sie sich bitte an unseren technischen Support – wir helfen Ihnen umgehend weiter\n\n@premium_assistent ⬇️",
        "app_not_found": "❌ Anwendung nicht gefunden",
        "back": "⬅️ Zurück zum Menü",
    }
}

def get_text(language: str, key: str) -> str:
    if language not in TRANSLATIONS:
        language = "en"
    return TRANSLATIONS[language].get(key, f"[Missing: {key}]")