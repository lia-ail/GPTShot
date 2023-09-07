import tkinter as tk
import pystray
from IMG_rec import screen_shot


class DragSelectApp:
    def __init__(self, r, image, shift):
        self.root_window = r
        self.output_window = None
        self.output_area = None
        self.image = image
        self.icon = None
        self.language = "ENG"
        self.butt = None
        self.canvas = tk.Canvas(self.root_window, bg="black")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_rectangle(
            0, 0, self.canvas.winfo_width(), self.canvas.winfo_height(), fill="black"
        )

        self.start_x, self.start_y = None, None
        self.cur_x, self.cur_y = None, None
        self.selection_rect = None

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.shift = shift

        self.output_window = tk.Toplevel()
        self.output_window.geometry("1000x300")
        self.output_window.title("Output")
        self.output_window.protocol("WM_DELETE_WINDOW", self.on_close_output)
        self.output_area = tk.Text(self.output_window, width=900, height=150)
        self.output_area.place(x=0, y=0)
        self.output_window.withdraw()

    def on_button_press(self, event):
        if self.butt:
            self.butt.place_forget()
        if self.selection_rect:
            self.canvas.delete(self.selection_rect)
        self.start_x, self.start_y = event.x, event.y

    def on_mouse_drag(self, event):
        if self.selection_rect:
            self.canvas.delete(self.selection_rect)

        self.cur_x, self.cur_y = event.x, event.y
        self.selection_rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, self.cur_x, self.cur_y, fill="#B2B2B2", outline="blue", dash=(3, 3)
        )

    def on_button_release(self, event):
        self.cur_x, self.cur_y = event.x, event.y
        self.butt = tk.Button(self.root_window, text="OK", command=self.ok)
        self.butt.place(x=self.cur_x-25, y=self.cur_y+5)

    def show_window(self):
        self.icon.stop()
        self.icon = None
        self.root_window.after(0, self.root_window.deiconify)
        self.root_window.focus_force()

    def quit_window(self, ic, item):
        self.icon.stop()
        self.root_window.destroy()

    def hide_w(self):
        self.root_window.withdraw()
        self.start_menu()

    def start_menu(self):
        def set_language(lang):
            def inner(ic, item):
                self.language = lang

            return inner

        def get_language(lang):
            def inner(item):
                return self.language == lang

            return inner

        if self.selection_rect:
            self.canvas.delete(self.selection_rect)
        if self.butt:
            self.butt.place_forget()
        if not self.icon:
            self.icon = pystray.Icon("GPTShot", self.image, menu=pystray.Menu(
                pystray.MenuItem("Make a shot", self.show_window),
                pystray.MenuItem("Language", pystray.Menu(
                    pystray.MenuItem(
                        "ENG",
                        set_language("ENG"),
                        checked=get_language("ENG"),
                        radio=True),
                    pystray.MenuItem(
                        "DEU",
                        set_language("DEU"),
                        checked=get_language("DEU"),
                        radio=True),
                    pystray.MenuItem(
                        "UKR",
                        set_language("UKR"),
                        checked=get_language("UKR"),
                        radio=True)
                )),
                pystray.MenuItem("Exit", self.quit_window)
            ))

            self.icon.run()
            self.root_window.deiconify()

    def ok(self):
        text = screen_shot(self.start_x, self.start_y, self.cur_x, self.cur_y, self.shift, self.language)
        self.root_window.withdraw()
        self.output_window.deiconify()
        self.output_area.insert(tk.END, text)
        self.output_window.focus_force()
        self.start_menu()

        # self.hide_w()
        # self.output_area.insert(tk.END, text)
        # self.output_window.deiconify()

        # self.hide_w()
        # self.output_window.deiconify()

    def on_close_output(self):
        self.output_window.destroy()
        self.output_window, self.output_area = None, None



# if __name__ == "__main__":
#     root = tk.Tk()
#     root.attributes("-fullscreen", True)
#     root.attributes("-alpha", 0.4)
#     root.bind("<Escape>", lambda e, r=root: r.destroy())
#     app = DragSelectApp(root)
#     root.mainloop()










