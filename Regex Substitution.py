import re
[print(re.sub('(?<=\s)\&\&\s', 'and ', re.sub('\s\|\|\s', ' or ', input()))) for _ in range(int(input()))]