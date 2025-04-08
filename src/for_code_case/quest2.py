def quest2(music_list):
    ordered_list = sorted(music_list, reverse=True)
    randomized_list = []
    for i in range(len(ordered_list)):
        randomized_list.append(ordered_list[i])

        if len(randomized_list) == len(ordered_list):
            break
        else:
            randomized_list.append(ordered_list[len(ordered_list)-1-i])
            if len(randomized_list) == len(ordered_list):
                break

        print(randomized_list)
        return randomized_list

quest2([2, 10, 5, 3])