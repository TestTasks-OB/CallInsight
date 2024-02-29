import json
import os
from loguru import logger

folder_path = 'data'
if not os.path.exists(folder_path):
    os.makedirs(folder_path) 

def saveToFile(filename,data): 
    file_path = os.path.join(folder_path, f'{filename}.txt')
    
    with open(file_path, 'w') as file:
        file.write(data) 

    logger.info(f'Data successfully saved to {file_path}')
