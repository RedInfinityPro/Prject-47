from container.imports_library import *
from business_name_gen import BusinessName
import secrets

# format number
def format_number(num):
    """Formats large numbers with suffixes"""
    if num >= 1e6:
        suffixes = ['Mil', 'Bil', 'Tri', 'Qua', 'Qui', 'Sex', 'Sep']
        index = int(math.log10(num) // 3 - 2)
        return f"{num / 10**(6 + index * 3):.2f} {suffixes[index]}" if index < len(suffixes) else f"{num:.2e}"
    return f"{num:,.2f}"

# generate key
def generate_secure_key(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    key = ''.join(secrets.choice(alphabet) for _ in range(length))
    return key

# Rocket Content
class RocketContent:
    def __init__(self, ui_manager, scroll_container, screenSize):
        self.ui_manager = ui_manager
        self.scroll_container = scroll_container
        self.screenWidth, self.screenHeight = screenSize
        self.name = f"Rocket Name: {GenerateName()}"
        self.key = generate_secure_key(12)
        self.cost = self._weighted_random(1000, sys.maxsize, 50)
        self.fuelUse = self._weighted_random(50, 5000, 10)
        self.distance = self._weighted_random(1000, sys.maxsize, 10)
        self.upKeep = self._weighted_random(0.01, 50000, 20)
        self.storage = self._weighted_random(1, 50000, 20)
        self.availablePurchase = "Available"

    def _weighted_random(self, min_val, max_val, weight=3):
        # Using base as random value raised to a power creates a weighted distribution
        base = random.random() ** weight
        weighted_value = min_val + (max_val - min_val) * base
        return max(min_val, min(weighted_value, max_val))
    
    def build(self, i):
        panel_width = 200
        panel_height = 200
        """Builds the UI panel for each business entry."""
        self.rocketContainer = UIPanel(relative_rect=pygame.Rect((i * (panel_width + 1), 3), (panel_width, panel_height)), manager=self.ui_manager, container=self.scroll_container)
        self.name_label = UILabel(relative_rect=pygame.Rect((0, 0), (180, 20)), text=self.name, manager=self.ui_manager, container=self.rocketContainer)
        self.key_label = UILabel(relative_rect=pygame.Rect((0, 20), (180, 20)), text=f"Key: {self.key}", manager=self.ui_manager, container=self.rocketContainer)
        
        self.cost_label = UILabel(relative_rect=pygame.Rect((0, 115), (180, 20)), text=f"Cost: {format_number(self.cost)}", manager=self.ui_manager, container=self.rocketContainer)
        self.fuel_label = UILabel(relative_rect=pygame.Rect((0, 130), (180, 20)), text=f"Fuel: {format_number(self.fuelUse)}", manager=self.ui_manager, container=self.rocketContainer)
        self.distance_label = UILabel(relative_rect=pygame.Rect((0, 145), (180, 20)), text=f"Distance: {format_number(self.distance)}", manager=self.ui_manager, container=self.rocketContainer)
        self.upKeep_label = UILabel(relative_rect=pygame.Rect((0, 160), (180, 20)), text=f"Upkeep: {format_number(self.upKeep)}", manager=self.ui_manager, container=self.rocketContainer)
        self.storage_label = UILabel(relative_rect=pygame.Rect((0, 175), (180, 20)), text=f"Storage: {format_number(self.storage)}", manager=self.ui_manager, container=self.rocketContainer)
        
        # btn
        self.rocket_image = UIButton(relative_rect=pygame.Rect((60, 40), (70, 70)), text=f"{self.availablePurchase}", manager=self.ui_manager, container=self.rocketContainer)

# Rocket Upgrade
class RocketUpgrade:
    def __init__(self, ui_manager, scroll_container, screenSize):
        self.ui_manager = ui_manager
        self.scroll_container = scroll_container
        self.screenWidth, self.screenHeight = screenSize
        self.name = f"Rocket Upgrade: {GenerateName()}"
        self.key = generate_secure_key(12)
        self.cost = self._weighted_random(1000, sys.maxsize, 50)
        self.details_1 = random.choice(["Fuel Upgrade","Storage Upgrade","Upkeep Upgrade","Sold Cost Upgrade","Distance Upgrade"])
        self.details_2 = random.choice(["Fuel Upgrade","Storage Upgrade","Upkeep Upgrade","Sold Cost Upgrade","Distance Upgrade"])
        self.details_3 = random.choice(["Fuel Upgrade","Storage Upgrade","Upkeep Upgrade","Sold Cost Upgrade","Distance Upgrade"])
        self.availablePurchase = "Available"

    def _weighted_random(self, min_val, max_val, weight=3):
        # Using base as random value raised to a power creates a weighted distribution
        base = random.random() ** weight
        weighted_value = min_val + (max_val - min_val) * base
        return max(min_val, min(weighted_value, max_val))
    
    def build(self, i):
        panel_width = 200
        panel_height = 200
        """Builds the UI panel for each business entry."""
        self.rocketUpgrade_Container = UIPanel(relative_rect=pygame.Rect((i * (panel_width + 1), 3), (panel_width, panel_height)), manager=self.ui_manager, container=self.scroll_container)
        self.name_label = UILabel(relative_rect=pygame.Rect((0, 0), (180, 20)), text=self.name, manager=self.ui_manager, container=self.rocketUpgrade_Container)
        self.key_label = UILabel(relative_rect=pygame.Rect((0, 20), (180, 20)), text=f"Key: {self.key}", manager=self.ui_manager, container=self.rocketUpgrade_Container)
        
        self.cost_label = UILabel(relative_rect=pygame.Rect((0, 130), (180, 20)), text=f"Cost: {format_number(self.cost)}", manager=self.ui_manager, container=self.rocketUpgrade_Container)
        self.details_label_1 = UILabel(relative_rect=pygame.Rect((0, 145), (180, 20)), text=f"Details: {self.details_1}", manager=self.ui_manager, container=self.rocketUpgrade_Container)
        self.details_label_2 = UILabel(relative_rect=pygame.Rect((0, 160), (180, 20)), text=f"Details: {self.details_2}", manager=self.ui_manager, container=self.rocketUpgrade_Container)
        self.details_label_3 = UILabel(relative_rect=pygame.Rect((0, 175), (180, 20)), text=f"Details: {self.details_3}", manager=self.ui_manager, container=self.rocketUpgrade_Container)
        
        # btn
        self.rocket_upgrade_image = UIButton(relative_rect=pygame.Rect((60, 45), (70, 70)), text=f"{self.availablePurchase}", manager=self.ui_manager, container=self.rocketUpgrade_Container)
         
# Planet Store
class RocketStore:
    def __init__(self, ui_manager, screenSize):
        self.ui_manager = ui_manager
        self.screenWidth, self.screenHeight = screenSize
        self.x, self.y = 240, 100
        self.rocket_list = []
        self.rocket_upgrade_list = []
        self.store_open = True
        self._build()

    def _build(self):
        self.centerPanel = UIPanel(relative_rect=pygame.Rect((self.x, self.y), (self.screenWidth-250, self.screenHeight-160)), manager=self.ui_manager, starting_height=1)
        # labels
        UILabel(relative_rect=pygame.Rect((self.screenWidth/2-160, 10), (160, 30)), text="Rocket Store: ", manager=self.ui_manager, container=self.centerPanel)
        self.btn = UIButton(relative_rect=pygame.Rect((self.screenWidth-290, 2), (30, 30)), text=f"X", manager=self.ui_manager, container=self.centerPanel)
        # buttons
        self.scroll_container_rockets = pygame_gui.elements.UIScrollingContainer(relative_rect=pygame.Rect((0, 40), (self.screenWidth-255, 220)), manager=self.ui_manager, container=self.centerPanel)
        content_width = (90 * 220) + 320
        self.scroll_container_rockets.set_scrollable_area_dimensions((content_width, 200))

        for i in range(100):
            rocket = RocketContent(self.ui_manager, self.scroll_container_rockets, (self.screenWidth-270, self.screenHeight))
            rocket.build(i)
            self.rocket_list.append(rocket)
        
        UILabel(relative_rect=pygame.Rect((self.screenWidth/2-160, 270), (160, 30)), text="Upgrade Store: ", manager=self.ui_manager, container=self.centerPanel)
        # buttons 2
        self.scroll_container_upgrades = pygame_gui.elements.UIScrollingContainer(relative_rect=pygame.Rect((0, 300), (self.screenWidth-255, 220)), manager=self.ui_manager, container=self.centerPanel)
        content_width = (90 * 220) + 320
        self.scroll_container_upgrades.set_scrollable_area_dimensions((content_width, 200))

        for i in range(100):
            upgrades = RocketUpgrade(self.ui_manager, self.scroll_container_upgrades, (self.screenWidth-270, self.screenHeight))
            upgrades.build(i)
            self.rocket_upgrade_list.append(upgrades)
    
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