import pytesseract
from PIL import ImageGrab


def screen_shot(sx, sy, x, y, shift, language):
    im = ImageGrab.grab(bbox=(sx+shift, sy, x+shift, y), all_screens=True)

    conf = r'--psm 3 --oem 3 -l ' + (r'eng' if language == "ENG" else r'deu' if language == "DEU" else r'ukr')

    text = pytesseract.image_to_string(im, config=conf)

    return text
# im = Image.open("Screenshot 2023-09-06 094107.png")
#
# conf = r'--psm 3 --oem 3 -l eng'
#
# text = pytesseract.image_to_string(im, config=conf)
#
# print(text)
