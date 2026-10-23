
from pathlib import Path
import pandas as pd
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"

def load_polarization_data():
    """Load polarization CSVs only; EIS files have a different schema."""
    frames = []
    for path in sorted(RAW_DIR.rglob("*.csv")):
        try:
            df = pd.read_csv(path)
        except Exception:
            continue
        required = {"current_density", "cell_voltage", "power_density"}
        if not required.issubset(df.columns):
            continue
        family = path.parent.name
        # Power density is intentionally excluded from predictors because it is
        # computed from current density × cell voltage and would leak the target.
        out = pd.DataFrame({
            "current_density": pd.to_numeric(df["current_density"], errors="coerce"),
            "pressure": pd.to_numeric(df["pressure"], errors="coerce") if "pressure" in df else np.nan,
            "relative_humidity": pd.to_numeric(df["relative_humidity"], errors="coerce") if "relative_humidity" in df else np.nan,
            "test_family": family,
            "source_file": str(path.relative_to(RAW_DIR)),
            "cell_voltage": pd.to_numeric(df["cell_voltage"], errors="coerce"),
        })
        # Some test series encode operating stage as 'set'; retain it if available.
        if "set" in df.columns:
            out["operating_set"] = df["set"].astype(str)
        else:
            out["operating_set"] = "not_recorded"
        frames.append(out)
    if not frames:
        raise FileNotFoundError(f"No polarization CSVs found under {RAW_DIR}")
    data = pd.concat(frames, ignore_index=True)
    data = data.replace([np.inf, -np.inf], np.nan)
    data = data.dropna(subset=["current_density", "cell_voltage"])
    # Physical plausibility checks: remove only non-finite values; avoid arbitrary
    # voltage/current cutoffs that could silently discard valid measurements.
    return data.reset_index(drop=True)
