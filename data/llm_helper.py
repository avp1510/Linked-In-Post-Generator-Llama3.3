from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

llm = ChatGroq(groq_api_key = os.getenv("GROC_API_KEY"), model_name = "llama-3.3-70b-versatile")


if __name__ == "__main__":
    response = llm.invoke("whats are the two main components of a hard disk")
    print(response.content)