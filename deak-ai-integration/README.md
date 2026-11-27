# Industrial AI integration — valve service and maintenance

Planned AI integration for D.E.Á.K. Irányítástechnikai Kft. (Dunaújváros, Hungary). The company is the exclusive Hungarian distributor and Authorized Service Partner for Valmet flow control products (Neles, Jamesbury, Flowrox). It services control, shut-off and emergency shutdown valves for refining, chemicals, energy, pulp and paper, hydrogen and Power-to-X plants.

This folder will hold the reusable, client-neutral parts of the work. Client data, prices and internal processes are never committed here.

## Problems I will solve

| Area | Problem | Claude-based solution |
|---|---|---|
| Service and repair | Technician notes and diagnostic results end up in scattered files | Structured service reports and valve failure histories generated from notes and test data |
| Shutdown support | Plant outages need parts, people and timing planned to the hour | Planning agent that drafts outage schedules and parts lists from the maintenance history |
| Spare parts and inventory | Stock levels and lead times tracked by hand | MCP server exposing stock, orders and valve records to Claude |
| Logistics | Pickups, deliveries and on-site visits across the country | Route and schedule drafting from open jobs |
| Documentation and certification | Datasheets and certificates checked manually against specs | Drafting and cross-checking against manufacturer documentation |
| Knowledge retention | Know-how sits with senior technicians | Searchable knowledge base (see the Obsidian HQ template) |

## Planned open-source deliverables

- `maintenance-mcp/` — MCP server for service records, valve histories and spare parts
- `n8n-templates/` — service report, shutdown planning and job intake workflows
- `docs/` — a write-up of what works when you bring Claude into a real industrial service company

## Status

Planned. Work starts in the coming months.
