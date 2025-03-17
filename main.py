from container.imports_library import *
from generators.elements import *
from main_display import TopPanel, DetailsPanel, BottomPanel
from planet_store import PlanetStore
from rocket_store import RocketStore
# window
screenWidth, screenHeight = 1280, 720
current_time = time.time()
random.seed(current_time)
start_time = time.time()
increment_number = 1

# save and load content
def load_content():
    try:
        if not os.path.exists(r'save_files\file.pkl') or os.path.getsize(r'save_files\file.pkl') == 0:
            return 0, time.time()  # Return defaults if file doesn't exist or is empty
        with open(r'save_files\file.pkl', 'rb') as file:
            content = pickle.load(file)
            return content  # Expecting a tuple (saved_count, last_time)
    except (FileNotFoundError, EOFError, ValueError):
        return 0, time.time()  # Return safe default values

def save_content(content):
    with open(r'save_files\file.pkl', 'wb') as file: 
        pickle.dump(content, file) 

# app
class App(threading.Thread):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)
        pygame.display.set_caption("Game")
        self.clock = pygame.time.Clock()
        self.running = True
        # save data
        self.count, last_time = load_content()
        elapsed_time = time.time() - last_time
        self.count += int(elapsed_time // increment_number)
        # ui_manager
        self.background_surface = pygame.Surface((screenWidth, screenHeight)).convert()
        self.ui_manager = UIManager((screenWidth, screenHeight))
        # Main display -->
        self.top_panel = TopPanel(self.ui_manager, (screenWidth, screenHeight))
        self.details_panel = DetailsPanel(self.ui_manager)
        self.bottom_panel = BottomPanel(self.ui_manager, (screenWidth, screenHeight))
        # planet display
        self.planet_panel = PlanetStore(self.ui_manager, (screenWidth, screenHeight))
        # rocket display
        self.rocket_panel = RocketStore(self.ui_manager, (screenWidth, screenHeight))
       
    def run(self):
        last_update = time.time()
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
            
            # update numbers
            if time.time() - last_update >= increment_number:
                self.count += 1
                last_update = time.time()
                save_content(content=[self.count, last_update])
                #print(f"Current number: {self.count}")

            # update
            self.top_panel.update(start_time)
            self.details_panel.update()
            self.clock.tick(64)
            pygame.display.flip()
            pygame.display.update()

# run
if __name__ == "__main__":
    app = App()
    app.run()