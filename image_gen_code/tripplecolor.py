from PIL import Image
import numpy as np

def process_image_with_triple_threshold(image_path, output_path, thresholds, colors):
    """
    Process an image to convert it to a representation based on three custom colors and thresholds.

    Parameters:
    - image_path: str, path to the input image.
    - output_path: str, path where the output image will be saved.
    - thresholds: list of int, brightness thresholds for converting pixels.
    - colors: list of str, hex color codes for the colors.
    """
    # Convert hex colors to RGB tuples
    colors_rgb = [tuple(int(colors[i].lstrip('#')[j:j+2], 16) for j in (0, 2, 4)) for i in range(3)]

    # Load the image
    image = Image.open(image_path).convert('L')  # convert image to grayscale

    # Apply the thresholds
    image_array = np.array(image)
    mask1 = image_array < thresholds[0]
    mask2 = (thresholds[0] <= image_array) & (image_array < thresholds[1])
    mask3 = image_array >= thresholds[1]

    # Create a new RGB image
    color_image_array = np.zeros((image_array.shape[0], image_array.shape[1], 3), dtype=np.uint8)

    # Apply the colors based on the thresholds
    color_image_array[mask1] = colors_rgb[0]
    color_image_array[mask2] = colors_rgb[1]
    color_image_array[mask3] = colors_rgb[2]

    # Convert the numpy array to an image
    color_image = Image.fromarray(color_image_array)

    # Save the final image
    color_image.save(output_path)
    return output_path

# Define the image paths and parameters
imagename = 'market'
image_path = './input/market.png'  # Replace with your actual image path
output_path = "./final/"+imagename+'daultone.png'  # Replace with your actual output path
thresholds = [150, 200]  # Define the thresholds
colors = ['#49a3fc','#fc4949','#262626' ]  # Define the colors

# Process the image
output_file_path = process_image_with_triple_threshold(image_path, output_path, thresholds, colors)
