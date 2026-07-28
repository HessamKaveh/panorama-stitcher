import cv2

from stitcher import PanoramaStitcher


LEFT_IMAGE = "../images/left.jpg"
RIGHT_IMAGE = "../images/right.jpg"

OUTPUT = "../outputs/panorama.jpg"


def main():

    left = cv2.imread(LEFT_IMAGE)

    right = cv2.imread(RIGHT_IMAGE)

    if left is None:
        print("Cannot load left image")
        return

    if right is None:
        print("Cannot load right image")
        return

    stitcher = PanoramaStitcher()

    panorama = stitcher.stitch(
        left,
        right
    )

    if panorama is None:
        print("Stitching failed")
        return

    cv2.imwrite(
        OUTPUT,
        panorama
    )

    cv2.imshow(
        "Panorama",
        panorama
    )

    cv2.waitKey(0)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
