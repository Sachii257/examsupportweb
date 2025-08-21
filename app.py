
    # app.py - The Complete and Corrected Code

import os
from flask import Flask, render_template, send_from_directory

# Initialize the Flask application
app = Flask(__name__)

# --- Configuration ---
# Define the path for the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# --- Helper Function (This is the corrected part) ---
def get_files_from_folder(folder_name):
    """
    A helper function to get a list of files from a specific folder.
    This function will also create the folder if it doesn't exist.
    """
    folder_path = os.path.join(app.config['UPLOAD_FOLDER'], folder_name)
    
    # This new line creates the directory if it doesn't already exist.
    # This prevents the app from crashing on a new server.
    os.makedirs(folder_path, exist_ok=True) 
    
    return os.listdir(folder_path)


# --- App Routes ---

@app.route('/')
def index():
    """Renders the home page."""
    return render_template('index.html')


@app.route('/question-papers')
def question_papers():
    """Renders the question papers page by listing files from the 'qp' folder."""
    files = get_files_from_folder('qp')
    return render_template('qp.html', files=files, title="Question Papers")


@app.route('/notes')
def notes():
    """Renders the notes page by listing files from the 'notes' folder."""
    files = get_files_from_folder('notes')
    return render_template('notes.html', files=files, title="Study Notes")


# --- File Download Routes ---

@app.route('/download/qp/<filename>')
def download_qp(filename):
    """Provides a download link for a specific question paper."""
    qp_directory = os.path.join(app.config['UPLOAD_FOLDER'], 'qp')
    return send_from_directory(directory=qp_directory, path=filename, as_attachment=True)


@app.route('/download/notes/<filename>')
def download_note(filename):
    """Provides a download link for a specific note."""
    notes_directory = os.path.join(app.config['UPLOAD_FOLDER'], 'notes')
    return send_from_directory(directory=notes_directory, path=filename, as_attachment=True)


# --- Run the App ---
if __name__ == '__main__':
    # The debug=True flag is for local development.
    # Render's Gunicorn server will run this file without using this block.
    app.run(debug=True)