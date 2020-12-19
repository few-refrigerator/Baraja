from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.carousel import Carousel
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from kivy.uix.behaviors import ButtonBehavior
from kivy.clock import Clock
from kivy.core.window import Window
import random

# Window.size = (280, 540)


# FUNCTIONS FOR COLOR CODES

def color_1r(r1):
    red_color = r1 / 255
    return float(red_color)


def color_2g(g1):
    green_color = g1 / 255
    return float(green_color)


def color_3b(b1):
    blue_color = b1 / 255
    return float(blue_color)


class CardDeck:
    def __init__(self):
        self.card_list = ['El gallo', 'El diablito', 'La dama', 'El catrín', 'El paraguas', 'La sirena', 'La escalera',
                          'La botella', 'El barril', 'El árbol', 'El melón', 'El valiente', 'El gorrito', 'La muerte',
                          'La pera', 'La bandera', 'El bandolón', 'El violoncello', 'La garza', 'El pájaro', 'La mano',
                          'La bota', 'La luna', 'El cotorro', 'El borracho', 'El negrito', 'El corazón', 'La sandía',
                          'El tambor', 'El camarón', 'Las jaras', 'El músico', 'La araña', 'El soldado', 'La estrella',
                          'El cazo', 'El mundo', 'El apache', 'El nopal', 'El alacrán', 'La rosa', 'La calavera',
                          'La campana', 'El cantarito', 'El venado', 'El sol', 'La corona', 'La chalupa', 'El pino',
                          'El pescado', 'La palma', 'La maceta', 'El arpa', 'La rana']
        self.card_img = {'El gallo': "gallo10.jpg", 'El diablito': "diablito.jpg", 'La dama': "dama.jpg",
                         'El catrín': "catrin.jpg", 'El paraguas': "paraguas.jpg", 'La sirena': "sirena.jpg",
                         'La escalera': "escalera.jpg", 'La botella': "botella.jpg", 'El barril': "barril.jpg",
                         'El árbol': "arbol.jpg", 'El melón': "melon.jpg", 'El valiente': "valiente.jpg",
                         'El gorrito': "gorrito.jpg", 'La muerte': "muerte.jpg", 'La pera': "pera.jpg",
                         'La bandera': "bandera.jpg", 'El bandolón': "bandolon.jpg",
                         'El violoncello': "violoncello.jpg", 'La garza': "garza.jpg", 'El pájaro': "pajaro.jpg",
                         'La mano': "mano.jpg", 'La bota': "bota.jpg", 'La luna': "luna.jpg",
                         'El cotorro': "cotorro.jpg", 'El borracho': "borracho.jpg", 'El negrito': "negrito.jpg",
                         'El corazón': "corazon.jpg", 'La sandía': "sandia.jpg", 'El tambor': "tambor.jpg",
                         'El camarón': "camaron.jpg", 'Las jaras': "jaras.jpg", 'El músico': "musico.jpg",
                         'La araña': "arana.jpg", 'El soldado': "soldado.jpg", 'La estrella': "estrella.jpg",
                         'El cazo': "cazo.jpg", 'El mundo': "mundo.jpg", 'El apache': "apache.jpg",
                         'El nopal': "nopal.jpg", 'El alacrán': "alacran.jpg", 'La rosa': "rosa.jpg",
                         'La calavera': "calavera.jpg", 'La campana': "campana.jpg", 'El cantarito': "cantarito.jpg",
                         'El venado': "venado.jpg", 'El sol': "sol.jpg", 'La corona': "corona.jpg",
                         'La chalupa': "chalupa.jpg", 'El pino': "pino.jpg", 'El pescado': "pescado.jpg",
                         'La palma': "palma.jpg", 'La maceta': "maceta.jpg", 'El arpa': "arpa.jpg",
                         'La rana': "rana.jpg"}
        self.drawn_cards = []
        self.reverse_list = []


