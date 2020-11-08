import qrcode


data = '123456789012345678901234567890'
img = qrcode.make(data)
filename = 'sampledInteger.png'
img.save(filename)

#extremely simple sample code to generate the QR code with given data.
#If there is a certian preference regarding the appearance of it, let me know
