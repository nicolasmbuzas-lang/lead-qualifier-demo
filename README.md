# AI Lead Qualification Agent

Automatically scores and categorizes inbound sales leads using Claude, so your sales team spends time on the leads that matter instead of manually reading through every form submission.

## What it does

1. Reads a CSV of raw inbound leads (name, company, email, message, budget)
2. Sends each lead to Claude with a structured prompt
3. Gets back a **score (1-10)**, **category** (Hot / Warm / Cold), a **one-sentence summary**, and a **recommended next action**
4. Writes everything to a new CSV, sorted hottest-first

This is a simplified standalone version of the kind of automation I build for clients — in production this would typically plug directly into a webhook from your contact form, Typeform, or CRM instead of reading a CSV, and push results straight into your CRM or Slack.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# edit .env and add your Anthropic API key (get one at console.anthropic.com)
```

## Usage

```bash
python lead_qualifier.py
```

Or with custom file paths:

```bash
python lead_qualifier.py my_leads.csv results.csv
```

## Example output

| name | company | score | category | summary | recommended_action |
|---|---|---|---|---|---|
| Sarah Kimani | Nairobi FreshFoods | 9 | Hot | Needs automated order-form processing within 2 weeks, has a budget in mind | Call within 24 hours to scope the integration |
| Marcus Webb | Webb & Partners Law | 8 | Hot | Wants an ongoing contractor for PDF-to-case-management automation | Schedule a discovery call, propose a retainer structure |
| Julie Tremblay | Tremblay Immobilier | 4 | Warm | Curious about automation but has no defined project yet | Send an educational follow-up, offer a free 15-min call |
| David Chen | Chen Logistics | 3 | Cold | Vague future interest, no timeline or budget | Add to a low-touch nurture sequence |
| (spam entry) | — | 1 | Cold | Unsolicited crypto spam | Ignore / mark as spam |

## Extending this

- **Webhook trigger**: swap the CSV read for a Flask/FastAPI endpoint that receives form submissions directly
- **CRM push**: write results to HubSpot/Pipedrive/Airtable via their API instead of a CSV
- **Slack alerts**: ping a `#hot-leads` channel automatically when `category == "Hot"`
- **n8n/Zapier version**: the same qualification logic can run as a step inside a no-code workflow, calling the Claude API directly from an HTTP node

## Why Claude here instead of keyword rules

Keyword-based lead scoring ("contains 'budget'" = +2 points) breaks the moment a lead phrases things differently. Claude reads the actual intent, tone, and urgency in free-text messages the way a human sales rep would — it correctly flagged the spam entry above with zero explicit spam keywords, and gave the Nairobi FreshFoods lead top priority based on both a firm timeline *and* a stated budget appearing together in one sentence.
