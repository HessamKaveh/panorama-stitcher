# Panorama Stitcher using OpenCV


A computer vision project that creates panoramic images by stitching multiple images together.


## Features

- ORB feature detection
- Feature descriptor extraction
- Brute Force feature matching
- Homography estimation using RANSAC
- Perspective warping
- Automatic panorama generation



## Pipeline


Input Images

↓

ORB Feature Detection

↓

Feature Matching

↓

Homography Estimation

↓

Perspective Transformation

↓

Panorama Image



## Installation


Create environment:


```bash
python3 -m venv venv

source venv/bin/activate
