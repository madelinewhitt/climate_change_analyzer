deactivate
source venv/bin/activate
# pip install -r requirements.txt
export PYTHONPATH=src
cd src
python3 data_processor.py
python3 algorithms.py #Isa needs to fix this
python3 time_series.py 
#Madeline python3 src/visualizer.py
cd ..
python3 -m unittest
