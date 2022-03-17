import pyqrcode
# url = pyqrcode.create('http://127.0.0.1:8000/mess')
# url.svg('qr.svg', scale=2)

# print(url.terminal(quiet_zone=1))

hall12=pyqrcode.create('12')
hall12.png('12.png')
