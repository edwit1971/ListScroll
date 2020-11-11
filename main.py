
from kivy.core.window        import Window
from kivy.uix.button         import Button
from kivy.uix.scrollview     import ScrollView
from kivy.uix.relativelayout import RelativeLayout

from kivymd.app             import MDApp
from kivymd.uix.list        import MDList
from kivymd.uix.floatlayout import MDFloatLayout



class ListScrollApp(MDApp):

    def __init__(self, **kwargs):
        super(ListScrollApp, self).__init__(**kwargs)
        self.Main_Win    = MDFloatLayout()
        self.Rel_Win     = RelativeLayout()
        self.List_Scr    = ScrollView()
        self.The_List    = MDList()
        return

    def build(self):
        #######################################
        self.Main_Win.size = Window.size
        Xc = int(self.Main_Win.width * 0.5)
        Yc = int(self.Main_Win.height * 0.5)
        #######################################
        self.Rel_Win.size_hint = (None, None)
        self.Rel_Win.width     = int(self.Main_Win.width * 0.3)
        self.Rel_Win.height    = int(self.Main_Win.height * 0.5)
        self.Rel_Win.x         = Xc - int(self.Rel_Win.width * 0.5)
        self.Rel_Win.y         = Yc - int(self.Rel_Win.height * 0.5)
        #######################################
        self.List_Scr.bar_inactive_color = (0.4, 0, 0, 1)
        self.List_Scr.bar_color   = (1, 0.15, 0.15, 1)
        self.List_Scr.bar_margin  = 5
        self.List_Scr.bar_width   = int(self.Rel_Win.width * 0.10)
        self.List_Scr.bar_pos_y   = 'right'
        # self.List_Scr.scroll_type = ['content']
        # self.List_Scr.scroll_type = ['bars']
        self.List_Scr.scroll_type = ['content', 'bars']
        #######################################
        Height1 = int(self.Rel_Win.height / 10)
        self.The_List.clear_widgets()
        for i in range(100):
            self.The_List.add_widget(Button(text=f"Button Number {i}", \
                                            size_hint = (None, None), \
                                            width = self.Rel_Win.width, \
                                            height = Height1))
        #######################################
        if(self.The_List.parent == None):
            self.List_Scr.add_widget(self.The_List)
        if(self.List_Scr.parent == None):
            self.Rel_Win.add_widget(self.List_Scr)
        if(self.Rel_Win.parent == None):
            self.Main_Win.add_widget(self.Rel_Win)
        #######################################
        self.List_Scr.scroll_x    = 1
        self.List_Scr.scroll_y    = 1
        #######################################
        return self.Main_Win

    
if __name__ == "__main__":
    ListScrollApp().run()

