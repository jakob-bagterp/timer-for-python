python3 build_package.py;
echo "";

python3 deploy_package.py;
#python3 deploy_test_package.py;
echo "";

pip3 uninstall timer-for-python;
echo "";

sleep 10s; # It takes a moment before the latest version of the newly uploaded package on PyPI is avaible. Let's wait a moment.
pip3 install timer-for-python;
#python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps timer-for-python;
