# Variables
IGNORE_DIRS := --ignore ./.venv
SCAN_NOTEBOOKS := --scan-notebooks

# Commands
.PHONY: requirements install run run_dev run_fastapi run_streamlit setup clean

# Run development server for FastAPI
run_fastapi_dev:
	./venv/bin/fastapi dev ./src/api.py

# Run production server for FastAPI
run_fastapi: venv/bin/activate
	./venv/bin/fastapi ./src/api.py

# Run development server for Streamlit
run_streamlit_dev:
	./venv/bin/streamlit run ./app.py
	

# Run production server for Streamlit
run_streamlit: venv/bin/activate
	./venv/bin/streamlit run ./app.py

requirements:
	pipreqs . $(IGNORE_DIRS) $(SCAN_NOTEBOOKS)

setup: requirements.txt
	./venv/bin/pip3.11 install --no-cache-dir --upgrade pip && \
    ./venv/bin/pip3.11 install --no-cache-dir -r requirements.txt

venv/bin/activate: requirements.txt
	./venv/bin/python3.11 -m venv venv
	./venv/bin/pip3.11 install --no-cache-dir -r requirements.txt


clean:
	rm -rf ./src/__pycache__
	rm -rf venv