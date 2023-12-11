# Image Background Remover Tool

This is a simple web application built with Flask that allows users to remove the background from an image using the `rembg` library.

## Files Overview:

### 1. `app.py`

This file contains the main Flask application. It handles routing, image processing, and file upload/download.

- **Dependencies:**
  - Flask: Web framework for Python.
  - rembg: Library for removing image backgrounds.
  - Pillow: Python Imaging Library fork, used for image processing.

- **Functionality:**
  - `convert_image`: Converts an image to a byte stream.
  - `fix_image`: Removes the background from an uploaded image.
  - `/`: Renders the main page.
  - `/upload`: Handles image uploads and initiates background removal.
  - **Run the App:** `python app.py`

### 2. `base.html`

This HTML template provides a basic structure for the web pages. It defines the layout, background, and styling for the application.

- **Styles:**
  - Uses a linear gradient background.
  - Applies a 3D parallax effect to the main container.
  - Utilizes a custom font.

### 3. `index.html`

This HTML template extends `base.html` and defines the content of the main page.

- **Content:**
  - App title and description.
  - Upload form with a file input and submit button.

### 4. `requirements.txt`

This file lists the required Python packages for the project.

- **Dependencies:**
  - rembg: Library for removing image backgrounds.
  - Pillow: Python Imaging Library fork, used for image processing.
  - Flask: Web framework for Python.

## How to Run:
1. Create Virtual Environment using Virtualenv
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the Flask application using `python app.py`.
4. Open your browser and navigate to `http://localhost:8080` to use the Image Background Remover Tool.