"""Prints contribution data for the site: the last twelve months plus every calendar year.

Usage: python3 contributions.py <login>   (needs the gh CLI, authenticated)
"""
import json, subprocess, sys
from datetime import datetime, timezone

LOGIN = sys.argv[1]
LEVEL = {'NONE': 0, 'FIRST_QUARTILE': 1, 'SECOND_QUARTILE': 2, 'THIRD_QUARTILE': 3, 'FOURTH_QUARTILE': 4}
FIELDS = '''
  contributionCalendar { totalContributions weeks { contributionDays { date contributionCount contributionLevel } } }
  totalCommitContributions totalPullRequestContributions totalIssueContributions
  totalPullRequestReviewContributions totalRepositoryContributions restrictedContributionsCount
  commitContributionsByRepository(maxRepositories: 25) {
    repository { name url isPrivate primaryLanguage { name color } }
    contributions { totalCount }
  }
'''

def gql(query, **variables):
    args = ['gh', 'api', 'graphql', '-f', f'query={query}']
    for k, v in variables.items():
        args += ['-f', f'{k}={v}']
    return json.loads(subprocess.check_output(args))['data']

def period(pid, label, start=None, end=None):
    sig, arg = ('', '') if start is None else (', $from: DateTime!, $to: DateTime!', '(from: $from, to: $to)')
    q = f'query($login: String!{sig}) {{ user(login: $login) {{ contributionsCollection{arg} {{ {FIELDS} }} }} }}'
    v = {'login': LOGIN} if start is None else {'login': LOGIN, 'from': start, 'to': end}
    c = gql(q, **v)['user']['contributionsCollection']
    cal = c['contributionCalendar']
    repos = [r for r in c['commitContributionsByRepository'] if not r['repository']['isPrivate']]
    return {
        'id': pid, 'label': label, 'total': cal['totalContributions'],
        'weeks': [[[d['date'], d['contributionCount'], LEVEL[d['contributionLevel']]] for d in w['contributionDays']] for w in cal['weeks']],
        'kinds': {
            'commits': c['totalCommitContributions'], 'prs': c['totalPullRequestContributions'],
            'issues': c['totalIssueContributions'], 'reviews': c['totalPullRequestReviewContributions'],
            'repos': c['totalRepositoryContributions'], 'private': c['restrictedContributionsCount'],
        },
        'repos': [[r['repository']['name'], r['repository']['url'], r['contributions']['totalCount'],
                   (r['repository']['primaryLanguage'] or {}).get('name'), (r['repository']['primaryLanguage'] or {}).get('color')]
                  for r in repos[:6]],
    }

now = datetime.now(timezone.utc)
years = gql('query($login: String!) { user(login: $login) { contributionsCollection { contributionYears } } }', login=LOGIN)['user']['contributionsCollection']['contributionYears']
periods = [period('last', 'Last 12 months')]
for y in sorted(years, reverse=True):
    end = now.strftime('%Y-%m-%dT%H:%M:%SZ') if y == now.year else f'{y}-12-31T23:59:59Z'
    periods.append(period(str(y), str(y), f'{y}-01-01T00:00:00Z', end))

json.dump({'updated': now.strftime('%Y-%m-%d'), 'periods': periods}, sys.stdout, separators=(',', ':'))
