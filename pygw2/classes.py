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
        if 'Pvp' in achi['flags']:
            self.pvp = True
        else:
            self.pvp = False

        if 'CategoryDisplay' in achi['flags']:
            self.meta = True
        else:
            self.meta = False

        if 'MoveToTop' in achi['flags']:
            self.mtt = True
        else:
            self.mtt = False

        if 'IgnoreNearlyComplete' in achi['flags']:
            self.inc = True
        else:
            self.inc = False

        if 'Repeatable' in achi['flags']:
            self.repeatable = True
        else:
            self.repeatable = False

        if 'Hidden' in achi['flags']:
            self.hidden = True
        else:
            self.hidden = False

        if 'RequiresUnlock' in achi['flags']:
            self.req_unlock = True
        else:
            self.req_unlock = False

        if 'RepairOnLogin' in achi['flags']:
            self.repair = True
        else:
            self.repair = False

        if 'Daily' in achi['flags']:
            self.daily = True
        else:
            self.daily = False

        if 'Weekly' in achi['flags']:
            self.weekly = True
        else:
            self.weekly = False

        if 'Monthly' in achi['flags']:
            self.monthly = True
        else:
            self.monthly = False

        if 'Permanent' in achi['flags']:
            self.permanent = True
        else:
            self.permanent = False

        self.tiers = achi['tiers']

        if 'prerequisites' in achi:
            self.prerequisites = achi['prerequisites']
        else:
            self.prerequisites = None

        if 'rewards' in achi:
            self.rewards = []
            for reward in achi['rewards']:
                self.rewards.append(create_object(reward))
        else:
            self.rewards = []

        if 'bits' in achi:
            self.bits = achi['bits']
        else:
            self.bits = None

        if 'point_cap' in achi:
            self.point_cap = achi['point_cap']
        else:
            self.point_cap = None

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
