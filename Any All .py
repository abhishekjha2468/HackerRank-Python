n,list=int(input()), input().split()
print(all([all([*map(lambda x: int(x)>0, list)]),any([*map(lambda y:y==y[::-1], list)])]))