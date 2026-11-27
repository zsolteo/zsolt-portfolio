# Open-source auto research and ads maker for e-commerce sellers

Small dropshipping and private label sellers spend most of their week on the same work: finding products, checking competitors, writing ad scripts, cutting videos and scheduling posts. Agencies and closed SaaS tools charge heavily for it. This toolkit does it with Claude, for free, under the MIT license.

I test everything on my own private label store first, so each piece is proven on real campaigns before it goes here.

## How it works

```
niche or product list
   -> research/product_research.py   scores products, finds angles and hooks
   -> ads/ad_maker.py                writes video ad scripts, shot lists, captions (EN/HU/...)
   -> remotion template              renders the video ad            (coming)
   -> workflows/ (n8n + Buffer)      schedules ads, reads results    (coming)
   -> results feed the next research round
```

## Quick start

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...

# 1. Research: score the example products (add --web to let Claude search current trends)
python research/product_research.py --niche "home gym accessories" \
    --products examples/products.csv --out research_report.json

# 2. Ads: scripts for the top 3 products in English and Hungarian
python ads/ad_maker.py --report research_report.json --top 3 --lang en,hu
```

Output goes to `ads/output/`: one Markdown file per product to read and shoot from, and one JSON file to feed into a video template or workflow.

## Status

| Part | Status |
|---|---|
| Product research agent | Working |
| Ad script and shot list maker | Working |
| Remotion video ad template | In progress |
| n8n + Buffer scheduling and results loop | In progress |

## Rules the tools follow

No fake reviews, no false product claims, no medical or income promises. Check every ad against the ad platform's policies before running it.

## License

MIT
