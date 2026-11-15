def solution(user_id, banned_id):
    def check_possible(u, b):
        if len(u) != len(b):
            return False

        for i in range(len(u)):
            if b[i] == '*':
                continue
            if u[i] != b[i]:
                return False

        return True

    possible = [[] for _ in range(len(banned_id))]

    for now_user_id in user_id:
        for idx in range(len(banned_id)):
            if check_possible(now_user_id, banned_id[idx]):
                possible[idx].append(now_user_id)

    visited = set()
    result = set()

    def recur(n):
        if n == len(banned_id):
            result.add(frozenset(visited))
            return

        for available_people in possible[n]:
            if available_people in visited:
                continue

            visited.add(available_people)
            recur(n + 1)
            visited.remove(available_people)

    recur(0)

    return len(result)