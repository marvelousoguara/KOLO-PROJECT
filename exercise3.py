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

bad = []
with open("clean_emails.txt", "r", encoding="utf-8") as f:
    for line in f:
        email = line.strip()
        if not is_valid_email(email):
            bad.append(email)

with open("bad_emails.txt", "w", encoding="utf-8") as f:
    for email in bad:
        f.write(email + "\n")

print(f"bad emails: {len(bad)}")