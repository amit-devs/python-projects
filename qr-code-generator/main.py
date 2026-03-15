import qrcode
data=input("Enter the URL: ").strip()
file_name=input("Enter the file name: ").strip()
qr=qrcode.QRCode(box_size=15,border=10)
qr.add_data(data)
img=qr.make_image(fill_color="white",back_color="black") # You can Customize the colors of your QR
img.save(f"output/{file_name}.png")
print("QR Code Generated Successfully")