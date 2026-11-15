def solution(k, room_number):
    answer = []
    parent = {}

    def find(room):
        path = []

        while room in parent:
            path.append(room)
            room = parent[room]

        for p in path:
            parent[p] = room

        return room

    for want_room in room_number:
        empty_room = find(want_room)
        answer.append(empty_room)
        parent[empty_room] = empty_room + 1

    return answer