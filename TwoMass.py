
def main():
    first_mass = [1, 6, 8, 3, 19, 0]
    second_mass = [3, 0, 3, 1, 100, 8]
    third_mass = [3, 8, 5]
    dict_with_sum = {"first mass": sum(first_mass), "second mass": sum(second_mass), "third mass": sum(third_mass)}
    max_massive_sum = max(dict_with_sum.values())
    print dict_with_sum.keys()[dict_with_sum.values().index(max_massive_sum)] + " with value " + str(max_massive_sum)

main()
