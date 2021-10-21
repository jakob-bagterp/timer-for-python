#!/bin/bash

python3 build_package.py;
echo "";

python3 deploy_package.py;
#python3 deploy_test_package.py;
echo "";

pip3 uninstall timer-for-python;
echo "";

# It takes a moment before the latest version of the newly uploaded package on PyPI is avaible. Let's wait a moment.
for i in {10..1}; do
    if [ $i == 1 ]; then
        echo "Waiting $i second before reinstall..."
    else
        echo "Waiting $i seconds before reinstall..."
    fi
    sleep 1s;
done

pip3 install timer-for-python;
#python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps timer-for-python;
