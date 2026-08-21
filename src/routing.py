def route_score(wait_min,distance_m,service_time_min,capacity_penalty=0): return wait_min+distance_m/75+service_time_min+capacity_penalty
