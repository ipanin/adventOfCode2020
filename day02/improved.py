# AoC 2020. Day 2. Password Philosophy
import util


def test(data, validation_fun, expected):
    result = 0
    for line in lines:
        if validation_fun(line):
            result += 1
    util.assert_equal(result, expected)


# line = "8-12 z: zxzzzzfxzlmzz"
def valid1(line: str) -> bool:
    parsed = line.split(' ')
    range_ = parsed[0]
    letter = parsed[1][0]
    passw = parsed[2]

    range_min, range_max = range_.split("-")

    cnt = passw.count(letter)
    return cnt >= int(range_min) and cnt <= int(range_max)


def valid2(line: str) -> bool:
    parsed = line.split(' ')
    range_ = parsed[0]
    letter = parsed[1][0]
    passw = parsed[2]

    pos1, pos2 = range_.split("-")

    a = passw[int(pos1)-1]
    b = passw[int(pos2)-1]

    return (a == letter or b == letter) and (a != b)


lines = util.load_str_lines_list('input.txt')

print("Part 1.")
test(lines, valid1, 548)

print("Part 2.")
test(lines, valid2, 502)

# print("Part 2.")
