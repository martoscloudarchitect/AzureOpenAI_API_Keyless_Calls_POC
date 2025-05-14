# import necessary libraries

## Required library to implement AI Agent
from openai import AzureOpenAI

## Required for Azure OpenAI Keyless API calls
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

## Reading the environment variables from .env file
import os
from dotenv import load_dotenv


# Reading the Azure AI Endpoint API Version and LLM Model from Environment Variables
load_dotenv(override=True)
azure_api_version=os.getenv("AZURE_AI_ENDPOINT_VERSION")
azure_api_model=os.getenv("AZURE_AI_CHAT_MODEL")
azure_api_endpoint=os.getenv("AZURE_AI_ENDPOINT")

## Option 2 - Use this when using Azure OpenAI Keyless API calls, this is recommended for dev and a must for production
keyless_credentials = DefaultAzureCredential()
token_provider = get_bearer_token_provider(
    keyless_credentials,
    "https://cognitiveservices.azure.com/.default")

# Keyless API Connection Client Object
client = AzureOpenAI(
    api_version=azure_api_version,
    azure_endpoint=azure_api_endpoint,

    # Option 2 - Second Test, to obtain a temporary auth token if using Keyless API calls - This is Recommended for production
    azure_ad_token_provider=token_provider
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