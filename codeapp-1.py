from kivy.app import App
from kivy.uix.recycleview import RecycleView

class RV(RecycleView):
    def __init__(self):
        super().__init__()
        content = ['hello', 'this is your world', 'leader. must obey']
        self.date = [{'text':item} for item in content]



class MyApp(App):
    def build(self):
        return RV()

MyApp().run()


