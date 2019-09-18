import requests
import json

def get_commits(github_id, repo):
    """Retrieve the commits for a specific user repository, using the Github API"""

    url = 'https://api.github.com/repos/{}/{}/commits'.format(github_id, repo)
    response = requests.get(url)
    todos = json.loads(response.text)

    commit_count = 0

    for data in todos:
        commit_count += 1

    return commit_count

def get_repos(github_id):
    """Retrieves a user's list of repositories using the GitHub API"""

    url = 'https://api.github.com/users/{}/repos'.format(github_id)
    response = requests.get(url)
    todos = json.loads(response.text)

    repo_list = []
    
    for data in todos:
        repo_list.append(data['name'])

    return repo_list

def display_repos_and_commits(github_id):
    """Display user's list of repositories and the number of commits in each one"""

    repo_list = get_repos(github_id)

    for repo in repo_list:
        commits_count = get_commits(github_id, repo)
        print('Repo: {} Number of commits: {}'.format(repo, commits_count))