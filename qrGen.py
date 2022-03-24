import pyqrcode
url = pyqrcode.create('https://gentle-temple-87499.herokuapp.com/exit')
url.png('qrexit.png',scale=5)
