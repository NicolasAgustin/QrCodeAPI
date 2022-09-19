import cv2
import qrcode
import numpy as np

from io import BytesIO
from PIL import Image
from flask import Response, send_file


def generate_qr(options: dict) -> Response:
    """ Function to generate the QR image based on the
        text.


    Args:
        options (dict): Dictionary with the options for generate
            the QRcode

    Returns:
        Response: Response
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(options['text'])
    qr.make(fit=True)

    img: Image = qr.make_image(
        fill_color=options['fill_color'],
        back_color=options['back_color']
    ).convert('RGB')

    img_io = BytesIO()
    img.save(img_io, 'JPEG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


def decode_qr(data: bytes):
    """ Function that receives an image and
        decode it to obtain the text

    Args:
        data (bytes): Image as bytes

    Raises:
        Exception: Raises an exception if it cannot decode
            QRcode

    Returns:
        _type_: _description_
    """
    image = np.asarray(bytearray(data), dtype='uint8')
    img = cv2.imdecode(image, cv2.IMREAD_COLOR)
    qr_detector = cv2.QRCodeDetector()

    data, vert_array, bin_qrcode = qr_detector.detectAndDecode(img)

    if vert_array is None:
        raise Exception(
            'No se pudo decodificar el codigo QR provisto.'
        )

    return data


if __name__ == '__main__':
    generate_qr('')
