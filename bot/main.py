"""Runnable Telegram bot combining store + personal flows.

Requires environment variables:
- TELEGRAM_TOKEN (required)
- BOT_OWNER_IDS (comma-separated Telegram user IDs)
- BOT_STAFF_IDS (optional)
- BOT_PERSONAL_IDS (optional)
"""

from __future__ import annotations

import asyncio
import logging
from textwrap import dedent
from typing import Iterable

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command

from bot.config import BotSettings, load_settings
from bot.personal_services import PersonalClient
from bot.store_services import StoreClient


def _deny_if_not_allowed(cfg: BotSettings, user_id: int, allowed_roles: Iterable[str]) -> str | None:
    if cfg.is_allowed(user_id, allowed_roles):
        return None
    return "You do not have access to this command."


def build_dispatcher(cfg: BotSettings) -> Dispatcher:
    store_client = StoreClient()
    personal_client = PersonalClient()

    router = Router(name="main")

    @router.message(Command("start"))
    async def start(message: types.Message) -> None:
        await message.answer(
            dedent(
                """
                Hi! I'm your combined store + personal assistant.
                Try /help to see available commands.
                """
            ).strip()
        )

    @router.message(Command("help"))
    async def help_cmd(message: types.Message) -> None:
        await message.answer(
            dedent(
                """
                Commands:
                /catalog – list SKUs (owner/staff)
                /order <id> – lookup order (owner/staff)
                /refund <id> – create refund (owner/staff)
                /lowstock – items at/below threshold (owner/staff)
                /ticket <subject> – open support ticket (owner/staff)
                /tasks – list personal tasks (owner/personal)
                /addtask <text> – add a task (owner/personal)
                /habit <name> – add a habit (owner/personal)
                /calendar – upcoming events (owner/personal)
                /note <topic> – stash a note in inbox (owner/personal)
                /inbox – inbox summary (owner/personal)
                """
            ).strip()
        )

    @router.message(Command("catalog"))
    async def catalog(message: types.Message) -> None:
        denial = _deny_if_not_allowed(cfg, message.from_user.id, {"owner", "staff"})
        if denial:
            await message.answer(denial)
            return
        lines = store_client.list_catalog()
        await message.answer("\n".join(lines))

    @router.message(Command("order"))
    async def order_status(message: types.Message) -> None:
        denial = _deny_if_not_allowed(cfg, message.from_user.id, {"owner", "staff"})
        if denial:
            await message.answer(denial)
            return
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            await message.answer("Usage: /order <id>")
            return
        order = store_client.find_order(args[1])
        if not order:
            await message.answer("Order not found")
            return
        await message.answer(
            f"Order {order.id}: {order.status} (total ${order.total:.2f}, placed {order.placed_at:%Y-%m-%d %H:%M} UTC)"
        )

    @router.message(Command("refund"))
    async def refund(message: types.Message) -> None:
        denial = _deny_if_not_allowed(cfg, message.from_user.id, {"owner", "staff"})
        if denial:
            await message.answer(denial)
            return
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            await message.answer("Usage: /refund <id>")
            return
        try:
            confirmation = store_client.create_refund(args[1])
        except KeyError:
            await message.answer("Order not found")
            return
        await message.answer(confirmation)

    @router.message(Command("lowstock"))
    async def lowstock(message: types.Message) -> None:
        denial = _deny_if_not_allowed(cfg, message.from_user.id, {"owner", "staff"})
        if denial:
            await message.answer(denial)
            return
        items = store_client.low_stock()
        if not items:
            await message.answer("No low-stock items.")
            return
        await message.answer("\n".join(items))

    @router.message(Command("ticket"))
    async def ticket(message: types.Message) -> None:
        denial = _deny_if_not_allowed(cfg, message.from_user.id, {"owner", "staff"})
        if denial:
            await message.answer(denial)
            return
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            await message.answer("Usage: /ticket <subject>")
            return
        ticket_obj = store_client.open_ticket(args[1])
        await message.answer(f"Ticket {ticket_obj.id} opened: {ticket_obj.subject}")

    @router.message(Command("tasks"))
    async def tasks(message: types.Message) -> None:
        denial = _deny_if_not_allowed(cfg, message.from_user.id, {"owner", "personal"})
        if denial:
            await message.answer(denial)
            return
        await message.answer("\n".join(personal_client.list_tasks()))

    @router.message(Command("addtask"))
    async def addtask(message: types.Message) -> None:
        denial = _deny_if_not_allowed(cfg, message.from_user.id, {"owner", "personal"})
        if denial:
            await message.answer(denial)
            return
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            await message.answer("Usage: /addtask <description>")
            return
        task = personal_client.add_task(args[1])
        await message.answer(f"Added task: {task.description}")

    @router.message(Command("habit"))
    async def habit(message: types.Message) -> None:
        denial = _deny_if_not_allowed(cfg, message.from_user.id, {"owner", "personal"})
        if denial:
            await message.answer(denial)
            return
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            await message.answer("Usage: /habit <name>")
            return
        habit_obj = personal_client.add_habit(args[1])
        await message.answer(f"Added habit: {habit_obj.name}")

    @router.message(Command("calendar"))
    async def calendar(message: types.Message) -> None:
        denial = _deny_if_not_allowed(cfg, message.from_user.id, {"owner", "personal"})
        if denial:
            await message.answer(denial)
            return
        await message.answer("\n".join(personal_client.calendar_digest()))

    @router.message(Command("note"))
    async def note(message: types.Message) -> None:
        denial = _deny_if_not_allowed(cfg, message.from_user.id, {"owner", "personal"})
        if denial:
            await message.answer(denial)
            return
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            await message.answer("Usage: /note <topic>")
            return
        topic = personal_client.add_note(args[1])
        await message.answer(f"Captured note: {topic}")

    @router.message(Command("inbox"))
    async def inbox(message: types.Message) -> None:
        denial = _deny_if_not_allowed(cfg, message.from_user.id, {"owner", "personal"})
        if denial:
            await message.answer(denial)
            return
        await message.answer("\n".join(personal_client.inbox_summary()))

    dispatcher = Dispatcher(name="dispatcher")
    dispatcher.include_router(router)
    return dispatcher


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    cfg = load_settings()
    bot = Bot(token=cfg.telegram_token, parse_mode=ParseMode.HTML)
    dp = build_dispatcher(cfg)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
