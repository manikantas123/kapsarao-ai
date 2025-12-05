class EvaluatorAgent:
    def __init__(self, cfg):
        self.cfg = cfg

    def validate(self, insights, summary):
        validated = []

        for ins in insights:
            if not isinstance(ins, dict):
                continue  # prevents crashes

            delta = abs(ins.get("delta", 0))

            severity = (
                "high" if delta > 0.25 else
                "medium" if delta > 0.10 else
                "low"
            )

            strength = round(delta * 4, 3)

            ins["severity"] = severity
            ins["strength"] = strength
            ins["confidence"] = min(0.99, ins.get("confidence", 0.85))

            validated.append(ins)

        return validated
