
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

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

# Example usage:
image_path = './final/marketdaultone.png'  # Use the path to your processed image
output_path = './final/marketdaultonewithnoise.png'  # Specify your desired output path
add_grain_effect(image_path, output_path)
