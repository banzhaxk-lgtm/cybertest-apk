import threading
import queue
import time
import random

class AsynchronousNetworkEngine:
    def __init__(self):
        self.outbound_queue = queue.Queue()
        self.inbound_queue = queue.Queue()
        self.is_active = False
        self._worker_thread = None

    def start_service(self):
        """Spawns the background network lifecycle loop."""
        if not self.is_active:
            self.is_active = True
            self._worker_thread = threading.Thread(target=self._network_io_loop, daemon=True)
            self._worker_thread.start()

    def stop_service(self):
        """Request background worker shutdown and wait briefly for it to exit."""
        self.is_active = False
        if self._worker_thread and self._worker_thread.is_alive():
            self._worker_thread.join(timeout=2.0)

    def enqueue_telemetry_packet(self, data: dict):
        """Safe thread-facing access to load operational data payloads."""
        self.outbound_queue.put(data)

    def fetch_incoming_updates(self) -> list:
        """Flushes operational queues back onto UI clock controllers."""
        updates = []
        while True:
            try:
                updates.append(self.inbound_queue.get_nowait())
            except queue.Empty:
                break
        return updates

    def _network_io_loop(self):
        """
        The continuous background network cycle. Exclusively handles intensive I/O operations
        away from drawing threads.
        """
        while self.is_active:
            # 1. Handle Outbound Telemetry Trailing
            while True:
                try:
                    payload = self.outbound_queue.get_nowait()
                except queue.Empty:
                    break
                try:
                    # This project currently simulates network delivery; no server is configured.
                    time.sleep(0.2)
                    print(f"[Network Daemon] Simulated packet handling: {payload}")
                finally:
                    self.outbound_queue.task_done()

            # 2. Simulate Receiving Inbound Data Updates from Server
            # In a live app, this replaces a long-poll API request or web socket handler.
            if random.random() < 0.3:  # 30% chance to fetch an update cycle
                mock_server_response = {
                    "timestamp": time.time(),
                    "server_status": "ONLINE",
                    "registered_load": random.randint(12, 98)
                }
                self.inbound_queue.put(mock_server_response)

            time.sleep(1.0) # Rest thread briefly to conserve battery and CPU resources
