import csv
import os
import random

OPENINGS = [
    "I came across your company and wanted to reach out.",
    "Your work in your industry caught my attention.",
    "I wanted to introduce myself and connect with your team.",
]

os.makedirs("outreach", exist_ok=True)

count = 0

with open("scored_leads.csv", "r", encoding="utf-8", errors="replace") as f:
    for row in csv.DictReader(f):
        if row["tier"].strip().lower() != "hot":
            continue

        first_name = row["first_name"].strip().split()[0]
        company = row["company"].strip()
        industry = row["industry"].strip()
        opening = random.choice(OPENINGS)

        message = (
            f"Hi {first_name},\n\n"
            f"{opening}\n\n"
            f"I came across {company} and was interested in your work in the "
            f"{industry} industry.\n\n"
            f"I'd love to connect and explore whether there might be an "
            f"opportunity to work together.\n\n"
            f"Best regards,\n"
            f"The Kolo Team\n"
        )

        domain = row["email"].strip().split("@")[1]
        filename = f"{first_name}_{domain}.txt".lower()
        path = os.path.join("outreach", filename)

        with open(path, "w", encoding="utf-8") as out:
            out.write(message)

        count += 1

print(f"Created {count} message files in the outreach folder.")