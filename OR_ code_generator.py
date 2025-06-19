import  qrcode
data = input("enter the text or URL:").strip()
filename = input(" enter the file name:").strip()
qr = qrcode.QRCode(box_size=10 ,border=4 )
qr.add_data(data)
image=qr.make_image(fill_color='black', black_color='white')
image.save(filename)
print(f'file saved as name{filename}')