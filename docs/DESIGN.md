# Design: Cost-Aware Auto-Routing

**Project:** `cost-aware-auto-routing`  
**Parent system design:** [09 — Multi-Model Routing / API Platform](https://github.com/Debashis2007/cost-aware-auto-routing/blob/main/09-multi-model-routing-api-platform.md)

## 1. What this POC demonstrates

Route short/easy prompts to small model unless user pinned; always return chosen model.

## 2. Architecture (POC)

```text
pin? → else heuristic(small|frontier) → respond with chosen_model
```

## 3. Patterns used (and why)

| Pattern | Why used | Where in code |
|---------|----------|---------------|
| Pin overrides auto | Deterministic enterprise/dev needs. | `pin` field. |
| Cheap-default routing | Cost control at platform layer. | Length heuristic. |
| Transparency | Hidden routing erodes trust. | `chosen_model` + `transparent`. |

## 4. Key endpoints

`GET /health`, `POST /route`

## 5. Tradeoffs / POC limits

Replace length heuristic with a real complexity classifier later.

## 6. How to run

See the **Run (self-contained POC)** section in [`../README.md`](../README.md).

This folder is self-contained and can be published as its own GitHub repository.

## 7. Design walkthrough video

> **Watch on YouTube:** [Cost Aware Auto Routing — System Design #Shorts](https://youtu.be/9FjuGcUSwFQ)
>
> Direct link: **https://youtu.be/9FjuGcUSwFQ**

Also available in-repo:
- GIF preview: [`video/design-overview.gif`](./video/design-overview.gif)
- MP4 download: [`video/design-overview.mp4`](./video/design-overview.mp4)
- Narration script: [`video/narration.txt`](./video/narration.txt)

---

**Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.**  
Unauthorized copying or redistribution of this material is prohibited.  
GitHub: [Debashis2007](https://github.com/Debashis2007)

