from typing import Optional
from pygw2.api.items import ItemsApi
from pygw2.api.misc import MiscellaneousApi
from pygw2.utils import LazyLoader

items_api = ItemsApi()
misc_api = MiscellaneousApi()


def parse_item(data: Optional[dict]) -> Optional[dict]:
    if data is None:
        return data

    data["item_"] = LazyLoader(items_api.get, data["id"])
    if "infusions" in data and data["infusions"]:
        data["infusions_"] = LazyLoader(items_api.get, *data["infusions"])
    if "upgrades" in data and data["upgrades"]:
        data["upgrades_"] = LazyLoader(items_api.get, *data["upgrades"])
    if "skin" in data and data["skin"]:
        data["skin_"] = LazyLoader(items_api.skins, data["skin"])
    if "stats" in data and data["stats"]:
        data["stats"]["values_"] = LazyLoader(items_api.itemstats, data["stats"]["id"])
    if "dyes" in data and data["dyes"]:
        data["dyes_"] = LazyLoader(misc_api.colors, *data["dyes"])

    return data
