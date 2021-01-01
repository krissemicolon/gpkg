build:
	crystal build src/main.cr -o gpkg

install:
	mv gpkg /usr/local/bin	

uninstall:
	rm -f /usr/local/bin/gpkg
