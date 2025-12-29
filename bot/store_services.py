"""Lightweight store service stubs for the Telegram bot.

Replace these with real integrations (e.g., Shopify, WooCommerce, custom APIs).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List
import datetime as dt


@dataclass
class Order:
    id: str
    status: str
    total: float
    placed_at: dt.datetime


@dataclass
class Ticket:
    id: str
    subject: str
    created_at: dt.datetime


class StoreClient:
    def __init__(self) -> None:
        self._inventory = {
            "sku-101": {"name": "Notebook", "qty": 4},
            "sku-202": {"name": "Pen", "qty": 25},
        }
        self._orders: Dict[str, Order] = {
            "1001": Order(id="1001", status="shipped", total=29.99, placed_at=dt.datetime.utcnow()),
            "1002": Order(id="1002", status="processing", total=58.50, placed_at=dt.datetime.utcnow()),
        }
        self._tickets: List[Ticket] = []

    def list_catalog(self) -> List[str]:
        return [f"{sku}: {item['name']} (qty {item['qty']})" for sku, item in self._inventory.items()]

    def find_order(self, order_id: str) -> Order | None:
        return self._orders.get(order_id)

    def create_refund(self, order_id: str) -> str:
        if order_id not in self._orders:
            raise KeyError("Order not found")
        return f"Refund request created for order {order_id}"

    def low_stock(self, threshold: int = 5) -> List[str]:
        return [
            f"{sku}: {item['name']} (qty {item['qty']})"
            for sku, item in self._inventory.items()
            if item["qty"] <= threshold
        ]

    def open_ticket(self, subject: str) -> Ticket:
        ticket_id = f"tkt-{len(self._tickets) + 1}"
        ticket = Ticket(id=ticket_id, subject=subject, created_at=dt.datetime.utcnow())
        self._tickets.append(ticket)
        return ticket
