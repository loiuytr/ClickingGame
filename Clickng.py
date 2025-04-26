from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from random import randint
from kivy.clock import Clock
import json
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.core.window import Window





class EnemyImage(ButtonBehavior, Image):
    pass

class MiniGameImage(ButtonBehavior, Image):
    pass

Upgrade = False
Upgrade_1 = False
Upgrade_2 = False
Upgrade_3 = False
Upgrade_4 = False
Upgrade_5 = False
Upgrade_6 = False
Upgrade_7 = False
Upgrade_8 = False
Upgrade_9 = False

strart_minigame = False

PassiveIncome = False
PassiveIncomeForCoins = False
PassiveIncomeForCoins_2 = False
PassiveIncomeForCoins_3 = False
Update_Fon = False
Update_House = False
Update_Button = False
clicks = 0
need_caught_mouse = 0
Add_monster = False
enemy_running =  False
minigame_open = False

def saved_data():
    with open('clickis_data.json', 'w') as json_file:
        json.dump({'clicks': clicks}, json_file)
       


def load_data():
    global clicks
    try:
        with open('clickis_data.json', 'r') as json_file:
            data = json.load(json_file)
            clicks = data.get('clicks', 0)
    except FileNotFoundError:
        clicks = 0 

press_time = 0

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        self.enemy_is_animating = False
        global minigame_open
        if minigame_open == False:
            Clock.schedule_interval(self.enemy_damage, 1)
            Clock.schedule_interval(self.animated_enemy, 40)
        if minigame_open:
            Clock.unschedule(self.animated_enemy)
            Clock.unschedule(self.animated_enemy_1)
        global Add_monster
        Clock.schedule_interval(self.enemy_damage_for_other, 1)
        Clock.schedule_interval(self.enabled_button, 30)

        load_data()
        





        self.img = Image(
            source='BackgroudForGame.png',
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        self.img_dog  = Image(
            source = 'dogkoin.png',
            size_hint = (None,None),
            size=(150,150),
            pos = (-30,-30),
            opacity=0,
            
            
        )

        self.btn_task = Button(
            text = 'Tasks',
            size_hint=(None, None),
            size=(170, 50),
            pos_hint={'center_x': 0.4, 'center_y': .9},
            
        )

        self.img_for_enemy = EnemyImage(
            source = 'enemyForGame.png',
            size_hint = (None,None),
            size=(80,70),
            pos = (30,100),
            opacity=0
            
        )

        self.img_for_enemy_1 = EnemyImage(
            source = 'EnemyForGame_1.png',
            size_hint = (None,None),
            size=(80,70),
            pos = (730,100),
            opacity=0
            
        )
        

        self.img_for_animation = Image(
            source='click.png',
            size_hint = (None,None),
            size = (50,50),
            pos = (200,100),
            opacity=0

        )
        
        self.img_for_house = Image(
            source='HouseForGame.png',
            size_hint = (None,None),
            size = (250,250),
            pos = (500,100),
            opacity=0

        )

        self.mini_game_button = Button(
            text = 'Wanna play minigame?',
            size_hint=(None, None),
            size=(170, 50),
            pos_hint={'center_x': 0.6, 'center_y': .97},
            opacity = 0


        )
        self.mini_game_button.disabled = False


        self.img_a_lot_of_coins = Image(
            source = 'AloOfCoins.png',
            size_hint = (None,None),
            size = (150,100),
            pos = (125,80),
            opacity = 0     
        )

        self.img_coins = Image(
            source = 'CoinsForGame.png',
            size_hint = (None,None),
            size=(100,100),
            pos = (100,0),
            opacity = 0
        )
        self.img_coins_2 = Image(
            source = 'CoinsForGame.png',
            size_hint = (None,None),
            size=(100,100),
            pos = (200,0),
            opacity = 0
        )
        

        text_layout = BoxLayout(
            size_hint=(None, None),
            size=(200, 60),
            pos_hint={'right': 1, 'top': 1},
            padding=(10, 10)
        )

        self.label = Label(
            text='Clicks: 0',
            color=(0, 0, 0, 1),
            font_size='24sp',
            size_hint=(None, None),
            size=(150, 50)
        )

        self.btn_click = Button(
           
            size_hint=(None, None),
            size=(100, 100),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            background_normal = 'ClickMe.png',
            background_down = 'ClickMe.png'
        )

        self.btn_shop = Button(
     
            size_hint=(None, None),
            size=(80, 70),
            pos_hint={'center_x': 0.08, 'center_y': 0.9},
            background_normal = 'Shop.png'
        )
        self.btn_decoration = Button(
            
            size_hint = (None,None),
            size=(90,80),
            pos_hint={'center_x':0.18,'center_y':0.9},
            background_normal = 'Shop1.png'
        )

        self.btn_click.bind(on_press=self.on_button_press)
        self.mini_game_button.bind(on_press=self.start_minigame)
        self.btn_task.bind(on_press=self.open_task)
        

        self.btn_shop.bind(on_press=self.open_shop)
        self.btn_decoration.bind(on_press=self.open_decoratoin_shop)
        self.img_for_enemy.bind(on_press=self.hide_enemy)
        self.img_for_enemy_1.bind(on_press=self.hide_enemy_for_another)
        
        text_layout.add_widget(self.label)
        
        layout.add_widget(self.img)

        layout.add_widget(self.img_for_animation)
        layout.add_widget(self.img_dog)
        layout.add_widget(self.btn_task)
       
        layout.add_widget(self.img_coins)
        layout.add_widget(self.mini_game_button)
        layout.add_widget(self.img_coins_2)

        layout.add_widget(self.img_a_lot_of_coins)

        layout.add_widget(self.btn_decoration)
        layout.add_widget(self.img_for_house)
        layout.add_widget(text_layout)
        layout.add_widget(self.btn_click)
        layout.add_widget(self.btn_shop)
        layout.add_widget(self.img_for_enemy_1)
        layout.add_widget(self.img_for_enemy)

        self.add_widget(layout)


    def enabled_button(self,dt):
        global strart_minigame
        strart_minigame = True
        self.mini_game_button.disabled = False
        self.mini_game_button.opacity = 1
        Clock.schedule_once(self.disenabled_button, 10)

    def disenabled_button(self,dt):
        global strart_minigame
        strart_minigame = False
        self.mini_game_button.disabled = True
        self.mini_game_button.opacity = 0

    def start_minigame(self,instance):
        if strart_minigame:
            self.manager.current = 'mini_game'


    def open_task(self,instance):
        self.manager.current = 'task'

    def on_button_press(self, instance):
        global Upgrade, clicks, Upgrade_1, press_time,Add_monster
        

        press_time += 1

        bonus_clicks = 0

        if Upgrade:
            bonus_clicks += 2
        if Upgrade_1:
            bonus_clicks += 3
        if Upgrade_2:
            bonus_clicks += 4
        if Upgrade_3:
            bonus_clicks += 5
        if Upgrade_4:
            bonus_clicks += 6
        if Upgrade_5:
            bonus_clicks += 9
        if Upgrade_6:
            bonus_clicks += 10
        if Upgrade_7:
            bonus_clicks += 12
        if Upgrade_8:
            bonus_clicks += 15
        if Upgrade_9:
            bonus_clicks += 20

        clicks += 1 + bonus_clicks

        self.label.text = f'Clicks: {clicks}'

        self.animate_click_effect()
        if press_time % 50 == 0:
            self.animated_enemy(0)

        



    def open_shop(self, instance):
        self.manager.current = 'shop'  
    def open_decoratoin_shop(self,instance):
        self.manager.current = 'shop_decoration'
    def animate_click_effect(self):
        a = randint(1, 4)

        if a == 1:
            start_x = 200
            start_y = 100
        elif a == 2:
            start_x = 500
            start_y = 100
        elif a == 3:
            start_x = 350
            start_y = 200
        elif a == 4:
            start_x = 250
            start_y = 100

        
        self.img_for_animation.opacity = 1
        self.img_for_animation.pos = (start_x,start_y)

       
        anim = Animation(pos=(start_x, 300), opacity=0, duration=0.5)
        anim.start(self.img_for_animation)
    
    def animated_enemy(self, dt):
        if self.enemy_is_animating:
            return
        self.enemy_is_animating = True
        print('1')
        self.img_for_enemy.opacity = 1
        self.img_for_enemy.pos = (30, 100)


        anim_enemy = Animation(pos=(800, 100), duration=5)
        anim_enemy.bind(on_complete=self.hide_enemy_after_animation)
        anim_enemy.start(self.img_for_enemy)

    def animated_enemy_1(self, dt):
        global enemy_running
        if enemy_running:
            return
        enemy_running = True
        print('2')
        self.img_for_enemy_1.opacity = 1
        self.img_for_enemy_1.pos = (730, 100)


        anim_enemy_1 = Animation(pos=(-30, 100), duration=5)
        anim_enemy_1.bind(on_complete=self.hide_enemy_after_animation_other)
        anim_enemy_1.start(self.img_for_enemy_1)     
        
        

        
            




    def start_passive_income(self):
        Clock.schedule_interval(self.give_passive_click, 2)

    def start_passive_income_for_coins(self):
        Clock.schedule_interval(self.give_passive_click_for_coins, 2)

    def start_passive_income_for_coins_2(self):
        Clock.schedule_interval(self.give_passive_click_for_coins_2, 2)

    def start_passive_income_for_coins_3(self):
        Clock.schedule_interval(self.give_passive_click_for_coins_3, 2)

    def start_passive_income_for_fon(self):
        Clock.schedule_interval(self.give_passive_click_for_fon, 2)

    def start_passive_income_for_house(self):
        Clock.schedule_interval(self.give_passive_click_for_house, 2)

    def start_passive_income_for_button(self):
        Clock.schedule_interval(self.give_passive_click_for_button, 2)

    def give_passive_click(self, dt):
        global clicks
        clicks += 1
        self.label.text = f'Clicks: {clicks}'

    def give_passive_click_for_coins(self, dt):
        global clicks
        clicks += 2
        self.label.text = f'Clicks: {clicks}'


    def give_passive_click_for_coins_2(self, dt):
        global clicks
        clicks += 5
        self.label.text = f'Clicks: {clicks}'

    def give_passive_click_for_coins_3(self, dt):
        global clicks
        clicks += 10
        self.label.text = f'Clicks: {clicks}'

    def give_passive_click_for_fon(self, dt):
        global clicks
        clicks += 100
        self.label.text = f'Clicks: {clicks}'


    def give_passive_click_for_house(self, dt):
        global clicks
        clicks += 250
        self.label.text = f'Clicks: {clicks}'


    def give_passive_click_for_button(self, dt):
        global clicks
        clicks += 400
        self.label.text = f'Clicks: {clicks}'


    def hide_enemy(self, instance):
        global clicks
        instance.opacity = 0
        clicks += 50
        self.label.text = f'Clicks: {clicks}'

    def hide_enemy_for_another(self, instance):
        global clicks
        instance.opacity = 0
        clicks += 150
        self.label.text = f'Clicks: {clicks}'

    def enemy_damage(self, dt):
        global clicks
        if self.img_for_enemy.opacity == 1 and clicks > 0:
            clicks -= 10
            self.label.text = f'Clicks: {clicks}'

    def enemy_damage_for_other(self, dt):
        global clicks
        if self.img_for_enemy_1.opacity == 1 and clicks > 0:
            clicks -= 1000
            self.label.text = f'Clicks: {clicks}'

    def hide_enemy_after_animation(self, animation, widget):
        widget.opacity = 0
        self.enemy_is_animating = False

    def hide_enemy_after_animation_other(self, animation, widget):
        global enemy_running
        widget.opacity = 0
        enemy_running = False
    def on_enter(self):
        if Add_monster:
            Clock.schedule_interval(self.animated_enemy_1, 20)


class ShopDecoration(Screen):
    def __init__(self, **kwargs):
        super(ShopDecoration, self).__init__(**kwargs)
        decoration_layout = FloatLayout()

        label_welcom = Label(
            text = 'Welcome to the decoration shop',
            font_size = '30sp',
            pos_hint = {'center_x': 0.5, 'center_y':0.9 }
        )
        img_shope_decoration = Image(
            source='imgShope.jpg',
            keep_ratio = False,
            allow_stretch = True,
            size_hint = (1,1),
            pos_hint = {'x':0,'y':0}
        )

        btn_update_fon = Button(
            text = 'Update Fon - 2500',
            size_hint= (None,None),
            size = (120,50),
            pos_hint={'center_x': 0.9, 'center_y': 0.6}
        
        )

        btn_update_house = Button(
            text = 'Buy house - 5000',
            size_hint= (None,None),
            size = (120,50),
            pos_hint={'center_x': 0.1, 'center_y': 0.4}
        
        )


        btn_passive = Button(
            text='Dog Coin - 15',
            size_hint=(None, None),
            size=(120, 50),
            pos_hint={'center_x': 0.1, 'center_y': 0.6}
        )

        btn_passive1 = Button(
            text = 'Coins',
            size_hint=(None,None),
            size = (120,50),
            pos_hint = {'center_x': 0.3,'center_y': 0.6}
        )

        btn_passive_2 = Button(
            text = 'More Coins',
            size_hint=(None,None),
            size = (120,50),
            pos_hint = {'center_x': 0.5,'center_y': 0.6}          
        )
        btn_passive_3 = Button(
            text = 'A lot of coins',
            size_hint=(None,None),
            size = (120,50),
            pos_hint = {'center_x': 0.7,'center_y': 0.6}          
        )

        btn_update_button = Button(
            text = 'Upgrade button',
            size_hint=(None,None),
            size = (120,50),
            pos_hint = {'center_x': 0.3,'center_y': 0.4}          
        )
        


        btn_passive.bind(on_press=self.buy_passive_income)
        btn_passive_3.bind(on_press=self.buy_passive_income_for_a_lot_of_coins)
        btn_passive_2.bind(on_press=self.buy_passive_income_for_coins_2)
        
        btn_update_house.bind(on_press = self.buy_passive_income_for_house)
        


        btn_back_to_menu = Button(
            text = 'Back',
            size_hint = (None,None),
            size = (120,50),
            pos_hint ={'center_x':0.08,'center_y':0.9}
        )


        btn_back_to_menu.bind(on_press=self.back_to_menu)
        btn_update_fon.bind(on_press = self.buy_passive_income_for_fon)
        btn_passive1.bind(on_press=self.buy_passive_income_for_coins)
        btn_update_button.bind(on_press = self.buy_passive_income_for_button)

        decoration_layout.add_widget(img_shope_decoration)
        decoration_layout.add_widget(btn_update_fon)
        decoration_layout.add_widget(btn_update_house)
        decoration_layout.add_widget(btn_passive_2)
        decoration_layout.add_widget(btn_update_button)
        decoration_layout.add_widget(btn_passive_3)
        decoration_layout.add_widget(btn_passive1)
        decoration_layout.add_widget(btn_passive)
        decoration_layout.add_widget(btn_back_to_menu)
        decoration_layout.add_widget(label_welcom)
        self.add_widget(decoration_layout)

    

    def buy_passive_income(self, instance):
        global PassiveIncome, clicks,PassiveIncomeForCoins
        

        if PassiveIncome:
            instance.text = 'Already running'
            return

        if clicks >= 50:
            clicks -= 50
            PassiveIncome = True
            instance.text = 'Running'
            main_screen = self.manager.get_screen('main')
            main_screen.img_dog.opacity = 1
            main_screen.label.text = f'Clicks: {clicks}'
            main_screen.start_passive_income()
        else:
            instance.text = 'Need 50 clicks'

    def buy_passive_income_for_coins(self, instance):
        global PassiveIncomeForCoins, clicks,PassiveIncome
        

        if PassiveIncomeForCoins:
            instance.text = 'Already running'
            return

        if clicks >= 150:
            clicks -= 150
            PassiveIncomeForCoins = True
            instance.text = 'Running'
            main_screen = self.manager.get_screen('main')
            main_screen.img_coins.opacity = 1
            main_screen.label.text = f'Clicks: {clicks}'
            main_screen.start_passive_income_for_coins()
        else:
            instance.text = 'Need 150 clicks'

    def buy_passive_income_for_coins_2(self, instance):
        global PassiveIncome, clicks,PassiveIncomeForCoins,PassiveIncomeForCoins_2
        

        if PassiveIncomeForCoins_2:
            instance.text = 'Already running'
            return

        if clicks >= 777:
            clicks -= 777
            PassiveIncomeForCoins_2 = True
            instance.text = 'Running'
            main_screen = self.manager.get_screen('main')
            main_screen.img_coins_2.opacity = 1
            main_screen.label.text = f'Clicks: {clicks}'
            main_screen.start_passive_income_for_coins_2()
        else:
            instance.text = 'Need 777 clicks'

    def buy_passive_income_for_a_lot_of_coins(self, instance):
        global PassiveIncome, clicks,PassiveIncomeForCoins,PassiveIncomeForCoins_2,PassiveIncomeForCoins_3
        

        if PassiveIncomeForCoins_3:
            instance.text = 'Already running'
            return

        if clicks >= 1500:
            clicks -= 1500
            PassiveIncomeForCoins_3 = True
            instance.text = 'Running'
            main_screen = self.manager.get_screen('main')
            main_screen.img_a_lot_of_coins.opacity = 1
            main_screen.label.text = f'Clicks: {clicks}'
            main_screen.start_passive_income_for_coins_3()
        else:
            instance.text = 'Need 1500 clicks'

    def buy_passive_income_for_fon(self, instance):
        global PassiveIncome, clicks,PassiveIncomeForCoins,PassiveIncomeForCoins_2,PassiveIncomeForCoins_3,Update_Fon,Add_monster
        

        if Update_Fon:
            instance.text = 'Already running'
            return

        if clicks >= 2500:
            clicks -= 2500
            Update_Fon = True
            Add_monster = True
            instance.text = 'Running'
            main_screen = self.manager.get_screen('main')
            main_screen.img.source = 'FonGameTrees.jpg'
            main_screen.label.text = f'Clicks: {clicks}'
            main_screen.start_passive_income_for_fon()
        else:
            instance.text = 'Need 2500 clicks'


    def buy_passive_income_for_house(self, instance):
        global PassiveIncome, clicks,PassiveIncomeForCoins,PassiveIncomeForCoins_2,PassiveIncomeForCoins_3,Update_Fon,Add_monster,Update_House
        

        if Update_House:
            instance.text = 'Already running'
            return

        if clicks >= 5000:
            clicks -= 5000
            Update_House = True
            
            instance.text = 'Running'
            main_screen = self.manager.get_screen('main')
            main_screen.img_for_house.opacity = 1
            main_screen.label.text = f'Clicks: {clicks}'
            main_screen.start_passive_income_for_house()
        else:
            instance.text = 'Need 5000 clicks'

    def buy_passive_income_for_button(self, instance):
        global PassiveIncome, clicks,PassiveIncomeForCoins,PassiveIncomeForCoins_2,PassiveIncomeForCoins_3,Update_Fon,Add_monster,Update_House,Update_Button
        

        if Update_Button:
            instance.text = 'Already running'
            return

        if clicks >= 10000:
            clicks -= 10000
            Update_Button = True
            
            instance.text = 'Running'
            main_screen = self.manager.get_screen('main')
            main_screen.btn_click.background_normal = 'Bitcoin.png'
            main_screen.btn_click.background_down = 'Bitcoin.png'
            main_screen.label.text = f'Clicks: {clicks}'
            main_screen.start_passive_income_for_button()
        else:
            instance.text = 'Need 10000 clicks'

    def back_to_menu(self, instance):
        self.manager.current = 'main'
            


class MiniGame(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mini_game_layout = FloatLayout()
        self.add_widget(self.mini_game_layout)
        global minigame_open
        minigame_open = True

        self.btn_back = Button(
            text='Back',
            size_hint=(None, None),
            size=(120, 50),
            pos_hint={'center_x': 0.1, 'center_y': 0.9}
        )
        self.btn_back.bind(on_press=self.back_to_menu)

        self.label_welcom = Label(
            text = 'Caught all mouse!',
            font_size = '30sp',
            pos_hint = {'center_x': 0.5, 'center_y':0.9 }
        )

        self.label_wining = Label(
            text = "Nice job you recived  1000 clicks",
            size_hint = (None,None),
            font_size = '30sp',
            pos_hint = {'center_x':0.5,'center_y':0.6},
            opacity = 0 
        )

        self.img_for_minigame = Image(
            source='FonForGameCave.png',
            keep_ratio=False,
            allow_stretch=True,
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )

        self.mini_game_layout.add_widget(self.img_for_minigame)
        self.mini_game_layout.add_widget(self.btn_back)
        self.mini_game_layout.add_widget(self.label_wining)
        self.mini_game_layout.add_widget(self.label_welcom)

       
        self.bind(on_enter=self.spawn_random_mice)

        

    def spawn_random_mice(self, *args):
        
        for child in self.mini_game_layout.children[:]:
            if isinstance(child, MiniGameImage):
                self.mini_game_layout.remove_widget(child)

        num_mice = randint(10, 20)
        global need_caught_mouse
        need_caught_mouse = num_mice
        for _ in range(num_mice):
            self.spawn_mouse()

    def spawn_mouse(self):
        mouse_width, mouse_height = 100, 50

     
        screen_width =  800
        screen_height = 600

      
        x = randint(0, screen_width - mouse_width)
        y = randint(0, screen_height - mouse_height)

        mouse = MiniGameImage(
            source='Mouse.png',
            size_hint=(None, None),
            size=(mouse_width, mouse_height),
            pos=(x, y)
        )

        self.mini_game_layout.add_widget(mouse)
        mouse.bind(on_press=self.click_on_mouse)
    def back_to_menu(self, instance):
        global minigame_open 
        minigame_open = False
        self.label_wining.opacity = 0
        self.manager.current = 'main'

    def click_on_mouse(self, instance):
        global need_caught_mouse,minigame_open
        
        self.mini_game_layout.remove_widget(instance)
        need_caught_mouse -= 1

        if need_caught_mouse == 0:
            global clicks
            self.label_wining.opacity = 1
            clicks += 1000
        
class TaskUI(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        task_layout = FloatLayout()

        self.btn_back  = Button(
            text = 'Back',
            size_hint = (None,None),
            size = (120,50),
            pos_hint = {'center_x':0.1,'center_y':0.9}
        )


        self.img_for_back = Image(
            source = 'FonForTask.jpg',
            keep_ratio = False,
            allow_stretch = True,
            size_hint = (1,1),
            pos_hint = {'x':0,'y':0}
        )

        

        self.btn_back.bind(on_press=self.back_to_menu)
        task_layout.add_widget(self.img_for_back)
        task_layout.add_widget(self.btn_back)
        self.add_widget(task_layout)



    def back_to_menu(self,instance):
        self.manager.current = 'main'

class ShopScreen(Screen):
    def __init__(self, **kwargs):
        super(ShopScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        img_shope = Image(
            source='imgShope.jpg',
            keep_ratio = False,
            allow_stretch = True,
            size_hint = (1,1),
            pos_hint = {'x':0,'y':0}
        )

        label = Label(
            text="Welcome to the Shop!",
            font_size='30sp',
            pos_hint={'center_x': 0.5, 'center_y': 0.9}
        )

        btn_back = Button(
            text='Back',
            size_hint=(None, None),
            size=(100, 40),
            pos_hint={'center_x': 0.1, 'center_y': 0.9}
        )
        btn_back.bind(on_press=self.go_back)
    
        btn_upgrade_1 = Button(
            text='Upgrade-1(+2)',
            size_hint=(None,None),
            size=(120,50),
            pos_hint={'center_x':0.1,'center_y':0.6}
        )

        btn_upgrade_2 = Button(
            text='Upgrade-2 (+3)',
            size_hint=(None,None),
            size=(120,50),
            pos_hint={'center_x':0.3,'center_y':0.6}
        )
        btn_upgrade_3 = Button(
            text='Upgrade-3 (+4)',
            size_hint=(None,None),
            size=(120,50),
            pos_hint={'center_x':0.5,'center_y':0.6}
        )
        btn_upgrade_4 = Button(
            text='Upgrade-4 (+5)',
            size_hint=(None,None),
            size=(120,50),
            pos_hint={'center_x':0.7,'center_y':0.6}
        )

        btn_upgrade_5 = Button(
            text='Upgrade-5 (+6)',
            size_hint=(None,None),
            size=(120,50),
            pos_hint={'center_x':0.9,'center_y':0.6}
        )
        btn_upgrade_6 = Button(
            text='Upgrade-6 (+9)',
            size_hint=(None,None),
            size=(120,50),
            pos_hint={'center_x':0.9,'center_y':0.4}
        )
        btn_upgrade_7 = Button(
            text='Upgrade-7 (+10)',
            size_hint=(None,None),
            size=(120,50),
            pos_hint={'center_x':0.7,'center_y':0.4}
        )
        btn_upgrade_8 = Button(
            text='Upgrade-8 (+12)',
            size_hint=(None,None),
            size=(120,50),
            pos_hint={'center_x':0.5,'center_y':0.4}
        )
        btn_upgrade_9 = Button(
            text='Upgrade-9 (+15)',
            size_hint=(None,None),
            size=(120,50),
            pos_hint={'center_x':0.3,'center_y':0.4}
        )
        btn_upgrade_10 = Button(
            text='Upgrade-10 (+20)',
            size_hint=(None,None),
            size=(120,50),
            pos_hint={'center_x':0.1,'center_y':0.4}
        )



        btn_upgrade_4.bind(on_press=self.upgarede_pess_3)
        btn_upgrade_5.bind(on_press=self.upgarede_pess_4)

        layout.add_widget(img_shope)
        layout.add_widget(btn_upgrade_4)
        layout.add_widget(btn_upgrade_6)
        layout.add_widget(btn_upgrade_7)
        layout.add_widget(btn_upgrade_8)
        layout.add_widget(btn_upgrade_9)
        layout.add_widget(btn_upgrade_10)

        btn_upgrade_6.bind(on_press=self.upgarede_pess_5)
        btn_upgrade_7.bind(on_press=self.upgarede_pess_6)
        btn_upgrade_8.bind(on_press=self.upgarede_pess_7)
        btn_upgrade_9.bind(on_press=self.upgarede_pess_8)
        btn_upgrade_10.bind(on_press=self.upgarede_pess_9)
        layout.add_widget(btn_upgrade_5)
        layout.add_widget(btn_upgrade_2)
        layout.add_widget(btn_upgrade_3)
        layout.add_widget(label)
        layout.add_widget(btn_back)
        layout.add_widget(btn_upgrade_1)
        self.add_widget(layout)
        btn_upgrade_1.bind(on_press=self.upgarede_pess)
        btn_upgrade_2.bind(on_press=self.upgarede_pess_1)
        btn_upgrade_3.bind(on_press=self.upgarede_pess_2)


    def upgarede_pess(self, instance):
        global Upgrade,clicks
        
        if clicks >= 10:
            Upgrade = True
            instance.text = 'Upgraded'
            clicks -= 10
            main_screen = self.manager.get_screen('main')
            main_screen.label.text = f'Clicks: {clicks}'
        elif Upgrade:
            instance.text = 'Already upgraded'
        else:
            instance.text = 'Need 10 clicks'

    def upgarede_pess_1(self, instance):
        global Upgrade_1,clicks,Upgrade
        
        if clicks >= 100:
            
            Upgrade_1 = True
            instance.text = 'Upgraded'
            clicks -= 100
            main_screen = self.manager.get_screen('main')
            main_screen.label.text = f'Clicks: {clicks}'
        elif Upgrade_1:
            instance.text = 'Already upgraded'
        else:
            instance.text = 'Need 100 clicks'       
        
    def upgarede_pess_2(self, instance):
        global Upgrade_1,clicks,Upgrade,Upgrade_2
        
        if clicks >= 250:
            
            Upgrade_2 = True
            instance.text = 'Upgraded'
            clicks -= 250
            main_screen = self.manager.get_screen('main')
            main_screen.label.text = f'Clicks: {clicks}'
        elif Upgrade_2:
            instance.text = 'Already upgraded'
        else:
            instance.text = 'Need 250 clicks'
    def upgarede_pess_3(self, instance):
        global Upgrade_3, clicks
        if Upgrade_3:
            instance.text = 'Already upgraded'
        elif clicks >= 500:
            Upgrade_3 = True
            clicks -= 500
            instance.text = 'Upgraded'
            main_screen = self.manager.get_screen('main')
            main_screen.label.text = f'Clicks: {clicks}'
        else:
            instance.text = 'Need 500 clicks'

    def upgarede_pess_4(self, instance):
        global Upgrade_4, clicks
        if Upgrade_4:
            instance.text = 'Already upgraded'
        elif clicks >= 1000:
            Upgrade_4 = True
            clicks -= 1000
            instance.text = 'Upgraded'
            main_screen = self.manager.get_screen('main')
            main_screen.label.text = f'Clicks: {clicks}'
        else:
            instance.text = 'Need 1000 clicks'
    def upgarede_pess_5(self, instance):
        global Upgrade_5, clicks
        if Upgrade_5:
            instance.text = 'Already upgraded'
        elif clicks >= 1500:
            Upgrade_5 = True
            clicks -= 1500
            instance.text = 'Upgraded'
            self.manager.get_screen('main').label.text = f'Clicks: {clicks}'
        else:
            instance.text = 'Need 1500 clicks'

    def upgarede_pess_6(self, instance):
        global Upgrade_6, clicks
        if Upgrade_6:
            instance.text = 'Already upgraded'
        elif clicks >= 2000:
            Upgrade_6 = True
            clicks -= 2000
            instance.text = 'Upgraded'
            self.manager.get_screen('main').label.text = f'Clicks: {clicks}'
        else:
            instance.text = 'Need 2000 clicks'

    def upgarede_pess_7(self, instance):
        global Upgrade_7, clicks
        if Upgrade_7:
            instance.text = 'Already upgraded'
        elif clicks >= 3000:
            Upgrade_7 = True
            clicks -= 3000
            instance.text = 'Upgraded'
            self.manager.get_screen('main').label.text = f'Clicks: {clicks}'
        else:
            instance.text = 'Need 3000 clicks'

    def upgarede_pess_8(self, instance):
        global Upgrade_8, clicks
        if Upgrade_8:
            instance.text = 'Already upgraded'
        elif clicks >= 4000:
            Upgrade_8 = True
            clicks -= 4000
            instance.text = 'Upgraded'
            self.manager.get_screen('main').label.text = f'Clicks: {clicks}'
        else:
            instance.text = 'Need 4000 clicks'

    def upgarede_pess_9(self, instance):
        global Upgrade_9, clicks
        if Upgrade_9:
            instance.text = 'Already upgraded'
        elif clicks >= 5000:
            Upgrade_9 = True
            clicks -= 5000
            instance.text = 'Upgraded'
            self.manager.get_screen('main').label.text = f'Clicks: {clicks}'
        else:
            instance.text = 'Need 5000 clicks'




    def go_back(self, instance):
        self.manager.current = 'main'  



class MyApp1(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(ShopScreen(name='shop'))
        sm.add_widget(ShopDecoration(name='shop_decoration'))
        sm.add_widget(MiniGame(name='mini_game'))
        sm.add_widget(TaskUI(name='task'))
        return sm
    def on_stop(self):

        saved_data()

if __name__ == '__main__':
    MyApp1().run()
