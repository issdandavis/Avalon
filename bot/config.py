"""Configuration helpers for the Telegram bot runtime."""

from dataclasses import dataclass, field
from typing import Iterable, Set
import os


@dataclass
class BotSettings:
    telegram_token: str
    owner_ids: Set[int] = field(default_factory=set)
    staff_ids: Set[int] = field(default_factory=set)
    personal_ids: Set[int] = field(default_factory=set)

    def role_for(self, user_id: int) -> str:
        if user_id in self.owner_ids:
            return "owner"
        if user_id in self.staff_ids:
            return "staff"
        if user_id in self.personal_ids:
            return "personal"
        return "guest"

    def is_allowed(self, user_id: int, allowed_roles: Iterable[str]) -> bool:
        return self.role_for(user_id) in set(allowed_roles)


def _parse_id_set(raw: str | None) -> Set[int]:
    if not raw:
        return set()
    return {int(item.strip()) for item in raw.split(",") if item.strip()}


def load_settings() -> BotSettings:
    token = os.environ.get("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_TOKEN is required to run the bot")

    return BotSettings(
        telegram_token=token,
        owner_ids=_parse_id_set(os.environ.get("BOT_OWNER_IDS")),
        staff_ids=_parse_id_set(os.environ.get("BOT_STAFF_IDS")),
        personal_ids=_parse_id_set(os.environ.get("BOT_PERSONAL_IDS")),
    )
