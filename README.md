# Lead-Generation-automation-

Company Lead Generator

A Python automation tool that discovers high-potential web development leads from BSE-listed companies by identifying:

Official websites

Website quality & status

Public email addresses

Companies with poor or missing websites (ideal prospects)

This tool helps freelancers, agencies, and sales teams quickly identify businesses that may need website development or redesign services.

 Features

✅ Automatically finds official company websites
✅ Filters out aggregator & social media domains
✅ Evaluates website quality & availability
✅ Extracts publicly available email addresses
✅ Identifies companies with:

- No website

- Poor website

- Dead website

- Under construction website

✅ Generates ready-to-use lead lists

🗂 Project Structure
├── main.py                 # Main automation script
├── bse_companies.xlsx      # Input file (BSE company list)
├── all_results.csv         # Complete scan results
├── qualified_leads.csv     # High-potential leads
 How It Works
 
1. Input Data

The script loads company names from:
bse_companies.xlsx
Column used:
Security Name

2. Website Discovery

Uses DuckDuckGo search (ddgs) to find official websites while filtering unwanted domains such as:
LinkedIn
Wikipedia
Moneycontrol
Social media platforms

3️. Website Quality Check

Each website is categorized as:
Good Website
Poor Website
Dead Website
Under Construction
No Website

Evaluation is based on:

HTTP response status
Page content size
Construction indicators

4️. Email Extraction

The script extracts emails from:
mailto: links
Website text content

5️. Lead Qualification

Companies are marked as qualified leads if they have:
No website
Poor website
Dead website
Under construction website

Use Cases

✔ Freelancers looking for web development clients
✔ Digital agencies generating outbound leads
✔ Sales teams prospecting businesses
✔ Startup founders offering digital services

Notes & Best Practices

Respect website terms and data usage policies.
Use extracted emails responsibly.
Add delays (time.sleep) to avoid request blocking.
Increase limits responsibly to avoid IP bans.

Future Improvements

LinkedIn contact discovery
Website technology detection
SEO & performance scoring
CRM integration
Automated outreach support

🤝 Contributing

Pull requests and improvements are welcome!

📜 License

This project is open-source and available under the MIT License
