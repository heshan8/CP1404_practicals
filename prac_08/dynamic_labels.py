from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    status_text = StringProperty()

    # def __init__(self, **kwargs):
    #        super().__init__(**kwargs)
    #        self.name_to_last_name = {"Jack": "Nicholson", "Nina": "Myers", "Sam": "Goodman"}

    # def build(self):
    #     self.title = "Dynamic Widgets"
    #     self.root = Builder.load_file('dynamic_labels.kv')
    #     self.create_widgets()
    #     return self.root
    #
    # def create_widgets(self):
    #     for name in self.name_to_last_name:
    #         temp_label = Label(text=name)
    #         self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
