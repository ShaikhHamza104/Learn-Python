import  qrcode
from  PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

data = "https://www.google.com"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="white")
img.save("qrcode.png")