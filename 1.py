"""
Write a function solution that, given an integer N, returns a string
consisting of N lowercase letters (a-z) such that each letter occurs an
odd number of times. We only care about occurrences of letters that
appear at least once in the result.
Examples:
1. Given N = 4, the function may return "code" (each of the letters "c", "o",
"d" and "e" occurs once). Other correct answers are: "cats", "uutu" or
"xxxy".
2. Given N = 7, the function may return "gwgtgww" ("g" and "w" occur three
times each and "t" occurs once).
3. Given N = 1, the function may return "z".
Write an efficient algorithm for the following assumptions:
• N is an integer within the range [1…200,000].
Copyright 2009-2021 by Codility Limited. All Rights Reserved. Unauthorized copying,
publication or disclosure prohibited.
"""

#================================

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    if N % 2 == 0:
        return f"{'a'*(N-1)}{'b'}"
    return f"{'a'*N}"
