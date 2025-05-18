import os
from groq import Groq
import asyncio

# Create the Groq client
api_key=os.environ.get("GROQ_API_KEY")
client = Groq(api_key=api_key, )

def iterative_chat() -> str:
    """
    Sends a prompt to the Groq Chat Completions endpoint and returns the assistant's reply.
    """
    # if not (prompt and isinstance(prompt,str) and len(prompt) > 0):
    #     print('Wrong prompt')
    #     return 
    
    system_prompt = {
    "role": "system",
    "content": ''
    
    }

    # Initialize the chat history
    chat_history = [system_prompt]
    while True:
    # Get user input from the console
        user_input = input("You: ")

        # Append the user input to the chat history
        chat_history.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(model="llama3-70b-8192",
                                                    messages=chat_history,
                                                    max_tokens=1000,
                                                    temperature=1.2)
        # Append the response to the chat history
        chat_history.append({
            "role": "assistant",
            "content": response.choices[0].message.content
        })
        # Print the response
        print("Assistant:", response.choices[0].message.content)

def generate_answer_sync(prompt: str) -> str:
    """
    Sends a prompt to the Groq Chat Completions endpoint and returns the assistant's reply.
    """
    if not (prompt and isinstance(prompt, str) and len(prompt) > 0):
        raise ValueError("Invalid prompt")
    
    # Chat history with initial prompt
    chat_history = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=chat_history,
        max_tokens=1000,
        temperature=1.2
    )

    return response.choices[0].message.content

async def generate_answer_async(prompt: str) -> str:
    """
    Asynchronously sends a prompt to the Groq Chat Completions endpoint and returns the assistant's reply.
    """
    if not (prompt and isinstance(prompt, str) and len(prompt) > 0):
        raise ValueError("Invalid prompt")

    chat_history = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]

    # Run the synchronous call in a thread
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=chat_history,
        max_tokens=1000,
        temperature=1.2
    )

    return response.choices[0].message.content


async def main():
    result = await generate_answer_async("Explain the importance of the large language models")
    print("Resposta:", result)

if __name__ == "__main__":
    asyncio.run(main())
    #iterative_chat()