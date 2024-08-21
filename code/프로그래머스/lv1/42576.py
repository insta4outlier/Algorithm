from collections import Counter


def solution(participant, completion):
    counter = Counter(participant)
    for c in completion:
        counter[c] -= 1
    return counter.most_common(1)[0][0]
