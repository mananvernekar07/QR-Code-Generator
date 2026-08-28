import qrcode

data = input("Enter text or URL: ")

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color="black", back_color="white")

image.save("qrcode.png")

print("QR code saved successfully!")