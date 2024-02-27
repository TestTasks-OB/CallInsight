from flask import Flask, request, jsonify
from flasgger import Swagger
from dotenv import load_dotenv
from .transcription import getTranscription
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
    
    try:
      result = getTranscription(audio_file)
    except Exception as e:  
      return jsonify({'error':str(e)}), 429
    if audio_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    #audio_file.save(audio_file.filename)
    
    return jsonify({'message': 'Audio file uploaded successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)