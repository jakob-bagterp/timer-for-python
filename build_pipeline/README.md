# Build Pipeline
## Prerequisites
To execute any of the build scripts, ensure that:

* The scripts are executed from this `build_pipeline` folder
* The current Git branch is `master`
* The version number in `version.py` is up to date

## Full Deployment
The deployment script executes the following processes:

1. Run unit tests and only continue if all tests passed
2. Build package from current source code
3. Upload newly built package to PyPI
4. Reinstall newly uploaded version of Timer for Python from PyPI

To run the full deployment to either production or test, use the following commands with `prod` or `test` as argument:

#### Production
```shell
bash pipeline.sh prod
```

#### Test
```shell
bash pipeline.sh test
```

## Separate Scripts
Use the following commands to execute separate scripts.

### Run Tests
```shell
python3 -m helper.test
```

### Build
```shell
python3 -m helper.build_package
```

### Upload to PyPI
#### Production
```shell
python3 -m helper.deploy_package
```

#### Test
```shell
python3 -m helper.deploy_test_package
```
