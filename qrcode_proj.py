import qrcode
from PIL import Image

#I've tested the QR code on my S10+ and it does  take me to my github repo!

img = qrcode.make("Your input text goes here!")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

#your website can go here!
qr.add_data('https:// .....')

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

img.save("qrcode_sample.png")

#Add an image in the project folder, then replace the "me.jpg" to your image name.
logo_display = Image.open("me.jpg")

logo_display.thumbnail((60,60))

logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)

img.paste(logo_display, logo_pos)

img.save("my_qrcode.png")