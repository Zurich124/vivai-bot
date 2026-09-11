from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot.languages import get_text


def language_selection_keyboard() -> InlineKeyboardMarkup:
    """Выбор языка при старте"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇬🇧 English", callback_data="lang:en"),
                InlineKeyboardButton(text="🇩🇪 Deutsch", callback_data="lang:de"),
            ]
        ]
    )


def main_menu_keyboard(language: str) -> InlineKeyboardMarkup:
    """Главное меню после выбора языка"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=get_text(language, "animate"), callback_data="menu:animate")],
            [InlineKeyboardButton(text=get_text(language, "about"), callback_data="menu:about")],
        ]
    )


def back_to_menu_keyboard(language: str) -> InlineKeyboardMarkup:
    """Кнопка назад в меню"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=get_text(language, "back"), callback_data="menu:start")],
        ]
    )