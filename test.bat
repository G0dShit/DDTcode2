del /f /s /q result\*.*
pytest --alluredir result -n 4  execute_cases.py
allure generate ./result/ -o ./report/ --clean