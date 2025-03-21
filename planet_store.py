from container.imports_library import *
from generators.elements import *
from generators.planet_name_gen import *
from generators.business_name_gen import *

# Planet Content
class PlanetContent:
    def __init__(self, ui_manager, scroll_container, screenSize):
        self.ui_manager = ui_manager
        self.scroll_container = scroll_container
        self.screenWidth, self.screenHeight = screenSize
        self.name = f"Planet Name: {GenerateName()}"
        self.companyName = f"Business Name: {BusinessName()}"
        self.cost = Large_Number_Random_Generator(10**18, sys.maxsize)
        self.distance = Large_Number_Random_Generator(24, sys.maxsize)
        self.upKeep = Weighted_Random(0.01, sys.maxsize, 20)
        self.availablePurchase = "Available"
        self.currencyConversion = Weighted_Random(-9.00, 9.00, 1)
    
    def build(self, i):
        panel_width = self.screenWidth - 20
        panel_height = 70
        """Builds the UI panel for each business entry."""
        self.planetContainer = UIPanel(relative_rect=pygame.Rect((3, i * (panel_height + 1)), (panel_width, panel_height)), manager=self.ui_manager, container=self.scroll_container)
        self.btn = UIButton(relative_rect=pygame.Rect((0, 0), (100, panel_height-7)), text=f"{self.availablePurchase}", manager=self.ui_manager, container=self.planetContainer)
        self.name_label = UILabel(relative_rect=pygame.Rect((100, 5), (300, 20)), text=self.name, manager=self.ui_manager, container=self.planetContainer)
        self.companyName_label = UILabel(relative_rect=pygame.Rect((100, 20), (300, 20)), text=self.companyName, manager=self.ui_manager, container=self.planetContainer)
        cost_txt = f"Cost: ${Format_Number(self.cost)}"
        self.cost_label = UILabel(relative_rect=pygame.Rect((100, 40), (300, 20)), text=cost_txt, manager=self.ui_manager, container=self.planetContainer)
        # price
        self.planetContainer_2 = UIPanel(relative_rect=pygame.Rect((self.screenWidth - 325, -1), (300, panel_height)), manager=self.ui_manager, container=self.planetContainer)
        distance_txt = f"Distance: ${Format_Number(self.distance)}"
        self.distance_label = UILabel(relative_rect=pygame.Rect((1, 1), (300, 20)), text=distance_txt, manager=self.ui_manager, container=self.planetContainer_2)
        upKeep_txt = f"Up Keep: ${Format_Number(self.upKeep)}"
        self.upKeep_label = UILabel(relative_rect=pygame.Rect((1, 20), (300, 20)), text=upKeep_txt, manager=self.ui_manager, container=self.planetContainer_2)
        currencyConversion_txt = f"Currency Conversion: ${Format_Number(self.currencyConversion)} -> 1 USD"
        self.currencyConversion_label = UILabel(relative_rect=pygame.Rect((1, 40), (300, 20)), text=currencyConversion_txt, manager=self.ui_manager, container=self.planetContainer_2)

# Planet Store
class PlanetStore:
    def __init__(self, ui_manager, screenSize):
        self.ui_manager = ui_manager
        self.screenWidth, self.screenHeight = screenSize
        self.x, self.y = 240, 100
        self.planet_list = []
        self.store_open = True
        self._build()

    def _build(self):
        self.centerPanel = UIPanel(relative_rect=pygame.Rect((self.x, self.y), (self.screenWidth-250, self.screenHeight-160)), manager=self.ui_manager, starting_height=1)
        # labels
        UILabel(relative_rect=pygame.Rect((self.screenWidth/2-160, 10), (160, 30)), text="Planet Store: ", manager=self.ui_manager, container=self.centerPanel)
        self.btn = UIButton(relative_rect=pygame.Rect((self.screenWidth-290, 2), (30, 30)), text=f"X", manager=self.ui_manager, container=self.centerPanel)
        # buttons
        self.scroll_container = pygame_gui.elements.UIScrollingContainer(relative_rect=pygame.Rect((0, 40), (self.screenWidth-255, self.screenHeight-210)), manager=self.ui_manager, container=self.centerPanel)
        content_height = (70 * 100) + 110
        self.scroll_container.set_scrollable_area_dimensions((self.screenWidth-290, content_height))

        for i in range(100):
            planet = PlanetContent(self.ui_manager, self.scroll_container, (self.screenWidth-270, self.screenHeight))
            planet.build(i)
            self.planet_list.append(planet)
    
    def toggle_store(self):
        """Toggles the visibility of the store panel."""
        if not self.store_open:
            self.close_store()
        else:
            self._build()
    
    def close_store(self):
        """Closes and removes the planet store UI from the screen."""
        if self.centerPanel:
            self.centerPanel.kill()
            self.store_open = False

    def handle_event(self, event):
        if self.btn.process_event(event):
            self.close_store()