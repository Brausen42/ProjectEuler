known_combos = []
known_totals = {}

def FindTotalSums(used,target):
    if sum(used) > target or str(sorted(used)) in known_combos:
        return 0
    known_combos.append(str(sorted(used)))
    if sum(used) in known_totals:
        return known_totals[sum(used)]
    elif sum(used) == target:
        return 1
    total = 0
    for n in [50,100,200]:
        temp = list(used)
        temp.append(n)
        total += FindTotalSums(temp,target)
    known_totals[sum(used)] = total
    return total

print(FindTotalSums([],200,))
