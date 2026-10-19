"""Writes a small stats table into README.md between the stats markers, from docs/contributions.json."""
import json, re
from datetime import date

data = json.load(open('docs/contributions.json'))
last, years = data['periods'][0], data['periods'][1:]
days = [d for w in last['weeks'] for d in w]

longest = run = 0
for _, c, _ in days:
    run = run + 1 if c else 0
    longest = max(longest, run)
best = max(days, key=lambda d: d[1])
best_day = date.fromisoformat(best[0]).strftime('%-d %b %Y')
active = sum(1 for d in days if d[1])
k = last['kinds']
by_year = ' · '.join(f'{p["label"]}: {p["total"]:,}' for p in years)

block = f'''<!-- stats:start -->
| Last 12 months | Active days | Public commits | Private work | Pull requests | Longest streak | Busiest day |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **{last["total"]:,}** contributions | {active} of {len(days)} | {k["commits"]:,} | {k["private"]:,} | {k["prs"]} | {longest} days | {best[1]:,} on {best_day} |

<sub>By year: {by_year}. Updated {data["updated"]}.</sub>
<!-- stats:end -->'''

readme = open('README.md').read()
open('README.md', 'w').write(re.sub(r'<!-- stats:start -->.*?<!-- stats:end -->', lambda m: block, readme, flags=re.S))
