import platform
import os

class DeviceManager:
    @staticmethod
    def get_mobile_id() -> str:
        """
        Retrieves a persistent identifier for the target framework.
        In production Android/Kivy environments, this safely accesses the native hardware context.
        """
        # Detect if running under the android platform lifecycle
        if platform.system().lower() == 'android' or 'ANDROID_ARGUMENT' in os.environ:
            try:
                from jnius import autoclass
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                currentActivity = PythonActivity.mActivity
                Secure = autoclass('android.provider.Settings$Secure')
                
                android_id = Secure.getString(
                    currentActivity.getContentResolver(), 
                    Secure.ANDROID_ID
                )
                return str(android_id) if android_id else "unknown_android"
            except Exception:
                return "android_emulated_id_01"
        
        # Fallback for desktop testing / lab simulation environments
        return f"desktop_node_{platform.node() or 'mobile_id_01'}"
