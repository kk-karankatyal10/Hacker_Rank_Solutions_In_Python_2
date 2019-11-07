import bisect
# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    res = []
    s = sorted(list(set(scores)))
    l = len(s)
    for v in alice:
         res.append(l - bisect.bisect_right(s, v) +1)
             
    return res
