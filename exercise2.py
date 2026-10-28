seen = set()
clean = []
with open("raw_emails.txt", "r", encoding="utf-8", errors="replace") as f:
    for line in f:
        email = line.strip().lower()
        if email and email not in seen:
            seen.add(email)
            clean.append(email)

with open("clean_emails.txt", "w", encoding="utf-8") as f:
    for email in clean:
        f.write(email + "\n")

print(f" unique emails: {len(clean)}")                    