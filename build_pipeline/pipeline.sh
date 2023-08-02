#!/bin/bash

PROD="prod"
TEST="test"

# Get and set arguments for either deployment to production or test.
if [ $1 == $PROD ]; then
    TARGET=$PROD
elif [ $1 == $TEST ]; then
    TARGET=$TEST
else
    echo "Argument \"$1\" is invalid."
    echo "Use valid arguments instead:"
    echo "Use \"bash pipeline.sh $PROD\" to run build pipeline for PRODUCTION."
    echo "Use \"bash pipeline.sh $TEST\" to run build pipeline for TEST."
    exit 1
fi

# Run unit tests and only continue if all tests passed.
python3 -m helper.run_tests
EXIT_CODE=$?
if [ $EXIT_CODE != 0 ]; then # If exit code 0, all tests passed. But if any other exit code, some error happened. More info: https://docs.pytest.org/en/latest/reference/exit-codes.html
    echo "Unit tests not passed. Try again."
    echo "Exit code: $EXIT_CODE"
    exit 1
fi
echo ""

# Build new package from current branch (i.e. remember to set branch to "master" in Git).
python3 -m helper.build_package
echo ""

# Upload newly built package to PyPI.
if [ $TARGET == $PROD ]; then
    python3 -m helper.deploy_package.prod
elif [ $TARGET == $TEST ]; then
    python3 -m helper.deploy_package.test
else
    echo "Something went wrong. Try again."
    exit 1
fi
echo ""

# Remove existing installation of Timer for Python before reinstallation.
pip uninstall timer-for-python
echo ""

# It takes a moment before the latest version of the newly uploaded package on PyPI is avaible. Let's wait a moment.
for i in {10..1}; do
    if [ $i == 1 ]; then
        echo "Waiting $i second before reinstall..."
    else
        echo "Waiting $i seconds before reinstall..."
    fi
    sleep 1s
done

# Reinstall newly uploaded and latest version Timer for Python.
if [ $TARGET == $PROD ]; then
    pip install timer-for-python
elif [ $TARGET == $TEST ]; then
    python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps timer-for-python
else
    echo "Something went wrong. Try again."
    exit 1
fi
echo ""
