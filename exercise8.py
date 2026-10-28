import csv

FILE = "scored_leads.csv"


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


def load_leads():
    with open(FILE, "r", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        return list(reader), reader.fieldnames


def save_leads(leads, fieldnames):
    with open(FILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(leads)


def search_leads(leads):
    term = input("Enter company name: ").strip().lower()
    if not term:
        print("Please type something to search for.")
        return

    matches = [l for l in leads if term in l["company"].lower()]

    if not matches:
        print("No leads found.")
        return

    print("\nResults:")
    for i, lead in enumerate(matches, start=1):
        print(f"{i}. {lead['name']} - {lead['company']}")


def show_hot_leads(leads):
    print("\n===== HOT LEADS =====")
    found = False
    for lead in leads:
        if lead["tier"].strip().lower() == "hot":
            found = True
            print(f"\nName: {lead['name']}")
            print(f"Company: {lead['company']}")
            print(f"Industry: {lead['industry']}")
            print(f"Score: {lead['score']}")
            print(f"Tier: {lead['tier']}")
    if not found:
        print("No hot leads yet.")


def add_lead(leads, fieldnames):
    name = input("Name: ").strip().title()
    email = input("Email: ").strip().lower()
    company = input("Company: ").strip()

    if not is_valid_email(email):
        print("Invalid email address. Please try again.")
        return

    # Start with every column blank, then fill in what we know
    lead = {col: "" for col in fieldnames}
    lead["name"] = name
    lead["email"] = email
    lead["company"] = company
    lead["industry"] = "Unknown"
    lead["employees"] = "Unknown"
    lead["score"] = 0
    lead["tier"] = "cold"

    leads.append(lead)
    print(f"Added {name}.")


def main():
    try:
        leads, fieldnames = load_leads()
    except FileNotFoundError:
        print(f"{FILE} not found. Run exercise7.py first.")
        return

    while True:
        print("\n===== MINI CRM =====\n")
        print("1. Search for a lead")
        print("2. Show hot leads")
        print("3. Add a new lead")
        print("4. Save and quit")
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            search_leads(leads)
        elif choice == "2":
            show_hot_leads(leads)
        elif choice == "3":
            add_lead(leads, fieldnames)
        elif choice == "4":
            save_leads(leads, fieldnames)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")


main()