import cv2


def draw_matches(
    imageA,
    imageB,
    matcher_result
):

    kpA = matcher_result["kpA"]

    kpB = matcher_result["kpB"]

    matches = matcher_result["matches"][:50]


    output = cv2.drawMatches(

        imageA,

        kpA,

        imageB,

        kpB,

        matches,

        None,

        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS

    )


    return output
