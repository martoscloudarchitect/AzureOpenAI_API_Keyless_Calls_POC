# import necessary libraries
import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Setup the OpenAI client to use either Azure or GitHub Models
load_dotenv(override=True)

# Reading the Azure AI Endpoint API Version and LLM Model from Environment Variables
azure_api_version=os.getenv("AZURE_AI_ENDPOINT_VERSION")
azure_api_model=os.getenv("AZURE_AI_CHAT_MODEL")

## Option 1 - Use this when using Azure OpenAI Keys to make OpenAI API Calls, this is not recommended for production
azure_api_endpoint=os.getenv("AZURE_AI_ENDPOINT")
azure_api_key=os.getenv("AZURE_AI_KEY")


# Create a client object for accessing via Resource Key the Azure OpenAI API
client = AzureOpenAI(
        api_version=azure_api_version,
        azure_endpoint=azure_api_endpoint,
        api_key=azure_api_key
    )

# Setup a system prompt and user prompt to pass for the Large Language to know how to handle your request and how to respond
system_prompt = "You are a Master Jedi from Star Wars incorporating Master Yoda's style to provide answer to a user. User a response and always weight the dark side of the force as a potential risk."

user_prompt = "What is the capital of France?"

# Submit a chat completion request to Azure OpenAI, taking the expected behavior from system_prompt and user Natural Language input via user_prompt
response = client.chat.completions.create(
        model=azure_api_model,
        messages=[
            {
                "role": "system", 
                "content": system_prompt
            },
            {
                "role": "user", 
                "content": user_prompt}
        ],
        max_tokens=300,
    )

# Print the response
print(response.choices[0].message.content)