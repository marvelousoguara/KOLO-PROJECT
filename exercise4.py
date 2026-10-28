import csv

counts = {}
total_leads = 0

with open("leads.csv", "r", encoding = "utf-8", errors = "replace", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total_leads += 1
        country = row["country"].strip().title()
        if country:
            counts[country] = counts.get(country, 0) + 1     

print(counts)               
print(f"Total leads: {total_leads}")