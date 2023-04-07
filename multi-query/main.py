'''
Author: Mrx
Date: 2023-04-03 22:32:26
LastEditors: Mrx
LastEditTime: 2023-04-03 22:37:50
FilePath: \multi-query\main.py
Description: 

Copyright (c) 2023 by Mrx, All Rights Reserved. 
'''
import openai
import time

# Set up your OpenAI API key
openai.api_key = "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"

# Define the prompts for each question
question_prompts = [
    "What is the meaning of life?",
    "How do I become more productive?",
    "What are some tips for improving my communication skills?"
]

# Define a function to generate a response from OpenAI's GPT-3 model
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Have a conversation with ChatGPT
print("Hi ChatGPT, I have a few questions for you.")
for i, prompt in enumerate(question_prompts):
    print(f"\nQuestion {i+1}: {prompt}")
    time.sleep(1)  # Pause for 1 second to avoid API rate limits
    response = generate_response(prompt)
    print(f"Answer: {response}")
