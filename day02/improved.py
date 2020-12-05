# AoC 2020. Day 2. Password Philosophy
import util
import re


def better():
    lines = [re.split('[: -]', l.strip()) for l in open(r'C:\git\github\adventOfCode2020\day02\input.txt')]
    lines1 = [(int(p1), int(p2), pwd.count(ch)) for p1, p2, ch, _, pwd in lines]
    lines2 = [(pwd[int(p1)-1] == ch, pwd[int(p2)-1] == ch) for p1, p2, ch, _, pwd in lines]
    part1 = sum(n1 <= matches <= n2 for n1, n2, matches in lines1)
    part2 = sum(p1 ^ p2 for p1, p2 in lines2)
    print(part1, part2)


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

better()
# print("Part 2.")
