'''
Author: Mrx
Date: 2023-04-06 15:47:21
LastEditors: Mrx
LastEditTime: 2023-04-06 16:54:45
FilePath: \multi-query\test4.py
Description: 

Copyright (c) 2023 by Mrx, All Rights Reserved. 
'''
import openai
import json
import time

openai.api_key = "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"

info = "I want you to act as a cybersecurity specialist. I will provide some commit information of the code repository, and your job is to judge whether the commit is a vulnerability patch based on these commit information. According to the commit information, please be sure to clearly state 'Yes.' or 'No.' or 'Not sure.' at the beginning of the answer. Please note that the beginning of the answer must be one of these three forms, not anything else. If a commit message is not a vulnerability patch, please state 'No.' at the beginning of the answer. The commit info is:"
# Load questions from JSON file
with open("questions1.json", encoding='utf-8') as f:
    questions = json.load(f)

# Create file to store responses
answer_list = []
    # Loop through questions and get responses
for question in questions:
    q = info + question
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": q}
        ]
    )
    time.sleep(0.5)
    answer_list.append('Q:' + question )
    answer_list.append('A:' + response.choices[0].message["content"])
    print(response.choices[0].message["content"])
json.dump(answer_list,open('answer_list.json','w',encoding='utf-8'),ensure_ascii=False,indent=4)
        
