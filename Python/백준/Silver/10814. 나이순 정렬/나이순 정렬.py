N = int(input())
person_list = []
people = 0
for _ in range(N):
    age, name = input().split()
    person_dict = dict()
    person_dict['age'] = int(age)
    person_dict['name'] = name
    person_dict['people'] = int(people)
    person_list.append(person_dict)
    people += 1

result = sorted(person_list, key=lambda x:x['age'])
for idx in range(N):
    print(f'{result[idx]["age"]} {result[idx]["name"]}')

