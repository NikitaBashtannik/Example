import time

import pywinauto
from pywinauto.application import Application

app = Application(backend="uia").start(cmd_line=r"C:\Users\Admin\Desktop\PuTTY\putty.exe")
time.sleep(5)
app = Application().connect(title = "PuTTY Configuration")
window = app.PuTTYConfigBox
window.set_focus()
window[u"Host Name (or IP address):Edit"].type_keys("192.168.10.1")
window[u"Port:Edit"].type_keys("21")
window["Open"].click()
