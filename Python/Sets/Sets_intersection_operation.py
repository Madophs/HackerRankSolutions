m = int(input())
english = set(list(map(int, input().split())))
n = int(input())
french = set(list(map(int, input().split())))
print(len(english.intersection(french)))
