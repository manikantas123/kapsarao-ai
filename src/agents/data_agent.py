import pandas as pd
from pathlib import Path
from src.utils.schema import validate_schema
from src.utils.logging import log_agent_event


class DataAgent:

    def __init__(self, cfg):
        self.cfg = cfg
        self.path = Path(cfg["data_path"])
        self.segments = cfg.get("segments", [])

    def summarize(self, filters):
        try:
            # ---- LOAD ----
            df = pd.read_csv(self.path)
            log_agent_event("data_agent", "Loaded CSV", {"rows": len(df)})

            # ---- VALIDATE SCHEMA ----
            required = [
                "campaign_name", "adset_name", "date",
                "spend", "impressions", "clicks", "ctr",
                "purchases", "revenue", "roas",
                "creative_type", "creative_message",
                "audience_type", "platform", "country"
            ]
            validate_schema(df, required)

            # ---- CLEAN TYPES ----
            df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")
            df["spend"] = pd.to_numeric(df["spend"], errors="coerce").fillna(0)
            df["impressions"] = pd.to_numeric(df["impressions"], errors="coerce").fillna(0).astype(int)
            df["clicks"] = pd.to_numeric(df["clicks"], errors="coerce").fillna(0).astype(int)
            df["purchases"] = pd.to_numeric(df["purchases"], errors="coerce").fillna(0).astype(int)
            df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce").fillna(0)

            df["ctr"] = df["clicks"] / df["impressions"].replace(0, 1)
            df["roas"] = df["revenue"] / df["spend"].replace(0, 1)

            df = df.sort_values("date")

            # ---- DAILY AGG ----
            daily = df.groupby("date").agg({
                "spend": "sum",
                "impressions": "sum",
                "clicks": "sum",
                "ctr": "mean",
                "purchases": "sum",
                "revenue": "sum",
                "roas": "mean"
            }).reset_index()

            # ---- BASELINE / RECENT ----
            if len(daily) > 14:
                baseline = daily.iloc[:-14].copy()
                recent = daily.iloc[-14:].copy()
            else:
                baseline = daily.copy()
                recent = daily.copy()

            # ---- SEGMENT ANALYSIS ----
            segment_summary = {}

            for seg in self.segments:
                if seg not in df.columns:
                    continue

                seg_df = df.groupby(seg).agg({
                    "spend": "mean",
                    "impressions": "mean",
                    "clicks": "mean",
                    "ctr": "mean",
                    "purchases": "mean",
                    "revenue": "mean",
                    "roas": "mean"
                }).reset_index()

                segment_summary[seg] = seg_df.to_dict(orient="records")

            # ---- RETURN ----
            return {
                "data": df,
                "daily": daily,
                "baseline": baseline,
                "recent": recent,
                "segments": segment_summary
            }

        except Exception as e:
            log_agent_event("data_agent", "DataAgent Failure", {"error": str(e)})
            raise e
