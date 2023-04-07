'''
Author: Mrx
Date: 2023-03-30 10:03:58
LastEditors: Mrx
LastEditTime: 2023-04-06 16:26:44
FilePath: \crawler\a.py
Description: 

Copyright (c) 2023 by Mrx, All Rights Reserved. 
'''
import requests
import json
def get_commit_info(page):
    url=f"https://gitee.com/api/v5/repos/opengauss/openGauss-server/commits?access_token=82e66bc201b7212f0dc14e9807ee27df&state=open&sort=created&direction=desc&page={page}&per_page=100"
    headers = {
        'Content-Type': 'application/json',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Referer": "https://www.example.com/",
        "Cookie": "cookie_string_here"
        }
    ret=requests.get(url,headers=headers)
    # print(ret.json())
    commit_list=[]
    for commit in ret.json():
        # print(commit)
        # if commit['commit_type_detail']['ident'] in ['bug','task']:
        if True:
            new_commit={}
            info = commit['commit']['message']  
            info = info.replace('\n', ' ')
            info = info.replace('Merge pull request ', ' ')
            new_commit['url'] = commit['html_url']
            # new_commit['info'] = commit['commit']['message']  
            new_commit['info'] = info
            commit_list.append(new_commit)
    return commit_list

# def get_url_list(commit_list):
            
            

if __name__=="__main__":
    commit_list=[]
    for page in range(1,7):
        # print(type(page))
        commit_list += get_commit_info(page)
        # get_commit_info(page)
    json.dump(commit_list,open('commit_list.json','w',encoding='utf-8'),ensure_ascii=False,indent=4)
    print(len(commit_list))
    # url_list = []
    commit_info_list = []
    for commit in commit_list:
        # url_list.append(commit['url'])
        commit_info_list.append(commit['info'])
    # json.dump(url_list,open('url_list.json','w',encoding='utf-8'),ensure_ascii=False,indent=4)
    json.dump(commit_info_list,open('commit_info_list.json','w',encoding='utf-8'),ensure_ascii=False,indent=4)
