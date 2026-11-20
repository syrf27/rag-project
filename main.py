import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def main():
    print("Hello from rag-project!")
    llm = ChatOpenAI(
        model="openai/gpt-oss-20b",
        api_key=os.environ["GROQ_API_KEY"],
        base_url="https://api.groq.com/openai/v1",
        temperature=0,
    )
    response = llm.invoke("What is the capital of France?")
    print(response)


if __name__ == "__main__":
    main()
