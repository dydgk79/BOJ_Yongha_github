def solution(genres, plays):
    answer = []
    genre_dict = dict()
    genre_total = dict()

    for idx in range(len(genres)):
        genre_total[genres[idx]] = genre_total.get(genres[idx], 0) + plays[idx]

        if genres[idx] not in genre_dict.keys():
            genre_dict[genres[idx]] = [(plays[idx], idx)]
        else:
            genre_album = genre_dict[genres[idx]]

            if len(genre_album) == 1:
                genre_album.append((plays[idx], idx))
                genre_album.sort(key=lambda x: (-x[0], x[1]))
            else:
                new_song = (plays[idx], idx)
                genre_album.append(new_song)
                genre_album.sort(key=lambda x: (-x[0], x[1]))
                genre_dict[genres[idx]] = genre_album[:2]

    best = list(genre_dict.items())

    best.sort(key=lambda x: genre_total[x[0]], reverse=True)

    for genre, items in best:
        for item in items:
            answer.append(item[1])

    return answer