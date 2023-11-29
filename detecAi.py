import os
import re
from PIL import Image
import pytesseract
import argparse

def extract_text(image_path):
    try:
        # Use Tesseract OCR to extract text
        text = pytesseract.image_to_string(Image.open(image_path))
        return text
    except Exception as e:
        return f"Error: {str(e)}"

def process_folder(folder_path, regex_patterns, batch_size, output_file):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder not found - {folder_path}")
        return

    # Compile regex patterns
    compiled_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in regex_patterns]

    # Iterate through all files in the folder
    image_paths = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the file is an image (you can customize the file extensions as needed)
        if os.path.isfile(file_path) and any(file_path.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png']):
            image_paths.append(file_path)

    # Process images in batches
    matched_images = []
    for i in range(0, len(image_paths), batch_size):
        batch = image_paths[i:i+batch_size]

        print(f"\nProcessing batch of {len(batch)} images:")
        for image_path in batch:
            print(f"\nProcessing image: {image_path}")

            # Extract text from the image
            extracted_text = extract_text(image_path)

            # Check if any regex pattern is matched in the extracted text
            if any(pattern.search(extracted_text) for pattern in compiled_patterns):
                print("Pattern matched!")
                print("Extracted Text:")
                print(extracted_text)

                # Save the name of the matched image
                matched_images.append(os.path.basename(image_path))
            else:
                print("No pattern matched.")

    # Save the names of matched images to a text file
    with open(output_file, 'w') as f:
        for img_name in matched_images:
            f.write(f"{img_name}\n")

    print(f"\nMatched Images saved to: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Batch Text Extraction Tool using Tesseract OCR")
    parser.add_argument("-f", "--folder", dest="folder_path", required=True, help="Path to the folder containing images for text extraction")
    parser.add_argument("-mr", "--regex", dest="regex_patterns", nargs="+", required=True, help="List of regex patterns to search for in the text")
    parser.add_argument("-bs", "--batch-size", dest="batch_size", type=int, default=25, help="Number of images to process in each batch")
    parser.add_argument("-o", "--output-file", dest="output_file", default="matched_images.txt", help="Output file to save the names of matched images")

    args = parser.parse_args()
    folder_path = args.folder_path
    regex_patterns = args.regex_patterns
    batch_size = args.batch_size
    output_file = args.output_file

    process_folder(folder_path, regex_patterns, batch_size, output_file)

if __name__ == "__main__":
    main()
