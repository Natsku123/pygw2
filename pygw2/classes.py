import datetime
from .api import achievements
from .api import items


class ApiError(Exception):
    """Raised if API returns something unexpected."""
    pass


class Coins:
    def __init__(self, coins: dict):
        self.count = coins['count']
        if 'type' in coins:
            del coins['type']
        self.json = coins


class Character:
    def __init__(self, chard):
        self.name = chard.get('name', None)
        self.race = chard.get('race', None)
        self.gender = chard.get('gender', None)
        self.profession = chard.get('profession', None)
        self.level = chard.get('level', None)
        self.guild = chard.get('guild', None)
        self.age = chard.get('age', None)
        self.created = datetime.datetime.fromisoformat(chard.get('created', None))
        self.deaths = chard.get('deaths', None)
        self.crafting = chard.get('crafting', None)
        self.title = chard.get('title', None)
        self.backstory = chard.get('backstory', None)
        self.wvw_abilities = chard.get('wvw_abilities', None)
        self.specializations = chard.get('specializations', None)
        self.skills = chard.get('skills', None)
        self.equipment = {}
        items_list = []
        for item in chard['equipment']:
            items_list.append(item['id'])
        items_list = items.get(ids=items_list)
        for item in chard['equipment']:

            infusions = item.get('infusions', None)
            if infusions is not None:
                infusions = items.get(ids=infusions)

            upgrades = item.get('upgrades', None)
            if upgrades is not None:
                upgrades = items.get(ids=upgrades)

            # TODO resolve skin against /v2/skins
            # TODO resolve itemstats against /v2/itemstats
            # TODO resolve dyes against /v2/colors
            self.equipment[item['slot']] = {
                "item": items_list[chard['equipment'].index(item)],
                "infusions": infusions,
                "upgrades": upgrades,
                "skin": item.get('skin', None),
                "stats": item.get('stats', None),
                "binding": item.get('binding', None),
                "charges": item.get('charges', None),
                "bound_to": item.get('bound_to', None),
                "dyes": item.get("dyes", None)
            }
        self.recipes = chard.get('recipes', None)
        self.equipment_pvp = {
            "amulet": chard['equipment_pvp']['amulet'],
            "rune": items.get(ids=[chard['equipment_pvp']['rune']]),
            "sigils": items.get(ids=chard['equipment_pvp']['sigils'])
        }
        self.training = chard.get('training', None),
        self.bags = []
        bags_ids = []
        for bag in chard['bags']:
            bags_ids.append(bag['id'])
        bags_items = items.get(ids=bags_ids)
        i = 0
        for bag in chard['bags']:
            items_ids = []
            for item in bag['inventory']:
                if item is not None:
                    items_ids.append(item['id'])

            items_list = items.get(ids=items_ids)

            inventory = {}
            n = 0
            for item in bag['inventory']:
                if item is not None:
                    for itm_obj in items_list:
                        if itm_obj.id == item['id']:
                            infusions = item.get('infusions', None)
                            if infusions is not None:
                                infusions = items.get(ids=infusions)

                            upgrades = item.get('upgrades', None)
                            if upgrades is not None:
                                upgrades = items.get(ids=upgrades)

                            # TODO resolve skin against /v2/skins
                            # TODO resolve itemstats against /v2/itemstats
                            # TODO make item object more 'precise'
                            inventory[n] = {
                                "item": itm_obj,
                                "count": item['count'],
                                "infusions": infusions,
                                "upgrades": upgrades,
                                "skin": item.get('skin', None),
                                "stats": item.get('stats', None),
                                "binding": item.get('binding', None),
                                "bound_to": item.get('bound_to', None)
                            }
                            break
                else:
                    inventory[n] = None
                n = n + 1
            self.bags.append({
                "bag": bags_items[i],
                "size": bag['size'],
                "inventory": inventory
            })
            i = i + 1
        # TODO resolve recipes
        # TODO resolve skills
        # TODO resolve specializations
        # TODO resolve backstory
        # TODO resolve title
        # TODO resolve guild
        # TODO resolve wvw abilities against /v2/wvw/abilities
        # TODO resolve pvp amulet against /v2/wvw/amulets


