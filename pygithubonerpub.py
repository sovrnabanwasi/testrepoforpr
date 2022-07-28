import requests
import json
import pandas as pd
import datetime as dt


####
# inputs
####
username = 'sovrnabanwasi'

# from https://github.com/user/settings/tokens
token = ''
token = 'xxx'
repo = 'testrepoforpr'

repos_url = 'https://api.github.com/orgs/sovrn/repos?per_page=100&page=1'
pull_url = 'https://api.github.com/repos/sovrn/{reponame}/pulls?state=all'


##public url
pull_url = 'https://api.github.com/repos/sovrnabanwasi/{reponame}/pulls?state=all'
# create a re-usable session object with the user creds in-built
gh_session = requests.Session()
gh_session.auth = (username, token)
newurl = pull_url.replace('{reponame}',repo)
pulls = json.loads(gh_session.get(newurl).text)


newpulls = list(filter(lambda d: d['created_at'] >= '2022-07-01', pulls))

if len(newpulls) > 0:
    for item in newpulls:
        merged = item['merged_at']
        closed = item['closed_at']
        if not merged:
            print(closed)
            merged = dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        else:
            merged = merged
        created = (item['created_at'])
        #created = created[:10]
        print(created)
        print (repo + ": Pull Request Title::::" + item['title'])
        merge_time = dt.datetime.strptime(merged, "%Y-%m-%dT%H:%M:%SZ") -dt.datetime.strptime(created, "%Y-%m-%dT%H:%M:%SZ")
        print("PR Merge Time:" + str(merge_time))


