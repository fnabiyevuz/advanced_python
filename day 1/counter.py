from collections import Counter

results = Counter("Andijon viloyati")

print(results.keys())
print(results.values())
print(results.items())
print(results.most_common(1))
print(results.most_common(3))
print(results["A"])

