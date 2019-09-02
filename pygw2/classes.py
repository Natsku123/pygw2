from .api import achievements


class ApiError(Exception):
    """Raised if API returns something unexpected."""
    pass


class Coins:
    def __init__(self, coins: dict):
        self.count = coins['count']
        if 'type' in coins:
            del coins['type']
        self.json = coins


class Item:
    def __init__(self, item: dict):
        self.id = item['id']
        if 'type' in item:
            del item['type']
        self.json = item


class Mastery:
    def __init__(self, mastery: dict):
        self.id = mastery['id']
        self.region = mastery['region']
        if 'type' in mastery:
            del mastery['type']
        self.json = mastery


class Title:
    def __init__(self, title: dict):
        self.id = title['id']
        if 'type' in title:
            del title['type']
        self.json = title


class AchievementCategory:
    def __init__(self, achicategory: dict):
        self.id = achicategory['id']
        self.name = achicategory['name']
        self.description = achicategory['description']
        self.order = achicategory['order']
        self.icon = achicategory.get('icon', None)
        self.achievements = achievements.get(achicategory['achievements'])

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return "AchievementCategory(id={0.id})".format(self)


class AchievementGroup:
    def __init__(self, achigroup: dict):
        self.id = achigroup['id']
        self.name = achigroup['name']
        self.description = achigroup['description']
        self.order = achigroup['order']
        self.categories = achigroup['categories']

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return "AchievementGroup(id={0.id})".format(self)


class Achievement:
    def __init__(self, achi: dict):
        self.id = achi['id']

        if 'icon' in achi:
            self.icon = achi['icon']
        else:
            self.icon = None

        self.name = achi['name']
        self.description = achi['description']
        self.requirement = achi['requirement']
        self.locked_text = achi['locked_text']
        self.type = achi['type']

        # Go through all the flags
        self.pvp = 'Pvp' in achi['flags']
        self.meta = 'CategoryDisplay' in achi['flags']
        self.mtt = 'MoveToTop' in achi['flags']
        self.inc = 'IgnoreNearlyComplete' in achi['flags']
        self.repeatable = 'Repeatable' in achi['flags']
        self.hidden = 'Hidden' in achi['flags']
        self.req_unlock = 'RequiresUnlock' in achi['flags']
        self.repair = 'RepairOnLogin' in achi['flags']
        self.daily = 'Daily' in achi['flags']
        self.weekly = 'Weekly' in achi['flags']
        self.monthly = 'Monthly' in achi['flags']
        self.permanent = 'Permanent' in achi['flags']

        self.tiers = achi['tiers']
        self.prerequisites = achi.get('prerequisites', None)

        if 'rewards' in achi:
            self.rewards = []
            for reward in achi['rewards']:
                self.rewards.append(create_object(reward))
        else:
            self.rewards = []

        self.bits = achi.get('bits', None)
        self.point_cap = achi.get('point_cap', None)

        if 'type' in achi:
            del achi['type']
        self.json = achi

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return "Achievement(id={0.id})".format(self)


def create_object(d: dict):
    """
    Converts dict to object.
    :param d: dict
    :return: object
    """
    if d['type'] == "Mastery":
        return Mastery(d)
    elif d['type'] == "Coins":
        return Coins(d)
    elif d['type'] == "Title":
        return Title(d)
    elif d['type'] == "Item":
        return Item(d)
    else:
        return None
