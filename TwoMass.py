
def main():
    first_mass = [1, 6, 8, 3, 19, 1000, 0]
    second_mass = [3, 0, 3, 1, 100, 8]
    third_mass = [3, 8, 5]
    get_max(first_mass, second_mass, third_mass)


def get_max(*all_mass):
    dict_with_sum = {}
    numb = 1
    for mass in all_mass:
        mass_number = "{0} mass".format(str(numb))
        dict_with_sum[mass_number] = sum(mass)
        numb += 1
    max_massive_sum = max(dict_with_sum.values())
    print dict_with_sum.keys()[dict_with_sum.values().index(max_massive_sum)] + " with value " + str(
        max_massive_sum)
main()
