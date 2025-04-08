import sys

N, M = map(int, sys.stdin.readline().split())

sentence_set = set()
sentence_dict = dict()

for _ in range(N):
    sentence = sys.stdin.readline().rstrip()
    if len(sentence) < M:
        continue
    if sentence in sentence_set:
        now_num = sentence_dict.get(sentence)
        sentence_dict.update({sentence:now_num+1})
    else:
        sentence_dict[sentence] = 1
        sentence_set.add(sentence)

result = sorted(sentence_dict, key=lambda x: (-sentence_dict.get(x), -len(x), x))
for item in result:
    sys.stdout.write(item+'\n')
