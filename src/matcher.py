import cv2
import numpy as np


class FeatureMatcher:

    def __init__(self):

        self.orb = cv2.ORB_create(
            nfeatures=3000
        )

        self.matcher = cv2.BFMatcher(
            cv2.NORM_HAMMING,
            crossCheck=True
        )

    def detect_and_describe(self, image):

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        keypoints, descriptors = self.orb.detectAndCompute(
            gray,
            None
        )

        return keypoints, descriptors

    def match(self, imageA, imageB):

        kpA, desA = self.detect_and_describe(
            imageA
        )

        kpB, desB = self.detect_and_describe(
            imageB
        )

        if desA is None or desB is None:
            return None

        matches = self.matcher.match(
            desA,
            desB
        )

        matches = sorted(
            matches,
            key=lambda x: x.distance
        )

        if len(matches) < 10:
            return None

        ptsA = np.float32(
            [
                kpA[m.queryIdx].pt
                for m in matches
            ]
        ).reshape(-1,1,2)

        ptsB = np.float32(
            [
                kpB[m.trainIdx].pt
                for m in matches
            ]
        ).reshape(-1,1,2)

        H, mask = cv2.findHomography(
            ptsB,
            ptsA,
            cv2.RANSAC,
            5.0
        )

        if H is None:
            return None

        return {
            "homography": H,
            "matches": matches,
            "kpA": kpA,
            "kpB": kpB
        }
