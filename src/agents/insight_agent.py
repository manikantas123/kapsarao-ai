class InsightAgent:

    def __init__(self, cfg):
        self.cfg = cfg

    def propose(self, summary, plan):
        base = summary["baseline"]
        recent = summary["recent"]

        insights = []
        metrics = ["roas", "ctr", "spend", "revenue", "clicks"]

        for m in metrics:
            b = base[m].mean()
            r = recent[m].mean()

            delta = 0 if b == 0 else (r - b) / b
            pct = delta * 100

            insights.append({
                "metric": m,
                "hypothesis": f"{m.upper()} is {'declining' if delta < 0 else 'improving'} over time.",
                "delta": float(delta),
                "evidence": {
                    "baseline_avg": float(b),
                    "current_avg": float(r),
                    "relative_change_pct": float(pct)
                }
            })

        # ---- SEGMENT INSIGHTS ----
        segments = summary.get("segments", {})
        seg_insights = []

        for seg_name, rows in segments.items():
            for row in rows:
                seg_insights.append({
                    "type": "segment_driver",
                    "segment": seg_name,
                    "value": row[seg_name],
                    "roas": row["roas"],
                    "ctr": row["ctr"]
                })

        return {"global": insights, "segments": seg_insights}
