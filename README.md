# Kolo practice pack: file handling with real-world data

## The setup

You've just joined **Kolo**, a small startup in Lagos, as the ops intern. The sales team runs on spreadsheets and they are a mess. Your job is to clean them up with Python.

Everything here uses what you're learning right now: file handling, loops, dictionaries, functions, and a bit of error handling. No new libraries except `csv`, `os` and `random`, which all come with Python.

**What's in the folder**

- `raw_emails.txt`: newsletter signups, typed in by hand. Messy.
- `leads.csv`: the sales team's list of people they want to sell to.
- `enrichment.csv`: extra info about each company, bought from a data provider.

Put all the files in the same folder as your script. Do one or two exercises per sitting, alongside the course, not instead of it.

Each exercise has a **Check** line. If your numbers match, you've got it, even if your code looks nothing like the solution.

---

## Level 1: warm-up (raw_emails.txt)

### 1. How big is the list?

Open `raw_emails.txt` and print how many lines it has, and how many of those lines are not blank.

**Check:** 20 lines, 18 non-blank.

**Hint:** a line with only spaces in it is still blank. What does `.strip()` do to it?

### 2. Clean the list

Make a new file `clean_emails.txt` with one email per line where every email is:

- trimmed (no spaces before or after)
- lowercase
- listed only once

In sales teams this is called **list hygiene**, and removing repeats is **deduping** (short for de-duplicating).

**Check:** 14 unique emails. After exercise 3 takes out the bad ones, **10** are left.

**Hint:** `Seun.O@gmail.com` and `seun.o@gmail.com` are the same person. Clean first, then check if you've seen it before.

### 3. Catch the bad emails

Write a function `is_valid_email(email)` that returns `True` or `False`. A valid email here:

- has exactly one `@`
- has something before the `@`
- has a `.` after the `@`, but not straight after it and not at the very end
- has no spaces

Write the bad ones to `bad_emails.txt`. Sending to bad emails makes emails **bounce**, and too many bounces gets a company's emails marked as spam.

**Check:** 4 bad emails.

---

## Level 2: the lead list (leads.csv)

A **lead** is a person the sales team might sell to. A list of them lives in a **CRM** (customer relationship management tool). Ours is just a CSV for now.

### 4. Summarise the list

Read `leads.csv` with `csv.DictReader` and count how many leads come from each country. Store the counts in a dictionary.

**Check:** 27 rows. Nigeria should be **14**.

**Hint:** if you see `Nigeria`, `nigeria` and `Nigeria ` as three different countries, look at the raw data carefully. Then fix it with `.strip()` and `.title()`.

### 5. Clean the lead list

Write `clean_leads.csv` with:

- every value trimmed
- emails lowercase, countries in title case
- rows with invalid emails removed (reuse your function from exercise 3)
- duplicate people removed (same email = same person)

**Check:** 23 clean leads, 4 dropped.

**Hint:** use `csv.DictWriter` to write. Open files with `newline=""` for both reading and writing CSVs, or you'll get blank rows on Windows.

### 6. Enrich it

`enrichment.csv` tells you each company's industry and number of employees. Adding extra data to a lead list like this is called **enrichment**. Company facts like industry and size are called **firmographics**.

Load `enrichment.csv` into a dictionary where the key is `company_domain`. Then add `industry` and `employees` columns to every lead and write `enriched_leads.csv`. If a company isn't in the enrichment file, write `unknown`.

Also: wrap the file opening in `try/except FileNotFoundError` so the script doesn't crash if someone deletes `enrichment.csv`.

**Check:** 21 enriched, 2 not found. Which companies are missing?

### 7. Score the leads

Sales teams can't call everyone, so they rank leads. This is **lead scoring**. The type of company they most want to sell to is their **ICP** (ideal customer profile).

Kolo's ICP is:

- **Senior people (+3 points):** job title includes founder, CEO, CTO, COO, head, director or VP
- **Right industry (+2):** Fintech, SaaS, Healthtech or Logistics
- **Right size (+2):** 11 to 200 employees

Write a function `score_lead(row)` that returns the score. Then give each lead a tier: 6 or more is **hot**, 3 to 5 is **warm**, 0 to 2 is **cold**. Write `scored_leads.csv` with `score` and `tier` columns added.

**Check:** 8 hot, 11 warm, 4 cold.

**Bug hunt:** Kemi is a *Marketing Coordinator* and Kwame is an *Ops Coordinator*. Neither is senior, so they should both score **4** (warm). If either of them shows up as hot, your code has a bug. Find out why. (This one is worth writing down when you figure it out.)

---

## Level 3: boss level

### 8. Mini CRM with a while loop

Build a menu that keeps running until the user quits:

```
1) Search by company  2) Show hot leads  3) Add a lead  4) Save and quit
```

- Load `scored_leads.csv` at the start
- **1** asks for a company name and prints everyone who works there (partial matches count: `pay` should find Paystride and Calabash Pay)
- **2** prints all hot leads
- **3** asks for a name, email and company. If the email is invalid, say so and go back to the menu without adding it
- **4** saves everything back to the file and ends the loop with `break`
- Anything else: print a message and show the menu again. The program must never crash, whatever gets typed

**Check:** type `7`, `abc`, and just press Enter at the menu. The program should survive all three.

**Hint:** start with `while True:`. The *only* way out should be option 4. Sketch the menu on paper first: what happens for each choice, and where does the loop go next?

### 9. Write the outreach

Reaching out to leads is called **outreach**. For every hot lead, write a short personalised message into its own text file inside a folder called `outreach/`.

- Name each file like `adaeze_paystride.ng.txt`
- Use their first name, company and industry in the message
- Use `random.choice()` to pick the opening line from a list of three, so the messages don't all start the same way

**Check:** 8 files in `outreach/`.

**Hint:** `os.makedirs("outreach", exist_ok=True)` creates the folder, and doesn't complain if it already exists.

---

## Words used in this pack

These are words sales and marketing teams use every day. Together they're often called the company's **GTM** (go-to-market) side.

| Word | Meaning |
|---|---|
| Lead | A person you might sell to |
| CRM | The tool where leads and customers are stored |
| List hygiene | Keeping contact lists clean and accurate |
| Dedupe | Remove duplicate records |
| Bounce | An email that fails to deliver |
| Enrichment | Adding extra data to a lead or company |
| Firmographics | Facts about a company: industry, size, location |
| ICP | Ideal customer profile: the kind of company you most want to sell to |
| Lead scoring | Ranking leads by how likely they are to buy |
| Outreach | Contacting leads, usually by email or LinkedIn |