class Item:
    def __init__(self, item: dict):
        self.id = item.get('id', None)
        self.chat_link = item.get('chat_link', None)
        self.name = item.get('name', None)
        self.icon = item.get('icon', None)
        self.description = item.get('description', None)
        self.rarity = item.get('rarity', None)
        self.level = item.get('level', None)
        self.vendor_value = item.get('vendor_value', 0)
        self.default_skin = item.get('default_skin', None)

        # Go through all the flags
        if 'flags' in item:
            self.accountBindOnUse = 'AccountBindOnUse' in item['flags']
            self.accountBound = 'AccountBound' in item['flags']
            self.attuned = 'Attuned' in item['flags']
            self.bulkConsume = 'BulkConsume' in item['flags']
            self.deleteWarn = 'DeleteWarning' in item['flags']
            self.hideSuffix = 'HideSuffix' in item['flags']
            self.infused = 'Infused' in item['flags']
            self.monsterOnly = 'MonsterOnly' in item['flags']
            self.noMysticForge = 'NoMysticForge' in item['flags']
            self.noSalvage = 'NoSalvage' in item['flags']
            self.noSell = 'NoSell' in item['flags']
            self.notUpgradeable = 'NotUpgradeable' in item['flags']
            self.noUnderwater = 'NoUnderwater' in item['flags']
            self.soulbindOnAcquire = 'SoulbindOnAcquire' in item['flags']
            self.soulBindOnUse = 'SoulBindOnUse' in item['flags']
            self.tonic = 'Tonic' in item['flags']
            self.unique = 'Unique' in item['flags']
        else:
            self.accountBindOnUse = None
            self.accountBound = None
            self.attuned = None
            self.bulkConsume = None
            self.deleteWarn = None
            self.hideSuffix = None
            self.infused = None
            self.monsterOnly = None
            self.noMysticForge = None
            self.noSalvage = None
            self.noSell = None
            self.notUpgradeable = None
            self.noUnderwater = None
            self.soulbindOnAcquire = None
            self.soulBindOnUse = None
            self.tonic = None
            self.unique = None

        # Go through all the game types.
        if 'game_types' in item:
            self.activity = 'Activity' in item['game_types']
            self.dungeon = 'Dungeon' in item['game_types']
            self.pve = 'Pve' in item['game_types']
            self.pvp = 'Pvp' in item['game_types']
            self.pvpLobby = 'PvpLobby' in item['game_types']
            self.wvw = 'Wvw' in item['game_types']

        else:
            self.activity = None
            self.dungeon = None
            self.pve = None
            self.pvp = None
            self.pvpLobby = None
            self.wvw = None

        if 'restrictions' in item:
            self.asura = 'Asura' in item['restrictions']
            self.charr = 'Charr' in item['restrictions']
            self.human = 'Human' in item['restrictions']
            self.norn = 'Norn' in item['restrictions']
            self.sylvari = 'Sylvari' in item['restrictions']
            self.elementalist = 'Elementalist' in item['restrictions']
            self.engineer = 'Engineer' in item['restrictions']
            self.guardian = 'Guardian' in item['restrictions']
            self.mesmer = 'Mesmer' in item['restrictions']
            self.necromancer = 'Necromancer' in item['restrictions']
            self.ranger = 'Ranger' in item['restrictions']
            self.thief = 'Thief' in item['restrictions']
            self.warrior = 'Warrior' in item['restrictions']
        else:
            self.asura = None
            self.charr = None
            self.human = None
            self.norn = None
            self.sylvari = None
            self.elementalist = None
            self.engineer = None
            self.guardian = None
            self.mesmer = None
            self.necromancer = None
            self.ranger = None
            self.thief = None
            self.warrior = None


class ArmorItem(Item):
    def __init__(self, item: dict):
        self.type = item.get('type', None)
        self.weight_class = item.get('weight_class', None)
        self.defense = item.get('defense', None)

        self.infusion_slots = []
        for inf in item.get('infusion_slots', []):
            self.infusion_slots.append(InfusionSlot(inf))

        self.infix_upgrade = None
        if item.get('infix_upgrade', None):
            self.infix_upgrade = InfixUpgrade(item['infix_upgrade'])

        # TODO convert to items
        self.suffix_item_id = item.get('suffix_item_id', None)
        self.secondary_suffix_item_id = item.get('suffix_item_id', None)

        # TODO needs further implementation (stats)
        self.stat_choices = item.get('stat_choices', None)
        super().__init__(item)


class BackItem(Item):
    def __init__(self, item: dict):
        self.infusion_slots = []
        for inf in item.get('infusion_slots', []):
            self.infusion_slots.append(InfusionSlot(inf))

        self.infix_upgrade = None
        if item.get('infix_upgrade', None):
            self.infix_upgrade = InfixUpgrade(item['infix_upgrade'])

        # TODO convert to items
        self.suffix_item_id = item.get('suffix_item_id', None)
        self.secondary_suffix_item_id = item.get('suffix_item_id', None)

        # TODO needs further implementation (stats)
        self.stat_choices = item.get('stat_choices', None)
        super().__init__(item)


