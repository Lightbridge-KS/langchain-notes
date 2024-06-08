import os
import openai
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def chat_with_gpt3(prompt_user):
    """Chat with GPT-3.5

    Args:
        prompt_user (str): User Prompt

    Returns:
        str: completion string
    """
    completion = my_chat_completion(client, model = "gpt-3.5-turbo", prompt_user=prompt_user)
    printChatCompletion(completion)
    msg_content = completion.choices[0].message.content
    return msg_content


def my_chat_completion(client: openai.OpenAI, model: str = "gpt-3.5-turbo",
                       seed: int = 1, temperature: float = 1.0,
                       prompt_system: str = "You are a helpful assistant.",
                       prompt_user: str = "Hello",
                       *args, **kwargs) -> dict:

    completion = client.chat.completions.create(
        model=model,
        seed=seed,  # For reproducibility
        temperature=temperature,
        messages=[
            {"role": "system", "content": prompt_system},
            {"role": "user", "content": prompt_user}
        ],
        *args, **kwargs
    )
    return completion


def printChatCompletion(cc: openai.types.chat.chat_completion.ChatCompletion):
    print(cc.choices[0].message.content)
    
    
# Ensure that the main functions are not executed if this script is imported
if __name__ == "__main__":
    test_prompt = "Hello, how can I help you today?"
    response = chat_with_gpt3(test_prompt)
    print(f"Response: {response}")