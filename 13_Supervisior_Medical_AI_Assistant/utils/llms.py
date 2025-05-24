import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY


class LLMModel:
    def __init__(self, model_name = "gemini-2.0-flash-thinking-exp-01-21"):
        if not model_name:
            raise ValueError("Model is not defined")
        
        self.model_name = model_name
        self.gemini2_flash_think_model = ChatGoogleGenerativeAI(model = self.model_name)
        

    def getmodel(self):
        return self.gemini2_flash_think_model
    

if __name__ == "__main__":
    llm_instance = LLMModel()
    llm_model = llm_instance.getmodel()
    response = llm_model.invoke("hi")
    print(response)