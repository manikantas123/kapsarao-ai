from src.utils.logging import log_agent_event

class PlannerAgent:
    """
    Converts the user's goal into a structured agent execution plan.
    The plan is explicit, machine-readable, and defines:
      - steps
      - dependencies
      - agent responsibilities
      - expected outputs
    """

    def __init__(self, cfg):
        self.cfg = cfg

    def decompose(self, query: str):
        """
        Returns a list of step dictionaries.
        Example:
        [
            {"step": 1, "agent": "data", "task": "...", ...}
        ]
        """
        log_agent_event("planner", f"Decomposing query: {query}")

        plan = []

        # -------------------------------------
        # Step 1 – Load + validate data
        # -------------------------------------
        plan.append({
            "step": 1,
            "agent": "data_agent",
            "task": "Load CSV, validate schema, preprocess fields, compute grouped & daily stats",
            "requires": None,
            "produces": "data_summary",
            "on_error": "abort"
        })

        # -------------------------------------
        # Step 2 – Generate hypotheses
        # -------------------------------------
        plan.append({
            "step": 2,
            "agent": "insight_agent",
            "task": "Analyze summary; detect ROAS shifts, CTR changes, underperforming segments",
            "requires": "data_summary",
            "produces": "raw_insights",
            "on_error": "continue_with_empty"
        })

        # -------------------------------------
        # Step 3 – Validate hypotheses
        # -------------------------------------
        plan.append({
            "step": 3,
            "agent": "evaluator_agent",
            "task": "Compare baseline vs recent metrics; compute deltas; add severity/confidence",
            "requires": "raw_insights + data_summary",
            "produces": "evaluated_insights",
            "on_error": "continue_with_raw_insights"
        })

        # -------------------------------------
        # Step 4 – Generate creatives tied to insights
        # -------------------------------------
        plan.append({
            "step": 4,
            "agent": "creative_agent",
            "task": "Generate creatives grounded in insights; include angles, hooks, messages, CTA",
            "requires": "evaluated_insights + data_summary",
            "produces": "creative_recommendations",
            "on_error": "use_safe_defaults"
        })

        # -------------------------------------
        # Step 5 – Final reporting
        # -------------------------------------
        plan.append({
            "step": 5,
            "agent": "reporter",
            "task": "Write MD report summarizing insights, deltas, reasoning, and creatives",
            "requires": "evaluated_insights + creative_recommendations",
            "produces": "report.md",
            "on_error": "write_partial_report"
        })

        log_agent_event("planner", "Generated execution plan")
        return plan
