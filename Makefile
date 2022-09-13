test:
	python setup.py test
 
create_dist:
	rm -rf dist
	python setup.py sdist
	echo "DID YOU UPDATE THE VERSION NUMBER?"

publish: create_dist
	twine upload dist/*