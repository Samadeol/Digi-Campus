import pyqrcode
url = pyqrcode.create('http://172.23.34.5:8000/entry')
url.png('qr.png', scale=1.5)
