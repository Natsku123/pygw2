from enum import Enum


class Races(str, Enum):
    Asura = "Asura"
    Charr = "Charr"
    Human = "Human"
    Norn = "Norn"
    Sylvari = "Sylvari"


class Gender(str, Enum):
    Male = "Male"
    Female = "Female"


class Professions(str, Enum):
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


class EquipmentLocation(str, Enum):
    Equipped = "Equipped"
    Armory = "Armory"
    EquippedFromLegendaryArmory = "EquippedFromLegendaryArmory"
    LegendaryArmory = "LegendaryArmory"


class EquipmentSlot(str, Enum):
    HelmAquatic = "HelmAquatic"
    Backpack = "Backpack"
    Coat = "Coat"
    Boots = "Boots"
    Gloves = "Gloves"
    Helm = "Helm"
    Leggings = "Leggings"
    Shoulders = "Shoulders"
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


class NoveltySlot(str, Enum):
    Chair = "Chair"
    Music = "Music"
    HeldItem = "HeldItem"
    Miscellaneous = "Miscellaneous"
    Tonic = "Tonic"


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
    Bag = "Bag"
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
    Longbow = "Longbow"
    Mace = "Mace"
    Pistol = "Pistol"
    Rifle = "Rifle"
    Scepter = "Scepter"
    Shield = "Shield"
    Shortbow = "Shortbow"
    Speargun = "Speargun"
    Spear = "Spear"
    Staff = "Staff"
    Sword = "Sword"
    Greatsword = "Greatsword"
    Torch = "Torch"
    Trident = "Trident"
    Warhorn = "Warhorn"
    Null = "None"


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


class AchievementRewardType(str, Enum):
    Coins = "Coins"
    Item = "Item"
    Mastery = "Mastery"
    Title = "Title"


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


class RecipeType(str, Enum):
    Axe = "Axe"
    Dagger = "Dagger"
    Focus = "Focus"
    Greatsword = "Greatsword"
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
    Boots = "Boots"
    Coat = "Coat"
    Gloves = "Gloves"
    Helm = "Helm"
    Leggings = "Leggings"
    Shoulders = "Shoulders"
    Amulet = "Amulet"
    Earring = "Earring"
    Ring = "Ring"
    Dessert = "Dessert"
    Feast = "Feast"
    IngredientCooking = "IngredientCooking"
    Meal = "Meal"
    Seasoning = "Seasoning"
    Snack = "Snack"
    Soup = "Soup"
    Food = "Food"
    Component = "Component"
    Inscription = "Inscription"
    Insignia = "Insignia"
    LegendaryComponent = "LegendaryComponent"
    Refinement = "Refinement"
    RefinementEctoplasm = "RefinementEctoplasm"
    RefinementObsidian = "RefinementObsidian"
    GuildConsumable = "GuildConsumable"
    GuildDecoration = "GuildDecoration"
    GuildConsumableWvw = "GuildConsumableWvw"
    Backpack = "Backpack"
    Bag = "Bag"
    Bulk = "Bulk"
    Consumable = "Consumable"
    Dye = "Dye"
    Potion = "Potion"
    UpgradeComponent = "UpgradeComponent"


class RecipeFlag(str, Enum):
    AutoLearned = "AutoLearned"
    LearnedFromItem = "LearnedFromItem"


class SkinType(str, Enum):
    Armor = "Armor"
    Weapon = "Weapon"
    Back = "Back"
    Gathering = "Gathering"


class SkinFlag(str, Enum):
    ShowInWardrobe = "ShowInWardrobe"
    NoCost = "NoCost"
    HideIfLocked = "HideIfLocked"
    OverrideRarity = "OverrideRarity"


class DyeSlotMaterial(str, Enum):
    cloth = "cloth"
    leather = "leather"
    metal = "metal"
    fur = "fur"


class ProfessionTrainingCategory(str, Enum):
    Skills = "Skills"
    Specializations = "Specializations"
    EliteSpecializations = "EliteSpecializations"


class ProfessionTrainingTrackType(str, Enum):
    Trait = "Trait"
    Skill = "Skill"


class ProfessionWeaponFlag(str, Enum):
    Mainhand = "Mainhand"
    Offhand = "Offhand"
    TwoHand = "TwoHand"
    Aquatic = "Aquatic"


class ProfessionWeaponFlags(str, Enum):
    NoRacialSkills = "NoRacialSkills"
    NoWeaponSwap = "NoWeaponSwap"


