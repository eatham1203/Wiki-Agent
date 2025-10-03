from dotenv import load_dotenv
from pydantic import BaseSettings
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()  # Load environment variables from .env file

# Setting up an LLms configuration class
llm = ChatOpenAI()
llm2 = ChatAnthropic()