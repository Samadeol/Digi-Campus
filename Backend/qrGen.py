import pyqrcode
url = pyqrcode.create('http://192.168.0.111:8000/entry')
url.png('qr.png', scale=2)