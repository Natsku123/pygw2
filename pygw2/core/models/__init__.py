from .account import *
from .achievements import *
from .character import *
from .crafting import *
from .general import *
from .guild import *
from .items import *
from .map import *
from .pvp import *
from .sab import *
from .misc import *

# Update forward refs
DailyAchievement.update_forward_refs(ProductAccess=ProductAccess)

Character.update_forward_refs(SAB=SAB, PvPEquipment=PvPEquipment)

GuildTeam.update_forward_refs(
    PvpWinLoss=PvpWinLoss, PvpLadderStats=PvpLadderStats, PvpGame=PvpGame
)

Mini.update_forward_refs(Item=Item)
Novelty.update_forward_refs(Item=Item)
Title.update_forward_refs(Achievement=Achievement)
