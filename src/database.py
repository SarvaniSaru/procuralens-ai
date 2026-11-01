"""Database location and initialization bridge for the Streamlit app."""
from pathlib import Path
DB_PATH = Path(__file__).resolve().parents[1] / "data" / "procuralens.db"
