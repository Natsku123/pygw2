from typing import Optional
from pygw2.api.items import ItemsApi
from pygw2.api.misc import MiscellaneousApi
from pygw2.utils import LazyLoader

items_api = ItemsApi()
misc_api = MiscellaneousApi()


def parse_item(data: Optional[dict]) -> Optional[dict]:
    if data is None:
        return data

    data["_item"] = LazyLoader(items_api.get, data["id"])
    if data["infusions"]:
        data["_infusions"] = LazyLoader(items_api.get, *data["infusions"])
    if data["upgrades"]:
        data["_upgrades"] = LazyLoader(items_api.get, *data["upgrades"])
    if data["skin"]:
        data["_skin"] = LazyLoader(items_api.skins, data["skin"])
    if data["stats"]:
        data["stats"]["_values"] = LazyLoader(items_api.itemstats, data["stats"]["id"])
    if data["dyes"]:
        data["_dyes"] = LazyLoader(misc_api.colors, *data["dyes"])

    return data
