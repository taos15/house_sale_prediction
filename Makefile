# Variables
IGNORE_DIRS := --ignore ./.venv
SCAN_NOTEBOOKS := --scan-notebooks

# Commands
.PHONY: requirements install run run_dev run_fastapi run_streamlit setup clean

# Run development server for FastAPI
run_fastapi_dev:
	fastapi dev ./src/api.py

# Run production server for FastAPI
run_fastapi: venv/bin/activate
	./venv/bin/fastapi ./src/api.py

# Run development server for Streamlit
run_streamlit_dev:
	streamlit run ./src/app.py

# Run production server for Streamlit
run_streamlit: venv/bin/activate
	./venv/bin/streamlit run ./src/app.py

requirements:
	pipreqs . $(IGNORE_DIRS) $(SCAN_NOTEBOOKS)

setup: requirements.txt
	pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install --no-cache-dir -r requirements.txt

clean:
	rm -rf ./src/__pycache__
	rm -rf venv