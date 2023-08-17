from PIL import Image, ImageDraw
import random

def main():
    width = 640
    height = 480

    # Create an all-white (width, height)-sized image.  A color is a
    # 3-tuple (red, green, blue), where the color components red,
    # etc. are integers from 0-255.  Black is (0, 0, 0).  White is
    # (255, 255, 255).
    #
    # Image.new is documented here:
    # https://pillow.readthedocs.io/en/latest/reference/Image.html#PIL.Image.new
    image = Image.new('RGB', (width, height), color=(255, 255, 255))

    # draw can draw basic shapes like lines.
    #
    # ImageDraw.Draw is documented here:
    # https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html#PIL.ImageDraw.Draw
    draw = ImageDraw.Draw(image)

    # Draw 10 random colored lines.
    for _ in range(10):
        # random.randrange(end) returns a random integer from the
        # range from 0 to end-1.  In other words, it is the range [0,
        # end) inclusive of 0 and exclusive of end.
        #
        # random.randrange is documented here:
        # https://docs.python.org/3/library/random.html#random.randrange
        startx = random.randrange(width)
        starty = random.randrange(height)
        endx = random.randrange(width)
        endy = random.randrange(height)

        r = random.randrange(255)
        g = random.randrange(255)
        b = random.randrange(255)

        color = (r, g, b)

        # ImageDraw.draw is documented here:
        # https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.line
        draw.line([startx, starty, endx, endy], fill=color, width=2)
        
    # Save the image to a file.
    image.save('output.png')

# Run the main function.
main()

