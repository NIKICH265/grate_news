from enum import Enum


class NewsStatus(Enum):
    confirm: str = "confirm"
    pending: str = "pending"
    reject: str = "reject"
