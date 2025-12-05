class CreativeAgent:
    def __init__(self, cfg):
        self.cfg = cfg

    def generate(self, summary, validated_insights):
        creatives = []

        for ins in validated_insights:

            # Safety check
            if not isinstance(ins, dict):
                continue

            metric = ins.get("metric")
            severity = ins.get("severity", "low")

            # ---- ROAS Creative ----
            if metric == "roas":
                creatives.append({
                    "campaign": "ALL_CAMPAIGNS",
                    "metric": "roas",
                    "severity": severity,
                    "angle": "Value & Performance Messaging",
                    "why_this_angle": "ROAS drop indicates ads are not delivering proportional value.",
                    "hooks": [
                        "More Comfort. Less Cost.",
                        "Engineered for Everyday Value.",
                        "High Performance. Zero Compromise."
                    ],
                    "ctas": ["Shop Now", "Discover Your Comfort Upgrade"]
                })

            # ---- CTR Creative ----
            elif metric == "ctr":
                creatives.append({
                    "campaign": "ALL_CAMPAIGNS",
                    "metric": "ctr",
                    "severity": severity,
                    "angle": "Attention Boosting Hooks",
                    "why_this_angle": "CTR drop indicates users are not stopping to engage.",
                    "hooks": [
                        "Stop Scrolling!",
                        "Your Comfort Revolution Starts Here."
                    ],
                    "ctas": ["Shop Now", "Learn More"]
                })

            # ---- Spend / Revenue / Clicks ----
            else:
                creatives.append({
                    "campaign": "ALL_CAMPAIGNS",
                    "metric": metric,
                    "severity": severity,
                    "angle": "General Creative Improvement",
                    "why_this_angle": f"{metric.upper()} underperformance suggests messaging or visual refresh needed.",
                    "hooks": [
                        "Experience Better Everyday Performance.",
                        "Designed For Your Lifestyle."
                    ],
                    "ctas": ["Shop Now", "Try It Today"]
                })

        return creatives
