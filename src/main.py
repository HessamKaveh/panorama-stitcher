import cv2

from stitcher import PanoramaStitcher
from matcher import FeatureMatcher
from visualize import draw_matches


LEFT_IMAGE = "../images/left.jpg"
RIGHT_IMAGE = "../images/right.jpg"

OUTPUT = "../outputs/panorama.jpg"
MATCH_OUTPUT = "../outputs/matches.jpg"



def main():


    left = cv2.imread(
        LEFT_IMAGE
    )


    right = cv2.imread(
        RIGHT_IMAGE
    )


    if left is None or right is None:

        print(
            "Images not found"
        )

        return



    matcher = FeatureMatcher()


    match_result = matcher.match(
        left,
        right
    )


    if match_result is None:

        print(
            "No enough matches"
        )

        return



    matches_image = draw_matches(

        left,

        right,

        match_result

    )


    cv2.imwrite(

        MATCH_OUTPUT,

        matches_image

    )



    stitcher = PanoramaStitcher()


    panorama = stitcher.stitch(

        left,

        right

    )


    if panorama is None:

        print(
            "Stitching failed"
        )

        return



    cv2.imwrite(

        OUTPUT,

        panorama

    )


    print(
        "Panorama saved:",
        OUTPUT
    )


    print(
        "Matches saved:",
        MATCH_OUTPUT
    )



if __name__ == "__main__":

    main()
