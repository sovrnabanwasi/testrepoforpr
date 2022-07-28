import requests
import json
import pandas as pd
import datetime as dt



####
#  Inputs
#  username: username
#  token : token
#  orgname : by default this will be sovrn. Can be specified as the user's github name 
#  repos: List of repos to check
#  closedate: Will check for pull requests after this specific date and all other open pull requests that haven't yet been closed
####


def main():
    pd.options.display.max_colwidth = 1000
    
    pull_url = 'https://api.github.com/repos/{orgname}/{reponame}/pulls?state=all'
    username = 'sovrnabanwasi'
    orgname = 'sovrnabanwasi'
    token = 'xxx'
    repos = ['testrepoforpr', 'viglink']
    closedate = '2022-07-01'

    # from https://github.com/user/settings/tokens
    # repos_url = 'https://api.github.com/orgs/sovrn/repos?per_page=100&page=1'
 
    
    # create a re-usable session object with the user creds in-built
    gh_session = requests.Session()
    gh_session.auth = (username, token)
    newurl = pull_url.replace('{orgname}',orgname)
    
    pull_req_list = []
    for reponame in repos:
        pull_url = newurl.replace('{reponame}',reponame)
        
        resp = gh_session.get(pull_url)
        if resp.status_code == 200:
            pulls = json.loads(resp.text)
            newpulls = []
            newpulls = list(filter(lambda d: d['created_at'] >= '2022-07-01', pulls))

            if len(newpulls) > 0:
                for item in newpulls:
                    pull_req_dict = {}
                    ##print(item.keys())
                    merged = item['merged_at']
                    closed = item['closed_at']
                    status = 'closed'
                    if not merged:
                        merged = dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
                        status = 'open'
                    else:
                        merged = merged
                    created = (item['created_at'])
                    #created = created[:10]
                    #print (reponame + ": Pull Request Title::::" + item['title'])
                    merge_time = dt.datetime.strptime(merged, "%Y-%m-%dT%H:%M:%SZ") -dt.datetime.strptime(created, "%Y-%m-%dT%H:%M:%SZ")
                    pull_req_dict['reponame'] = reponame
                    pull_req_dict['status'] = status
                    pull_req_dict['title'] = item['title']
                    pull_req_dict['merge_time'] = merge_time
                    pull_req_list.append(pull_req_dict)
                    #if status == 'open':
                        #print("Open Pull Requests")
                        #print("PR Open Time:" + str(merge_time))
                    #else:
                        #print("Closed Pull Requests")
                        #print("PR Merge Time:" + str(merge_time))
                    
        else:
            pull_req_dict = {}
            pull_req_dict['reponame'] = reponame
            pull_req_dict['status'] = 'doesnotexist'
            pull_req_dict['title'] = ''
            pull_req_dict['merge_time'] = ''
            pull_req_list.append(pull_req_dict)
    
    df = pd.DataFrame(pull_req_list)
    
    print(df)
main()