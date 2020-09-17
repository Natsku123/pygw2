from enum import Enum


class Race(str, Enum):
    Asura = "Asura"
    Charr = "Charr"
    Human = "Human"
    Norn = "Norn"
    Sylvari = "Sylvari"


class Gender(str, Enum):
    Male = "Male"
    Female = "Female"


class Profession(str, Enum):
    Elementalist = "Elementalist"
    Engineer = "Engineer"
    Guardian = "Guardian"
    Mesmer = "Mesmer"
    Necromancer = "Necromancer"
    Ranger = "Ranger"
    Revenant = "Revenant"
    Thief = "Thief"
    Warrior = "Warrior"


class Discipline(str, Enum):
    Armorsmith = "Armorsmith"
    Artificer = "Artificer"
    Chef = "Chef"
    Huntsman = "Huntsman"
    Jeweler = "Jeweler"
    Leatherworker = "Leatherworker"
    Scribe = "Scribe"
    Tailor = "Tailor"
    Weaponsmith = "Weaponsmith"


class EquipmentSlot(str, Enum):
    HelmAquatic = "HelmAquatic"
    Backpack = "Backpack"
    Coat = "Coat"
    Boots = "Boots"
    Gloves = "Gloves"
    Helm = "Helm"
    Leggings = "Leggings"
    Shoulders = "Shoulder"
    Accessory1 = "Accessory1"
    Accessory2 = "Accessory2"
    Ring1 = "Ring1"
    Ring2 = "Ring2"
    Amulet = "Amulet"
    WeaponAquaticA = "WeaponAquaticA"
    WeaponAquaticB = "WeaponAquaticB"
    WeaponA1 = "WeaponA1"
    WeaponA2 = "WeaponA2"
    WeaponB1 = "WeaponB1"
    WeaponB2 = "WeaponB2"
    Sickle = "Sickle"
    Axe = "Axe"
    Pick = "Pick"


class Binding(str, Enum):
    Character = "Character"
    Account = "Account"


class Attribute(str, Enum):
    BoonDuration = "BoonDuration"
    ConditionDamage = "ConditionDamage"
    ConditionDuration = "ConditionDuration"
    CritDamage = "CritDamage"
    Healing = "Healing"
    Power = "Power"
    Precision = "Precision"
    Toughness = "Toughness"
    Vitality = "Vitality"


class CharacterFlag(str, Enum):
    Beta = "Beta"


class ItemType(str, Enum):
    Armor = "Armor"
    Back = "Back"
    Consumable = "Consumable"
    Container = "Container"
    CraftingMaterial = "CraftingMaterial"
    Gathering = "Gathering"
    Gizmo = "Gizmo"
    Key = "Key"
    MiniPet = "MiniPet"
    Tool = "Tool"
    Trait = "Trait"
    Trinket = "Trinket"
    Trophy = "Trophy"
    UpgradeComponent = "UpgradeComponent"
    Weapon = "Weapon"


class ItemRarity(str, Enum):
    Junk = "Junk"
    Basic = "Basic"
    Fine = "Fine"
    Masterwork = "Masterwork"
    Rare = "Rare"
    Exotic = "Exotic"
    Ascended = "Ascended"
    Legendary = "Legendary"


class ItemFlags(str, Enum):
    AccountBindOnUse = "AccountBindOnUse"
    AccountBound = "AccountBound"
    Attuned = "Attuned"
    BulkConsume = "BulkConsume"
    DeleteWarning = "DeleteWarning"
    HideSuffix = "HideSuffix"
    Infused = "Infused"
    MonsterOnly = "MonsterOnly"
    NoMysticForge = "NoMysticForge"
    NoSalvage = "NoSalvage"
    NoSell = "NoSell"
    NotUpgradeable = "NotUpgradeable"
    NoUnderwater = "NoUnderwater"
    SoulbindOnAcquire = "SoulbindOnAcquire"
    SoulBindOnUse = "SoulBindOnUse"
    Tonic = "Tonic"
    Unique = "Unique"


class GameTypes(str, Enum):
    Activity = "Activity"
    Dungeon = "Dungeon"
    Pve = "Pve"
    Pvp = "Pvp"
    PvpLobby = "PvpLobby"
    Wvw = "Wvw"


class UpgradeType(str, Enum):
    Attunement = "Attunement"
    Infusion = "Infusion"


class InfusionSlotType(str, Enum):
    Enrichment = "Enrichment"
    Infusion = "Infusion"


class ArmorSlot(str, Enum):
    Boots = "Boots"
    Coat = "Coat"
    Gloves = "Gloves"
    Helm = "Helm"
    HelmAquatic = "HelmAquatic"
    Leggings = "Leggings"
    Shoulders = "Shoulders"


