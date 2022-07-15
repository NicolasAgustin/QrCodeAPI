import cv2
import qrcode
import numpy as np

from io import BytesIO
from PIL import Image
from flask import Response, send_file


def generate_qr(text: str) -> Response:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)

    img: Image = qr.make_image(
        fill_color='black',
        back_color='white'
    ).convert('RGB')

    img_io = BytesIO()
    img.save(img_io, 'JPEG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


def decode_qr(data: bytes):
    image = np.asarray(bytearray(data), dtype='uint8')
    img = cv2.imdecode(image, cv2.IMREAD_COLOR)
    qr_detector = cv2.QRCodeDetector()

    data, vert_array, bin_qrcode = qr_detector.detectAndDecode(img)

    if vert_array is None:
        raise Exception(
            'No se pudo decodificar el codigo QR provisto.'
        )

    print(data)

    return data


if __name__ == '__main__':
    generate_qr('')
