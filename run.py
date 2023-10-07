from io import BytesIO
import win32clipboard
from PIL import ImageGrab, Image
from pynput.keyboard import GlobalHotKeys
import pystray
from pystray import MenuItem as item


def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()


def remove_header():
    print('removing header')
    im = ImageGrab.grabclipboard()
    output = BytesIO()
    im.save(output, "BMP")
    data = output.getvalue()[14:]  # removes the BMP header (14 bytes) | clipboard only uses DIB
    output.close()
    send_to_clipboard(win32clipboard.CF_DIB, data)


def onQuit():
    icon.visible = False
    icon.stop()


listener = GlobalHotKeys({'<ctrl>+<alt>+x': remove_header})
listener.start()

image = Image.open('icon.png')
menu = (
        item('Behead', remove_header, default=True),
        item('Quit', onQuit)
        )

icon = pystray.Icon('BeheadBMP', image, 'BeheadBMP', menu)
icon.run()
