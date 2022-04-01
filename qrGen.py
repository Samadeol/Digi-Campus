import pyqrcode
for i in range(1,14):
    url = pyqrcode.create('https://digi-campus.herokuapp.com/entry/'+str(i))
    url.png('Entry'+str(i)+'.png',scale=5)
