import keyboard
import pyautogui
import time
from PIL import ImageGrab
from model.Macro import Macro

class MacroController:
    def __init__(self, need_seat_cnt, offset, alarm, view=None):
        self.view = view
        self.macro = Macro(need_seat_cnt, offset, alarm, logger=self.log)
        keyboard.add_hotkey(';', self.stop_macro)

    def log(self, msg):
        if self.view and hasattr(self.view, 'log'):
            self.view.log(msg)
        else:
            print(msg)

    def start_macro(self):
        self.macro.start_macro()

    def stop_macro(self):
        self.macro.stop_macro()

    def select_seat_area(self):
        self.log("📍 좌석 영역 선택 시작: 좌상단 'a', 우하단 'b'를 누르세요.")
        left_top = self._wait_for_key('a')
        right_bottom = self._wait_for_key('b')
        self.macro.seat_axis = [left_top, right_bottom]
        self.log(f"✅ 좌석 영역 선택 완료: {self.macro.seat_axis}")
        self.view.capture_region(left_top, right_bottom)

    def select_seat_grade(self):
        my_class_list = list(self.macro.seat_class) if self.macro.seat_class else []
        self.log("🎨 좌석 등급 선택 시작: 색상 위에서 'a', 마친 후 'c'를 누르세요.")
        
        while True:
            if self.view and hasattr(self.view, 'root'):
                self.view.root.update()
                
            if keyboard.is_pressed('a'):
                x, y = pyautogui.position()
                screen = ImageGrab.grab()
                rgb = screen.getpixel((x, y))
                self.log(f"🎨 색상 등록됨: {rgb}")
                my_class_list.append(rgb)
                self.view.update_listbox(set(my_class_list))
                self.view.draw_color_rectangle(rgb)
                
                while keyboard.is_pressed('a'):
                    if self.view and hasattr(self.view, 'root'):
                        self.view.root.update()
                    time.sleep(0.01)

            if keyboard.is_pressed('c'):
                self.macro.seat_class = set(my_class_list)
                self.view.update_listbox(self.macro.seat_class)
                self.log("✅ 좌석 등급 선택 완료!")
                
                while keyboard.is_pressed('c'):
                    if self.view and hasattr(self.view, 'root'):
                        self.view.root.update()
                    time.sleep(0.01)
                break
                
            time.sleep(0.01)

    def select_refresh_axis(self):
        self.log("🔄 새로고침 버튼 위치 지정: 'a' 키를 누르세요.")
        self.macro.refresh_axis = self._wait_for_key('a')
        self.log(f"✅ 새로고침 좌표 설정됨: {self.macro.refresh_axis}")

    def select_complete_axis(self):
        self.log("🎯 좌석 선택 완료 버튼 위치 지정: 'a' 키를 누르세요.")
        self.macro.pay_axis = self._wait_for_key('a')
        self.log(f"✅ 선택 완료 좌표 설정됨: {self.macro.pay_axis}")


    def on_listbox_click(self, event):
        selected_index = self.view.color_listbox.curselection()
        if selected_index:
            selected_color = self.view.color_listbox.get(selected_index)
            self.view.draw_color_rectangle(selected_color)

    def _wait_for_key(self, key):
        while keyboard.is_pressed(key):
            if self.view and hasattr(self.view, 'root'):
                self.view.root.update()
            time.sleep(0.01)

        while True:
            if self.view and hasattr(self.view, 'root'):
                self.view.root.update()

            if keyboard.is_pressed(key):
                pos = pyautogui.position()
                while keyboard.is_pressed(key):
                    if self.view and hasattr(self.view, 'root'):
                        self.view.root.update()
                    time.sleep(0.01)
                return pos

            time.sleep(0.01)

