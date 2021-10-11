from puzzle import Puzzle
import pygame
import pygame_gui
import time
import colors

SCREEN_SIZE = (1280, 720)

#Setup
pygame.init()
BASICFONT = pygame.font.Font('FiraCode-Retina.ttf',50)

pygame.display.set_caption('teste')
window_surface = pygame.display.set_mode(SCREEN_SIZE)
background = pygame.Surface(SCREEN_SIZE)
background.fill(pygame.Color(colors.BABY_BLUE))
manager = pygame_gui.UIManager(SCREEN_SIZE, 'theme.json')

pygame_gui.core.IWindowInterface.set_display_title(self=window_surface,new_title="8-Puzzle")


#Elements
### title label
pygame_gui.elements.ui_label.UILabel(manager=manager,
                                     text="8-Puzzle Game",
                                     object_id="#title-game", # (pos-width,pos-height),(width,height)
                                     relative_rect=pygame.Rect((540, 10), (175, 70))
                                     )

### shuffle button
button_layout_rect = pygame.Rect((1000, 260), (250, 30))
shuffle_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                             text='Shuffle',
                                             object_id="shuffle-btn",
                                             manager=manager)

### set with initial state button
set_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1000, 230), (250, 30)),
                                             text='Set Puzzle',
                                             object_id="set-btn",
                                             manager=manager)

### algorithmOptions DropDown
dropdown_layout_rect = pygame.Rect((1000, 600), (250, 35))
algorithmOptions = ["A*","Best First"]
algorithmDropDown = pygame_gui.elements.UIDropDownMenu(options_list=algorithmOptions,
                                                       starting_option=algorithmOptions[1],
                                                       relative_rect=dropdown_layout_rect,
                                                       object_id="#algorithm-dropdown",
                                                       manager=manager)
### solve button
solve_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1000, 640), (250, 30)),
                                             text='Solve Puzzle',
                                             object_id="solve-btn",
                                             manager=manager)

### Search label
pygame_gui.elements.ui_label.UILabel(parent_element=algorithmDropDown,
                                     manager=manager,
                                     text="Heuristic Search:", # (pos-width,pos-height),(width,height)
                                     relative_rect=pygame.Rect((835, 600), (150, 30)))

### initial state input
    # message_html = "<b>Digite o estado inicial: </b>"
    # 1,2,4,5,8,7,6,0
report_rect = pygame.Rect((1000, 200), (250, 40))
initial_state = pygame_gui.elements.UITextEntryLine(relative_rect=report_rect,
                                                    manager=manager,
                                                    object_id="#input-state")

### initial state label
pygame_gui.elements.ui_label.UILabel(parent_element=initial_state,
                                     manager=manager,
                                     text="Initial State:", # (pos-width,pos-height),(width,height)
                                     relative_rect=pygame.Rect((855, 200), (140, 30)))

### alert label
alert_label = pygame_gui.elements.ui_label.UILabel(
                                     manager=manager,
                                     text="",
                                     relative_rect=pygame.Rect((970, 150), (200, 30)))

def draw_blocks(blocks):
    for block in blocks:
        if block['block'] != 0:
            pygame.draw.rect(window_surface, colors.BLUE_GROTTO, block['rect'])
            textSurf = BASICFONT.render(str(block['block']), True, colors.NAVY_BLUE)
            textRect = textSurf.get_rect()
            textRect.center = block['rect'].left+50,block['rect'].top+50
            window_surface.blit(textSurf, textRect)
        else:
            pygame.draw.rect(window_surface, colors.ROYAL_BLUE, block['rect'])

window_surface.blit(background, (0, 0))
pygame.display.update()
clock = pygame.time.Clock()
puzzle = Puzzle.new(250, 220, 330, 330)
puzzle.initialize()
algorithm = "Best First"
is_running = True
while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == shuffle_button:
                    puzzle.randomBlocks()
                elif event.ui_element == set_button:
                    if not puzzle.setBlocks(initial_state.get_text()):
                        alert_label.set_text("puzzle text invalid!")
                    else:
                        alert_label.set_text("")
                elif event.ui_element == solve_button:
                    if algorithm == "Best First":   
                        alert_label.set_text(str(puzzle.bestFirst()))
            elif event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == algorithmDropDown:
                    algorithm = event.text
            elif event.user_type == pygame_gui.UI_TEXT_ENTRY_CHANGED and event.ui_element == initial_state:
                print("")
        manager.process_events(event)
        
        
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    draw_blocks(puzzle.blocks)
    pygame.display.update()
