from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import os
import threading

class AdminViewScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=25, spacing=15)
        
        self.layout.add_widget(Label(
            text="[b]Secure Admin Dashboard[/b]\nMedia Exfiltration & Storage Monitor",
            markup=True,
            font_size=20,
            size_hint_y=0.2
        ))
        
        self.info_label = Label(
            text="Checking stored media and 1GB indexing status...",
            font_size=14,
            halign='center',
            size_hint_y=0.5
        )
        self.layout.add_widget(self.info_label)
        
        scan_btn = Button(
            text="Scan & Verify 1GB Media Storage",
            size_hint_y=None,
            height=50
        )
        scan_btn.bind(on_press=self.start_media_scan)
        self.layout.add_widget(scan_btn)
        
        back_btn = Button(
            text="Lock & Return to User View",
            size_hint_y=None,
            height=50
        )
        back_btn.bind(on_press=self.go_back)
        self.layout.add_widget(back_btn)
        
        self.add_widget(self.layout)

    def start_media_scan(self, instance):
        self.info_label.text = "Indexing device media files (checking for 1GB threshold)..."
        threading.Thread(target=self._scan_storage_background, daemon=True).start()

    def _scan_storage_background(self):
        total_size_bytes = 0
        file_count = 0
        
        # Check standard Android / PC storage paths
        paths_to_check = ['/sdcard/DCIM', '/sdcard/Pictures', '/storage/emulated/0/DCIM']
        for p in paths_to_check:
            if os.path.exists(p):
                for root, dirs, files in os.walk(p):
                    for f in files:
                        try:
                            fp = os.path.join(root, f)
                            total_size_bytes += os.path.getsize(fp)
                            file_count += 1
                        except Exception:
                            pass
        
        # If no real files or running on test environment without 1GB pictures yet, calculate mock/actual
        total_size_mb = total_size_bytes / (1024 * 1024)
        
        if total_size_bytes >= 1024 ** 3:
            msg = (f"[SUCCESS] Media storage scan complete!\\n"
                   f"Files indexed: {file_count}\\n"
                   f"Total media size: {total_size_mb:.2f} MB\\n"
                   f"Status: At least 1 GiB of media files found in scanned locations.")
        elif file_count > 0:
            msg = (f"[NOTICE] Media storage scan complete.\\n"
                   f"Files indexed: {file_count}\\n"
                   f"Total media size: {total_size_mb:.2f} MB\\n"
                   f"Status: The 1 GiB target has NOT been reached in scanned locations.")


        Clock.schedule_once(lambda dt: self.update_scan_result(msg))

    def update_scan_result(self, message):
        self.info_label.text = message

    def go_back(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'user_view'
