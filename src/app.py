from flask import Flask, request, jsonify
from flasgger import Swagger
from dotenv import load_dotenv
from loguru import logger
from src.augmentTranscription import augmentTranscription
from src.saveTranscription import saveToFile
load_dotenv('../.env')

app = Flask(__name__)
Swagger(app)
@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    """
    Upload an audio file.

    ---
    tags:
      - Audio
    parameters:
      - name: audio
        in: formData
        type: file
        required: true
        description: The audio file to upload.
    responses:
      200:
        description: Audio file uploaded successfully.
      400:
        description: Bad request. No audio file provided or no selected file.
      429:
        description: quota OpenAI
    """
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400
    
    audio_file = request.files['audio']
    
    if audio_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400 
    try:
      result = augmentTranscription(audio_file)  
      file_name = audio_file.filename.rsplit('.', 1)[0].lower()
      logger.info(result)
      saveToFile(file_name, result['result']['summary'])
      return jsonify(result),200
    except Exception as e:  
      return jsonify({'error':str(e)}), 429
     

def main():
    app.run()
     