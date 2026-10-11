from kivy.app import App
from ui.manager import initialize_screen_manager
from core.network_client import AsynchronousNetworkEngine

class TelemetryApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.network_engine = AsynchronousNetworkEngine()
        self.network_engine.start_service()

    def build(self):
        self.title = "Telemetry & Assessment Tool"
        return initialize_screen_manager()

    def on_stop(self):
        self.network_engine.stop_service()

if __name__ == '__main__':
    TelemetryApp().run()
