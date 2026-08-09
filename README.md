# Use Case: Cost-Aware Auto-Routing

**Author fingerprint:** `DBHATT-Debashis2007-SystemDesignPOC-2026` — Debashis Bhattacharjee ([@Debashis2007](https://github.com/Debashis2007))

**YouTube walkthrough:** [Cost Aware Auto Routing — System Design #Shorts](https://youtu.be/9FjuGcUSwFQ)

**Design doc:** [docs/DESIGN.md](./docs/DESIGN.md) — architecture, patterns, and why.


**Parent system design:** [09 — Multi-Model Routing / API Platform](../09-multi-model-routing-api-platform.md)

## Users & problem

Apps want “good enough” quality at lowest cost. A router sends easy prompts to small models and escalates hard ones—transparently.

## Requirements & SLOs

| Requirement | Target |
|-------------|--------|
| Save cost | Majority traffic on small model |
| Quality floor | Escalate on low confidence / hard tasks |
| Transparency | Response shows model used |
| Determinism opt-out | Allow pin/disable auto |

## Design (from parent)

```
Request → complexity/confidence classifier
  → small model → (optional) verify → escalate to large
  → log route decision + cost
```

Reuse router hooks from **09**; separate fleets from [01](../01-llm-inference-serving.md).

## Specializations

| Concern | Auto-route choice |
|---------|-------------------|
| Policy | Never auto-route if user pinned model |
| Cascade | Bound extra latency/cost on escalate |
| Eval | Track win rate vs always-large |
| Safety | Run safety on final output path |

## Failure modes

- Oscillation → sticky per session; hysteresis.
- Classifier bias → monitor slice quality regressions ([05](../05-model-monitoring-observability.md)).
- Hidden model → always return chosen revision.




## Design walkthrough (opens on GitHub)

> **Watch on YouTube:** [Cost Aware Auto Routing — System Design #Shorts](https://youtu.be/9FjuGcUSwFQ)


![Design overview](docs/video/design-overview.gif)

Full narrated video (download): [docs/video/design-overview.mp4](docs/video/design-overview.mp4)

## Run (self-contained POC)

This folder is a **standalone** project (safe to split into its own GitHub repo).

```bash
cd cost-aware-auto-routing
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
PYTHONPATH=. python -m uvicorn app.main:app --reload --port 8000
```

```bash
curl -s http://127.0.0.1:8000/health | jq
```

curl -s -X POST http://127.0.0.1:8000/route -H 'Content-Type: application/json' -d '{"prompt":"2+2?"}' | jq

---

**Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.**  
Unauthorized copying or redistribution of this material is prohibited.  
GitHub: [Debashis2007](https://github.com/Debashis2007)

