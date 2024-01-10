# detectAi is Image Text Extraction with Tesseract OCR

## Description
This Python script processes a folder of images, extracts text using Tesseract OCR, and matches the extracted text against specified regex patterns. It is designed to handle batch processing of images and identifies images that contain text matching the given patterns.

## Installation

### Prerequisites
- Python 3.x
- Tesseract OCR installed on your system

### Dependencies
Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

## Tesseract OCR

Ensure Tesseract OCR is installed on your system. Installation instructions can be found at Tesseract's GitHub repository.
Usage

Run the script with the following command:

```
python script_name.py -f [folder_path] -mr [regex_patterns] -bs [batch_size] -o [output_file]

```

+ -f/--folder: Path to the folder containing images.
+ -mr/--regex: List of regex patterns to search in the text.
+ -bs/--batch-size: Number of images to process in each batch (default: 25).
+ -o/--output-file: Output file to save the names of matched images (default: matched_images.txt)

## Example

```
python script_name.py -f ./images -mr "\\d{3}-\\d{2}-\\d{4}"  -bs 10 -o results.txt
```
## Contributing

Contributions to this project are welcome. Please fork the repository and open a pull request with your changes or suggestions.

## Acknowledgments

    Tesseract OCR, for the OCR engine.
    Pillow, for image processing capabilities.
