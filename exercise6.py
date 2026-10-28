import csv

"""Load enrichment data into a dictionary, keyed by company_domain"""
enrichment = {}

try:
    with open("enrichment.csv", "r", encoding="utf-8", errors="replace") as f:
        for row in csv.DictReader(f):
            domain = row["company_domain"].strip().lower()
            enrichment[domain] = {
                "industry": row["industry"].strip(),
                "employees": row["employees"].strip(),
            }
except FileNotFoundError:
    print("enrichment.csv not found. Put it in the same folder and try again.")
    raise SystemExit

""" Match each lead against the dictionary"""
enriched = []
not_found = 0

with open("clean_leads.csv", "r", encoding="utf-8", errors="replace") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames + ["industry", "employees"]

    for row in reader:
        domain = row["company_domain"].strip().lower()

        if domain in enrichment:
            row["industry"] = enrichment[domain]["industry"]
            row["employees"] = enrichment[domain]["employees"]
            enriched.append(row)
        else:
            print("Not found:", domain)
            not_found += 1
            enriched.append(row)

"""Save the result"""
with open("enriched_leads.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(enriched)

print(f"Enriched leads: {len(enriched)}")
print(f"Companies not found: {not_found}")