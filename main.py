import PIL.Image
import tkinter as tk
import window_geometry
from tests import DragSelectApp


s = window_geometry.monitor_areas()
image = PIL.Image.open("ukr_text.jpg")
root = tk.Tk()
root.overrideredirect(True)
root.geometry(window_geometry.size())
root.attributes("-alpha", 0.4)
app = DragSelectApp(root, image, min(siz[0] for siz in s))
root.bind("<Escape>", lambda e: app.hide_w())
app.hide_w()
root.mainloop()
