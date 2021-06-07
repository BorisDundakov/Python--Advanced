nums_list = [int(el) for el in input().split()]


def neg_vs_pos(numbers_list):
    negatives = []
    positives = []
    for el in range(len(numbers_list)):
        negatives = list(filter(lambda number: number < 0, numbers_list))
        positives = list(filter(lambda number: number > 0, numbers_list))
    print(sum(negatives))
    print(sum(positives))

    if abs(sum(negatives)) > sum(positives):
        print('The negatives are stronger than the positives')
    else:
        print('The positives are stronger than the negatives')


neg_vs_pos(nums_list)
