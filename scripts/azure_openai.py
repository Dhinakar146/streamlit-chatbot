import os
from langchain.chat_models import AzureChatOpenAI


def send_message(question: str) -> str:
    """This function generates response from the GPT-4 model"""

    # Load API key
    os.environ["OPENAI_API_KEY"] = os.getenv('AZURE_API_KEY')

    # initializing the chat model
    chat_model = AzureChatOpenAI(
        model_name='gpt-4-32k',
        deployment_name='gpt-4-32k',
        temperature=0.5,
        n=1
    )
    return chat_model.invoke(question).content
