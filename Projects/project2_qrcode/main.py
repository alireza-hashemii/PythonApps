import qrcode
import PIL
import qrcode.constants

qr = qrcode.QRCode(version=1 , error_correction=qrcode.constants.ERROR_CORRECT_H, border=4, box_size=15)


qr.add_data('https://drive.google.com/file/d/1Hgvy4grh3UtWLhvmyuEq3-4Q1jpVtjEO/view?usp=drive_link')
qr.make(fit=True)


image = qr.make_image(fill_color= 'black', back_color='white')
image.save('qrcode_image.png')