# Sciware
## Testing and packaging workshop guide


## Repo setup and packaging

### Fork and clone the repo

- Go to https://github.com/flatironinstitute/sciware-testing-python
- Log in to Github (if necessary)
- Click "Fork" in upper right
   - Choose your username (if prompted)
- `git clone https://github.com/YOURUSER/sciware-testing-python.git`
   - Other instructions under green "Code" button dropdown


### Setup your repo

- `cd sciware-testing-python`
- `pip3 install -e .`
   - Or `pip3 install --user -e .` without venv/conda
- `pytest`

You should see: `12 passed, 2 skipped, 2 xfailed, 1 xpassed`


### Code overview

- Code lives in `sciware_testing_python/*.py` (main module: `exercise.py`)
- Tests live in `tests/test_*.py`
- Let's look at `sciware_testing_python/exercise.py` now
   - `sum_numbers`: what does it do? how do you use it?



## Exercise: write tests

### Simple tests

- Open `tests/test_exercise.py`
- Write some tests for `sum_numbers`
   - Fill in `test_sum_numbers_yours` and `test_sum_numbers_empty`
   - Change `pass` to `assert sum_numbers(..) == ..`
- Run `pytest tests/test_exercise.py`

#### Bonus: commit and push your changes


## Exercise: doctests

- Open `sciware_testing_python/exercise.py`
- Add another doctest to the lines in quoted documentation:
   - ```text
     Example
     -------
     >>> sum_numbers([])
     0
     ```
   - Any `>>>` line in a docstring will be executed and compared to the expected output on the following line
- Run `pytest --doctest-modules sciware_testing_python/exercise.py`


## Exercise: test-driven fixes

- Look at `sciware_testing_python/exercise.py` `add_vectors`
   - It has a problem (but don't fix it yet)
- Add a new test for `add_vectors` to `tests/test_exercise.py`
- `pytest tests/test_exercise.py`: FAIL!
- Fix `add_vectors` and try again
   - Hint: change `*` to `+`


## Exercise: testing for error cases

- Update the `test_sum_strings` test in `tests/test_exercise.py` to call `sum_numbers` on a list of strings
- `pytest tests/test_exercise.py`: FAIL
- Tell pytest that this should actually fail:
   - Add (uncomment) `@pytest.mark.xfail(strict=True)` before the function
- Run tests again: now it should pass


### Exercise: test-driven development (TDD)

- Open `tests/test_tdd.py` and look at the tests
   - We wrote a test before writing the code for `count_twos`
- Remove the `@pytest.mark.skip` line for `test_count_twos`
- Run `pytest tests/test_tdd.py`: FAIL!
   - `count_twos` doesn't exist yet!
- Add a `count_twos` function to `sciware_testing_python/exercise.py`
- Run the tests again to pass


### Bonus: other pytest features

- See examples in `tests/test_examples.py`
- `@pytest.mark.parameterize`
   - can be used to loop over input arguments for your test
   - `@pytest.mark.parameterize("arg1, arg2, ...", [[val1, val2, ...], ...]`
- `@pytest.fixture`
   - Fixtures are called automatically to generate/load matching arguments



## CI: Github Actions

### Enable action on your fork

- Click on "Actions" tab
- Click "I understand ... enable"


### Exercise: improve CI tests

- Open `.github/workflows/exercise.yml`
- Add `3.9` to `python-version` to add testing for Python 3.9
- Add a `pytest --doctest-modules` to the Test step
- Commit and push (to your repo)


### Bonus: 

- Open `README.md`
- Fix the badge link to point to your repo


### Bonus: Code coverage

- Run `pytest --cov`
- Open `.github/workflows/exercise.yml`
- Update the Test step so it runs `pytest --doctest-modules --cov`


### Code Coverage (cont.)

- Setup your account at codecov.io
   - Link it to `sciware-testing-python`
   - Go to Settings -> Repository Upload Token and copy the token
- Uncomment the Codecov step and paste your token
- Commit and push (to your repo)



## Bonus: Typing

- Run `mypy`
- Add type some annotations to `sciware_testing_python/exercise.py` (see `examples.py`)
