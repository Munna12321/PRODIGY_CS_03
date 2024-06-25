from PIL import Image

def encrypt_image(image_path, key):
    try:
        with Image.open(image_path) as img:
            pixels = img.load()
            width, height = img.size

            for py in range(height):
                for px in range(width):
                    r, g, b = pixels[px, py]
                    pixels[px, py] = (r ^ key, g ^ key, b ^ key)

        img.save("encrypted_image.png")
        print("Image encrypted successfully.")
    except Exception as e:
        print(f"Error during encryption: {e}")

def decrypt_image(image_path, key):
    try:
        with Image.open(image_path) as img:
            pixels = img.load()
            width, height = img.size

            for py in range(height):
                for px in range(width):
                    r, g, b = pixels[px, py]
                    pixels[px, py] = (r ^ key, g ^ key, b ^ key)

        img.save("decrypted_image.png")
        print("Image decrypted successfully.")
    except Exception as e:
        print(f"Error during decryption: {e}")

if __name__ == "__main__":
    image_path = input("Enter the path of the image: ")
    try:
        key = int(input("Enter the encryption/decryption key: "))
        # Encrypt the image
        encrypt_image(image_path, key)
        # Decrypt the image
        decrypt_image("encrypted_image.png", key)
    except ValueError:
        print("Invalid key. Please enter a valid integer.")
    except Exception as e:
        print(f"Unexpected error: {e}")
