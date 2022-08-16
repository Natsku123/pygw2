from .account import *
from .achievements import *
from .commerce import *
from .character import *
from .crafting import *
from .general import *
from .guild import *
from .items import *
from .map import *
from .pvp import *
from .sab import *
from .misc import *
from .backstory import *
from .wvw import *

# Update forward refs
DailyAchievement.update_forward_refs(ProductAccess=ProductAccess)

BiographyAnswer.update_forward_refs(BiographyQuestion=BiographyQuestion)
Story.update_forward_refs(Season=Season)

Character.update_forward_refs(SAB=SAB, PvPEquipment=PvPEquipment)
EquipmentTab.update_forward_refs(PvPEquipment=PvPEquipment)

GuildTeam.update_forward_refs(
    PvpWinLoss=PvpWinLoss, PvpLadderStats=PvpLadderStats, PvpGame=PvpGame
)

Mini.update_forward_refs(Item=Item)
Novelty.update_forward_refs(Item=Item)
Title.update_forward_refs(Achievement=Achievement)

Transaction.update_forward_refs(Item=Item)
ItemListing.update_forward_refs(Item=Item)
Price.update_forward_refs(Item=Item)

GuildPvpGame.update_forward_refs(PvpScores=PvpScores)

WvWMatchWorlds.update_forward_refs(World=World)
WvWMapObjectives.update_forward_refs(Guild=Guild, GuildUpgrade=GuildUpgrade)
WvWObjective.update_forward_refs(MapSector=MapSector, Map=Map)
