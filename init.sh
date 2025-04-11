#!/bin/bash

echo "Activating the virtual environment..."
source venv/bin/activate

echo "Installing dependencies from requirements.txt..."
#pip install -r requirements.txt

export PYTHONPATH=src

echo "Creating necessary directories..."
mkdir -p data/generated_data
mkdir -p data/generated_data/images

cd src

echo "Running data_processor.py..."
#python3 data_processor.py

echo "Running algorithms.py..."
python3 algorithms.py

echo "Running multi_algorithms.py..."
python3 multi_algorithms.py

echo "Running time_series.py..."
python3 time_series.py

echo "Running clust.py..."
python3 clust.py

cd ..

echo "Running unit tests..."
python3 -m unittest

