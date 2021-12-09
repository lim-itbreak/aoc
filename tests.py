import os
import sys

aoc: str = os.path.dirname(__file__)

year: str
for year in sorted(os.listdir(aoc)):
    if year.startswith("20"):
        if len(sys.argv) == 1 or year in sys.argv:
            day: str
            for day in sorted(os.listdir(os.path.join(aoc, year))):
                if day.startswith("day"):
                    print(f"=== {year} Day {int(day.split('_')[1])} ===")
                    os.chdir(os.path.join(aoc, year, day))
                    os.system("mypy solution.py")
                    os.system("pytest")
