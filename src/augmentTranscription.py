
from src.transcription import getTranscription
from src.chains.augmentChain import AugmentChain
from src.chains.summaryActionsChain import SummaryActionsChain
from loguru import logger
import json

def augmentTranscription(audio_file):
    tokens =[]
    result = getTranscription(audio_file)
    augm = AugmentChain()
    augm.run(text=result.text)
    logger.info(augm.data['text'])
    logger.info(augm.data['tokens'])
    tokens.append(augm.data['tokens'])
    summ = SummaryActionsChain()
    summ.run(text=augm.data['text'])
    logger.info(summ.data['text'])
    logger.info(summ.data['tokens'])
    tokens.append(summ.data['tokens']) 
    return {'result':json.loads(summ.data['text']), 'tokens':tokens }