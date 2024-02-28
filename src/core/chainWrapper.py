import traceback
from timeit import default_timer as timer
from langchain_community.callbacks import get_openai_callback
from abc import ABC, abstractmethod
from langchain.callbacks.base import BaseCallbackManager 



def openai_callback_decorator(tag):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            with get_openai_callback() as cb: 
                result = func(self, *args, **kwargs)
                self.data['tokens'] = {'tag':tag
                                        ,   'totalTokens':cb.total_tokens
                                        ,   'promptTokens':cb.prompt_tokens
                                        ,   'completionTokens':cb.completion_tokens
                                        ,   'successfulRequests':cb.successful_requests
                                        ,   'totalCost':cb.total_cost}
            return result
        return wrapper
    return decorator



class ChainCore(ABC): 
    @abstractmethod
    def __init__(self,callback_manager:BaseCallbackManager = None):  
        pass

    @abstractmethod
    def run(self, **kwargs)->dict:
        pass