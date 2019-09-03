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


class Account:
    def __init__(self, acc: dict):
        self.id = acc['id']
        self.age = acc['age']
        self.name = acc['name']
        self.world = acc['world']
        self.guilds = acc['guilds']
        self.guild_leader = acc['guild_leader']
        self.created = acc['created']

        # Go through access
        self.pff = 'PlayForFree' in acc['access']
        self.gw2 = 'GuildWars2' in acc['access']
        self.hot = 'HeartOfThorns' in acc['access']
        self.pof = 'PathOfFire' in acc['access']

        self.commander = acc['commander']
        self.fractal_level = acc['fractal_level']
        self.daily_ap = acc['daily_ap']
        self.monthly_ap = acc['monthly_ap']
        self.wvw_rank = acc['wvw_rank']
        self.last_modified = acc['last_modified']

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Account(id={0})".format(self.id)


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
        self.id = achi.get('id', None)
        self.icon = achi.get('icon', None)
        self.name = achi.get('name', None)
        self.description = achi.get('description', None)
        self.requirement = achi.get('requirement', None)
        self.locked_text = achi.get('locked_text', None)
        self.type = achi.get('type', None)

        # Go through all the flags
        if 'flags' in achi:
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
        else:
            self.pvp = None
            self.meta = None
            self.mtt = None
            self.inc = None
            self.repeatable = None
            self.hidden = None
            self.req_unlock = None
            self.repair = None
            self.daily = None
            self.weekly = None
            self.monthly = None
            self.permanent = None

        self.tiers = achi.get('tiers', None)
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


class AchievementProgress(Achievement):
    def __init__(self, achi: dict, achio: dict=None):
        self.bits = achi.get("bits", None)
        self.current = achi.get("current", None)
        self.max = achi.get("max", None)
        self.done = achi['done']
        self.repeated = achi.get("repeated", None)
        self.unlocked = achi.get("unlocked", True)

        # Add rest of achievement information.
        if achio is None:
            try:
                achievement = achievements.get([achi['id']], json=True)[0]

                super().__init__(achievement)
            except ApiError:
                pass
        else:
            super().__init__(achio)


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
