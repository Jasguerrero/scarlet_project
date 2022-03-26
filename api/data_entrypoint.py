import datetime
from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from pymongo import MongoClient


class DataEntryPoint:
    def __init__(self, client: 'MongoClient'):
        self.db_client = client

    def save_point(self, session: Dict, loot: Dict):
        point = {
            **session,
            **loot,
            "created_at": datetime.datetime.now(),
            "updated_at": datetime.datetime.now()
        }

        self.db_client["scarlet"]["data"].insert_one(point)
