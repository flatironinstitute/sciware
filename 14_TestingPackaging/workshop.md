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

You should see: 9 passed, 2 skipped, 2 xfailed, 1 xpassed


### Code overview

- Code lives in `sciware_testing_python/*.py` (main module: `main.py`)
- Tests live in `test/test_*.py`
- Let's look at `sciware_testing_python/main.py` now
   - `sum_numbers`: what does it do? how do you use it?


## Exercise: write tests

### Simple tests

- Open `tests/test_exercise.py`
- Write some tests for `sum_numbers`
   - fill in `test_sum1` and `test_sum2`
- Run `pytest tests/test_exercise.py`

#### Bonus: commit and push your changes


## Exercise: doctests

- Open `sciware_testing_python/main.py`
- Add some lines in the quoted documentation:
   - ```
     >>> code
     result
     ```
- Run `pytest --doctest-modules`


## Exercise: test-driven fixes

- Look at `sciware_testing_python/main.py` `add_vectors`
   - It has a problem (but don't fix it yet)
- Add a new test for `add_vectors` to `tests/test_exercise.py`
- `pytest tests/test_exercise.py`: FAIL!
- Fix `add_vectors` and try again


## Exercise: testing for error cases

- Add a test to `tests/test_exercise.py` to call `sum_numbers` on a list of strings
- `pytest tests/test_exercise.py`: PASS?!
- Tell pytest that this should actually fail:
   - Add `@pytest.mark.xfail(strict=True)` before the function
   - Run tests again: now it should fail
- Fix `sum_numbers` in `sciware_testing_python/main.py` to check for non-numbers
- Run tests again to pass


### Bonus: test-driven development (TDD)

- Open `tests/test_tdd.py` and look at the test
- Remove the `@pytest.mark.skip` line
- Run `pytest tests/test_tdd.py`: FAIL!
- Add a `count_ones` function to `sciware_testing_python/main.py`
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
- Add a `pytest --doctest-modules` test step
- Add python 3.9
- Commit and push (to your repo)


### Bonus: 

- Open `README.md`
- Fix the badge link to point to your repo



## Bonus: Code coverage
