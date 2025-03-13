import pygame
import pygame_gui
import random, sys, math, time
from pygame_gui.ui_manager import UIManager
from pygame_gui.elements import UIPanel, UIButton, UILabel, UITextEntryLine, UIScrollingContainer, UIStatusBar
# hand made
from businessName_gen import BusinessName

screenWidth, screenHeight = 650, 645
current_time = time.time()
random.seed(current_time)

def format_number(num):
    """Formats large numbers with suffixes"""
    if num >= 1e6 and num < 1e9:
        return f"{num / 1e6:.2f} Mil"
    elif num >= 1e9 and num < 1e12:
        return f"{num / 1e9:.2f} Bil"
    elif num >= 1e12 and num < 1e15:
        return f"{num / 1e12:.2f} Tri"
    elif num >= 1e15 and num < 1e18:
        return f"{num / 1e15:.2f} Qua"
    elif num >= 1e18 and num < 1e21:
        return f"{num / 1e18:.2f} Qui"
    elif num >= 1e21 and num < 1e24:
        return f"{num / 1e21:.2f} Sex"
    elif num >= 1e24:
        return f"{num / 1e24:.2f} Sep"
    elif num >= 1000:
        return f"{num:,.2f}"  # Add commas for thousands
    else:
        return f"{num:.2f}"

def format_time(num_time):
    if num_time > 60 and num_time < 3600:
        return f"{num_time / 1e6:.1f} Min"
    elif num_time > 3600 and num_time < 216000:
        return f"{num_time / 1e9:.1f} Hou"
    elif num_time > 216000 and num_time < 12960000:
        return f"{num_time / 1e12:.1f} Days"
    elif num_time > 12960000:
        return f"{num_time / 1e15:.1f} Years"
    else:
        return f"{num_time:.1f} Sec"
    
# business
class Business:
    def __init__(self, ui_manager, scroll_container):
        self.ui_manager = ui_manager
        self.scroll_container = scroll_container
        self.name = BusinessName()
        self.moneyPer = self._moneyPer_module()
        self.qualityCost, self.upgradeCost = self._get_cost()
        self.price_output_current = 0
        self.purchased = False
        self.btn_text = "Buy"
    
    def _weighted_random(self, min_val, max_val, weight=3):
        # Using base as random value raised to a power creates a weighted distribution
        base = random.random() ** weight
        weighted_value = min_val + (max_val - min_val) * base
        return max(min_val, min(weighted_value, max_val))
    
    def _moneyPer_module(self):
        self.money = self._weighted_random(100.00, sys.maxsize, 50)
        self.time_per = round(self._weighted_random(100.00, sys.maxsize, 25), 2)
        return f"${format_number(self.money)} per {format_time(self.time_per)}"
    
    def _get_cost(self):
        self.qualityCost = self._weighted_random(0.01, sys.maxsize, 50)
        self.upgradeCost = self._weighted_random(0.01, sys.maxsize, 50)
        return f"${format_number(self.qualityCost)}",f"${format_number(self.upgradeCost)}"
    
    def build(self, i):
        panel_width = screenWidth - 20
        panel_height = 50
        """Builds the UI panel for each business entry."""
        self.businessContainer = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((1, i * panel_height), (panel_width, panel_height)), manager=self.ui_manager, container=self.scroll_container)
        self.btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1, 1), (40, 40)), text=self.btn_text, manager=self.ui_manager, container=self.businessContainer)
        self.label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((40, 0), (len(self.name) * 9, 20)), text=self.name, manager=self.ui_manager, container=self.businessContainer)
        # Progress Bar for Revenue
        self.price_output = pygame_gui.elements.UIStatusBar(relative_rect=pygame.Rect((40, 20), (screenHeight-180, 20)), manager=self.ui_manager, container=self.businessContainer)
        self.price_output.percent_full = self.price_output_current
        self.labelPrice = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((screenHeight-350,0), (len(self.moneyPer) * 9, 20)), text=self.moneyPer, manager=self.ui_manager, container=self.businessContainer)
        self.quality_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((screenHeight-140, 1), (110, 20)), text=self.qualityCost, manager=self.ui_manager, container=self.businessContainer)
        self.upgrade_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((screenHeight-140, 23), (110, 20)), text=self.upgradeCost, manager=self.ui_manager, container=self.businessContainer)

    def update(self, time_delta):
        if self.purchased:
            """Updates the price_output progress bar based on time passed."""
            progress_rate = (time_delta / self.time_per) * 100
            self.price_output_current += progress_rate
            # Reset if it goes over 100%
            if self.price_output_current >= 1:
                self.purchased = False
                self.price_output_current = 0
                self.btn.set_text("Buy")

            self.price_output.percent_full = self.price_output_current
        
    def handle_event(self, event):
        global money
        if self.btn.process_event(event) and not self.purchased:
            self.purchased = True
            self.btn.set_text("Sold")
            money += self.money

