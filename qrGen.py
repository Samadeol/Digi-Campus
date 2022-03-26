import pyqrcode
url = pyqrcode.create('https://gentle-temple-87499.herokuapp.com/entry')
url.png('qrexit.png',scale=5)