class Bag(Item):
    def __init__(self, item: dict):
        self.size = item.get('size', None)
        self.no_sell_or_sort = item.get('no_sell_or_sort', None)
        super().__init__(item)


class ConsumableItem(Item):
    def __init__(self, item: dict):
        self.type = item.get("type", None)
        self.description = item.get('description', None)
        self.duration_ms = item.get('duration_ms', None)
        self.unlock_type = item.get('unlock_type', None)

        # TODO change to dye
        self.color_id = item.get('color_id', None)

        # TODO change to recipe
        self.recipe_id = item.get('recipe_id', None)
        self.extra_recipe_id = item.get('extra_recipe_id', None)

        # TODO change to guild upgrade
        self.guild_upgrade_id = item.get('guild_upgrade_id', None)

        self.apply_count = item.get('apply_count', None)
        self.name = item.get('name', None)
        self.icon = item.get('icon', None)

        # TODO change to skins
        self.skins = item.get('skins', None)

        super().__init__(item)


class ContainerItem(Item):
    def __init__(self, item: dict):
        self.type = item.get('type', None)
        super().__init__(item)


class GatheringToolItem(Item):
    def __init__(self, item: dict):
        self.type = item.get('type', None)
        super().__init__(item)


class GizmoItem(Item):
    def __init__(self, item: dict):
        self.type = item.get('type', None)

        # TODO change to guild upgrade
        self.guild_upgrade_id = item.get('guild_upgrade_id', None)
        super().__init__(item)


class MiniatureItem(Item):
    def __init__(self, item: dict):

        # TODO change to mini
        self.type = item.get('minipet_id', None)
        super().__init__(item)


class SalvageKitItem(Item):
    def __init__(self, item: dict):
        self.type = item.get('type', None)
        self.charges = item.get('charges', None)
        super().__init__(item)


class TrinketItem(Item):
    def __init__(self, item: dict):
        self.type = item.get('type', None)

        self.infusion_slots = []
        for inf in item.get('infusion_slots', []):
            self.infusion_slots.append(InfusionSlot(inf))

        self.infix_upgrade = None
        if item.get('infix_upgrade', None):
            self.infix_upgrade = InfixUpgrade(item['infix_upgrade'])

        # TODO convert to items
        self.suffix_item_id = item.get('suffix_item_id', None)
        self.secondary_suffix_item_id = item.get('suffix_item_id', None)

        # TODO needs further implementation (stats)
        self.stat_choices = item.get('stat_choices', None)
        super().__init__(item)


class UpgradeComponentItem(Item):
    def __init__(self, item: dict):
        self.type = item.get('type', None)

        if 'flags' in item:
            self.upgradeAxe = 'Axe' in item['flags']
            self.upgradeDagger = 'Dagger' in item['flags']
            self.upgradeFocus = 'Focus' in item['flags']
            self.upgradeGreatsword = 'Greatsword' in item['flags']
            self.upgradeHammer = 'Hammer' in item['flags']
            self.upgradeHarpoon = 'Harpoon' in item['flags']
            self.upgradeLongBow = 'LongBow' in item['flags']
            self.upgradeMace = 'Mace' in item['flags']
            self.upgradePistol = 'Pistol' in item['flags']
            self.upgradeRifle = 'Rifle' in item['flags']
            self.upgradeScepter = 'Scepter' in item['flags']
            self.upgradeShield = 'Shield' in item['flags']
            self.upgradeShortBow = 'ShortBow' in item['flags']
            self.upgradeSpeargun = 'Speargun' in item['flags']
            self.upgradeStaff = 'Staff' in item['flags']
            self.upgradeSword = 'Sword' in item['flags']
            self.upgradeTorch = 'Torch' in item['flags']
            self.upgradeTrident = 'Trident' in item['flags']
            self.upgradeWarhorn = 'Warhorn' in item['flags']
            self.upgradeHeavyArmor = 'HeavyArmor' in item['flags']
            self.upgradeMediumArmor = 'MediumArmor' in item['flags']
            self.upgradeLightArmor = 'LightArmor' in item['flags']
            self.upgradeTrinket = 'Trinket' in item['flags']
        else:
            self.upgradeAxe = None
            self.upgradeDagger = None
            self.upgradeFocus = None
            self.upgradeGreatsword = None
            self.upgradeHammer = None
            self.upgradeHarpoon = None
            self.upgradeLongBow = None
            self.upgradeMace = None
            self.upgradePistol = None
            self.upgradeRifle = None
            self.upgradeScepter = None
            self.upgradeShield = None
            self.upgradeShortBow = None
            self.upgradeSpeargun = None
            self.upgradeStaff = None
            self.upgradeSword = None
            self.upgradeTorch = None
            self.upgradeTrident = None
            self.upgradeWarhorn = None
            self.upgradeHeavyArmor = None
            self.upgradeMediumArmor = None
            self.upgradeLightArmor = None
            self.upgradeTrinket = None

        if 'infusion_upgrade_flags' in item:
            self.infusionEnrichment = 'Enrichment' in item['infusion_upgrade_flags']
            self.infusion = 'Infusion' in item['infusion_upgrade_flags']
            self.infusionDefense = 'Defense' in item['infusion_upgrade_flags']
            self.infusionOffense = 'Offense' in item['infusion_upgrade_flags']
            self.infusionUtility = 'Utility' in item['infusion_upgrade_flags']
            self.infusionAgony = 'Agony' in item['infusion_upgrade_flags']
        else:
            self.infusionEnrichment = None
            self.infusion = None
            self.infusionDefense = None
            self.infusionOffense = None
            self.infusionUtility = None
            self.infusionAgony = None

        self.suffix = item.get('suffix', None)

        self.infix_upgrade = None
        if item.get('infix_upgrade', None):
            self.infix_upgrade = InfixUpgrade(item['infix_upgrade'])

        self.bonuses = item.get('bonuses', None)
        super().__init__(item)


