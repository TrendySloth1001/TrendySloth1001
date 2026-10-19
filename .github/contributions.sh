#!/usr/bin/env bash
# Prints the last year of contributions as {total, weeks: [[[date, count, level], ...], ...]}
set -euo pipefail
gh api graphql -f login="$1" -f query='
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount contributionLevel } }
      }
    }
  }
}' --jq '
  {"NONE":0,"FIRST_QUARTILE":1,"SECOND_QUARTILE":2,"THIRD_QUARTILE":3,"FOURTH_QUARTILE":4} as $lv
  | .data.user.contributionsCollection.contributionCalendar
  | {total: .totalContributions,
     weeks: [.weeks[] | [.contributionDays[] | [.date, .contributionCount, $lv[.contributionLevel]]]]}'
