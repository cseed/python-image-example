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

    # Set the (terrain) color to green.
    color = (0, 255, 0)

    # We specify coordinates for lines on the unit scale from [0.0,
    # 1.0].  This helper function scales lines on the unit scale to
    # the width x height scale of the image.
    def scale_line(line):
        # Subtract height coordinates from 1.0 because unit
        # coordinates have the origin (0, 0) in the lower-left, but
        # PIL images have the origin in the upper-right.
        return [width*line[0], height*(1.0 - line[1]), width*line[2], height*(1.0 - line[3])]

    # Points for the terrain.  Initially empty.  We will laod them
    # from a file.
    heights = []

    # Open the file 'heights.txt'
    with open('heights.txt', 'r') as f:
        # For each line
        for line in f:
            # Strip any leading or, more importantly, trailing white
            # space (e.g. a newline character)
            line = line.strip()
            # If the line is not empty
            if line:
                # Convert it to a float and add it to the list of heights
                heights.append(float(line))
        
    N = len(heights)
    # For each point, not including the last one
    for i in range(N - 1):
        # Draw a line from this point to the next one.  The
        # x-coordinates are equally spaced.
        draw.line(scale_line([i / N, heights[i],
                              (i + 1) / N, heights[i + 1]]),
                  fill=color, width=2)

    # Save the image to a file.
    image.save('output.png')

# Run the main function.
main()

