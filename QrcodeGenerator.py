import qrcode

#pip install qrcode
input_URL = "ali mahjoob"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

qr.add_data(input_URL)
qr.make(fit=True)

img = qr.make_image(fill_color="Black", back_color="white")
img.save("qrcode.png")

print(qr.data_list)
