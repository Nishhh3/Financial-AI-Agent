from groq import Groq

# Replace with your actual API key
groq_client = Groq(api_key="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")  
models = groq_client.models.list()
print(models)
