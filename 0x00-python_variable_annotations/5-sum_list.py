""" The `5-sum_list` module supplies a funcion `sum_list` """


def sum_list(input_list: list[float]) -> float:
    """
    sum_list: Function that returns sum of floats in the list

    Args:
    input_list: List of floats

    Return:
    sum: float
    """
    sum = 0
    for num in input_list:
        sum += num
    return (sum)
