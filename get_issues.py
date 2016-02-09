"""get_issues.py"""

import github3
import os

GH_NAME= os.environ.get('GH_NAME')
GH_PASSWD = os.environ.get('GH_PASSWORD')
GH_TOKEN = os.environ.get('GH_TOKEN')
gh = github3.login(GH_NAME, GH_PASSWD)

# Get all Jupyter repos
repos = [r.refresh() for r in gh.repositories_by('jupyter')]

for repo in repos:
    print(repo.name, repo.url)
    print('   ', repo.description)
    print('   ', repo.homepage)
    print('   Open   ', repo.open_issues_count)

for repo in repos:
	text = ('%s: %d' % (repo.name, repo.open_issues_count))
	print(text)
