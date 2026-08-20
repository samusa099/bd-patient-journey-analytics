from pathlib import Path
import json,zipfile,sys
R=Path(__file__).resolve().parents[1]
req=["README.md","ROADMAP.md","MANIFEST.json","data/processed/journey_summary.csv","excel/Hospital_Patient_Journey_Analytics_v0.1.xlsx"]
e=[p for p in req if not (R/p).exists()]
for p in R.rglob("*.xlsx"):
 e += [] if zipfile.is_zipfile(p) else [str(p)]
print("PASS: v0.1.0 validated" if not e else "FAIL: "+str(e));sys.exit(bool(e))
