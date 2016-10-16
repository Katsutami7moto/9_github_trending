import requests

API_ADDRESS = 'https://api.github.com'
TOP_COUNT = 20


def get_trending_repositories(top_size: int) -> list:
    repos_url = '{api}/search/repositories?sort=stars'.format(api=API_ADDRESS)
    repositories = requests.get(url=repos_url).json()
    return repositories['items'][:top_size]


def get_open_issues_amount(repo_owner: str, repo_name: str) -> int:
    issues_url = '{api}/repos/:{owner}/:{repo}/issues'.format(api=API_ADDRESS, owner=repo_owner, repo=repo_name)
    issues = requests.get(url=issues_url).json()
    return len(issues)


if __name__ == '__main__':
    pass
