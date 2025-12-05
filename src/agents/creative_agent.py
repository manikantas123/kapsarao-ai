class CreativeAgent:

    def __init__(self, cfg):
        self.cfg = cfg

    def generate(self, summary, validated):
        outputs = []

        for ins in validated:
            m = ins["metric"]
            sev = ins["severity"]

            if m == "roas":
                angle = "Value & Performance Messaging"
                why = "ROAS drop suggests ads are not delivering proportional value."
                hooks = ["Better Value for Every Rupee.", "High Performance. Zero Compromise."]
            elif m == "ctr":
                angle = "Attention Grabbing Hooks"
                why = "CTR drop means users are not stopping to engage."
                hooks = ["Stop Scrolling!", "Your Comfort Revolution Starts Here."]
            else:
                angle = "General Creative Improvement"
                why = "Metric underperforming."
                hooks = ["Experience Better Everyday Performance.", "Designed For Your Lifestyle."]

            outputs.append({
                "campaign": "ALL_CAMPAIGNS",
                "metric": m,
                "severity": sev,
                "angle": angle,
                "why_this_angle": why,
                "hooks": hooks,
                "ctas": ["Shop Now", "Discover Your Comfort Upgrade", "Try It Today"]
            })

        return outputs
