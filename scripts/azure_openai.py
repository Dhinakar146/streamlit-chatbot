import os
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def get_response(user_query, chat_history):
    """This function streams response using azure openai GPT-4 model"""
    # Load API key
    os.environ["OPENAI_API_KEY"] = os.getenv('AZURE_API_KEY')

    template = """
    You are a helpful assistant. Answer the following questions considering the history of the conversation:

    Chat history: {chat_history}

    User question: {user_question}
    """

    prompt = ChatPromptTemplate.from_template(template)

    llm = AzureChatOpenAI(
        model_name='gpt-4-32k',
        deployment_name='gpt-4-32k',
        temperature=0.5,
        n=1
    )

    chain = prompt | llm | StrOutputParser()

    return chain.stream({
        "chat_history": chat_history,
        "user_question": user_query,
    })
