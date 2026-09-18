import keyboard
import pyautogui
import time
from PIL import ImageGrab
from model.Macro import Macro

class MacroController:
    def __init__(self, need_seat_cnt, offset, alarm, view):
        self.macro = Macro(need_seat_cnt, offset, alarm)
        self.view = view
        keyboard.add_hotkey(';', self.stop_macro)

    def start_macro(self):
        self.macro.start_macro()

    def stop_macro(self):
        self.macro.stop_macro()

    def select_seat_area(self):
        left_top = self._wait_for_key('a')
        right_bottom = self._wait_for_key('b')
        self.macro.seat_axis = [left_top, right_bottom]
        print(f"Selected seat point: {self.macro.seat_axis}")
        self.view.capture_region(left_top, right_bottom)

    def select_seat_grade(self):
        my_class_list = list(self.macro.seat_class) if self.macro.seat_class else []
        print("좌석 등급 선택 시작: 색상 위에서 'a' 키를 누르고, 마친 후 'c' 키를 누르세요.")
        
        while True:
            if self.view and hasattr(self.view, 'root'):
                self.view.root.update()
                
            if keyboard.is_pressed('a'):
                x, y = pyautogui.position()
                screen = ImageGrab.grab()
                rgb = screen.getpixel((x, y))
                print(f"Selected Color: {rgb}")
                my_class_list.append(rgb)
                self.view.update_listbox(set(my_class_list))
                
                while keyboard.is_pressed('a'):
                    if self.view and hasattr(self.view, 'root'):
                        self.view.root.update()
                    time.sleep(0.01)

            if keyboard.is_pressed('c'):
                self.macro.seat_class = set(my_class_list)
                self.view.update_listbox(self.macro.seat_class)
                print("좌석 등급 선택 완료!")
                
                while keyboard.is_pressed('c'):
                    if self.view and hasattr(self.view, 'root'):
                        self.view.root.update()
                    time.sleep(0.01)
                break
                
            time.sleep(0.01)

    def select_refresh_axis(self):
        print("새로고침 버튼 위치 지정: 'a' 키를 누르세요.")
        self.macro.refresh_axis = self._wait_for_key('a')
        print(f"새로고침 좌표: {self.macro.refresh_axis}")

    def select_complete_axis(self):
        print("좌석 선택 완료 버튼 위치 지정: 'a' 키를 누르세요.")
        self.macro.pay_axis = self._wait_for_key('a')
        print(f"선택 완료 좌표: {self.macro.pay_axis}")

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

