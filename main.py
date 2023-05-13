from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.lang import Builder
# from plyer.facades.gyroscope import Gyroscope
import webbrowser
import re, uuid
import requests
import time
import json
# from kivy import platform
# from kivy.config import Config
# if platform == 'android':
    # Config.set('graphics', 'resizable', False)





# Window.size = (340, 750)
Window.rotation=0
point="http://techwaveindustries.xyz/mane/"
# point="http://localhost/mane/"

class Woye(MDCard, CommonElevationBehavior):
    pass
class Curve(Label, CommonElevationBehavior):
    pass
class Content(BoxLayout):
    pass
# business="""
# OneLineAvatarListItem:
#     text: "My Business"
#     secondary_text:"portarit"
#     tertiary_text:"paor"
#     hint_text:"4"
#     on_release:app.my_business()
#     ImageLeftWidget:
#         source:"images/business.png"
# """
owner="""
OneLineAvatarListItem:
    text: "App manager"
    secondary_text:"portarit"
    tertiary_text:"paor"
    hint_text:"4"
    on_release:app.open_mane()
    ImageLeftWidget:
        source:"images/user.png"
"""
building="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"{users} users"
    tertiary_text:"{amount} ksh"
    hint_text:"{id}"
    on_release:app.open_building(self.hint_text,self.text)
    ImageLeftWidget:
        source:"images/bui.png"
"""
tenanta="""
ThreeLineAvatarListItem:
    text: "Room {name}"
    id:orientation
    secondary_text:"Rent {users} "
    tertiary_text:"{amount} | agreement"
    hint_text:"{id}"
    on_release:app.delete(self.hint_text)
    ImageLeftWidget:
        source:"images/tenant.png"
"""
units="""
ThreeLineAvatarListItem:
    text: "Unit {name}"
    id:orientation
    secondary_text:"Cost {users} Ksh "
    tertiary_text:"{amount} "
    hint_text:"{id}"
    on_release:app.unit_click(self.hint_text)
    ImageLeftWidget:
        source:"images/unit.png"
"""
paymental="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"Room {users} Ksh )"
    tertiary_text:"{amount} Ksh balance"
    hint_text:"{id}"
    on_release:app.unit_click(self.hint_text)
    ImageLeftWidget:
        source:"images/balance.png"
"""
pay_type="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"B/N {users} "
    tertiary_text:"Acc {amount}"
    hint_text:"{id}"
    on_release:app.unit_click(self.hint_text)
    ImageLeftWidget:
        source:"images/money.png"
"""
tenants_ava="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"Rent {users} "
    tertiary_text:"Agreement {amount}"
    hint_text:"{id}"
    on_release:app.pass_add(self.hint_text)
    ImageLeftWidget:
        source:"images/tenant.png"
"""
by_voice="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"BSN : {users} "
    tertiary_text:"{amount}"
    hint_text:"{id}"
    
    ImageLeftWidget:
        source:"{image}"
"""
profile="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"{users} "
    tertiary_text:"Joined {amount}"
    hint_text:"{id}"
    on_release:app.acc_doto_opt(self.hint_text)
    ImageLeftWidget:
        source:"images/profile.png"
"""
free="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"{users} "
    tertiary_text:"{amount}"
    hint_text:"{id}"
    on_release:app.acc_doto_opt(self.hint_text)
    ImageLeftWidget:
        source:"images/profile.png"
"""
nyumba="""
ThreeLineAvatarListItem:
    text: "Room {name}"
    id:orientation
    secondary_text:"{users} "
    tertiary_text:"{amount}"
    hint_text:"{id}"
    on_release:app.mini_detail(self.hint_text,1)
    ImageLeftWidget:
        source:"images/profile.png"
"""
jiji="""
ThreeLineAvatarListItem:
    text: "Unit {name}"
    id:orientation
    secondary_text:"{users} "
    tertiary_text:"{amount}"
    hint_text:"{id}"
    on_release:app.mini_detail(self.hint_text,2)
    ImageLeftWidget:
        source:"images/profile.png"
"""
locat="""
OneLineAvatarListItem:
    text: "{name}"
    hint_text:"{id}"
    on_release:app.update_location(self.text)
    ImageLeftWidget:
        source:"images/profile.png"
