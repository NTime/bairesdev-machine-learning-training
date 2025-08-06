# Dimensionality Reduction

A script to reduce image colors to shades of gray and black and white without using libraries for the transformation.

## Notes

- For the transformation, "ITU-R BT.601" formula was used.

- Adjust the threshold for better clarity on black and white outputs.
    - Lower: If too black
    - Higher: If too white

For the two images in this repository the threshold was adjusted as follows:

- [Bird](./images/bird-andrei-r-popescu.jpg): 90
- [Woman](./images/pexels.jpg): 110

## Credits

Photos:

- Bird: Andrei R. Popescu via Unsplash
- Woman: Hardeep Singh via Pexels
