pytest-coverage:
	pytest -vv --cov --cov-report=term-missing
pytest-collect:
	pytest --collect-only
check-build:
	python3 setup.py bdist_wheel sdist
check-bdist:
	python3 setup.py bdist_wheel
check-sdist:
	python3 setup.py sdist
ruff:
	ruff check .
ruff-fix:
	ruff check --fix .
venv-remove:
	rm -rf .venv
venv-deactivate:
	deactivate
venv-activate:
	source .venv/bin/activate
venv-setup:
	python3 -m venv .venv
clean-package:
	rm -Rf ./build; rm -Rf ./dist; rm -Rf ./.eggs; rm -Rf ./*.egg-info; rm -Rf ./**/*.egg-info; rm -Rf ./.coverage; 
clean-pycache:
	rm -Rf ./.pytest_cache; rm -Rf ./**/__pycache__; rm -Rf ./**/**/__pycache__;
clean: clean-package clean-pycache