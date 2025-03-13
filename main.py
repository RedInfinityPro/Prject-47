from container.imports_library import *
# hand made
from business_name_gen import BusinessName
from planet_store import PlanetStore
from rocket_store import RocketStore
# window
screenWidth, screenHeight = 1280, 720
current_time = time.time()
random.seed(current_time)
start_time = time.time()

# format number
def format_number(num):
    """Formats large numbers with suffixes"""
    if num >= 1e6:
        suffixes = ['Mil', 'Bil', 'Tri', 'Qua', 'Qui', 'Sex', 'Sep']
        index = int(math.log10(num) // 3 - 2)
        return f"{num / 10**(6 + index * 3):.2f} {suffixes[index]}" if index < len(suffixes) else f"{num:.2e}"
    return f"{num:,.2f}"

# top panel
class TopPanel:
    def __init__(self, ui_manager):
        self.ui_manager = ui_manager
        self.topPanel = UIPanel(relative_rect=pygame.Rect((0, 0), (screenWidth, 90)), manager=self.ui_manager, starting_height=1)
        self.planetName = "Earth"
        self._build()

    def _build(self):
        # labels
        UILabel(relative_rect=pygame.Rect((10, 10), (160, 30)), text="Business Name: ", manager=self.ui_manager, container=self.topPanel)
        self.time_played = UILabel(relative_rect=pygame.Rect((screenWidth-170, 10), (160, 30)), text="Played Time: 00:00:00", manager=self.ui_manager, container=self.topPanel)
        self.planet_name = UILabel(relative_rect=pygame.Rect((screenWidth-170, 40), (160, 30)), text="planet Name: Earth", manager=self.ui_manager, container=self.topPanel)
        # buttons
        button_x = (screenWidth - 3 * 130 - 20) // 2

        self.randomizeName = UIButton(relative_rect=pygame.Rect((300, 10), (150, 30)), text="Randomize Name", manager=self.ui_manager, container=self.topPanel)
        
        self.storageUnit = UIButton(relative_rect=pygame.Rect((button_x, 45), (130, 30)), text="Storage Unit", manager=self.ui_manager, container=self.topPanel)
        self.rocketStore = UIButton(relative_rect=pygame.Rect((button_x + 140, 45), (130, 30)), text="Rocket Store", manager=self.ui_manager, container=self.topPanel)
        self.planetStore = UIButton(relative_rect=pygame.Rect((button_x + 280, 45), (130, 30)), text="Planet Store", manager=self.ui_manager, container=self.topPanel)
        #elements
        self.textBusiness_Name = UITextEntryLine(relative_rect=pygame.Rect((145, 10), (150, 30)), manager=self.ui_manager, container=self.topPanel)
    
    def update(self):
        # play time
        play_time = time.time() - start_time
        hours, remainder = divmod(play_time, 3600)
        minutes, remainder = divmod(remainder, 60)
        seconds, milliseconds = divmod(remainder, 1)
        milliseconds *= 1000
        self.time_played.set_text(f"Play Time: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}.{int(milliseconds):03d}")
        self.planet_name.set_text(f"Planet: {self.planetName}")

    def handle_event(self, event, planet_panel, rocket_panel):
        if self.randomizeName.process_event(event):
            self.textBusiness_Name.set_text(BusinessName())
        
        if self.planetStore.process_event(event):
            planet_panel.store_open = not planet_panel.store_open
            planet_panel.toggle_store()
        
        if self.rocketStore.process_event(event):
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
        self.money.set_text(f"Money: ${format_number(self.money_value)}")
        self.gold.set_text(f"Gold: ${format_number(self.gold_value)}")
        self.megaBucks.set_text(f"Mega Bucks: ${format_number(self.megaBucks_value)}")

# bottom panel
class BottomPanel:
    def __init__(self, ui_manager):
        self.ui_manager = ui_manager
        self.bottomPanel = UIPanel(relative_rect=pygame.Rect((0, screenHeight-50), (screenWidth, 50)), manager=self.ui_manager, starting_height=1)
        self._build()

    def _build(self):
        # btn
        self.manager = UIButton(relative_rect=pygame.Rect((screenWidth//2 + 130, 10), (120, 30)), text="Managers", manager=self.ui_manager, container=self.bottomPanel)
        self.upgrades = UIButton(relative_rect=pygame.Rect((screenWidth//2 - 250, 10), (120, 30)), text="Upgrades", manager=self.ui_manager, container=self.bottomPanel)

        #elements
        self.searchBar = UITextEntryLine(relative_rect=pygame.Rect((screenWidth//2 - 100, 10), (200, 30)), manager=self.ui_manager, container=self.bottomPanel, placeholder_text="Search...")
    
# main
class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)
        pygame.display.set_caption("Game")
        self.background_surface = pygame.Surface((screenWidth, screenHeight)).convert()
        # ui_manager
        self.ui_manager = UIManager((screenWidth, screenHeight), r'json_files\Earth.json')
        self.clock = pygame.time.Clock()
        self.running = True
        # panels
        self.planet_panel = PlanetStore(self.ui_manager, (screenWidth, screenHeight))
        self.rocket_panel = RocketStore(self.ui_manager, (screenWidth, screenHeight))
        # -->
        self.top_panel = TopPanel(self.ui_manager)
        self.details_panel = DetailsPanel(self.ui_manager)
        self.bottom_panel = BottomPanel(self.ui_manager)
        
    def run(self):
        while self.running:
            time_delta = self.clock.tick(64) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end_time = time.time()
                    self.running = False
                    sys.exit()
                self.ui_manager.process_events(event)
                self.top_panel.handle_event(event, self.planet_panel, self.rocket_panel)
                if self.planet_panel.store_open:
                    self.planet_panel.handle_event(event)

                if self.rocket_panel.store_open:
                    self.rocket_panel.handle_event(event)
            # Draw elements
            self.ui_manager.update(time_delta)
            self.screen.blit(self.background_surface, (0, 0))
            self.ui_manager.draw_ui(self.screen)

            # update
            self.top_panel.update()
            self.details_panel.update()
            self.clock.tick(64)
            pygame.display.flip()
            pygame.display.update()


# run
if __name__ == "__main__":
    app = App()
    app.run()