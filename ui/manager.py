from kivy.uix.screenmanager import ScreenManager
from ui.user_view import UserViewScreen
from ui.admin_view import AdminViewScreen

def initialize_screen_manager() -> ScreenManager:
    sm = ScreenManager()
    sm.add_widget(UserViewScreen(name='user_view'))
    sm.add_widget(AdminViewScreen(name='admin_view'))
    return sm
