import os

year: str = os.path.dirname(__file__)

day: str
for day in sorted(os.listdir(year)):
    if day.startswith("day"):
        os.chdir(os.path.join(year, day))
        os.system("pytest")
