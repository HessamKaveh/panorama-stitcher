import cv2
import numpy as np

from matcher import FeatureMatcher


class PanoramaStitcher:

    def __init__(self):

        self.matcher = FeatureMatcher()


    def stitch(self, left, right):

        result = self.matcher.match(
            left,
            right
        )

        if result is None:

            return None


        H = result["homography"]


        h_left, w_left = left.shape[:2]
        h_right, w_right = right.shape[:2]


        panorama = cv2.warpPerspective(

            right,

            H,

            (
                w_left + w_right,
                max(h_left, h_right)
            )

        )


        panorama[
            0:h_left,
            0:w_left
        ] = left


        panorama = self.crop_black(
            panorama
        )


        return panorama


    def crop_black(self, image):

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )


        _, thresh = cv2.threshold(

            gray,

            1,

            255,

            cv2.THRESH_BINARY

        )


        contours, _ = cv2.findContours(

            thresh,

            cv2.RETR_EXTERNAL,

            cv2.CHAIN_APPROX_SIMPLE

        )


        if len(contours) == 0:

            return image


        largest = max(

            contours,

            key=cv2.contourArea

        )


        x, y, w, h = cv2.boundingRect(
            largest
        )


        return image[
            y:y+h,
            x:x+w
        ]
