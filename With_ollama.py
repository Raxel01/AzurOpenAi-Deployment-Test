from litellm import completion

messages = [{'role' : 'assistant', "content" : "you are kind helpful assistant that\
                                    Answer users Question be kind on you replies and if you don't know something just say I dont know",
             'role' : 'user'     ,      "content" : "What's is RAG in Machine Learning"
            }]

try:
    Fullresponse = completion(
            model="ollama/llama3.2:1b",
            messages = messages,
            api_base="http://ollama:11434",
            # stream=True,
    )
    responseContent = Fullresponse.choices[0].message.content
    messages.append({
        'role'    : 'assistant',
        'content' : responseContent 
    })
    
    print(responseContent)
    # Issue is that ollama and Litellm are not on the same network
except Exception as e:
    print(f'Error : {e}')
