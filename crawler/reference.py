'''
Author: Mrx
Date: 2023-03-30 10:03:58
LastEditors: Mrx
LastEditTime: 2023-03-30 15:48:28
FilePath: \crawler\reference.py
Description: 

Copyright (c) 2023 by Mrx, All Rights Reserved. 
'''
import requests
import json
def get_issue_info(page):
    url=f"https://gitee.com/api/v5/repos/opengauss/openGauss-server/issues?access_token=82e66bc201b7212f0dc14e9807ee27df&state=open&sort=created&direction=desc&page={page}&per_page=100"
    headers = {
        'Content-Type': 'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Referer": "https://www.example.com/",
        "Cookie": "cookie_string_here"
        }
    ret=requests.get(url,headers=headers)
    # print(ret.json())
    issuse_list=[]
    for issuse in ret.json():
        # print(issuse)
        if issuse['issue_type_detail']['ident'] in ['bug','task']:
            new_issue={}
            new_issue['title']=issuse['title']
            new_issue['body']=issuse['body']
            new_issue['url']=issuse['html_url']
            new_issue['number']=issuse['number']
            new_issue['state']=issuse['state']
            new_issue['type']=issuse['issue_type_detail']['ident']
            issuse_list.append(new_issue)
    return issuse_list

# def get_url_list(issue_list):
            
            

if __name__=="__main__":
    issue_list=[]
    for page in range(1,7):
        print(type(page))
        issue_list += get_issue_info(page)
        # get_issue_info(page)
    json.dump(issue_list,open('issue_list.json','w',encoding='utf-8'),ensure_ascii=False,indent=4)
    print(len(issue_list))
    url_list = []
    for issue in issue_list:
        url_list.append(issue['url'])
    json.dump(url_list,open('url_list.json','w',encoding='utf-8'),ensure_ascii=False,indent=4)

