from openai import AzureOpenAI
from dotenv import load_dotenv
import os

# load environment
try:
    load_dotenv()

    messages = [{'role' : 'assistant', "content" : "you are kind helpful assistant that\
                                    Answer users Question be kind on you replies and if you don't know something sjust say I dont know",
             'role' : 'user'     ,      "content" : "What's is RAG in Machine Learning"
             }]

    OPEN_AI_API_KEY=os.getenv('OPEN_AI_API_KEY')
    AZURE_ENDPOINT=os.getenv('AZURE_ENDPOINT')
    AZURE_DEPLOYMENT_NAME=os.getenv('AZURE_DEPLOYMENT_NAME')
    AZURE_API_VERSION=os.getenv('AZURE_API_VERSION')

    AzureClient = AzureOpenAI(
        api_key=OPEN_AI_API_KEY,
        api_version=AZURE_API_VERSION,
        azure_endpoint=AZURE_ENDPOINT
    )

    fullResponse = AzureClient.chat.completions.create(
        model=AZURE_DEPLOYMENT_NAME,
        messages=messages
    )

    modelResponse = fullResponse.choices[0].message.content
    messages.append({
        'role'    : 'assistant',
        'content' : modelResponse 
    })

    print(modelResponse)
except Exception as e:
    print(f'Error reason : {e}')

