import pyqrcode
url = pyqrcode.create('http://172.23.19.192:8000/entry')
url.png('qr.png', scale=4)