from dotenv import load_dotenv
# from pydantic import BaseSettings
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()  # Load environment variables from .env file

# Setting up an LLms configuration class
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro"
)
response = llm.invoke("What is the meaning of life?")
print(response)