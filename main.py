from cv2 import cv2
import pyqrcode
import io
import numpy as np
import sys

content = ""
for line in sys.stdin:
  content += line

print(content.rstrip())

buffer = io.BytesIO()

qr = pyqrcode.create(content.rstrip())
qr.png(buffer, scale=2)

buffer.seek(0)

array = np.asarray(bytearray(buffer.read()), dtype=np.uint8)
image = cv2.imdecode(array, cv2.IMREAD_COLOR)
# cv2.namedWindow("QR code", cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty("QR code",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.imshow('QR code', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
sys.exit()