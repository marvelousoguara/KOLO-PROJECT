import csv
import re

SENIOR_PATTERN = re.compile(
    r"\b(founder|ceo|cto|coo|head|director|vp)\b", re.IGNORECASE
)
GOOD_INDUSTRIES = {"fintech", "saas", "healthtech", "logistics"}


def score_lead(row):
    score = 0

    # 1. Senior position: +3
    if SENIOR_PATTERN.search(row["job_title"]):
        score += 3

    # 2. Good industry: +2
    if row["industry"].strip().lower() in GOOD_INDUSTRIES:
        score += 2

    # 3. Good company size (11-200 employees): +2
    try:
        employees = int(row["employees"].strip().replace(",", ""))
        if 11 <= employees <= 200:
            score += 2
    except ValueError:
        pass  # blank or non-numeric: no points

    return score


def get_tier(score):
    if score >= 6:
        return "hot"
    if score >= 3:
        return "warm"
    return "cold"


scored = []
tier_counts = {"hot": 0, "warm": 0, "cold": 0}

with open("enriched_leads.csv", "r", encoding="utf-8", errors="replace") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames + ["score", "tier"]

    for row in reader:
        score = score_lead(row)
        tier = get_tier(score)
        row["score"] = score
        row["tier"] = tier
        tier_counts[tier] += 1
        scored.append(row)

with open("scored_leads.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(scored)

print(f"{tier_counts['hot']} hot")
print(f"{tier_counts['warm']} warm")
print(f"{tier_counts['cold']} cold")