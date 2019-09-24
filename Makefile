# The ancient unix build program.

# Let Python unittest module find and run tests itself
test:
	python -m unittest discover -p "*_test.py"

# Manual way.  
# This requires each *_test.py file to have a "main" that invokes unittest.
dumbtest: *_test.py
	for t in $?; do \
		echo Running $$t; \
		python $$t; \
	done;

clean:
	rm *.pyc
	rm -f __pycache__ src/__pycache__
