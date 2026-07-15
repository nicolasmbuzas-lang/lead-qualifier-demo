"""
AI-powered lead qualification agent.

Reads a CSV of inbound leads, uses Claude to score and categorize each one,
and writes the enriched results to a new CSV sorted by priority (hottest first).

Usage:
    python lead_qualifier.py [input_csv] [output_csv]

Requires:
    ANTHROPIC_API_KEY environment variable (or a .env file — see .env.example)
"""

import csv
import os
import sys

import anthropic
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

MODEL = os.environ.get("CLAUDE_MODEL", "claude-opus-4-8")

SYSTEM_PROMPT = """You are a B2B sales development assistant. Given information \
about an inbound lead (name, company, message, and stated budget if any), assess \
how promising the lead is for a follow-up call.

Score from 1 (not a fit, spam, or no real intent) to 10 (urgent, well-funded, \
clear need). Categorize as "Hot" (score 8-10), "Warm" (score 4-7), or "Cold" \
(score 1-3). Write a one-sentence summary of what the lead wants, and a concrete \
recommended next action for the sales rep."""


class LeadQualification(BaseModel):
    score: int = Field(description="Lead quality score from 1 to 10")
    category: str = Field(description='One of: "Hot", "Warm", "Cold"')
    summary: str = Field(description="One-sentence summary of what the lead wants")
    recommended_action: str = Field(description="Concrete next step for the sales rep")


def qualify_lead(client: anthropic.Anthropic, lead: dict) -> LeadQualification:
    lead_text = (
        f"Name: {lead.get('name', 'Unknown')}\n"
        f"Company: {lead.get('company', 'Unknown')}\n"
        f"Email: {lead.get('email', 'Unknown')}\n"
        f"Budget: {lead.get('budget', 'Not stated')}\n"
        f"Message: {lead.get('message', '')}"
    )

    response = client.messages.parse(
        model=MODEL,
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": lead_text}],
        output_format=LeadQualification,
    )
    return response.parsed_output


def main() -> None:
    input_path = sys.argv[1] if len(sys.argv) > 1 else "leads.csv"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "qualified_leads.csv"

    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit(
            "ANTHROPIC_API_KEY is not set. Copy .env.example to .env and add your key."
        )

    client = anthropic.Anthropic()

    with open(input_path, newline="", encoding="utf-8") as f:
        leads = list(csv.DictReader(f))

    if not leads:
        sys.exit(f"No leads found in {input_path}")

    results = []
    for i, lead in enumerate(leads, start=1):
        print(f"[{i}/{len(leads)}] Qualifying {lead.get('name', 'unknown')}...")
        qualification = qualify_lead(client, lead)
        results.append({**lead, **qualification.model_dump()})

    results.sort(key=lambda r: r["score"], reverse=True)

    fieldnames = list(leads[0].keys()) + ["score", "category", "summary", "recommended_action"]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"\nDone. Wrote {len(results)} qualified leads to {output_path}")


if __name__ == "__main__":
    main()
