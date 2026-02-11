# Unit Testing of Timer for Python
## Prerequisites
The test framework is `pytest`, which can be installed from [here](https://docs.pytest.org/en/stable/getting-started.html).

## Run Tests
From the project base directory, use this command to run all tests:

```shell
pytest
```

## Run Tests in Parallel
Alternatively, other variations of this command to run all tests in parallel with `pytest-xdist`:

```shell
pytest -n auto  # Run all tests in parallel on all available CPU cores.
pytest -n auto -v  # As before, but with verbose output.
```
