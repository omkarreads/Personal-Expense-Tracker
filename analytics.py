import numpy as np
import itertools

def calc_stats(items):
    if not items:
        return {}
    
    amounts = np.array([x.cost for x in items])
    return {
        "total": float(np.sum(amounts)),
        "avg": float(np.mean(amounts)),
        "max": float(np.max(amounts)),
        "min": float(np.min(amounts)),
        "count": len(amounts)
    }
  
def cat_breakdown(items):
    res = {}
    for x in items:
        k = x.cat.title()
        res[k] = res.get(k, 0.0) + x.cost
    return res

def get_running_total(items):
    costs = [x.cost for x in items]
    return list(itertools.accumulate(costs))

def get_unique_cats(items):
    return set(x.cat.title() for x in items)
