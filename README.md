# AoC

My inelegant but simplistic solutions for [Advent of Code](https://adventofcode.com).

No external dependencies, but does require Python 3.10 - I really wanted to try out `match`, so sue me!

Scripts/tests can be run after changing the working directory to the containing `day_##` folder.  You can also run:

* `python solutions.py` to run all `day_##/solution.py` (for all years)
* `python solutions.py YYYY YYYY YYYY` to run all `day_##/solution.py` for each `YYYY`
* `python tests.py` to run `pytest` in all `day_##` folders (for all years)
* `python tests.py YYYY YYYY YYYY` to run `pytest` in all `day_##` folders for each `YYYY`

Code is `isort`ed, `black`end, `mypy`ed, and `pytest`ed.  I may be over-type-hinting, but it's mostly for practice/experimentation.
