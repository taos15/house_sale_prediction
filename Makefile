# Variables
IGNORE_DIRS := --ignore ./.venv
SCAN_NOTEBOOKS := --scan-notebooks
NUMPY_VERSION := numpy>=1.23,<2.0

# Commands
.PHONY: requirements install run  setup clean

# Run server for Streamlit
run: 
	streamlit run ./app.py --server.port=8501 --server.address=0.0.0.0

# Creates the requirements.txt if it does not exist, it uses `@` to suppress the stdo.
# it uses sed to overwrite the numpy version, and get a losen version.	
requirements:
	@if [ ! -f requirements.txt ]; then \
		echo "Generating requirements.txt..."; \
		pipreqs . $(IGNORE_DIRS) $(SCAN_NOTEBOOKS); \
		if grep -q "^numpy" requirements.txt; then \
			sed -i '' "s/^numpy.*/$(NUMPY_VERSION)/" requirements.txt; \
		else \
			echo "$(NUMPY_VERSION)" >> requirements.txt; \
		fi \
	else \
		echo "requirements.txt already exists. Skipping generation."; \
	fi

setup: requirements
	pip3.11 install --no-cache-dir --upgrade pip && \
    pip3.11 install --no-cache-dir -r requirements.txt

clean:
	rm -rf ./src/__pycache__
	rm -rf venv