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
```

## Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Put images:

images/

├── left.jpg

└── right.jpg

## Run:

```bash
cd src

python main.py
```

## Output

Generated files:

outputs/

├── panorama.jpg

└── matches.jpg

## Technologies

* Python

* OpenCV

* NumPy

## Computer Vision Concepts

* Feature Detection

* Feature Matching

* Homography

* RANSAC
Image Warping
