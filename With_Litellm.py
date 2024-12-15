from openai import AzureOpenAI
from dotenv import load_dotenv
import os
from litellm import completion

# Link litellm with Azure-App
# load environment
try : 
    load_dotenv()
    OPEN_AI_API_KEY=os.getenv('OPEN_AI_API_KEY')
    AZURE_ENDPOINT=os.getenv('AZURE_ENDPOINT')
    AZURE_DEPLOYMENT_NAME=os.getenv('AZURE_DEPLOYMENT_NAME')
    AZURE_API_VERSION=os.getenv('AZURE_API_VERSION')

    os.environ["AZURE_API_KEY"] = OPEN_AI_API_KEY
    os.environ["AZURE_API_BASE"] = AZURE_ENDPOINT
    os.environ["AZURE_API_VERSION"] = AZURE_API_VERSION

    messages = [{'role' : 'assistant', "content" : "you are kind helpful assistant that\
                                    Answer users Question be kind on you replies and if you don't know something just say I dont know",
             'role' : 'user'     ,      "content" : "What's is RAG in Machine Learning"
             }]

# azure call
    deploymentName = f'azure/{AZURE_DEPLOYMENT_NAME}'
    fullresponse = completion(
        deploymentName,
        messages = messages,
    )
    reponseContent = fullresponse.choices[0].message.content
    print(reponseContent)
except  Exception as e:
    print('Error : {e}')
