def encounter_total(rows): return sum(float(r['patient_payable_bdt']) for r in rows)
def payment_touchpoints(service_count,centralized=True): return 1 if centralized else max(1,service_count)
