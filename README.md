# Image Converter

This project contains two Python scripts for converting images: one for PNG to ICO conversion and another for image to SVG conversion with color options.

## Features

- PNG to ICO conversion
- Image to SVG conversion with color selection
- User-friendly command-line interface
- Progress bar for visual feedback

## Requirements

> [!IMPORTANT]  
> Make sure you have the following installed:
> - Python 3.x
> - Pillow library
> - tqdm library
> - potrace (for SVG conversion)

## Installation

1. Clone this repository
2. Install required Python libraries:
   ```
   pip install Pillow tqdm
   ```
3. Install potrace:
   - On macOS: `brew install potrace`
   - On Ubuntu: `sudo apt-get install potrace`
   - On Windows: Download from [potrace website](http://potrace.sourceforge.net/)

## Usage

### PNG to ICO Conversion

Run the following command:

```
python png_to_ico.py <path_to_png_file>
```

### Image to SVG Conversion

Run the following command:

```
python svg.py <path_to_image_file>
```

## Color Options for SVG

When converting to SVG, you can choose from the following colors:

1. White
2. Black
3. Red
4. Blue
5. Orange

> [!CAUTION]
> The color selection affects the foreground color of the SVG. The background will be transparent.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).