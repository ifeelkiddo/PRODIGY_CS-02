from PIL import Image # type: ignore

def encrypt_image(input_path, output_path, key):
    
    #open the image
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            encrypted_pixel = (b, g, r)
            pixels[i, j] = encrypted_pixel

    #save the encrypted image
    img.save(output_path)
    print("Image encrypted successfully!!")

def decrypt_image(input_path, output_path, key):
    
    #open the incrypted image
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            decrypted_pixel = (b, g, r)

            pixels[i, j] = decrypted_pixel
    #save the decrypted image
    img.save(output_path)
    print("image decrypted successfully!!")

input_image = r"C:\Users\aayus\OneDrive\Desktop\task2\input.jpg" #replace with your image path
encrypted_image = r"C:\Users\aayus\OneDrive\Desktop\task2\decrypted_image.jpg"
decrypted_image = r"C:\Users\aayus\OneDrive\Desktop\task2\encrypted_image.jpg"

# Encrypt the image
encrypt_image(input_image, encrypted_image, key=None)

# Decrypt the image
decrypt_image(encrypted_image, decrypted_image, key=None)