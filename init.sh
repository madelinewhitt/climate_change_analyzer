deactivate
source venv/bin/activate
# pip install -r requirements.txt
export PYTHONPATH=src
cd src
python3 data_processor.py
python3 algorithms.py 
python3 time_series.py 
python3 multi_algorithms.py #Needs fixing
python3 clust.py
#Madeline python3 src/visualizer.py
cd ..
python3 -m unittest
