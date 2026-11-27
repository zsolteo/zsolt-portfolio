"""Auto research: score product ideas for a niche with Claude.

Usage:
    export ANTHROPIC_API_KEY=...
    python research/product_research.py --niche "home gym accessories" \
        --products examples/products.csv --out research_report.json

    # let Claude search the web for current trends and competitors
    python research/product_research.py --niche "pet grooming" --web

products.csv needs a `name` column; `price`, `cost` and `notes` are optional.
Without --products, Claude proposes 10 candidates for the niche itself.
"""

import argparse
import csv
import json
import os
import sys

import anthropic

MODEL = os.environ.get("CLAUDE_MODEL", "claude-sonnet-5-5")

SCHEMA = """Return ONLY valid JSON in this shape:
{
  "niche": str,
  "summary": str,
  "products": [
    {
      "name": str,
      "score": int,               // 0-100 overall
      "demand": int,              // 0-10
      "competition": int,         // 0-10, 10 = crowded
      "margin_potential": int,    // 0-10
      "ad_friendliness": int,     // 0-10, how well it shows in a short video ad
      "target_customer": str,
      "angles": [str],            // 3 ad angles that would sell it
      "hooks": [str],             // 3 first-line hooks for a 15-30 s video ad
      "risks": [str]
    }
  ]
}
Sort products by score, highest first."""


def load_products(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows or "name" not in rows[0]:
        sys.exit(f"{path} needs a header row with a 'name' column")
    return rows


def build_prompt(niche, products):
    if products:
        listing = "\n".join(
            f"- {p['name']}"
            + (f" | price {p['price']}" if p.get("price") else "")
            + (f" | cost {p['cost']}" if p.get("cost") else "")
            + (f" | {p['notes']}" if p.get("notes") else "")
            for p in products
        )
        task = f"Evaluate these candidate products for the niche '{niche}':\n{listing}"
    else:
        task = f"Propose and evaluate 10 product ideas for the niche '{niche}'."
    return (
        "You are a product researcher for a small dropshipping / private label seller "
        "who sells mainly through short video ads.\n"
        f"{task}\n\n"
        "Judge demand, competition, margin potential and how well each product works "
        "in a short video ad. Be concrete and honest about risks (shipping, returns, "
        "saturation, ad policy).\n\n" + SCHEMA
    )


def extract_json(text):
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("no JSON object in the model output")
    return json.loads(text[start : end + 1])


def run(niche, products, web):
    client = anthropic.Anthropic()
    kwargs = {}
    if web:
        kwargs["tools"] = [{"type": "web_search_20250305", "name": "web_search", "max_uses": 5}]
    msg = client.messages.create(
        model=MODEL,
        max_tokens=8000,
        messages=[{"role": "user", "content": build_prompt(niche, products)}],
        **kwargs,
    )
    text = "".join(block.text for block in msg.content if block.type == "text")
    return extract_json(text)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--niche", required=True)
    ap.add_argument("--products", help="CSV with a 'name' column")
    ap.add_argument("--web", action="store_true", help="let Claude search the web")
    ap.add_argument("--out", default="research_report.json")
    args = ap.parse_args()

    products = load_products(args.products) if args.products else []
    report = run(args.niche, products, args.web)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    for p in report.get("products", []):
        print(f"{p.get('score', '?'):>3}  {p.get('name')}")
    print(f"\nFull report: {args.out}")


if __name__ == "__main__":
    main()
