import csv


def is_valid_email(email):
    if any(ch.isspace() for ch in email):
        return False
    if email.count("@") != 1:
        return False

    local, domain = email.split("@")

    if not local:
        return False
    if "." not in domain:
        return False
    if domain.startswith("."):
        return False
    if email.endswith("."):
        return False

    return True


seen = set()
clean = []
dropped = 0

"""Clean the leads data"""
with open("leads.csv", "r", encoding="utf-8", errors="replace", newline = "") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames

    for row in reader:
        row = {k: (v or "").strip() for k, v in row.items()}
        row["email"] = row["email"].lower()
        row["country"] = row["country"].title()
        row["first_name"] = row["first_name"].title()

        if not is_valid_email(row["email"]):
            print("Dropped (invalid):", row["email"])
            dropped += 1
            continue

        if row["email"] in seen:
            print("Dropped (duplicate):", row["email"])
            dropped += 1
            continue

        seen.add(row["email"])
        clean.append(row)

with open("clean_leads.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(clean)

print(f"Clean leads: {len(clean)}")
print(f"Dropped: {dropped}")