class WeaponItem(Item):
    def __init__(self, item: dict):
        self.type = item.get('type', None)
        self.damage_type = item.get('damage_type', None)
        self.min_power = item.get('min_power', None)
        self.max_power = item.get('max_power', None)
        self.defense = item.get('defense', None)

        self.infusion_slots = []
        for inf in item.get('infusion_slots', []):
            self.infusion_slots.append(InfusionSlot(inf))

        self.infix_upgrade = None
        if item.get('infix_upgrade', None):
            self.infix_upgrade = InfixUpgrade(item['infix_upgrade'])

        # TODO convert to items
        self.suffix_item_id = item.get('suffix_item_id', None)
        self.secondary_suffix_item_id = item.get('suffix_item_id', None)

        # TODO needs further implementation (stats)
        self.stat_choices = item.get('stat_choices', None)

        super().__init__(item)


class InfixUpgrade:
    def __init__(self, iu: dict):

        # TODO The itemstat id that can be resolved against /v2/itemstats.
        self.id = iu.get('id', None)

        self.attributes = iu.get('attributes', None)
        self.buff = iu.get('buff', None)


class InfusionSlot:
    def __init__(self, ins: dict):
        if 'flags' in ins:
            self.enrichment = 'Enrichment' in ins['flags']
            self.infusion = 'Infusion' in ins['flags']
        else:
            self.enrichment = False
            self.infusion = False

        self.item_id = ins.get('item_id', None)


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
        self.playForFree = 'PlayForFree' in acc['access']
        self.guildWars2 = 'GuildWars2' in acc['access']
        self.heartOfThorns = 'HeartOfThorns' in acc['access']
        self.pathOfFire = 'PathOfFire' in acc['access']

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
        self.achievements = achievements.get(ids=achicategory['achievements'])

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
            self.categoryDisplay = 'CategoryDisplay' in achi['flags']
            self.moveToTop = 'MoveToTop' in achi['flags']
            self.ignoreNearlyComplete = 'IgnoreNearlyComplete' in achi['flags']
            self.repeatable = 'Repeatable' in achi['flags']
            self.hidden = 'Hidden' in achi['flags']
            self.requiresUnlock = 'RequiresUnlock' in achi['flags']
            self.repairOnLogin = 'RepairOnLogin' in achi['flags']
            self.daily = 'Daily' in achi['flags']
            self.weekly = 'Weekly' in achi['flags']
            self.monthly = 'Monthly' in achi['flags']
            self.permanent = 'Permanent' in achi['flags']
        else:
            self.pvp = None
            self.categoryDisplay = None
            self.moveToTop = None
            self.ignoreNearlyComplete = None
            self.repeatable = None
            self.hidden = None
            self.requiresUnlock = None
            self.repairOnLogin = None
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
                achievement = achievements.get(ids=[achi['id']], json=True)[0]

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