class WeightClass(str, Enum):
    Heavy = "Heavy"
    Medium = "Medium"
    Light = "Light"
    Clothing = "Clothing"


class ConsumableType(str, Enum):
    AppearanceChange = "AppearanceChange"
    Booze = "Booze"
    ContractNpc = "ContractNpc"
    Currency = "Currency"
    Food = "Food"
    Generic = "Generic"
    Halloween = "Halloween"
    Immediate = "Immediate"
    MountRandomUnlock = "MountRandomUnlock"
    RandomUnlock = "RandomUnlock"
    Transmutation = "Transmutation"
    Unlock = "Unlock"
    UpgradeRemoval = "UpgradeRemoval"
    Utility = "Utility"
    TeleportToFriend = "TeleportToFriend"


class UnlockType(str, Enum):
    BagSlot = "BagSlot"
    BankTab = "BankTab"
    Champion = "Champion"
    CollectibleCapacity = "CollectibleCapacity"
    Content = "Content"
    CraftingRecipe = "CraftingRecipe"
    Dye = "Dye"
    GliderSkin = "GliderSkin"
    Minipet = "Minipet"
    Ms = "Ms"
    Outfit = "Outfit"
    RandomUlock = "RandomUlock"
    SharedSlot = "SharedSlot"


class ContainerType(str, Enum):
    Default = "Default"
    GiftBox = "GiftBox"
    Immediate = "Immediate"
    OpenUI = "OpenUI"


class GatheringToolType(str, Enum):
    Foraging = "Foraging"
    Logging = "Logging"
    Mining = "Mining"


class GizmoType(str, Enum):
    Default = "Default"
    ContainerKey = "ContainerKey"
    RentableContractNpc = "RentableContractNpc"
    UnlimitedConsumable = "UnlimitedConsumable"


class SalvageKitType(str, Enum):
    Salvage = "Salvage"


class TrinketType(str, Enum):
    Accessory = "Accessory"
    Amulet = "Amulet"
    Ring = "Ring"


class UpgradeComponentType(str, Enum):
    Default = "Default"
    Gem = "Gem"
    Rune = "Rune"
    Sigil = "Sigil"


class WeaponType(str, Enum):
    Axe = "Axe"
    Dagger = "Dagger"
    Focus = "Focus"
    Hammer = "Hammer"
    Harpoon = "Harpoon"
    LongBow = "LongBow"
    Mace = "Mace"
    Pistol = "Pistol"
    Rifle = "Rifle"
    Scepter = "Scepter"
    Shield = "Shield"
    ShortBow = "ShortBow"
    Speargun = "Speargun"
    Staff = "Staff"
    Sword = "Sword"
    Torch = "Torch"
    Trident = "Trident"
    Warhorn = "Warhorn"


class UpgradeComponentFlag(str, Enum):
    HeavyArmor = "HeavyArmor"
    MediumArmor = "MediumArmor"
    LightArmor = "LightArmor"
    Trinket = "Trinket"


class InfusionUpgradeFlag(str, Enum):
    Enrichment = "Enrichment"
    Infusion = "Infusion"
    Defense = "Defense"
    Offense = "Offense"
    Utility = "Utility"
    Agony = "Agony"


class AdditionalWeaponType(str, Enum):
    LargeBundle = "LargeBundle"
    SmallBundle = "SmallBundle"
    Toy = "Toy"
    ToyTwoHanded = "ToyTwoHanded"


class DamageType(str, Enum):
    Fire = "Fire"
    Ice = "Ice"
    Lightning = "Lightning"
    Physical = "Physical"
    Choking = "Choking"


class AccountAccess(str, Enum):
    PlayForFree = "PlayForFree"
    GuildWars2 = "GuildWars2"
    HeartOfThorns = "HeartOfThorns"
    PathOfFire = "PathOfFire"


class AchievementType(str, Enum):
    Default = "Default"
    ItemSet = "ItemSet"


class AchievementFlag(str, Enum):
    Pvp = "Pvp"
    CategoryDisplay = "CategoryDisplay"
    MoveToTop = "MoveToTop"
    IgnoreNearlyComplete = "IgnoreNearlyComplete"
    Repeatable = "Repeatable"
    Hidden = "Hidden"
    RequiresUnlock = "RequiresUnlock"
    RepairOnLogin = "RepairOnLogin"
    Daily = "Daily"
    Weekly = "Weekly"
    Monthly = "Monthly"
    Permanent = "Permanent"


class Region(str, Enum):
    Tyria = "Tyria"
    Maguuma = "Maguuma"
    Desert = "Desert"


class AchievementBitsType(str, Enum):
    Text = "Text"
    Item = "Item"
    Minipet = "Minipet"
    Skin = "Skin"