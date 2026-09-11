from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from pathlib import Path

from bot.keyboards import language_selection_keyboard, main_menu_keyboard
from bot.languages import get_text
from bot.user_settings import set_user_language, get_user_language
from bot.config import load_config

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message) -> None:
    """Старт - показать видео и выбор языка"""
    config = load_config()
    
    # Проверяем есть ли первое видео (preview)
    video_path = Path(config.preview_video_path)
    
    if video_path.exists():
        # Отправляем первое видео
        await message.answer_video(
            FSInputFile(video_path),
            caption="🎬 *Fulfill Your Desires*\n"
        "Fast, Quality, and Confidential with VivaAI\n\n"
        "Realize your boldest fantasies in just a few clicks:\n"
        "Create hot videos with your favorite blogger, actress, or even your friend's mom.\n\n"
        "850K+ 10M+ 4.9⭐"
        )

    # Отправляем выбор языка
    await message.answer(
        "👋 Welcome! / Willkommen!\n\n"
        "🇬🇧 English\n"
        "🇩🇪 Deutsch",
        reply_markup=language_selection_keyboard()
    )


@router.callback_query(F.data.startswith("lang:"))
async def select_language(callback: CallbackQuery) -> None:
    """Обработка выбора языка"""
    language = callback.data.split(":")[1]  # "en" или "de"
    
    # Сохраняем язык пользователя
    set_user_language(callback.from_user.id, language)
    
    config = load_config()
    
    # Проверяем есть ли второе видео (animation)
    animation_video_path = Path(config.animation_video_path)
    
    if animation_video_path.exists():
        # Отправляем второе видео
        await callback.message.answer_video(
            FSInputFile(animation_video_path),
            caption=("🎬 *Viva AI — Photo & Video Generation*\n\n"
         "📱 Directly in Telegram\n\n"
         "Upload a photo → choose a mode → get result in seconds\n\n"
         "✨ Around 1,000 modes for photo and video generation\n"
         "📹 Extend finished videos infinitely\n"
         "🔗 Combine different modes into chains\n"
         "⚡ Cinematic-quality video\n"
         "👻 All results are delivered only to you\n"
         "🔊 Generate videos with sound")
        )
    
    # Отправляем главное меню на выбранном языке
    await callback.message.answer(
        get_text(language, "welcome"),
        reply_markup=main_menu_keyboard(language)
    )
    await callback.answer()


@router.callback_query(F.data == "menu:start")
async def back_to_menu(callback: CallbackQuery) -> None:
    """Вернуться в меню"""
    language = get_user_language(callback.from_user.id)
    
    await callback.message.edit_text(
        get_text(language, "welcome"),
        reply_markup=main_menu_keyboard(language)
    )
    await callback.answer()