class SkillType(str, Enum):
    Bundle = "Bundle"
    Elite = "Elite"
    Heal = "Heal"
    Profession = "Profession"
    Utility = "Utility"
    Weapon = "Weapon"


class SkillSlot(str, Enum):
    Downed_1 = "Downed_1"
    Downed_2 = "Downed_2"
    Downed_3 = "Downed_3"
    Downed_4 = "Downed_4"
    Pet = "Pet"
    Profession_1 = "Profession_1"
    Profession_2 = "Profession_2"
    Profession_3 = "Profession_3"
    Profession_4 = "Profession_4"
    Profession_5 = "Profession_5"
    Utility = "Utility"
    Weapon_1 = "Weapon_1"
    Weapon_2 = "Weapon_2"
    Weapon_3 = "Weapon_3"
    Weapon_4 = "Weapon_4"
    Weapon_5 = "Weapon_5"


class SkillFactType(str, Enum):
    AttributeAdjust = "AttributeAdjust"
    Buff = "Buff"
    BuffConversion = "BuffConversion"
    ComboField = "ComboField"
    ComboFinisher = "ComboFinisher"
    Damage = "Damage"
    Distance = "Distance"
    Duration = "Duration"
    Heal = "Heal"
    HealingAdjust = "HealingAdjust"
    NoData = "NoData"
    Number = "Number"
    Percent = "Percent"
    PrefixedBuff = "PrefixedBuff"
    Radius = "Radius"
    Range = "Range"
    Recharge = "Recharge"
    Time = "Time"
    Unblockable = "Unblockable"


class ComboFieldType(str, Enum):
    Air = "Air"
    Dark = "Dark"
    Fire = "Fire"
    Ice = "Ice"
    Light = "Light"
    Lightning = "Lightning"
    Poison = "Poison"
    Smoke = "Smoke"
    Ethereal = "Ethereal"
    Water = "Water"


class ComboFinisherType(str, Enum):
    Blast = "Blast"
    Leap = "Leap"
    Projectile = "Projectile"
    Whirl = "Whirl"


class SkillCategories(str, Enum):
    DualWield = "DualWield"
    StealthAttack = "StealthAttack"
    Signet = "Signet"
    Cantrip = "Cantrip"
    Deception = "Deception"
    Glyph = "Glyph"
    Mantra = "Mantra"
    Meditation = "Meditation"
    Physical = "Physical"
    Shout = "Shout"
    Stance = "Stance"
    Trap = "Trap"
    Well = "Well"
    Consecration = "Consecration"
    FinalCharge = "FinalCharge"
    SpiritWeapon = "SpiritWeapon"
    Symbol = "Symbol"
    Tome = "Tome"
    Virtue = "Virtue"
    Ward = "Ward"
    CitadelOrder = "CitadelOrder"
    Consume = "Consume"
    Facet = "Facet"
    Legend = "Legend"
    LegendaryAssassin = "LegendaryAssassin"
    LegendaryCentaur = "LegendaryCentaur"
    LegendaryDemon = "LegendaryDemon"
    LegendaryDragon = "LegendaryDragon"
    LegendaryDwarf = "LegendaryDwarf"
    LegendaryRenegade = "LegendaryRenegade"
    Banner = "Banner"
    Burst = "Burst"
    PrimalBurst = "PrimalBurst"
    Rage = "Rage"
    EngineeringKit = "EngineeringKit"
    Elixir = "Elixir"
    Exceed = "Exceed"
    Gadget = "Gadget"
    PhotonForge = "PhotonForge"
    Toolbelt = "Toolbelt"
    Turret = "Turret"
    Beast = "Beast"
    CelestialAvatar = "CelestialAvatar"
    Pet = "Pet"
    Command = "Command"
    Spirit = "Spirit"
    Survival = "Survival"
    Kneel = "Kneel"
    Preparation = "Preparation"
    Stolenskill = "Stolenskill"
    Trick = "Trick"
    Venom = "Venom"
    Arcane = "Arcane"
    Attunement = "Attunement"
    Conjure = "Conjure"
    DualAttack = "DualAttack"
    Overload = "Overload"
    Ambush = "Ambush"
    Clone = "Clone"
    Glamour = "Glamour"
    Manipulation = "Manipulation"
    Phantasm = "Phantasm"
    Shatter = "Shatter"
    Corruption = "Corruption"
    Mark = "Mark"
    Minion = "Minion"
    Punishment = "Punishment"
    Shade = "Shade"
    Spectral = "Spectral"


