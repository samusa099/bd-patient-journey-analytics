def predict_wait(recent,arrivals,staff,peak=False): return round(max(1,.6*recent+.5*(arrivals/max(1,staff))+(4 if peak else 0)),2)
