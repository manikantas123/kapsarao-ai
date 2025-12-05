📊 Agentic Facebook Performance Analyst — Kasparro Assignment
Built by: Mummidi Manikanta

A fully functional Agentic Marketing Intelligence System that analyzes Facebook Ads performance, detects ROAS drops, evaluates insights with severity & confidence, and generates creative recommendations — similar to real-world marketing analytics platforms.

🚀 Overview

This system implements a multi-agent analytics pipeline capable of:

Automatically analyzing the last 14-day performance trends

Detecting shifts in ROAS, CTR, Spend, Revenue, Clicks

Validating insights using statistical deltas

Scoring insights with severity, confidence, and strength

Generating creative strategies, hooks, angles, and CTAs

Producing human-readable reports + JSON outputs

Designed as part of the Kasparro Agentic Performance Analyst Challenge.

🧠 System Architecture
User Query
    ↓
📌 Planner Agent
    Breaks query → actionable analysis tasks
    ↓
📌 Data Agent
    Loads CSV → validates schema → cleans data
    Computes 14-day baseline vs recent metrics
    ↓
📌 Insight Agent
    Detects shifts in ROAS, CTR, Spend, Revenue, Clicks
    Generates raw insights
    ↓
📌 Evaluator Agent
    Validates insights using deltas & thresholds
    Assigns severity + confidence
    ↓
📌 Creative Agent
    Builds creative strategies from insights
    (angles, hooks, messages, CTAs)
    ↓
📌 Orchestrator
    Writes:
      ✔ Markdown Report
      ✔ insights.json
      ✔ creatives.json

📂 Folder Structure
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
│       ├── io.py
│       ├── schema.py
│       ├── logging.py
│       └── helpers.py
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

Windows PowerShell

.venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the Pipeline

Run with any analysis query:

python -m src.orchestrator.run "Analyze ROAS drop in last 14 days"


Outputs appear in:

reports/report.md

reports/insights.json

reports/creatives.json

logs/*.jsonl

📑 What the System Does
✔ 1. Loads & Validates Facebook Ads CSV

Ensures required columns exist:

campaign_name, adset_name, date

spend, impressions, clicks, ctr

purchases, revenue, roas

creative_type, creative_message

audience_type, platform, country

✔ 2. Cleans Data & Computes Metrics

Fixes numeric types

Recomputes CTR & ROAS safely

Sorts by date

Aggregates daily metrics

✔ 3. Baseline vs Recent Split

Last 28 days → split into:

Baseline: first 14 days

Recent: last 14 days

✔ 4. Insight Generation

For each metric:

ROAS

CTR

Spend

Revenue

Clicks

The system evaluates:

Δ (relative change)

Hypothesis (declining / improving)

Severity (low/medium/high)

Confidence score

Evidence block with averages

✔ 5. Validation & Scoring

Evaluator assigns:

strength

severity

confidence

✔ 6. Creative Recommendations

Each underperforming metric receives:

Angle

Explanation

Hooks

CTAs

These creatives are grounded in performance data.

📌 Example Insight (from insights.json)
{
  "metric": "roas",
  "hypothesis": "ROAS is declining over time.",
  "severity": "medium",
  "delta": -0.089,
  "confidence": 0.85
}

🎨 Example Creative Idea (from creatives.json)
{
  "angle": "Value & Performance Messaging",
  "hooks": ["Better Value for Every Rupee", "High Performance. Zero Compromise"],
  "ctas": ["Shop Now", "Discover Your Comfort Upgrade"]
}

📘 Example Markdown Report (from report.md)
# ROAS Performance Diagnostic Report

## Key Insights
- ROAS → declining (-8.9%)
- Revenue → declining (-10.6%)
- CTR → no big change
- Spend → slightly down
- Clicks → declining

## Creative Recommendations
### Angle: Value & Performance Messaging
Hooks:
- Better Value for Every Rupee
- High Performance. Zero Compromise
CTAs:
- Shop Now

🧠 Skills Demonstrated

This project shows proficiency in:

Data Engineering

✔ CSV ingestion
✔ Schema validation
✔ Data cleaning & transformation
✔ Aggregation logic

AI/Agent Architecture

✔ Multi-agent workflow
✔ Task decomposition
✔ Insight generation logic
✔ Creative strategy modeling

Software Engineering

✔ Modular Python code
✔ Logging system
✔ Error handling
✔ YAML-driven configuration
✔ Fully reproducible pipeline

Marketing Analytics

✔ ROAS, CTR, CPC logic
✔ Trend analysis
✔ Creative recommendation frameworks

🎯 Conclusion

This project replicates a modern marketing intelligence engine using an agentic architecture — delivering actionable insights, validated metrics, and creative strategies automatically.

It demonstrates skills that are highly relevant for:

AI product development

Marketing analytics

Performance marketing tools

Data engineering pipelines

LLM-based reasoning systems