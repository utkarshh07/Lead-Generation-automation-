import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import time
# from googlesearch import search

INPUT_FILE = "bse_companies.xlsx"
OUTPUT_FILE = "qualified_leads.csv"

EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+"

# =============================
# FIND OFFICIAL WEBSITE
# =============================

from ddgs import DDGS
from urllib.parse import urlparse

BAD_DOMAINS = [
    "moneycontrol", "bloomberg", "reuters", "linkedin",
    "facebook", "twitter", "instagram", "youtube",
    "wikipedia", "screener", "trendlyne", "pdf"
]

def is_valid_domain(url):
    domain = urlparse(url).netloc.lower()
    return not any(bad in domain for bad in BAD_DOMAINS)

def find_website(company):
    try:
        query = company.replace("Ltd", "").replace("Limited", "")
        
        with DDGS() as ddgs:
            results = ddgs.text(query + " official website", max_results=8)

            for r in results:
                url = r["href"]

                if not is_valid_domain(url):
                    continue

                if url.endswith(".pdf"):
                    continue

                return url
    except Exception as e:
        print("Search error:", e)

    return "Not Found"

# =============================
# CHECK WEBSITE QUALITY
# =============================

def check_website(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=10)

        if r.status_code != 200:
            return "Dead Website"

        content = r.text.lower()

        if len(content) < 2000:
            return "Poor Website"

        if "under construction" in content:
            return "Under Construction"

        return "Good Website"

    except:
        return "No Website"

# =============================
# EXTRACT EMAILS
# =============================

def extract_emails(url):
    emails = set()
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=10)

        soup = BeautifulSoup(r.text, "html.parser")

        for link in soup.select("a[href^=mailto]"):
            emails.add(link.get("href").replace("mailto:", ""))

        found = re.findall(EMAIL_REGEX, soup.get_text())
        emails.update(found)

    except:
        pass

    return ", ".join(emails) if emails else "Not Found"
# =============================
# LOAD DATA
# =============================

df = pd.read_excel(INPUT_FILE)

companies = df["Security Name"].dropna().unique()

leads = []

for company in companies[:1000]:   
    print("Searching:", company)

    website = find_website(company)

    if website == "Not Found":
        leads.append([company, "Not Found", "No Website", "Not Found"])
        continue

    status = check_website(website)
    emails = extract_emails(website)

    leads.append([company, website, status, emails])

    time.sleep(1)

# save results
result = pd.DataFrame(leads, columns=["Company", "Website", "Status", "Emails"])

qualified = result[
    result["Status"].isin(["No Website", "Poor Website", "Dead Website", "Under Construction"])
]

# save full results
result.to_csv("all_results.csv", index=False)

# save only qualified leads
qualified.to_csv(OUTPUT_FILE, index=False)

print("\n✅ Lead generation complete!")