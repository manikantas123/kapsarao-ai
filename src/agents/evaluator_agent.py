class EvaluatorAgent:

    def __init__(self, cfg):
        self.cfg = cfg

    def validate(self, insights, summary):
        validated = []
        for i in insights:
            strength = abs(i["delta"]) * 4
            i["strength"] = round(strength, 3)
            validated.append(i)
        return validated
