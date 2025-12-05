from src.utils.logging import log_agent_event

class InsightAgent:

    def __init__(self, cfg):
        self.cfg = cfg

    def propose(self, summary, plan):
        # Validate summary structure
        if not isinstance(summary, dict):
            raise ValueError("InsightAgent expected a dictionary summary")

        if "baseline" not in summary or "recent" not in summary:
            raise KeyError("InsightAgent expected keys 'baseline' and 'recent'")

        baseline = summary["baseline"]
        recent = summary["recent"]
        daily = summary.get("daily")

        if baseline is None or recent is None:
            raise ValueError("Baseline or recent data missing")

        if not hasattr(baseline, "mean") or not hasattr(recent, "mean"):
            raise ValueError("Baseline/recent must be DataFrames")

        insights = []
        metrics = ["roas", "ctr", "spend", "revenue", "clicks"]

        for m in metrics:
            if m not in baseline.columns or m not in recent.columns:
                continue

            b = baseline[m].mean()
            r = recent[m].mean()

            delta = 0 if b == 0 else (r - b) / b

            insight = {
                "metric": m,
                "hypothesis": f"{m.upper()} is {'declining' if delta < 0 else 'improving'} over time.",
                "delta": float(delta),
                "severity": (
                    "high" if abs(delta) > 0.25
                    else "medium" if abs(delta) > 0.1
                    else "low"
                ),
                "confidence": 0.85,
                "evidence": {
                    "baseline_avg": float(b),
                    "current_avg": float(r),
                    "relative_change_pct": float(delta * 100),
                }
            }

            insights.append(insight)

        log_agent_event("insight_agent", "Generated insights", {"count": len(insights)})
        return insights
