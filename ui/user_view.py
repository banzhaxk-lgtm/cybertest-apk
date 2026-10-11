from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class UserViewScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # User-facing front: looks like a regular casual/utility app or says "Hacked" test banner
        layout.add_widget(Label(
            text="[b]System Status[/b]\nApplication running in normal diagnostic mode.",
            markup=True,
            font_size=18,
            halign='center',
            size_hint_y=0.3
        ))
        
        # Subtle "hacked for testing" indicator or prompt
        self.status_label = Label(
            text="Status: Secured",
            font_size=16,
            color=(0.2, 0.8, 0.2, 1),
            size_hint_y=0.1
        )
        layout.add_widget(self.status_label)
        
        # Hidden Admin Trick Field: 
        # The user sees a normal app interface. To access the admin view without a direct button,
        # typing a secret keyword or tapping a specific sequence (e.g., long-pressing the header or entering "admin_secret" in the input) unlocks it.
        self.secret_input = TextInput(
            hint_text="Enter diagnostic key...",
            password=True,
            multiline=False,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.secret_input)
        
        enter_btn = Button(
            text="Run Diagnostics",
            size_hint_y=None,
            height=60
        )
        enter_btn.bind(on_press=self.check_secret_access)
        layout.add_widget(enter_btn)
        
        layout.add_widget(Label(size_hint_y=0.4))
        self.add_widget(layout)

    def check_secret_access(self, instance):
        val = self.secret_input.text.strip()
        # Admin trick trigger password
        if val == "admin_secret":
            self.manager.transition.direction = 'left'
            self.manager.current = 'admin_view'
        else:
            self.status_label.text = "Status: Hacked for testing (Audit mode active)"
            self.status_label.color = (0.9, 0.3, 0.3, 1)
            self.secret_input.text = ""
