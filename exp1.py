from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def caesar_cipher_encrypt(value, key, max_value=255):
    return (value + key) % (max_value + 1)

def caesar_cipher_decrypt(value, key, max_value=255):
    return (value - key) % (max_value + 1)

def display_image(image, title):
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

def encrypt_image(input_image_path, output_image_path, key):
    img = Image.open(input_image_path).convert('L')
    img_array = np.array(img)

    encrypted_array = np.vectorize(lambda x: caesar_cipher_encrypt(x, key))(img_array)

    encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))
    encrypted_img.save(output_image_path)
    print(f"Encrypted image saved to {output_image_path}")

    display_image(img, "Original Image")
    display_image(encrypted_img, "Encrypted Image")

def decrypt_image(input_image_path, output_image_path, key):
    img = Image.open(input_image_path).convert('L')
    img_array = np.array(img)

    decrypted_array = np.vectorize(lambda x: caesar_cipher_decrypt(x, key))(img_array)

    decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))
    decrypted_img.save(output_image_path)
    print(f"Decrypted image saved to {output_image_path}")

    display_image(img, "Encrypted Image")
    display_image(decrypted_img, "Decrypted Image")

def generate_blank_image(encrypted_image_path, decrypted_image_path, output_image_path):
    encrypted_img = Image.open(encrypted_image_path).convert('L')
    decrypted_img = Image.open(decrypted_image_path).convert('L')

    encrypted_array = np.array(encrypted_img)
    decrypted_array = np.array(decrypted_img)

    blank_array = np.subtract(encrypted_array, decrypted_array, dtype=np.int16)
    blank_array = np.clip(blank_array, 0, 255).astype(np.uint8)

    blank_image = Image.fromarray(blank_array)
    blank_image.save(output_image_path)
    print(f"Blank image saved to {output_image_path}")

    display_image(blank_image, "Blank Image")

if __name__ == "__main__":
    key = int(input("Enter the Caesar cipher key (integer): "))

    encrypt_image('input_image_path.jpg', 'encrypted_image.png', key)

    decrypt_image('encrypted_image.png', 'decrypted_image.png', key)

    generate_blank_image('encrypted_image.png', 'decrypted_image.png', 'blank_image.png')
