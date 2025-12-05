📊 Agentic Facebook Performance Analyst — Kasparro Assignment

Built by Mummidi Manikanta
A fully working multi-agent ROAS diagnostic system that analyzes 14-day performance trends, validates insights, and generates creative recommendations based on real marketing signals.

🚀 Summary

This project implements an Agentic Analytics Pipeline similar to how modern marketing intelligence products work.
It uses multiple coordinated agents:

Planner Agent – Understands the query & breaks into tasks

Data Agent – Loads Facebook Ads CSV, validates schema, computes baseline vs recent metrics

Insight Agent – Detects ROAS/CTR/Spend/Revenues shifts

Evaluator Agent – Validates insights with strength, severity & confidence

Creative Agent – Generates performance-based creative recommendations

Orchestrator – Runs pipeline end-to-end and writes Markdown + JSON reports

Outputs include:

📄 reports/report.md — Human-readable diagnostic report
📈 reports/insights.json — Validated insights
🎨 reports/creatives.json — Creative ideas based on insights
🪵 logs/*.jsonl — Agent communication logs

🗂️ Folder Structure
kasparro-agentic-fb-analyst/
│
├── src/
│   ├── orchestrator/
│   │   └── run.py
│   ├── agents/
│   │   ├── planner_agent.py
│   │   ├── data_agent.py
│   │   ├── insight_agent.py
│   │   ├── evaluator_agent.py
│   │   └── creative_agent.py
│   ├── utils/
│   │   ├── io.py
│   │   ├── schema.py
│   │   ├── logging.py
│   │   └── helpers.py (optional)
│
├── data/
│   └── fb_ads.csv
│
├── config/
│   └── config.yaml
│
├── reports/
│   ├── report.md
│   ├── insights.json
│   └── creatives.json
│
├── logs/
│   └── *.jsonl
│
└── README.md

⚙️ Setup Instructions
1️⃣ Create Virtual Environment
python -m venv .venv

2️⃣ Activate Environment

Windows (PowerShell):

.venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the Pipeline

Run with your query:

python -m src.orchestrator.run "Analyze ROAS drop in last 14 days"


After successful execution, check:

reports/report.md
reports/insights.json
reports/creatives.json
logs/

📑 What This System Does
✔ Loads & Validates Facebook Ads Data

Ensures schema has:

campaign_name

adset_name

date

spend, impressions, clicks, ctr

purchases, revenue, roas

creative_type, creative_message

audience_type, platform, country

✔ Computes Baseline vs Recent Metrics

Aggregates last 28 days → splits into:

first 14 days (baseline)

last 14 days (recent)

✔ Generates Insights

For metrics:

ROAS

CTR

Spend

Revenue

Clicks

✔ Evaluates Severity & Confidence

Adds:

strength

severity level

confidence score

✔ Produces Creative Strategies

Value angles, hooks, CTAs based on performance dips.