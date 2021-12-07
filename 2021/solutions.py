import os

year: str = os.path.dirname(__file__)

day: str
for day in sorted(os.listdir(year)):
    if day.startswith("day"):
        print(f"=== Day {int(day.split('_')[1])} ===")
        os.chdir(os.path.join(year, day))
        os.system("python solution.py")