class Attunement(str, Enum):
    Fire = "Fire"
    Water = "Water"
    Air = "Air"
    Earth = "Earth"


class TraitTier(int, Enum):
    Weapon = 0
    Adept = 1
    Master = 2
    Grandmaster = 3


class TraitSlot(str, Enum):
    Major = "Major"
    Minor = "Minor"


class GuildEmblemFlags(str, Enum):
    FlipBackgroundHorizontal = "FlipBackgroundHorizontal"
    FlipBackgroundVertical = "FlipBackgroundVertical"


class GuildUpgradeType(str, Enum):
    AccumulatingCurrency = "AccumulatingCurrency"
    BankBag = "BankBag"
    Boost = "Boost"
    Claimable = "Claimable"
    Consumable = "Consumable"
    Decoration = "Decoration"
    GuildHall = "GuildHall"
    GuildHallExpedition = "GuildHallExpedition"
    Hub = "Hub"
    Queue = "Queue"
    Unlock = "Unlock"


class GuildUpgradeCostType(str, Enum):
    Item = "Item"
    Collectible = "Collectible"
    Currency = "Currency"
    Coins = "Coins"


class GuildLogEntryType(str, Enum):
    joined = "joined"
    invited = "invited"
    kick = "kick"
    rank_change = "rank_change"
    treasury = "treasury"
    stash = "stash"
    motd = "motd"
    upgrade = "upgrade"
    influence = "influence"
    invite_declined = "invite_declined"


class GuildStashOperation(str, Enum):
    deposit = "deposit"
    withdraw = "withdraw"
    move = "move"


class GuildUpgradeAction(str, Enum):
    queued = "queued"
    cancelled = "cancelled"
    completed = "completed"
    sped_up = "sped_up"


class GuildTeamMemberRole(str, Enum):
    Captain = "Captain"
    Member = "Member"


class PvpRatingType(str, Enum):
    Ranked = "Ranked"
    Unranked = "Unranked"


class ColorCategoryHue(str, Enum):
    Gray = "Gray"
    Brown = "Brown"
    Red = "Red"
    Orange = "Orange"
    Yellow = "Yellow"
    Green = "Green"
    Blue = "Blue"
    Purple = "Purple"


class ColorCategoryMaterial(str, Enum):
    Vibrant = "Vibrant"
    Leather = "Leather"
    Metal = "Metal"


class ColorCategoryRarity(str, Enum):
    Starter = "Starter"
    Common = "Common"
    Uncommon = "Uncommon"
    Rare = "Rare"
    Exclusive = "Exclusive"


class DungeonPathType(str, Enum):
    Story = "Story"
    Explorable = "Explorable"


class RaidWingEventType(str, Enum):
    Boss = "Boss"
    Checkpoint = "Checkpoint"


class WorldPopulation(str, Enum):
    Low = "Low"
    Medium = "Medium"
    High = "High"
    VeryHigh = "VeryHigh"
    Full = "Full"


class WorldRegion(int, Enum):
    NorthAmerica = 1
    Europe = 2


class StoryFlags(str, Enum):
    RequiresUnlock = "RequiresUnlock"


class PvpDivisionFlags(str, Enum):
    CanLosePoints = "CanLosePoints"
    CanLoseTiers = "CanLoseTiers"
    Repeatable = "Repeatable"


class WvWMapTypes(str, Enum):
    RedHome = "RedHome"
    GreenHome = "GreenHome"
    BlueHome = "BlueHome"
    Center = "Center"
    EdgeOfTheMists = "EdgeOfTheMists"


class WvWObjectiveTypes(str, Enum):
    Spawn = "Spawn"
    Camp = "Camp"
    Ruins = "Ruins"
    Tower = "Tower"
    Keep = "Keep"
    Castle = "Castle"
    Mercenary = "Mercenary"


class WvWTeams(str, Enum):
    Red = "Red"
    Green = "Green"
    Blue = "Blue"
    Neutral = "Neutral"


class WvWMapBonusTypes(str, Enum):
    Bloodlust = "Bloodlust"


class MailcarrierFlags(str, Enum):
    Default = "Default"


class TokenTypes(str, Enum):
    APIKey = "APIKey"
    Subtoken = "Subtoken"