class MainWindow(Screen):
    global secs_selected
    global main_timer

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.game_variable = CardDeck()
        self.start_btn_click = 0

        self.layout = FloatLayout()

        # BACKGROUND IMAGE
        self.background_img = Image(source='background_2.jpg', allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(self.background_img)

        # MAIN IMAGE BEFORE GAME STARTS
        self.main_img = Image(source='maybe_front10.png', size_hint=(0.4, 0.4), pos_hint={'x': 0.3, 'y': 0.3},
                              allow_stretch=True, keep_ratio=False)
        # self.main_img.texture.mag_filter = 'nearest'
        # self.main_img.texture.min_filter = 'nearest'
        self.layout.add_widget(self.main_img)

        # SIDE IMAGES
        self.side_img1 = ""
        self.side_img2 = ""
        self.side_img3 = ""

        # START DRAWING CARDS BUTTON
        self.start_button = Button(text="", background_color=(0, 0, 0, 0), background_normal='',
                                   size_hint=(.4, .05), pos_hint={'x': 0.3, 'y': 0.8},
                                   on_press=self.callback_shuffle)
        self.start_button.bind(on_press=self.callback_start)
        self.layout.add_widget(self.start_button)
        self.start_btn_img = Image(source='Untitled11.png', size_hint=(.4, .05), pos_hint={'x': 0.3, 'y': 0.8},
                                   allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(self.start_btn_img)
        self.start_btn_lab = Label(text="START", font_size="15sp", color=(0, 0, 0, 1), bold=True,
                                   size_hint=(.4, .05), pos_hint={'x': 0.3, 'y': 0.8})
        self.layout.add_widget(self.start_btn_lab)

        # SHUFFLE DECK BUTTON
        self.shuffle_button = Button(text="", size_hint=(.1, .1), pos_hint={'x': 0.85, 'y': 0.75},
                                     background_color=(0, 0, 0, 0), background_normal='')
        self.shuffle_button.bind(on_press=self.callback_shuffle)
        self.layout.add_widget(self.shuffle_button)
        self.shuffle_icon = Image(source='shuffle_icon6.png', size_hint=(.1, .1), pos_hint={'x': 0.85, 'y': 0.75},
                                  allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(self.shuffle_icon)

        # RESTART BUTTON
        self.restart_button = Button(text="", size_hint=(.1, .1), pos_hint={'x': 0.05, 'y': 0.75},
                                     background_color=(0, 0, 0, 0), background_normal='')
        self.restart_button.bind(on_press=self.callback_restart)
        self.layout.add_widget(self.restart_button)
        self.restart_icon = Image(source='refresh6.png', size_hint=(.1, .1), pos_hint={'x': 0.05, 'y': 0.75},
                                  allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(self.restart_icon)

        # NUMBER OF CARDS REMAINING ON DECK
        self.num_remain_img = Image(source='empty_circle6.png', size_hint=(.1, .1), pos_hint={'x': 0.85, 'y': 0.3},
                                    allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(self.num_remain_img)
        self.num_remain_lab = Label(text="54", bold=True, color=(0, 0, 0, 1),
                                    size_hint=(.1, .1), pos_hint={'x': 0.85, 'y': 0.3})
        self.layout.add_widget(self.num_remain_lab)

        # CARDS DRAWN HISTORY BUTTON
        self.card_history = Button(text="", size_hint=(.3, .1), pos_hint={'x': 0.35, 'y': 0.05},
                                   background_color=(0, 0, 0, 0),
                                   background_normal='',
                                   on_release=self.callback_history)
        self.layout.add_widget(self.card_history)

        # TIMER POPUP BUTTON
        self.timer_btn = Button(text="", size_hint=(.1, .1), pos_hint={'x': 0.05, 'y': 0.3},
                                background_color=(0, 0, 0, 0), background_normal='')
        self.timer_btn.bind(on_press=timer_popup)
        self.layout.add_widget(self.timer_btn)
        self.timer_icon = Image(source='clock6.png', size_hint=(.1, .1), pos_hint={'x': 0.05, 'y': 0.3},
                                allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(self.timer_icon)

        # RETURN TO MAIN SCREEN BUTTON
        self.return_button = Button(text="", size_hint=(.1, .1), pos_hint={'x': 0.05, 'y': 0.85},
                                    background_color=(0, 0, 0, 0), background_normal='',
                                    on_press=self.callback_return)
        # LAYOUT ADDED TO SCREEN
        self.add_widget(self.layout)

    def callback_return(self, event):
        sm.current = 'main'

    def callback_history(self, event):
        carousel = Carousel(direction='right')
        try:
            for num_slide in range(len(self.game_variable.reverse_list)):
                src = self.game_variable.card_img.get(self.game_variable.reverse_list[num_slide])
                img = Image(source=src, size_hint=(0.4, 0.4), pos_hint={'x': 0.3, 'y': 0.3},
                            allow_stretch=True, keep_ratio=False)
                carousel.add_widget(img)
        except IndexError:
            pass
        self.manager.get_screen('history').clear_widgets()
        self.manager.get_screen('history').add_widget(CardHistoryWindow().background_img)
        self.manager.get_screen('history').add_widget(carousel)
        self.manager.get_screen('history').add_widget(self.return_button)
        self.manager.get_screen('history').add_widget(CardHistoryWindow().back_icon)
        sm.current = 'history'

    def callback_restart(self, event):
        self.game_variable = CardDeck()
        self.start_btn_lab.text = "START"
        self.num_remain_lab.text = str(len(self.game_variable.card_list))
        self.layout.remove_widget(self.main_img)
        self.main_img = Image(source='maybe_front10.png', size_hint=(0.4, 0.4), pos_hint={'x': 0.3, 'y': 0.3},
                              allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(self.main_img)
        Clock.unschedule(self.game_starts)
        self.start_btn_click = 0
        self.update_side_img()

    def callback_shuffle(self, event):
        random.shuffle(self.game_variable.card_list)

    def callback_start(self, event):
        self.start_btn_click += 1

        # CONTINUES DRAWING CARDS
        if self.start_btn_click % 2 != 0:
            Clock.schedule_interval(self.game_starts, int(secs_selected))
            self.start_btn_lab.text = "PAUSE"
        # PAUSES
        elif self.start_btn_click % 2 == 0:
            Clock.unschedule(self.game_starts)
            self.start_btn_lab.text = "CONTINUE"

    def game_starts(self, dt):
        self.layout.remove_widget(self.main_img)
        self.update_side_img()
        try:
            card = self.game_variable.card_list.pop()
            if card in self.game_variable.card_img:
                self.main_img = Image(source=self.game_variable.card_img.get(card),
                                      size_hint=(0.4, 0.4), pos_hint={'x': 0.3, 'y': 0.3},
                                      allow_stretch=True, keep_ratio=False)
                self.layout.add_widget(self.main_img)
            self.game_variable.drawn_cards.append(card)
            self.num_remain_lab.text = str(len(self.game_variable.card_list))
        except IndexError:
            Clock.unschedule(self.game_starts)

    def update_side_img(self):
        try:
            self.layout.remove_widget(self.side_img1)
            self.layout.remove_widget(self.side_img2)
            self.layout.remove_widget(self.side_img3)
        except AttributeError:
            pass

        self.game_variable.reverse_list = self.game_variable.drawn_cards[::-1]

        try:
            self.side_img1 = Image(source=self.game_variable.card_img.get(self.game_variable.reverse_list[0]),
                                   size_hint=(0.1, 0.1), pos_hint={'x': 0.35, 'y': 0.05},
                                   allow_stretch=True, keep_ratio=False)
            self.layout.add_widget(self.side_img1)

            self.side_img2 = Image(source=self.game_variable.card_img.get(self.game_variable.reverse_list[1]),
                                   size_hint=(0.1, 0.1), pos_hint={'x': 0.45, 'y': 0.05},
                                   allow_stretch=True, keep_ratio=False)
            self.layout.add_widget(self.side_img2)

            self.side_img3 = Image(source=self.game_variable.card_img.get(self.game_variable.reverse_list[2]),
                                   size_hint=(0.1, 0.1), pos_hint={'x': 0.55, 'y': 0.05},
                                   allow_stretch=True, keep_ratio=False)
            self.layout.add_widget(self.side_img3)
        except IndexError:
            pass


class CardHistoryWindow(Screen):
    def __init__(self, **kwargs):
        super(CardHistoryWindow, self).__init__(**kwargs)

        # BACKGROUND IMAGE
        self.background_img = Image(source='background_2.jpg', allow_stretch=True, keep_ratio=False)

        # BACK ICON
        self.back_icon = Image(source='back_icon6.png', size_hint=(.1, .1), pos_hint={'x': 0.05, 'y': 0.85},
                               allow_stretch=True, keep_ratio=False)


main_timer = ""
secs_selected = 8


def timer_popup(event):
    global secs_selected
    global main_timer
    layout = FloatLayout()

    # DROPDOWN MENU TO SELECT TIMER
    dropdown = DropDown()
    secs_available = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    for i in secs_available:
        timer_button = Button(text=f'{i}', size_hint_y=None, height=30, on_release=update_sec_select)
        timer_button.bind(on_release=lambda timer_button: dropdown.select(timer_button.text))
        dropdown.add_widget(timer_button)

    main_timer = Button(text=f'Time: {secs_selected}s', font_size="14sp", color=(1, 1, 1, 1), bold=True,
                        size_hint=(.5, .1), pos_hint={'x': 0.25, 'y': 0.9})
    main_timer.bind(on_release=dropdown.open)
    dropdown.bind(on_select=lambda instance, x: setattr(main_timer, 'text', f'Time: {x}s'))
    layout.add_widget(main_timer)

    popup = Popup(title='Select seconds', content=layout, size_hint=(0.8, 0.8))
    dropdown.bind(on_select=popup.dismiss)

    popup.open()


def update_sec_select(event):
    global secs_selected
    global main_timer
    secs_available = ['2', '4', '6', '8', '0']

    try:
        if main_timer.text[7] in secs_available:
            secs_selected = main_timer.text[6:8]
        else:
            secs_selected = main_timer.text[6]
    except AttributeError:
        pass


sm = ScreenManager()
screens = [MainWindow(name='main'), CardHistoryWindow(name='history')]
for screen in screens:
    sm.add_widget(screen)


class Loteria(App):
    def build(self):
        return sm


if __name__ == "__main__":
    Loteria().run()
