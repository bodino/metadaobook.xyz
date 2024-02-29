from PIL import Image
import numpy as np
from scipy.ndimage import gaussian_filter

# grey #262626
# blue #49a3fc
# red'#fc4949'
def process_image_with_custom_colors(image_path, output_path, threshold=128, color1='#fc4949', color2='#49a3fc'):
    """
    Process an image to convert it to a representation based on custom colors and a brightness threshold.

    Parameters:
    - image_path: str, path to the input image.
    - output_path: str, path where the output image will be saved.
    - threshold: int, custom brightness threshold for converting pixels (default is 128).
    - color1: str, hex color code for the first color (default is '#262626').
    - color2: str, hex color code for the second color (default is '#fc4949').
    """
    # Convert hex colors to RGB tuples
    color1_rgb = tuple(int(color1.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    color2_rgb = tuple(int(color2.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

    # Load the image
    image = Image.open(image_path)

    # Convert the image to grayscale
    gray_image = image.convert('L')

    # Apply the custom threshold
    thresholded = gray_image.point(lambda p: 255 if p > threshold else 0)

    # Convert the thresholded image to an RGB image
    rgb_image = np.array(thresholded.convert('RGB'))

    # Apply custom colors based on the threshold
    # Use numpy indexing for efficiency
    mask = rgb_image[:, :, 0] > 128  # Mask for pixels to change to color2
    rgb_image[~mask] = color1_rgb  # Apply color1 to pixels below or equal to the threshold
    rgb_image[mask] = color2_rgb  # Apply color2 to pixels above the threshold

    # Convert back to an image
    final_image = Image.fromarray(rgb_image)
    # # Save the final image
    final_image.save(output_path)

    # Uncomment the following line to display the image directly in a Jupyter notebook environment
    # final_image.show()

def add_grain_effect(image_path, output_path, intensity=8, grain_size=1):
    """
    Add a subtle grain effect to an image by applying noise that marginally changes pixel colors based on surrounding pixels.

    Parameters:
    - image_path: str, path to the input image.
    - output_path: str, path where the output image will be saved.
    - intensity: int, the intensity of the noise (default is 5).
    - grain_size: float, the size of the grain effect (default is 1).
    """
    # Load the image
    image = Image.open(image_path)
    img_array = np.array(image)

    # Generate noise
    noise = np.random.normal(0, intensity, img_array.shape)

    # Apply a gaussian filter to the noise to simulate grain based on surrounding pixels
    blurred_noise = gaussian_filter(noise, sigma=grain_size)

    # Ensure the noise doesn't exceed the image's color bounds
    noisy_img_array = img_array + blurred_noise
    noisy_img_array = np.clip(noisy_img_array, 0, 255)

    # Convert back to an image
    noisy_image = Image.fromarray(noisy_img_array.astype('uint8'))

    # Save the final image
    noisy_image.save(output_path)

    # Uncomment the following line to display the image directly in a Jupyter notebook environment
    # noisy_image.show()





imagename = 'tree'
image_path = './input/tree.png'  # Replace with your actual image path
output_path = "./final/"+imagename+'daultone.png'  # Replace with your actual output path
output_path_grain = "./final/"+imagename+'final.png'
custom_threshold = 170  # Set your custom threshold value here
process_image_with_custom_colors(image_path, output_path, custom_threshold)
add_grain_effect(output_path, output_path_grain)
