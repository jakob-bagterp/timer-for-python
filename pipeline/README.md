# Build Pipeline
## Prerequisites
To execute any of the build scripts, ensure that:

* The scripts are executed from this `pipeline` folder
* The current Git branch is `master`
* The version number in `version.py` is up to date

## Full Deployment
The deployment script executes the following processes:

1. Build package from current source code
2. Upload newly built package to PyPI
3. Reinstall Timer for Python

To run the full deployment to either production or test, use the following commands with `prod` or `test` as argument:

### Production
```shell
bash pipeline.sh prod
```

### Test
```shell
bash pipeline.sh test
```

## Separate Scripts
Use the following commands to execute separate scripts.

### Build
```shell
python3 build_package.py
```

### Upload to PyPI
#### Production
```shell
python3 deploy_package.py
```

#### Test
```shell
python3 deploy_test_package.py
```
