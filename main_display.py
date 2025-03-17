from container.imports_library import *
from generators.elements import *

# top panel
class TopPanel:
    def __init__(self, ui_manager, screen_size):
        self.screenWidth, self.screenHeight = screen_size
        self.ui_manager = ui_manager
        self.topPanel = UIPanel(relative_rect=pygame.Rect((0, 0), (self.screenWidth, 90)), manager=self.ui_manager, starting_height=1)
        self.planetName = "Earth"
        self._build()

    def _build(self):
        # labels
        UILabel(relative_rect=pygame.Rect((10, 10), (160, 30)), text="Business Name: ", manager=self.ui_manager, container=self.topPanel)
        self.time_played = UILabel(relative_rect=pygame.Rect((self.screenWidth-170, 10), (160, 30)), text="Played Time: 00:00:00", manager=self.ui_manager, container=self.topPanel)
        self.planet_name = UILabel(relative_rect=pygame.Rect((self.screenWidth-170, 40), (160, 30)), text="planet Name: Earth", manager=self.ui_manager, container=self.topPanel)
        # buttons
        button_x = (self.screenWidth - 3 * 130 - 20) // 2

        self.randomizeName = UIButton(relative_rect=pygame.Rect((300, 10), (150, 30)), text="Randomize Name", manager=self.ui_manager, container=self.topPanel)
        
        self.storageUnit = UIButton(relative_rect=pygame.Rect((button_x, 45), (130, 30)), text="Storage Unit", manager=self.ui_manager, container=self.topPanel)
        self.rocketStore = UIButton(relative_rect=pygame.Rect((button_x + 140, 45), (130, 30)), text="Rocket Store", manager=self.ui_manager, container=self.topPanel)
        self.planetStore = UIButton(relative_rect=pygame.Rect((button_x + 280, 45), (130, 30)), text="Planet Store", manager=self.ui_manager, container=self.topPanel)
        #elements
        self.textBusiness_Name = UITextEntryLine(relative_rect=pygame.Rect((145, 10), (150, 30)), manager=self.ui_manager, container=self.topPanel)
    
    def update(self, start_time):
        # play time
        play_time = time.time() - start_time
        hours, remainder = divmod(play_time, 3600)
        minutes, remainder = divmod(remainder, 60)
        seconds, milliseconds = divmod(remainder, 1)
        milliseconds *= 1000
        self.time_played.set_text(f"Play Time: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}.{int(milliseconds):03d}")
        self.planet_name.set_text(f"Planet: {self.planetName}")

    def handle_event(self, event, planet_panel=None, rocket_panel=None):
        if self.randomizeName.process_event(event):
            self.textBusiness_Name.set_text(BusinessName())
        
        if self.planetStore.process_event(event) and not None:
            planet_panel.store_open = not planet_panel.store_open
            planet_panel.toggle_store()
        
        if self.rocketStore.process_event(event) and not None:
            rocket_panel.store_open = not rocket_panel.store_open
            rocket_panel.toggle_store()

# details
class DetailsPanel:
    def __init__(self, ui_manager):
        self.ui_manager = ui_manager
        self.detailsPanel = UIPanel(relative_rect=pygame.Rect((10, 90), (220, 120)), manager=self.ui_manager, starting_height=1)
        self.money_value, self.gold_value, self.megaBucks_value = 0.00, 0.00, 0.00
        self._build()

    def _build(self):
        # labels
        self.money = UILabel(relative_rect=pygame.Rect((10, 10), (200, 30)), text="Money: $0.00", manager=self.ui_manager, container=self.detailsPanel)
        self.gold = UILabel(relative_rect=pygame.Rect((10, 40), (200, 30)), text="Gold: $0.00", manager=self.ui_manager, container=self.detailsPanel)
        self.megaBucks = UILabel(relative_rect=pygame.Rect((10, 70), (200, 30)), text="Mega Bucks: $0.00", manager=self.ui_manager, container=self.detailsPanel)
 
    def update(self):
        self.money.set_text(f"Money: ${Format_Number(self.money_value)}")
        self.gold.set_text(f"Gold: ${Format_Number(self.gold_value)}")
        self.megaBucks.set_text(f"Mega Bucks: ${Format_Number(self.megaBucks_value)}")

# bottom panel
class BottomPanel:
    def __init__(self, ui_manager, screen_size):
        self.screenWidth, self.screenHeight = screen_size
        self.ui_manager = ui_manager
        self.bottomPanel = UIPanel(relative_rect=pygame.Rect((0, self.screenHeight-50), (self.screenWidth, 50)), manager=self.ui_manager, starting_height=1)
        self._build()

    def _build(self):
        # btn
        self.manager = UIButton(relative_rect=pygame.Rect((self.screenWidth//2 + 130, 10), (120, 30)), text="Managers", manager=self.ui_manager, container=self.bottomPanel)
        self.upgrades = UIButton(relative_rect=pygame.Rect((self.screenWidth//2 - 250, 10), (120, 30)), text="Upgrades", manager=self.ui_manager, container=self.bottomPanel)

        #elements
        self.searchBar = UITextEntryLine(relative_rect=pygame.Rect((self.screenWidth//2 - 100, 10), (200, 30)), manager=self.ui_manager, container=self.bottomPanel, placeholder_text="Search...")