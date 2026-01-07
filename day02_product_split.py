reviews = [
    {"product": "A", "score": 4},
    {"product": "B", "score": None},
    {"product": "a", "score": 5},
    {"product": "C", "score": 3},
    {"product": "b", "score": -2},
    {"product": "A", "score": 2},
    {"product": "c", "score": 4},
    {"product": "D", "score": 10}
]

totals = {}
counts = {}

for t in reviews:
    product = t["product"].upper()   # standardize
    score = t["score"]

    if score is None:
        score = 0

    if score < 0:
        continue

    if product not in ["A","B","C"]:
        continue

    totals[product] = totals.get(product, 0) + score
    counts[product] = counts.get(product, 0) + 1

avg = {}
for p in totals:
    avg[p] = round(totals[p] / counts[p], 2)

print("Average scores:", avg)
