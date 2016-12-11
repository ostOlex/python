
def main():
    first_mass = [1, 6, 8, 3, 19, 1000, 0]
    second_mass = [3, 0, 3, 1, 100, 8]
    third_mass = [3, 8, 5]
    get_max(first_mass, second_mass, third_mass)


def get_max(*all_mass):
    dict_with_sum = {}
    for mass in all_mass:
        dict_with_sum[sum(mass)] = mass
    max_massive_sum = max(dict_with_sum.keys())
    print "Max mss is "+str(dict_with_sum.get(max_massive_sum))
main()
