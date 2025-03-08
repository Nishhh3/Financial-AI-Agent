from groq import Groq

# Replace with your actual API key
groq_client = Groq(api_key="YOUR_GROQ_API_KEY")  
models = groq_client.models.list()
print(models)
