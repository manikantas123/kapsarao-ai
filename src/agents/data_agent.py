import pandas as pd
from pathlib import Path
from src.utils.schema import validate_schema, SchemaError
from src.utils.logging import log_agent_event


class DataAgent:
    def __init__(self, cfg):
        self.cfg = cfg
        self.path = Path(cfg["data_path"])

    def summarize(self, filters):
        try:
            # -------- LOAD DATA --------
            df = pd.read_csv(self.path)
            log_agent_event("data_agent", "Loaded CSV", {"rows": len(df)})

            # -------- SCHEMA VALIDATION --------
            required_cols = [
                "campaign_name", "adset_name", "date", "spend",
                "impressions", "clicks", "ctr", "purchases", "revenue", "roas",
                "creative_type", "creative_message", "audience_type",
                "platform", "country"
            ]
            validate_schema(df, required_cols)

            # -------- TYPE CLEANING --------
            df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")
            df["spend"] = pd.to_numeric(df["spend"], errors="coerce").fillna(0)
            df["impressions"] = pd.to_numeric(df["impressions"], errors="coerce").fillna(0).astype(int)
            df["clicks"] = pd.to_numeric(df["clicks"], errors="coerce").fillna(0).astype(int)
            df["purchases"] = pd.to_numeric(df["purchases"], errors="coerce").fillna(0).astype(int)
            df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce").fillna(0)

            # recompute ratios safely
            df["ctr"] = df["clicks"] / df["impressions"].replace(0, 1)
            df["roas"] = df["revenue"] / df["spend"].replace(0, 1)

            df = df.sort_values("date")
            log_agent_event("data_agent", "Cleaned data", {"rows": len(df)})

            # -------- DAILY AGGREGATION --------
            daily = df.groupby("date").agg({
                "spend": "sum",
                "impressions": "sum",
                "clicks": "sum",
                "ctr": "mean",
                "purchases": "sum",
                "revenue": "sum",
                "roas": "mean"
            }).reset_index()

            # -------- BASELINE / RECENT SPLIT --------
            if len(daily) > 14:
                baseline = daily.iloc[:-14].copy()
                recent = daily.iloc[-14:].copy()
            else:
                baseline = daily.copy()
                recent = daily.copy()

            log_agent_event("data_agent", "Split baseline/recent", {
                "baseline_rows": len(baseline),
                "recent_rows": len(recent)
            })

            # ---- FINAL STRUCTURE ----
            return {
                "data": df,
                "daily": daily,
                "baseline": baseline,
                "recent": recent
            }

        except SchemaError as e:
            log_agent_event("data_agent", f"Schema Error: {str(e)}")
            raise

        except Exception as e:
            log_agent_event("data_agent", f"Unexpected Error: {str(e)}")
            raise
