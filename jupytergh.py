"""Getting GitHub info on Jupyter repos"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
"""This notebook uses the github3py project maintained by Ian Cordasco."""

import getpass
from github3 import login

user = 'willingc'
password = getpass.getpass()

gh = login(user, password)
print(gh)
print(type(gh))

juporg = gh.organization('jupyter')
ipyorg = gh.organization('ipython')

for repo in juporg.iter_repos():
    print(repo, repo.open_issues_count, repo.description)
    repo.to_json

for repo in ipyorg.iter_repos():
    print(repo, repo.open_issues_count)

for issue in gh.iter_repo_issues('jupyter','notebook'):
    if issue.state == 'open':
        print(issue.number, issue.title)
myissues = gh.iter_repo_issues('jupyter','notebook')

for issue in gh.iter_repo_issues(owner='jupyter', repository='jupyter'):
    print(issue.number, issue.title)
    print(issue.labels)
    print(issue.created_at)
    print(issue.updated_at)
    
