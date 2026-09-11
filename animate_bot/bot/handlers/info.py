from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot.keyboards import back_to_menu_keyboard
from bot.languages import get_text
from bot.user_settings import get_user_language

router = Router()


@router.callback_query(F.data == "menu:about")
async def show_about(callback: CallbackQuery) -> None:
    """О сервисе"""
    language = get_user_language(callback.from_user.id)
    
    about_text = {
        "en": "ℹ️ About Us\n\nWe animate photos using AI technology.\n\nEnjoy! 🎉",
        "de": "ℹ️ Über Uns\n\nWir beleben Fotos mit KI-Technologie.\n\nViel Spaß! 🎉",
    }
    
    await callback.message.edit_text(
        about_text.get(language, about_text["en"]),
        reply_markup=back_to_menu_keyboard(language)
    )
    await callback.answer()