#!/bin/bash

PROD="prod"
TEST="test"

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

python3 build_package.py
echo ""

if [ $TARGET == $PROD ]; then
    python3 deploy_package.py
elif [ $TARGET == $TEST ]; then
    python3 deploy_test_package.py
else
    echo "Something went wrong. Try again."
    exit 1
fi
echo ""

pip3 uninstall timer-for-python
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

if [ $TARGET == $PROD ]; then
    pip3 install timer-for-python
elif [ $TARGET == $TEST ]; then
    python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps timer-for-python
else
    echo "Something went wrong. Try again."
    exit 1
fi
echo ""
