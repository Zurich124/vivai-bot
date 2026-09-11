from pathlib import Path
from typing import Optional

from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile

from bot.config import load_config
from bot.keyboards import main_menu_keyboard, back_to_menu_keyboard
from bot.languages import get_text
from bot.user_settings import get_user_language

router = Router()

IGNORED_SUFFIXES = {".txt", ".md", ".mp4", ".mov", ".avi", ".mkv", ".webm", ".flv", ".wmv"}


def find_app_file() -> Optional[Path]:
    """Ищет приложение в папке bot/assets/app/"""
    app_dir = Path(load_config().app_dir)
    if not app_dir.exists():
        return None
    for item in sorted(app_dir.iterdir()):
        if item.is_file() and item.suffix.lower() not in IGNORED_SUFFIXES:
            return item
    return None


@router.callback_query(F.data == "menu:animate")
async def send_app(callback: CallbackQuery) -> None:
    """Отправить видео, затем приложение"""
    language = get_user_language(callback.from_user.id)
    config = load_config()
    
    # Проверяем есть ли видео перед приложением
    result_video_path = Path(config.result_video_path)
    
    if result_video_path.exists():
        # Отправляем видео
        await callback.message.answer_video(
            FSInputFile(result_video_path),
            caption="✨Our app is completely free to use, with no limits or hidden restrictions. Enjoy fast, high-quality photo and video generation — simple, convenient, and with no unnecessary waiting."
        )
    
    # Ищем приложение
    app_file = find_app_file()

    if app_file is None:
        await callback.message.answer(
            get_text(language, "app_not_found"),
            reply_markup=back_to_menu_keyboard(language)
        )
        await callback.answer()
        return

    # Отправляем приложение
    await callback.message.answer_document(
        FSInputFile(app_file),
        caption=get_text(language, "app_caption"),
        reply_markup=main_menu_keyboard(language),
    )
    await callback.answer()