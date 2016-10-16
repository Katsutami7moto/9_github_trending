import requests
from datetime import date, timedelta

API_ADDRESS = 'https://api.github.com'
TOP_COUNT = 20


def get_trending_repositories() -> list:
    week_ago = date.today() - timedelta(weeks=1)
    week_ago_text = str(week_ago.isoformat())
    trend_params = {
        'q': 'created:>{}'.format(week_ago_text),
        'sort': 'stars',
        'order': 'desc'
    }
    repos_url = '{api}/search/repositories'.format(api=API_ADDRESS)
    repositories = requests.get(url=repos_url, params=trend_params).json()
    return repositories['items'][:TOP_COUNT]


def print_trending_repositories(repos):
    output = 'Name: {name}\n' \
             'Stars: {stars}\n' \
             'Issues: {issues}\n' \
             'URL: {url}\n\n'
    for repo in repos:
        print(output.format(name=repo['name'],
                            stars=repo['stargazers_count'],
                            issues=repo['open_issues_count'],
                            url=repo['html_url']))


if __name__ == '__main__':
    print('Trending repositories of this week: \n')
    print_trending_repositories(get_trending_repositories())
