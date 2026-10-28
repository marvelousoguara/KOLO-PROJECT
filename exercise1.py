total = 0 
non_blank = 0

with open ("raw_emails.txt", "r", encoding = "utf-8", errors = "replace") as f :
    for line in f:
        total += 1
        if line.strip():
            non_blank += 1

print(f"total lines: {total}")
print(f"non_ blank lines : {non_blank}")                 
