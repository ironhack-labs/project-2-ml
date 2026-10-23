from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from project_utils import load_polarization_data

def test_polarization_data_has_expected_schema_and_groups():
    df = load_polarization_data()
    assert len(df) > 0
    assert {'current_density', 'cell_voltage', 'source_file', 'test_family'}.issubset(df.columns)
    assert df['source_file'].nunique() > 1
    assert df['cell_voltage'].notna().all()
