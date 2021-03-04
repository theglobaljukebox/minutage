
# install python venv and install python libraries
env:
	python3 -m venv env
	./env/bin/python3 ./env/bin/pip3 install -r requirements.txt

update: env
	./env/bin/python3 ./env/bin/pip3 install --upgrade -r requirements.txt


all: download

help:
	@printf "\nIf you are an authenticated user and you want to update the data from Google Drive, run: make download\n\n"
	@printf "To build the dataset into CLDF format, run: make process (currently not working)\n\n"
	@printf "To validate the dataset, run: make test (currently not working)\n\n"

download: env
	@printf "Collecting data from google drive is only available to authenticated users."
	mkdir -p raw/
	./env/bin/python3 download_googledrive.py

clean:
	rm -rf raw/

