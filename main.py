from puzzle import Puzzle
import pygame
import pygame_gui
import time

screen_size = (1280, 720)



Text=(255,255,255)
# Color Palette
    # https://www.canva.com/colors/color-palettes/speckled-eggs/
pygame.init()

puzzle = Puzzle("","","",0,0,"left", [])
puzzle.initialize()


pygame.display.set_caption('8 Puzzle')
window_surface = pygame.display.set_mode(screen_size)

background = pygame.Surface(screen_size)
background.fill(pygame.Color('#0F0F0F'))

manager = pygame_gui.UIManager(screen_size, 'theme.json')

pygame_gui.core.IWindowInterface.set_display_title(self=window_surface,new_title="8-Puzzle")



# 
pygame_gui.elements.ui_label.UILabel(manager=manager,
                                     text="8-Puzzle Game",
                                     object_id="#title-game", # (pos-width,pos-height),(width,height)
                                     relative_rect=pygame.Rect((540, 10), (175, 70))
                                     )



button_layout_rect = pygame.Rect((1000, 600), (250, 30))
shuffle_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                             text='Shuffle',
                                             object_id="shuffle-btn",
                                             manager=manager)


dropdown_layout_rect = pygame.Rect((1000, 300), (250, 35))

algorithmOptions = ["A*","Best First", "Branch and Bound"]
algorithmDropDown = pygame_gui.elements.UIDropDownMenu(options_list=algorithmOptions,
                                                       starting_option=algorithmOptions[0],
                                                       relative_rect=dropdown_layout_rect,
                                                       object_id="#algorithm-dropdown",
                                                       manager=manager)

pygame_gui.elements.ui_label.UILabel(parent_element=algorithmDropDown,
                                     manager=manager,
                                     text="Heuristic Search:", # (pos-width,pos-height),(width,height)
                                     relative_rect=pygame.Rect((835, 300), (150, 30)))


# message_html = "<b>Digite o estado inicial: </b>"

# 1,2,4,5,8,7,6,0
report_rect = pygame.Rect((1000, 200), (250, 40))
initial_state = pygame_gui.elements.UITextEntryLine(relative_rect=report_rect,
                                                    manager=manager,
                                                    object_id="#input-state")



pygame_gui.elements.ui_label.UILabel(parent_element=initial_state,
                                     manager=manager,
                                     text="Initial State:", # (pos-width,pos-height),(width,height)
                                     relative_rect=pygame.Rect((855, 200), (140, 30)))

# Colocar apos a execução de um algoritmo
    #report_rect = pygame.Rect((200, 150), (250, 35))
    # report_window = pygame_gui.windows.UIConfirmationDialog(rect=report_rect,
    #                                                         manager=manager,
    #                                                         object_id="#report-window",
    #                                                         blocking=False,
    #                                                         window_title="Relatório",
    #                                                         action_short_name="Okay",
    #                                                         action_long_desc="Nós visitados: 62           Tempo Gasto: 12.00           Tamanho do caminho:32")

#report_window.process_event()
    # message_html = "<b>Um texto here!!!</b>"
    # message_window = pygame_gui.windows.UIMessageWindow(rect=report_rect,
    #                                                     manager=manager,
    #                                                     window_title="Relatório",
    #                                                     html_message=message_html)

BASICFONT = pygame.font.Font('FiraCode-Retina.ttf',50)

for block in puzzle.blocks:        
    pygame.draw.rect(window_surface, block['color'], block['rect'])
    textSurf = BASICFONT.render(block['block'], True, Text)
    textRect = textSurf.get_rect()
    textRect.center = block['rect'].left+50,block['rect'].top+50
    window_surface.blit(textSurf, textRect)
#time.sleep(30)
pygame.display.update()
clock = pygame.time.Clock()
is_running = True
time.sleep(5)

# while is_running:
#     time_delta = clock.tick(60)/1000.0
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             is_running = False
            
#         if event.type == pygame.USEREVENT:
#             if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
#                 if event.ui_element == shuffle_button:
#                     if initial_state.get_text() != "":
#                         print('Bora laaa')
#             if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
#                 if event.ui_element == algorithmDropDown:
#                     print("Selecionado: ",event.text)
#         manager.process_events(event)
        
#     manager.update(time_delta)
#     window_surface.blit(background, (0, 0))
#     manager.draw_ui(window_surface)

#     pygame.display.update()
