import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from Data.external_data import make_data

print(make_data().head())
