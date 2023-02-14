Command for start all api tests:
- With allure logs: python -m pytest --alluredir=test_results/  api/tests/
- Without allure logs: python -m pytest api/tests/

Command for start all ui tests:
- With allure logs: python -m pytest --alluredir=test_results/  ui/tests/
- Without allure logs: python -m pytest ui/tests/

Command for see result log of allure: allure serve test_results/

if you get allure error - create package test_results
