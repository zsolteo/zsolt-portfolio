"""Ads maker: turn a research report into ready-to-shoot video ad scripts.

Usage:
    python ads/ad_maker.py --report research_report.json --top 3 --lang en,hu

Writes one Markdown file per product into ads/output/ with:
hook, 15-30 s script with shot list, on-screen text, caption and hashtags.
The JSON next to it can be fed to a Remotion template or an n8n workflow.
"""

import argparse
import json
import os
import re

import anthropic

MODEL = os.environ.get("CLAUDE_MODEL", "claude-sonnet-5-5")

SCHEMA = """Return ONLY valid JSON:
{
  "product": str,
  "ads": [
    {
      "lang": str,
      "angle": str,
      "hook": str,
      "shots": [{"seconds": str, "visual": str, "voiceover": str, "on_screen_text": str}],
      "caption": str,
      "hashtags": [str],
      "cta": str
    }
  ]
}"""


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60] or "product"


def make_ads(client, product, langs, per_lang):
    prompt = (
        "You write short-form video ads (TikTok, Reels, Shorts) for a small e-commerce seller.\n"
        f"Product research:\n{json.dumps(product, ensure_ascii=False, indent=2)}\n\n"
        f"Write {per_lang} different ads per language for these languages: {', '.join(langs)}. "
        "Each ad uses a different angle from the research, opens with a scroll-stopping hook "
        "in the first 2 seconds, runs 15-30 seconds, and ends with one clear call to action. "
        "No false claims, no fake reviews, no medical or income promises.\n\n" + SCHEMA
    )
    msg = client.messages.create(
        model=MODEL, max_tokens=6000, messages=[{"role": "user", "content": prompt}]
    )
    text = "".join(b.text for b in msg.content if b.type == "text")
    return json.loads(text[text.find("{") : text.rfind("}") + 1])


def to_markdown(result):
    lines = [f"# Ads: {result['product']}", ""]
    for i, ad in enumerate(result["ads"], 1):
        lines += [f"## Ad {i} ({ad['lang']}) — {ad['angle']}", "", f"**Hook:** {ad['hook']}", ""]
        lines += ["| Time | Visual | Voiceover | On-screen text |", "|---|---|---|---|"]
        for s in ad["shots"]:
            lines.append(f"| {s['seconds']} | {s['visual']} | {s['voiceover']} | {s['on_screen_text']} |")
        lines += ["", f"**Caption:** {ad['caption']}", "", " ".join(ad["hashtags"]), "", f"**CTA:** {ad['cta']}", ""]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--report", required=True, help="JSON from research/product_research.py")
    ap.add_argument("--top", type=int, default=3, help="how many top products to write ads for")
    ap.add_argument("--lang", default="en", help="comma-separated, e.g. en,hu")
    ap.add_argument("--per-lang", type=int, default=2)
    ap.add_argument("--out-dir", default=os.path.join("ads", "output"))
    args = ap.parse_args()

    with open(args.report, encoding="utf-8") as f:
        report = json.load(f)
    products = sorted(report.get("products", []), key=lambda p: p.get("score", 0), reverse=True)[: args.top]
    langs = [l.strip() for l in args.lang.split(",") if l.strip()]

    os.makedirs(args.out_dir, exist_ok=True)
    client = anthropic.Anthropic()
    for product in products:
        result = make_ads(client, product, langs, args.per_lang)
        base = os.path.join(args.out_dir, slug(product["name"]))
        with open(base + ".json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        with open(base + ".md", "w", encoding="utf-8") as f:
            f.write(to_markdown(result))
        print(f"Wrote {base}.md")


if __name__ == "__main__":
    main()
