'''
Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral! You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.

The pixels in the input image are represented as integers. The algorithm distorts the input image in the following way: Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, including x itself. All the pixels on the border of x are then removed.

Return the blurred image as an integer, with the fractions rounded down.
'''
def boxBlur(image):
    size = 3
    blur = lambda x, y: int(sum(e for row in image[y:y+size] for e in row[x:x+size]) / (size * size))
    h = len(image)
    w = len(image[0])
    result = []
    for y in range(h - size + 1):
        a = []
        for x in range(w - size + 1):
            a.append(blur(x, y))
        result.append(a)
    return result


if __name__ == "__main__":
    image = [[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]]
    boxBlur(image)

