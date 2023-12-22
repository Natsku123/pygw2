from __future__ import annotations

from .account import (
    VaultSlot,
    Coins,
    MasteryLevel,
    Mastery,
    MasteryProgress,
    Account,
    ProductAccess,
    Pet,
    PetSkill,
    HomeCat,
    HomeNode,
    MountSkill,
    MountType,
    UnlockedFinisher,
    SharedInventorySlot,
    StorageMaterial,
    WalletCurrency,
    Legendary,
    OwnedLegendary,
    SubToken,
    TokenInfo,
)
from .achievements import (
    Achievement,
    AchievementReward,
    AchievementGroup,
    AchievementTier,
    AchievementCategory,
    AchievementProgress,
    AchievementBits,
    DailyAchievements,
    DailyAchievementLevel,
    DailyAchievement,
)
from .commerce import (
    DeliveryBox,
    DeliveryBoxItem,
    ExchangeRate,
    Listing,
    ItemListing,
    PriceInfo,
    Price,
    Transaction,
)
from .character import (
    Crafting,
    Attributes,
    Stats,
    Equipment,
    ItemInventory,
    Bag,
    SkillsBase,
    SkillTree,
    Skills,
    Specializations,
    SpecializationBase,
    CharacterCore,
    Build,
    BuildTab,
    EquipmentTab,
    Character,
    CharacterWvWAbility,
    ProfessionTrainingTrack,
    ProfessionTraining,
    WeaponSkill,
    ProfessionWeapon,
    ProfessionWeapons,
    Profession,
    Race,
    Specialization,
    SkillFactPrefix,
    SkillFact,
    SkillTraitedFact,
    Skill,
    TraitSkill,
    Trait,
    Legend,
)
from .crafting import Material, RecipeIngredient, RecipeGuildIngredient, Recipe
from .general import (
    Finisher,
    StatAttributes,
    ItemStat,
    DailyCrafting,
    DailyMapChest,
    DailyWorldBoss,
    Skin,
    DyeSlot,
    SkinDyeSlots,
    ArmorSkinDetails,
    WeaponSkinDetails,
    GatheringSkinDetails,
    Foo,
    MountSkin,
)
from .guild import (
    GuildEmblemBackground,
    GuildEmblemForeground,
    GuildEmblem,
    Guild,
    GuildEmblemImages,
    GuildPermission,
    GuildUpgradeCost,
    GuildUpgrade,
    GuildLogEntry,
    GuildMember,
    GuildRank,
    GuildStashSlot,
    GuildStash,
    GuildTreasuryNeeded,
    GuildTreasury,
    GuildTeamMember,
    GuildTeamSeason,
    GuildTeam,
    GuildPvpWinLoss,
    GuildPvpGame,
    GuildPvpLadderStats,
)
from .items import (
    Upgrade,
    Item,
    InfixUpgrade,
    InfixAttribute,
    InfixBuff,
    InfusionSlot,
    ArmorDetails,
    BackDetails,
    BagDetails,
    ConsumableDetails,
    ContainerDetails,
    GatheringToolDetails,
    GizmoDetails,
    MiniatureDetails,
    SalvageKitDetails,
    TrinketDetails,
    UpgradeComponentDetails,
    WeaponDetails,
    Outfit,
    Glider,
    Mailcarrier,
)
from .map import Continent, Map, MapSector
from .pvp import (
    PvPEquipment,
    PvpAttributes,
    PvpAmulet,
    PvpWinLoss,
    PvpStats,
    PvpStatsProfessions,
    PvpLadderStats,
    PvpScores,
    PvpGame,
    PvpRankLevel,
    PvpRank,
    PvpDivisionTier,
    PvpDivision,
    PvpLeaderboard,
    PvpLeaderboardsLadderSettingsTier,
    PvpLeaderboardsLadderSettings,
    PvpLeaderboardsLadder,
    PvpLeaderboardScore,
    PvpLeaderboardsLadderScoring,
    PvpLeaderboards,
    PvpSeason,
    PvpHeroStats,
    PvpHeroSkin,
    PvpHero,
    PvpStandings,
    PvpStandingsCurrent,
    PvpStandingsBest,
)
from .sab import SABZones, SABUnlocks, SABSong, SAB
from .misc import (
    ColorDetails,
    Color,
    Currency,
    DungeonPath,
    Dungeon,
    File,
    Quaggan,
    Mini,
    Novelty,
    RaidWingEvent,
    RaidWing,
    Raid,
    Title,
    World,
)
from .backstory import (
    BiographyAnswer,
    BiographyQuestion,
    StoryChapter,
    Story,
    Season,
    QuestGoal,
    Quest,
)
from .wvw import (
    WvWAbilityRank,
    WvWAbility,
    WvWRank,
    WvWStats,
    WvWMatchWorlds,
    WvWMapObjectives,
    WvWMapBonus,
    WvWMatchMap,
    WvWMapScores,
    WvWSkirmish,
    WvWMatch,
    WvWUpgradeTierUpgrade,
    WvWUpgradeTier,
    WvWUpgrade,
    WvWObjective,
)

# Update forward refs
DailyAchievement.model_rebuild()

BiographyAnswer.model_rebuild()
Story.model_rebuild()

Character.model_rebuild()
EquipmentTab.model_rebuild()

GuildTeam.model_rebuild()

Mini.model_rebuild()
Novelty.model_rebuild()
Title.model_rebuild()

Transaction.model_rebuild()
ItemListing.model_rebuild()
Price.model_rebuild()

GuildPvpGame.model_rebuild()

WvWMatchWorlds.model_rebuild()
WvWMapObjectives.model_rebuild()
WvWObjective.model_rebuild()
