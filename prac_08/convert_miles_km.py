from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

FACTOR_MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """Convert miles to kilometres"""

    def build(self):
        """Build the Kivy app"""
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, miles):
        """Calculate """
        calculation = self.get_valid_number() * FACTOR_MILES_TO_KM
        self.root.ids.output_label.text = str(f"{calculation}")

    def handle_increment(self, increment):
        miles = self.get_valid_number() + increment
        self.root.ids.input_miles.text = str(miles)

    def get_valid_number(self):
        """Get valid input"""
        try:
            user_input = float(self.root.ids.input_miles.text)
            return user_input
        except ValueError:
            return 0


MilesConverterApp().run()