class top_panel:
    def __init__(self, ui_manager):
        self.ui_manager = ui_manager
        self.topPanel = UIPanel(relative_rect=pygame.Rect((0, 0), (screenWidth, 100)), manager=self.ui_manager)
        # Business Name Input
        UILabel(relative_rect=pygame.Rect((10, 10), (125, 30)), text="Business Name: ", manager=ui_manager, container=self.topPanel)
        UILabel(relative_rect=pygame.Rect((screenWidth-125, 10), (125, 30)), text="Location: Earth", manager=ui_manager, container=self.topPanel)
        self.textBusiness_Name = UITextEntryLine(relative_rect=pygame.Rect((140, 10), (150, 30)), manager=ui_manager, container=self.topPanel)
        # panel btn
        self.displayMoney = UILabel(relative_rect=pygame.Rect((-80, 50), (300, 30)), text=f"Money: ${format_number(money)}", manager=ui_manager, container=self.topPanel)
            
        button_width, button_height = 110, 30
        button_spacing = 10
        start_x = (screenWidth - (button_width * 3 + button_spacing * 2)) // 2

        self.storageUnit = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((start_x, 50), (100, 30)), text="Storage Unit", manager=ui_manager, container=self.topPanel)
        self.rocketStore = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((start_x + button_width + button_spacing, 50), (button_width, button_height)), text="Rocket Store", manager=ui_manager, container=self.topPanel)
        self.universeMap = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((start_x * 2 + (button_width + button_spacing), 50), (button_width, button_height)), text="Universe Map", manager=ui_manager, container=self.topPanel)
        
    def update(self):
        self.displayMoney.set_text(f"Money: ${format_number(money)}")

# app
money = 0
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
        self.businesses = []
        self.top = top_panel(self.ui_manager)
        self._center_panel()

    def _center_panel(self):
        # scroll frame
        self.scroll_container = pygame_gui.elements.UIScrollingContainer(relative_rect=pygame.Rect((0, 100), (screenWidth, screenHeight-100)), manager=self.ui_manager)
        content_height = (50 * 100) + 1
        self.scroll_container.set_scrollable_area_dimensions((screenWidth - 20, content_height))

        for i in range(100):
            business = Business(self.ui_manager, self.scroll_container)
            business.build(i)
            self.businesses.append(business)

    def run(self):
        while self.running:
            time_delta = self.clock.tick(64) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()
                self.ui_manager.process_events(event)

                for business in self.businesses:
                    business.handle_event(event)
            # Draw elements
            self.ui_manager.update(time_delta)
            self.screen.blit(self.background_surface, (0, 0))
            self.ui_manager.draw_ui(self.screen)

            for business in self.businesses:
                business.update(time_delta)

            self.top.update()
            # update
            self.clock.tick(64)
            pygame.display.flip()
            pygame.display.update()

if __name__ == "__main__":
    app = App()
    app.run()