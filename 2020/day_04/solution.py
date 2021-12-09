from typing import Dict, List, TextIO

Input = List[Dict[str, str]]


def fields(passport: str):
    return dict(token.split(":") for token in passport.split())


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        return [fields(passport) for passport in fp.read().split("\n\n")]


def is_complete(passport: Dict[str, str]) -> bool:
    return set(passport).issuperset(
        set(
            (
                "byr",
                "iyr",
                "eyr",
                "hgt",
                "hcl",
                "ecl",
                "pid",
            )
        )
    )


def is_valid(passport: Dict[str, str]) -> bool:
    if is_complete(passport):
        byr: str = passport["byr"]
        if not (len(byr) == 4 and 1920 <= int(byr) <= 2002):
            return False

        iyr: str = passport["iyr"]
        if not (len(iyr) == 4 and 2010 <= int(iyr) <= 2020):
            return False

        eyr: str = passport["eyr"]
        if not (len(eyr) == 4 and 2020 <= int(eyr) <= 2030):
            return False

        hgt: str = passport["hgt"]
        if hgt.endswith("cm"):
            if not 150 <= int(hgt.rstrip("cm")) <= 193:
                return False
        elif hgt.endswith("in"):
            if not 59 <= int(hgt.rstrip("in")) <= 76:
                return False
        else:
            return False

        hcl: str = passport["hcl"]
        if not (
            len(hcl) == 7
            and hcl[0] == "#"
            and set(hcl[1:]).issubset("0123456789abcdef")
        ):
            return False

        ecl: str = passport["ecl"]
        if ecl not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
            return False

        pid: str = passport["pid"]
        if not (len(pid) == 9 and set(pid).issubset("0123456789")):
            return False

        return True

    return False


def part1(inputs: Input) -> int:
    return len([passport for passport in inputs if is_complete(passport)])


def part2(inputs: Input) -> int:
    return len([passport for passport in inputs if is_valid(passport)])


if __name__ == "__main__":
    inputs: Input = load_input(filename="puzzle")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
