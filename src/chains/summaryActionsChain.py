
from langchain.callbacks.base import BaseCallbackManager  
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate 
from loguru import _logger
from langchain.chains import LLMChain
from src.core.chainWrapper import openai_callback_decorator, ChainCore
from src.prompts.summaryActionsPrompt import SYSTEM_PROMPT

class SummaryActionsChain(ChainCore): 
    def __init__(self,callback_manager:BaseCallbackManager = None): 
        self.callback_manager = callback_manager
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, max_retries=3,request_timeout=60)
        prompt = PromptTemplate(
            input_variables=["question"],output_variables=["answer"],
            template=SYSTEM_PROMPT,
        )
        self.chain = LLMChain(llm=self.llm, prompt=prompt , callback_manager=self.callback_manager,return_final_only=False)
        self.data = {}

    @openai_callback_decorator(tag='augment')
    def run(self, text)->dict:
        result = self.chain.invoke(text) 
        self.data.update(result) 
        return self.data 
     