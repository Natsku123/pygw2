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
DailyAchievement.update_forward_refs()

BiographyAnswer.update_forward_refs()
Story.update_forward_refs()

Character.update_forward_refs()
EquipmentTab.update_forward_refs()

GuildTeam.update_forward_refs()

Mini.update_forward_refs()
Novelty.update_forward_refs()
Title.update_forward_refs()

Transaction.update_forward_refs()
ItemListing.update_forward_refs()
Price.update_forward_refs()

GuildPvpGame.update_forward_refs()

WvWMatchWorlds.update_forward_refs()
WvWMapObjectives.update_forward_refs()
WvWObjective.update_forward_refs()
