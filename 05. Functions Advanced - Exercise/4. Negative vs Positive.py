nums_list = [int(el) for el in input().split()]


def neg_vs_pos(numbers_list):
    negatives_list = []
    posiives_list = []

    for el in range(len(numbers_list)):
        if numbers_list[el] > 0:
            posiives_list.append(numbers_list[el])
        else:
            negatives_list.append(numbers_list[el])

    print(sum(negatives_list))
    print(sum(posiives_list))

    if abs(sum(negatives_list)) > sum(posiives_list):
        print('The negatives are stronger than the positives')
    else:
        print('The positives are stronger than the negatives')


neg_vs_pos(nums_list)
