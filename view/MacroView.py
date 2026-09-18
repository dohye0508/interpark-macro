from PIL import ImageGrab, ImageTk
import tkinter as tk

class MacroView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.setup_ui()

    def get_coordinates(self):
        desktop_x = [600, 600, 100, 600, 600, 600, 600, 600, 600]
        desktop_y = [50, 80, 100, 360, 420, 450, 480, 180, 130]

        for i in range(len(desktop_x)):
            desktop_x[i] *= 2

        desktop_y = [50, 120, 170, 590, 660, 730, 800, 250, 200]

        return desktop_x, desktop_y

    def setup_ui(self):
        _x, _y = self.get_coordinates()
        self.play_button = tk.Button(self.root, text="매크로 시작", command=self.controller.start_macro)
        self.play_button.place(x=_x[0], y=_y[0])
        
        self.pause_button = tk.Button(self.root, text="매크로 중지", command=self.controller.stop_macro)
        self.pause_button.place(x=_x[1], y=_y[1])

        canvas_width = 1000
        canvas_height = 1000
        self.canvas = tk.Canvas(self.root, width=canvas_width, height=canvas_height)
        self.canvas.place(x=_x[2], y=_y[2])

        self.button1 = tk.Button(self.root, text="좌석 영역 선택하기", command=self.controller.select_seat_area)
        self.button1.place(x=_x[3], y=_y[3])

        self.button2 = tk.Button(self.root, text="좌석 등급 선택하기", command=self.controller.select_seat_grade)
        self.button2.place(x=_x[4], y=_y[4])

        self.button3 = tk.Button(self.root, text="좌석 새로고침 좌표 가져오기", command=self.controller.select_refresh_axis)
        self.button3.place(x=_x[5], y=_y[5])

        self.button4 = tk.Button(self.root, text="좌석 선택 완료 좌표 가져오기", command=self.controller.select_complete_axis)
        self.button4.place(x=_x[6], y=_y[6])

        self.color_listbox = tk.Listbox(self.root, height=8, width=20)
        self.color_listbox.place(x=_x[7], y=_y[7])
        self.color_listbox.bind("<ButtonRelease-1>", self.controller.on_listbox_click)

        self.color_label = tk.Label(self.root, text="선택 색상 미리보기", font=("Malgun Gothic", 9, "bold"))
        self.color_label.place(x=_x[8], y=_y[8] - 25)

        self.color_canvas = tk.Canvas(self.root, width=140, height=60, bg="white", highlightthickness=1, highlightbackground="gray")
        self.color_canvas.place(x=_x[8], y=_y[8])

        self.log_label = tk.Label(self.root, text="실시간 실행 로그", font=("Malgun Gothic", 9, "bold"))
        self.log_label.place(x=_x[8], y=_y[8] + 75)

        self.log_text = tk.Text(self.root, width=45, height=22, font=("Consolas", 9))
        self.log_text.place(x=_x[8], y=_y[8] + 100)

    def log(self, message):
        from datetime import datetime
        now = datetime.now().strftime("[%H:%M:%S] ")
        full_msg = now + str(message) + "\n"
        print(full_msg, end="")
        if hasattr(self, 'log_text'):
            self.log_text.insert(tk.END, full_msg)
            self.log_text.see(tk.END)

    def capture_region(self, left_top, right_bottom):
        captured_image = ImageGrab.grab(bbox=(left_top[0], left_top[1], right_bottom[0], right_bottom[1]))
        captured_image = captured_image.resize((800, 800))

        tk_image = ImageTk.PhotoImage(captured_image)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
        self.canvas.image_names = tk_image

    def update_listbox(self, seat_class):
        self.color_listbox.delete(0, tk.END)
        for color in seat_class:
            self.color_listbox.insert(tk.END, str(color))
        if seat_class:
            latest_color = list(seat_class)[-1]
            self.draw_color_rectangle(latest_color)

    def draw_color_rectangle(self, rgb_values):
        self.color_canvas.delete("all")
        if isinstance(rgb_values, str):
            try:
                rgb_values = eval(rgb_values)
            except Exception:
                return

        if not isinstance(rgb_values, (tuple, list)) or len(rgb_values) < 3:
            return

        r, g, b = rgb_values[0], rgb_values[1], rgb_values[2]
        color_hex = "#{:02X}{:02X}{:02X}".format(r, g, b)
        
        self.color_canvas.create_rectangle(0, 0, 140, 60, fill=color_hex, outline="black", width=2)
        
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        text_color = "white" if brightness < 128 else "black"
        
        self.color_canvas.create_text(70, 20, text=f"RGB: ({r}, {g}, {b})", fill=text_color, font=("Malgun Gothic", 9, "bold"))
        self.color_canvas.create_text(70, 40, text=f"HEX: {color_hex}", fill=text_color, font=("Malgun Gothic", 9))
