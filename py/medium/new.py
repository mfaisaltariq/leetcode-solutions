# def solution(P, S):
#     empty_seats = []
#     total_cars = len(P)
    
#     for i, val in enumerate(P):
#         if S[i] - val > 0:
#             empty_seats.append(abs(S[i] - val))
#         else:
#             empty_seats.append(0)
#     carry = 0        
#     for i, val in enumerate(empty_seats):
#         if val + carry == 0:
#             continue
#         j = i +1
#         while j < (len(S)):
#             if val == S[j] - P[j] + carry:
#                 total_cars -= 1
#                 break
#             if val < S[j] - P[j] + carry:
#                 total_cars -= 1
#                 carry = S[j] - P[j] + carry
#                 break
#             j += 1
#     return total_cars

from audioop import reverse


def solution(P, S):
    people = sum(P)
    S.sort(reverse=True)

    idx = 0
    while (people > 0):
        people -= S[idx]
        idx += 1
    return idx

print(solution([4, 4, 2, 4], [5, 5, 2, 5]))