
# 🖼️ Image Grouper - Group Similar Images using Perceptual Hashing 🖼️

## Project Overview 📜

**Image Grouper** is a Python-based tool that groups visually similar images from a source folder and organizes them into subfolders in an output directory. It uses **perceptual hashing** to compare images by content, making it highly effective in identifying near-duplicate or similar images even if they differ slightly in size, format, or lighting. 

This tool is ideal for anyone looking to organize large collections of images by grouping duplicates or visually related photos together.

## Features ✨

- **Perceptual Hashing**: Images are compared based on their content, allowing for grouping of visually similar images.
- **Customizable Grouping**: Set the threshold for similarity to fine-tune how strictly images are grouped.
- **Efficient Image Processing**: Fast processing using multi-level file and image handling techniques.
- **Easy File Management**: The tool automatically creates subfolders for grouped images.
- **Supports Grouping and Removal**: You can either group similar images or remove duplicates.

## Project Structure 🏗️

The project is organized into several modules for ease of maintenance and extensibility:

```
image_grouper/
│
├── image_grouper.py        # Main file to execute the application
├── grouping/
│   ├── __init__.py         # Marks this directory as a Python package
│   ├── group_images.py     # Contains the grouping logic
│   └── image_handler.py    # Handles individual image hashing and comparison
│
├── utils/
│   ├── __init__.py         # Marks this directory as a Python package
│   └── file_utils.py       # Handles file operations (listing files, copying, etc.)
│
├── README.md               # Project documentation
└── config.py               # Configuration file with constants like resizing dimensions
```

## How It Works ⚙️

This project uses **perceptual hashing** to compare images based on their content, converting images to grayscale, resizing them, and then creating a hash based on the brightness of adjacent pixels.

1. **Image Hashing**: Each image is hashed using its pixel values, generating a unique but comparable hash.
2. **Hash Comparison**: Similar images have similar hashes, and the Hamming distance between two hashes is used to determine their similarity.
3. **Grouping**: Images with a Hamming distance below a configurable threshold are grouped together.
4. **Output**: Images are copied into subfolders in the output directory, each folder representing a group of similar images.

## Installation & Setup 💻

### Prerequisites:

- **Python 3.6+**
- **Pillow** library for image processing

### Installation Steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/image_grouper.git
   cd image_grouper
   ```

2. **Install Dependencies**:
   Install the necessary Python libraries using:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application:

To run the application, use the following command:

```bash
python image_grouper.py <input_folder> <output_folder> [group/remove]
```

#### Example:
```bash
python image_grouper.py ./images ./output group
```

This will group similar images from the `./images` folder into the `./output` folder.

### Configuration:

You can adjust settings like image size and similarity threshold in the `config.py` file:

- `Default_Resize_Width`: Resize width for image processing (default: 80 pixels).
- `Default_Resize_Height`: Resize height for image processing (default: 80 pixels).
- `Same_Image_Value`: Threshold for determining if two images are similar (default: 600).

## File Overview 📂

- **image_grouper.py**: Main script to execute the image grouping process.
- **grouping/group_images.py**: Contains the logic to group images based on their hash values.
- **grouping/image_handler.py**: Handles image resizing, hashing, and comparison.
- **utils/file_utils.py**: Utility functions for file handling, such as reading image files and computing hash differences.
- **config.py**: Stores configuration settings such as image dimensions and hash similarity threshold.

## Contribution 🤝

We welcome contributions to improve this project! If you'd like to contribute, please fork the repository, make your changes, and create a pull request. Be sure to include unit tests for any new features or fixes.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact 📧

If you have any questions or suggestions, feel free to reach out:

- **Email**: jferroal@gmail.com
- **GitHub**: [GitHub Profile](https://github.com/your-profile)

Happy image grouping! 🎉
