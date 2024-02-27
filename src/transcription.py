

import io   
import openai
from loguru import logger


SUPPORTED_FORMATS = ['flac', 'm4a', 'mp3', 'mp4', 'mpeg', 'mpga', 'oga', 'ogg', 'wav', 'webm']

def getTranscription(audio_file:bytes)->str:
    file_format = audio_file.filename.rsplit('.', 1)[-1].lower()
    if file_format not in SUPPORTED_FORMATS:
        return {'error': f'Unsupported file format: {file_format}. Supported formats: {", ".join(SUPPORTED_FORMATS)}'}
    file_content = audio_file.read()
    file_obj = io.BytesIO(file_content)
    file_obj.name = audio_file.filename
    client = openai.Client() 
    transcript = client.audio.transcriptions.create(
        model="whisper-1", 
        file=file_obj
    ) 
    logger.info(transcript)
    return transcript