import qrcode as qr

img = qr.make("http://192.168.158.142:8000")

img.save("desshop.png")