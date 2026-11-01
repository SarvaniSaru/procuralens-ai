from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from src.scoring import add_peer_metrics
from src.ranking import rank_suppliers
criteria=[{"criterion_id":1,"name":"Technical Capability","max_score":10,"weight":30},{"criterion_id":2,"name":"Implementation Plan","max_score":10,"weight":20},{"criterion_id":3,"name":"Commercial Value","max_score":10,"weight":20},{"criterion_id":4,"name":"Security & Compliance","max_score":10,"weight":20},{"criterion_id":5,"name":"Support & Experience","max_score":10,"weight":10}]
base=[("Apex Systems","2026-09-28",9.1,[9,8,6.5,9.5,9]),("NexaWorks","2026-09-29",8.6,[8.5,9,8,8,9]),("Orbit Digital","2026-09-27",8.8,[8.5,8,6,8.5,8.5]),("Cobalt Ridge Solutions","2026-09-26",8.4,[7.5,7,7,10,8]),("LumenForge AI","2026-09-30",7.4,[9,8,8.5,7,6.5])]
suppliers=[]
for name,submitted,experience,scores in base:
    suppliers.append({"supplier_name":name,"submission_date":submitted,"experience_rating":experience,"confirmed_non_compliant":False,"criteria":[{**c,"score":score} for c,score in zip(criteria,scores)]})
ranked=rank_suppliers(add_peer_metrics(suppliers)); payload={"app":"ProcureLens AI","rfp_run_id":"sample-demo-run","criteria_snapshot":criteria,"ranking_policy":["ppi_desc","submission_date_asc","experience_desc","supplier_name_asc"],"suppliers":ranked,"excluded_suppliers":[{"supplier_name":"BrightPath Tech","reason":"Confirmed mandatory certification failure"}]}
out=ROOT/"sample_output"/"sample_run.json"; out.parent.mkdir(exist_ok=True); out.write_text(json.dumps(payload,indent=2),encoding="utf-8"); print(out)
