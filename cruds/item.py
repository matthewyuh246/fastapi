from enum import Enum
from typing import Optional



class ItemStatus(Enum):
    ON_SALE = "ON_SALE"
    SOLD_OUT = "SOLD_OUT"


class Item:
    def __init__(
            self,
            id: int,
            name: str,
            price: int,
            description: Optional[str],
            status: ItemStatus
    ):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.status = status

items = [
    Item(1, "PC", 10000, "備品です", ItemStatus.ON_SALE),
    Item(2, "スマートフォン", 50000, None, ItemStatus.ON_SALE),
    Item(3, "Python本", 1000, "使用感あり", ItemStatus.SOLD_OUT),
]

def find_all():
    return items

# def find_by_id(id: int):
#     for item in items:
#         if item.id == id:
#             return item
#     return None

def find_by_id(id: int):
    left, right = 1, len(items)
    while left <= right:
        mid = (left + right) // 2
        mid_item = items[mid-1]
        if mid_item.id == id:
            return mid_item
        elif mid_item.id < id:
            left = mid + 1
        else:
            right = mid - 1
    return None

def find_by_name(name: str):
    filtered_items = []

    for item in items:
        if name in item.name:
            filtered_items.append(item)
    return filtered_items

def create(item_create):
    new_item = Item(
        len(items) + 1,
        item_create.get("name"),
        item_create.get("price"),
        item_create.get("description"),
        ItemStatus.ON_SALE,
    )
    items.append(new_item)
    return new_item

# def update(id: int, item_update):
#     for item in items:
#         if item.id == id:
#             item.name = item_update.get("name", item.name)
#             item.price = item_update.get("price", item.price)
#             item.description = item_update.get("description", item.description)
#             item.status = item_update.get("status", item.status)
#             return item
#     return None

def update(id: int, item_update):
    left, right = 1, len(items)
    while left <= right:
        mid = (left + right) // 2
        mid_item = items[mid-1]
        if mid_item.id == id:
            mid_item.name = item_update.get("name", mid_item.name)
            mid_item.price = item_update.get("price", mid_item.price)
            mid_item.description = item_update.get("description", mid_item.description)
            mid_item.status = item_update.get("status", mid_item.status)
            return mid_item
        elif mid_item.id < id:
            left = mid + 1
        else:
            right = mid - 1
    return None

def delete(id: int):
    left, right = 1, len(items)
    while left <= right:
        mid = (left + right) // 2
        mid_item = items[mid-1]
        if mid_item.id == id:
            delete_item = items.pop(mid-1)
            return delete_item
        elif mid_item.id < id:
            left = mid + 1
        else:
            right = mid - 1
    return None