import qrcode
from PIL import Image

qr = qrcode.QRCode(version = 1,
                   error_correction= qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=4,)
qr.add_data("http://192.168.158.142:8000")
qr.make(fit=True)
img = qr.make_image(fill_color = 'red', back_color = 'grey')
img.save("stackoverflow2.png")
