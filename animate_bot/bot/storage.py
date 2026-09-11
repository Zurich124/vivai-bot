import aiosqlite

_DB_PATH = "bot.db"


async def init_db(db_path: str = "bot.db") -> None:
    global _DB_PATH
    _DB_PATH = db_path
    async with aiosqlite.connect(_DB_PATH) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                accepted_terms INTEGER DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        await db.commit()


async def has_accepted_terms(user_id: int) -> bool:
    async with aiosqlite.connect(_DB_PATH) as db:
        cursor = await db.execute(
            "SELECT accepted_terms FROM users WHERE user_id = ?", (user_id,)
        )
        row = await cursor.fetchone()
        return bool(row and row[0])


async def set_accepted_terms(user_id: int) -> None:
    async with aiosqlite.connect(_DB_PATH) as db:
        await db.execute(
            """
            INSERT INTO users (user_id, accepted_terms) VALUES (?, 1)
            ON CONFLICT(user_id) DO UPDATE SET accepted_terms = 1
            """,
            (user_id,),
        )
        await db.commit()
