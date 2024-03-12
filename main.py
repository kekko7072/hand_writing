import cv2
import pytesseract


# Update the pytesseract tesseract_cmd attribute to point to the binary if it's not in the PATH
# Example for a typical installation location on macOS:
# pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

# Function to preprocess the image
def preprocess_image(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, thresh_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return thresh_img


# Function to extract text from the preprocessed image
def extract_text_from_image(image):
    # Extract text from image
    extracted_text = pytesseract.image_to_string(image)

    return extracted_text


if __name__ == "__main__":
    # Path to the image file
    image_path = 'test.jpeg'

    # Preprocess the image
    preprocessed_image = preprocess_image(image_path)

    # Extract text from the preprocessed image
    text = extract_text_from_image(preprocessed_image)

    print("Extracted Text:")
    print(text)