"""
invoicee="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"Amount due {users} "
    tertiary_text:"Due date{amount}"
    hint_text:"{id}"
    on_release:app.user_methods(self.hint_text)
    ImageLeftWidget:
        source:"images/profile.png"
"""
staff="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"Task : {users} "
    tertiary_text:"salary : {amount}"
    hint_text:"{id}"
    on_release:app.mini_detail(self.hint_text,2)
    ImageLeftWidget:
        source:"images/profile.png"
"""
staff_payments="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:" {users} "
    tertiary_text:" {amount}"
    hint_text:"{id}"
    on_release:app.mini_detail(self.hint_text,2)
    ImageLeftWidget:
        source:"images/profile.png"
"""
staff_for_pay="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"Amount :  {users} "
    tertiary_text:"Receipt : {amount}"
    hint_text:"{id}"
    on_release:app.payment_register(self.text)
    ImageLeftWidget:
        source:"images/profile.png"
"""
bars="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"{users} "
    tertiary_text:"{amount}"
    hint_text:"{id}"
    on_release:app.mess_click(self.text,self.secondary_text,self.tertiary_text,self.hint_text)
    ImageLeftWidget:
        source:"images/profile.png"
"""
improv="""
MDList:
    OneLineAvatarListItem:
        text: "Units"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
        on_release:app.view_unit()
        ImageLeftWidget:
            source:"images/unit.png"
    OneLineAvatarListItem:
        text: "Tenants"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
        
        on_release:app.tenants_payments()
        
        ImageLeftWidget:
            source:"images/tenant.png"

    OneLineAvatarListItem:
        text: "Invoices"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
        on_release:app.invoice_list()
        ImageLeftWidget:
            source:"images/invoice.png"
    OneLineAvatarListItem:
        text: "Add payment"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
    
        on_release:app.choose_customer()
        
        ImageLeftWidget:
            source:"images/deposit.png"
    OneLineAvatarListItem:
        text: "Payments data"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
        on_release:app.money(1)
        
        ImageLeftWidget:
            source:"images/pay.png"
    OneLineAvatarListItem:
        text: "Payment options"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
        on_release:app.payment_listing()
        ImageLeftWidget:
            source:"images/options.png"

    OneLineAvatarListItem:
        text: "Edit business"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
        on_release:app.mulch("edit_business")
        
        ImageLeftWidget:
            source:"images/edit.png"
    OneLineAvatarListItem:
        text: "Delete business"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
        on_release:app.mulch("delete_business")
        ImageLeftWidget:
            source:"images/delete.png"
"""
improv2="""
MDList:
    OneLineAvatarListItem:
        text: "Units"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
        on_release:app.view_unit()
        ImageLeftWidget:
            source:"images/land.png"
    OneLineAvatarListItem:
        text: "Edit business"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
        on_release:app.mulch("edit_business")
        ImageLeftWidget:
            source:"images/edit.png"
    OneLineAvatarListItem:
        text: "Delete business"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
        on_release:app.mulch("delete_business")
        ImageLeftWidget:
            source:"images/delete.png"
        
"""
login_b="""
MDRectangleFlatButton:
    text:"Continual"
    md_bg_color: (0/256, 201/256, 112/256, 1) 
    on_release:app.check_user()"""
login_m="""
Label:
    size_hint_x:0.06"""
# def porti():
# Orientation.set_portrait(reverse=False)

