default:
	make check
unit:
	python3 -m unittest discover -p "*_test.py"
doctest:
	python3 -m doctest *.py && echo "OK"
check:
	make unit doctest
generate:
	mkdir -p inputs && python3 generate.py inputs
