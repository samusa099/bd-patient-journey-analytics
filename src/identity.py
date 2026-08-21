from difflib import SequenceMatcher
def normalize_name(s): return ' '.join(s.lower().replace('.','').split())
def identity_score(a,b): return round(SequenceMatcher(None,normalize_name(a),normalize_name(b)).ratio(),4)
