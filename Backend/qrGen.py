import pyqrcode
url = pyqrcode.create('http://192.168.0.111:8000/hall')
url.png('qr.png', scale=2)

# print(url.terminal(quiet_zone=1))

# hall12=pyqrcode.create('12')
# hall12.png('12.png')
