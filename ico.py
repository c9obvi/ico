import os
from tkinter import Tk, filedialog
from PIL import Image
from tqdm import tqdm

def select_image():
    root = Tk()
    root.withdraw()  # Hide the root window
    root.lift()  # Bring the dialog to the front
    root.attributes('-topmost', True)
    
    file_path = filedialog.askopenfilename(
        filetypes=[("PNG files", "*.png")], title="Select a PNG image"
    )
    root.destroy()
    return file_path

def convert_to_ico(png_path):
    output_path = os.path.splitext(png_path)[0] + ".ico"
    img = Image.open(png_path)
    img.save(output_path, format="ICO")

    return output_path

def main():
    user_input = input("Do you want to select an image? (y/n): ")
    if user_input.lower() == 'y':
        png_path = select_image()
        if png_path:
            print(f"Selected file: {png_path}")
            print("Converting to ICO...")
            for _ in tqdm(range(100), desc="Progress", ascii=True):
                convert_to_ico(png_path)
            print(f"ICO file saved in the same directory: {convert_to_ico(png_path)}")
        else:
            print("No file selected. Exiting.")
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    main()