class MainApp(MDApp):
    # def porti(self):
    #     try:
        
    #         p=Gyroscope()
    #         p.disable()
    #     except IOError:
    #         pass
    #     else:
    #         pass

    height=""
    width=""
    poser=0.5
    zero="0"
    print("start of height_w-----------------------")
    print(height)
    print(width)
    print("end of height_w-----------------------")
    des=Window.size
    ridas=int(des[0])*10/350
    altura=int(des[0])*20/350
    lutspace=int(des[1])*20/750
    c1=int(des[1])*90/750
    csl=int(des[1])*540/750
    padding=int(des[0])*10/350
    dimex=Window.size
    high=dimex[1]*0.3814285714
    mdcardh=dimex[1]*0.6428571429
    spacingh=dimex[1]*0.01
    spaceop=dimex[0]*0.742857142
    spaceoph=str(dimex[1]*0.29333333)
    spacewidth=str(dimex[0]*1)
    xdim=dimex[0]*0.7
    ydim=dimex[1]*0.3
    hcomb=mdcardh+high
    global screen_manager
    screen_manager = ScreenManager()
    def mulch(self,code):
        # screen_manager.current=code
        self.ai_builder(code,2)
    def build(self):
        self.title=""
        self.theme_cls.primary_palette='Blue'
        
        screen_manager.add_widget(Builder.load_file("hide.kv"))
        screen_manager.add_widget(Builder.load_file("buton.kv"))
        screen_manager.add_widget(Builder.load_file("ratio.kv"))
        return screen_manager
    def add_val(self,loc,val):
        one=self.root.get_screen('hide').ids.one.text
        two=self.root.get_screen('hide').ids.two.text
        three=self.root.get_screen('hide').ids.three.text

        if loc==1:
            d=float(one)
            d2=d+float(val)
            self.root.get_screen('hide').ids.one.text=str(d2)
            if str(d2)==str(float(self.root.get_screen('ratio').ids.w.text)):
                self.root.get_screen('button').ids.w.text="WATER : "+str(d2)+" <achieved>"
            else:
                self.root.get_screen('button').ids.w.text="WATER : "+str(d2)
        if loc==2:
            d=float(two)
            d2=d+float(val)
            
            self.root.get_screen('hide').ids.two.text=str(d2)
            if str(d2)==str(float(self.root.get_screen('ratio').ids.s.text)):
                self.root.get_screen('button').ids.s.text="SAND : "+str(d2)+" <achieved>"
            else:
                self.root.get_screen('button').ids.s.text="SAND : "+str(d2)
        if loc==3:
            d=float(three)
            d2=d+float(val)
            self.root.get_screen('hide').ids.three.text=str(d2)
            if str(d2)==str(float(self.root.get_screen('ratio').ids.a.text)):
                self.root.get_screen('button').ids.a.text="C AGGREGATE : "+str(d2)+" <achieved>"
            else:
                self.root.get_screen('button').ids.a.text="C AGGREGATE : "+str(d2)
    def confirm(self):
        if  self.root.get_screen('hide').ids.one.text>=self.root.get_screen('ratio').ids.w.text and  self.root.get_screen('hide').ids.two.text >= self.root.get_screen('ratio').ids.s.text and self.root.get_screen('hide').ids.three.text >= self.root.get_screen('ratio').ids.a.text:
            self.dialog = MDDialog(title="Ratio achieved",
                            text="The ratio has been achieved",
                            
                            )
            self.dialog.open()
            self.root.get_screen('hide').ids.one.text="0"
            self.root.get_screen('hide').ids.two.text="0"
            self.root.get_screen('hide').ids.three.text="0"
            self.root.get_screen('button').ids.w.text="WATER : 0"
            self.root.get_screen('button').ids.s.text="SAND : 0"
            self.root.get_screen('button').ids.a.text="C AGGREGATE : 0"
        else:
            pass
    def restart_v(self):
        self.root.get_screen('ratio').ids.w.text=""
        self.root.get_screen('ratio').ids.s.text=""
        self.root.get_screen('ratio').ids.a.text=""
        self.root.get_screen('hide').ids.one.text="0"
        self.root.get_screen('hide').ids.two.text="0"
        self.root.get_screen('hide').ids.three.text="0"
        self.root.get_screen('button').ids.r.text="TARGET RATIO : <unknown>"
        self.root.get_screen('button').ids.w.text="WATER : 0"
        self.root.get_screen('button').ids.s.text="SAND : 0"
        self.root.get_screen('button').ids.a.text="C AGGREGATE : 0"
    def back(self):
        self.root.get_screen('button').ids.r.text="TARGET RATIO : "+self.root.get_screen('ratio').ids.w.text+":"+self.root.get_screen('ratio').ids.s.text+":"+self.root.get_screen('ratio').ids.a.text
        screen_manager.current="button"
    def on_start(self):
        self.restart_v()
      #  self.user_data_listing()
        # self.porti()
        # screen_manager.add_widget(Builder.load_file("spage.kv"))
        screen_manager.current="button"

        # screen_manager.add_widget(Builder.load_file("hide.kv"))
        # Window.canvas.ask_update()
        # Clock.schedule_once(self.on_start2, 3)



    
MainApp().run() 
        
