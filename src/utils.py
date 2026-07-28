import cv2


def resize(image, width=800):

    h, w = image.shape[:2]

    ratio = width / w

    height = int(
        h * ratio
    )

    return cv2.resize(
        image,
        (
            width,
            height
        )
    )
