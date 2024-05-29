"""Task-02 Pixel Manipulation for Image Encryption


Develop a simple image encryption tool using pixel manipulation.
 You can perform operations like swapping pixel values or applying a basic mathematical operation
  to each pixel. Allow users to encrypt and decrypt images."""

from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # swapping red and blue channels
            encrypted_pixel = (b, g, r)

            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # swapping red and blue channels back
            decrypted_pixel = (b, g, r)

            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image decrypted successfully!")

 # image path
input_image = r"C:\Users\user\PycharmProjects\Internship\PRODIGY_CS-02-main\input.jpg"
encrypted_image = r"C:\Users\user\PycharmProjects\Internship\PRODIGY_CS-02-main\decrypted_image.jpg"
decrypted_image = r"C:\Users\user\PycharmProjects\Internship\PRODIGY_CS-02-main\encrypted_image.jpg"


# Encrypt the image
encrypt_image(input_image, encrypted_image, key=None)

# Decrypt the image
decrypt_image(encrypted_image, decrypted_image, key=None)
