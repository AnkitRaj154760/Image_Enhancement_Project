# Image Enhancement Tool

A powerful, interactive web application built with Streamlit for editing and enhancing images. This tool allows users to apply various artistic filters, remove backgrounds, replace backgrounds, and fine-tune image properties like brightness, contrast, and sharpness.

## Features

- **Background Removal:** Seamlessly remove backgrounds from images using `rembg`.
- **Background Replacement:** Upload a new background to merge with your subject.
- **Image Enhancements:** Adjust Brightness, Contrast, Sharpness, and Blur.
- **Artistic Filters:** Apply creative effects such as Greyscale, Cartoon, Sketch, and Neon Glow.
- **Export & Download:** Download your edited creations in PNG format directly from the app.

## Technology Stack

- **[Streamlit](https://streamlit.io/):** For the interactive web interface.
- **[OpenCV](https://opencv.org/):** For artistic image processing (Cartoon, Sketch, Neon).
- **[Pillow (PIL)](https://python-pillow.org/):** For basic image manipulation and enhancements.
- **[Rembg](https://github.com/danielgatis/rembg):** For AI-powered background removal.
- **NumPy:** For matrix and image array operations.

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AnkitRaj154760/image-enhancement-tool.git
   cd image-enhancement-tool
   ```

2. **Install the dependencies:**
   It is recommended to use a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   Navigate into the `DIP` folder and run the Streamlit app:
   ```bash
   cd DIP
   streamlit run app.py
   ```

## Usage

1. Open the application in your browser (usually `http://localhost:8501`).
2. Upload an image (`.jpg`, `.jpeg`, `.png`).
3. Select an editing option from the sidebar.
4. Tweak the parameters or upload a new background.
5. Click **Download Image** to save the result.
