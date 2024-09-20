import os
import subprocess
from tkinter import Tk, filedialog
from PIL import Image
from tqdm import tqdm

def select_image():
    root = Tk()
    root.withdraw()  # Hide the root window
    root.lift()  # Bring the dialog to the front
    root.attributes('-topmost', True)
    
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Image files", "*.png;*.jpg;*.jpeg;*.webp"),
            ("PNG files", "*.png"),
            ("JPEG files", "*.jpg;*.jpeg"),
            ("WebP files", "*.webp"),
        ],
        title="Select an image"
    )
    root.destroy()
    return file_path

def select_color():
    colors = {
        '1': ('White', '#FFFFFF'),
        '2': ('Black', '#000000'),
        '3': ('Red', '#FF0000'),
        '4': ('Blue', '#0000FF'),
        '5': ('Orange', '#FFA500')
    }
    
    print("Select a color for the SVG:")
    for key, (color_name, _) in colors.items():
        print(f"{key}. {color_name}")
    
    while True:
        choice = input("Enter your choice (1-5): ")
        if choice in colors:
            return colors[choice]  # Return both color name and hex code
        print("Invalid choice. Please try again.")

def check_potrace_installed():
    try:
        subprocess.run(['potrace', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def convert_to_svg(image_path, color_info):
    color_name, color_hex = color_info
    # Open the image and convert it to black and white
    img = Image.open(image_path)
    img = img.convert('L')  # Convert to grayscale
    img = img.point(lambda x: 0 if x < 128 else 255, '1')  # Convert to black and white

    # Save as PBM file
    pbm_path = os.path.splitext(image_path)[0] + ".pbm"
    img.save(pbm_path, format='PPM')

    # Use potrace to convert PBM to SVG
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    svg_path = f"{os.path.dirname(image_path)}/{base_name}_{color_name.lower()}.svg"
    try:
        subprocess.run(['potrace', pbm_path, '-s', '-o', svg_path, '-C', color_hex], check=True)
    except subprocess.CalledProcessError as e:
        print("Error during conversion:", e)
        return None

    # Remove the temporary PBM file
    os.remove(pbm_path)

    return svg_path

def main():
    if not check_potrace_installed():
        print("Error: 'potrace' is not installed on your system.")
        print("Please install 'potrace' and try again.")
        return

    user_input = input("Do you want to select an image? (y/n): ")
    if user_input.lower() == 'y':
        image_path = select_image()
        if image_path:
            print(f"Selected file: {image_path}")
            color_info = select_color()
            print(f"Selected color: {color_info[0]}")
            print("Converting to SVG...")
            for _ in tqdm(range(100), desc="Progress", ascii=True):
                pass  # Just for the progress bar effect
            svg_path = convert_to_svg(image_path, color_info)
            if svg_path:
                print(f"SVG file saved: {svg_path}")
            else:
                print("Conversion failed.")
        else:
            print("No file selected. Exiting.")
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    main()
