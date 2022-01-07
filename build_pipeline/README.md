# Build Pipeline
## Prerequisites
To execute any of the build scripts, ensure that:

* The scripts are executed from this `build_pipeline` directory
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
python3 -m helper.run_tests
```

### Build
```shell
python3 -m helper.build_package
```

### Deploy to PyPI
#### Production
```shell
python3 -m helper.deploy_package.prod
```

#### Test
```shell
python3 -m helper.deploy_package.test
```

### Deploy to Homebrew
When a new package is built, deployment to Homebrew has the following manual steps:

1. Ensure that a [tag](https://github.com/jakob-bagterp/timer-for-python/tags) has been created for the latest version.
2. Based on the relevant version tag, create a [new release](https://github.com/jakob-bagterp/timer-for-python/releases) and upload the relevant `tar.gz` package.
3. Update the [Homebrew formula](https://github.com/jakob-bagterp/timer-for-python/blob/master/build_pipeline/homebrew/formula.rb) with link to the latest package file from step 2 and the file's SHA256 checksum.
4. From the `build_pipeline` directory, execute the following script to audit and deploy the Homebrew formula. Ensure that eventual errors are fixed before a pull request is created:

```shell
python3 -m homebrew.update_formula
```
