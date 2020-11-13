FINAL_PERCENTAGE = 99


def find_bouncy_numbers() -> [int, int]:
    percentage = 0
    count = 0
    bouncy_numbers = 0
    while percentage < FINAL_PERCENTAGE:
        count += 1
        if not is_increasing_number(number=str(count)) and not \
                is_decreasing_number(number=str(count)):
            bouncy_numbers += 1
            percentage = (bouncy_numbers * 100) / count
    return count, percentage


def is_increasing_number(
    *,
    number: str
) -> bool:
    previous_number = 0
    for i in number:
        n = int(i)
        if n < previous_number:
            return False
        previous_number = n
    return True


def is_decreasing_number(
    *,
    number: str
) -> bool:
    previous_number = 9
    for i in number:
        n = int(i)
        if n > previous_number:
            return False
        previous_number = n
    return True


if __name__ == "__main__":
    number, percentage = find_bouncy_numbers()
    print('number', number)
    print('percentage', percentage)

