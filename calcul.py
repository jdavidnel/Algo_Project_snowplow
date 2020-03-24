def compute(this_list):
    distance = 0
    actual_time = 0
    total_time = 0
    tmp_house = 0
    for house in this_list:
        distance = abs(house - tmp_house)
        actual_time += distance
        total_time += actual_time
        tmp_house = house
    return total_time / len(this_list)