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

VIZ_OUTPUT ?= -
visualize:
ifndef VIZ_INSTANCE
	$(error VIZ_INSTANCE is undefined)
endif
	python3 visualize.py $(VIZ_INSTANCE) --with-solution "$(VIZ_SOLUTION)" $(VIZ_OUTPUT)
