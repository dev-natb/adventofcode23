def parse(puzzle_input):
    return puzzle_input.rstrip().split("\n")


def part1(data):
    """
    Function to iterate over list (of strings) and read 1st/last DIGIT in each string
    return digits for each string on a single [new] line
    calculate value on each line and return total sum value
    """
    values = []

    for item in data:
        digits = []

        for character in item:
            if character.isdigit():
                digits.append(character)

        first = digits[0]
        last = digits[-1]

        values.append(int(first + last))

    return sum(values)


# def part2(data):
#     return data


def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    # solution2 = part2(data)

    print(f"Solution 1: {solution1}")
    # print(f"Solution 2: {solution2}")


if __name__ == "__main__":
    with open("input.txt") as fd:
        puzzle_input = fd.read()

    solve(puzzle_input)
