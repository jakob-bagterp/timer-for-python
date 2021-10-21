#!/bin/bash

python3 build_package.py;
echo "";

python3 deploy_package.py;
#python3 deploy_test_package.py;
echo "";

pip3 uninstall timer-for-python;
echo "";

# It takes a moment before the latest version of the newly uploaded package on PyPI is avaible. Let's wait a moment.
echo "Waiting 10 seconds before reinstall";
sleep 1s;
echo "Waiting 9 seconds before reinstall";
sleep 1s;
echo "Waiting 8 seconds before reinstall";
sleep 1s;
echo "Waiting 7 seconds before reinstall";
sleep 1s;
echo "Waiting 6 seconds before reinstall";
sleep 1s;
echo "Waiting 5 seconds before reinstall";
sleep 1s;
echo "Waiting 4 seconds before reinstall";
sleep 1s;
echo "Waiting 3 seconds before reinstall";
sleep 1s;
echo "Waiting 2 seconds before reinstall";
sleep 1s;
echo "Waiting 1 second before reinstall";
sleep 1s;

pip3 install timer-for-python;
#python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps timer-for-python;
