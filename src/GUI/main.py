from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_socketio import SocketIO
import os
import sys
import shutil
import time
import webview
import threading
import signal
from PIL import Image

app = Flask(__name__)
socketio = SocketIO(app, async_mode='threading')

# Paths
TEMP_FOLDER = os.path.join(os.getcwd(), 'temp')
OUTPUT_FOLDER = os.path.join(os.getcwd(), 'output')
os.makedirs(TEMP_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def resource_path(relative_path):
    """Get absolute path to resource, works for PyInstaller bundles."""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(__file__), relative_path)

def cleanup_folder(folder):
    try:
        if os.path.exists(folder):
            shutil.rmtree(folder)  # Recursively delete folder and its contents
            print(f"[Log]: Successfully deleted folder {folder}")
        else:
            print(f"[Log]: Folder {folder} does not exist, no cleanup needed.")
    except Exception as e:
        print(f"[Error]: Failed to delete folder {folder}: {e}")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    file_path = os.path.join(TEMP_FOLDER, file.filename)
    file.save(file_path)

    try:
        input_image = Image.open(file_path)
        if input_image.size != (72, 24):
            input_image = input_image.resize((72, 24))
        resized_image_path = os.path.join(TEMP_FOLDER, f"resized_{file.filename}")
        input_image.save(resized_image_path)
        print(f"[Log]: Image resized successfully: {resized_image_path}")
    except Exception as e:
        print(f"[Error]: Failed to resize image: {e}")
        return jsonify({'error': 'Failed to process image'}), 500

    return jsonify({'preview': f"/temp/{os.path.basename(resized_image_path)}", 'filePath': file_path})

@app.route('/temp/<filename>')
def get_temp_file(filename):
    return send_from_directory(TEMP_FOLDER, filename)

@app.route('/output/<filename>')
def get_output_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

@socketio.on('slice_image')
def slice_image(data):
    image_path = data['path']
    try:
        input_image = Image.open(image_path)
        skin_template = Image.open(resource_path("assets/skin_template.png"))
        counter = 26

        output_files = []
        for i in range(3):
            for j in range(9):
                if i == 0 and j == 0:
                    continue
                block = input_image.crop((j * 8, i * 8, j * 8 + 8, i * 8 + 8))
                skin = skin_template.copy()
                output_file = os.path.join(OUTPUT_FOLDER, f"skin_{counter}.png")
                skin.paste(block, (8, 8))
                skin.save(output_file)
                output_files.append(output_file)
                counter -= 1

        socketio.emit('slice_progress', {'progress': 100, 'output': output_files})
        print(f"[Done]: Slicing completed. Output files: {output_files}")
        cleanup_folder(TEMP_FOLDER)
    except Exception as e:
        print(f"[Error]: Slicing failed: {e}")
        socketio.emit('slice_progress', {'progress': 0, 'error': str(e)})

def run_gui():
    socketio.run(app, debug=False)

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_gui)
    flask_thread.daemon = True
    flask_thread.start()

    webview.create_window('NameMC Profile Art', 'http://127.0.0.1:5000')

    def shutdown(signal, frame):
        print("Shutting down Flask server...")
        cleanup_folder(TEMP_FOLDER)
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown)
    webview.start()
