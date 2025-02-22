import asyncio
from bleak import BleakServer
import pyautogui

class PPTServer:
    def __init__(self):
        self.server = BleakServer(self.handle_command)

    async def handle_command(self, command: str):
        print(f"Received command: {command}")
        if command == "NEXT":
            pyautogui.press("right")
        elif command == "PREV":
            pyautogui.press("left")
        elif command == "START":
            pyautogui.press("f5")
        elif command == "END":
            pyautogui.hotkey("esc")

    async def start_server(self):
        print("Starting BLE Server...")
        await self.server.start()
        await asyncio.sleep(3600)

if __name__ == "__main__":
    server = PPTServer()
    asyncio.run(server.start_server())
