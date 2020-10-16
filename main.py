"""
This entire script can be replaced with the command
`echo $some_data | qr --error-correction=H`

"""

import qrcode
import sys

content = sys.stdin.read().strip()

print(content)


qr = qrcode.QRCode(
    version=None, # The version parameter is an integer from 1 to 40 that controls the size of the QR Code (the smallest, version 1, is a 21x21 matrix). Set to None and use the fit parameter when making the code to determine this automatically.
    error_correction=qrcode.constants.ERROR_CORRECT_H, # HIGH error correction (30%)
    box_size=2, # The size of each box in the QR code; effectively a scale factor
    border=4, # border width
)

qr.add_data(content)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.show()
