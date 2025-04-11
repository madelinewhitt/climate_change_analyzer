
# Climate Change Analyzer

This project provides data processing and analytical tools for climate change data.

## **Setup Instructions**

### **1. Activate Virtual Environment**
Before running the project, activate the virtual environment:

```sh
source venv/bin/activate
```

To deactivate the virtual environment when done, use:

```sh
deactivate
```

### **2. Install Dependencies**
Ensure all required Python packages are installed:

```sh
pip install -r requirements.txt
```

### **3. Set Up the Environment**
Set the `PYTHONPATH` so the scripts can properly reference the `src` directory:

```sh
export PYTHONPATH=src
```

### **4. Run the Scripts**
You can run the project either by executing the scripts manually or by using the `init.sh` script.

#### **Run the Scripts Manually:**
Navigate to the `src` directory and execute the processing and analysis scripts:

```sh
cd src
python3 data_processor.py
python3 algorithms.py
python3 multi_algorithms.py  # Needs fixing
python3 time_series.py
python3 clust.py
```

Return to the root directory:
```sh
cd ..
```

#### **Run the Project Using init.sh:**
Alternatively, you can run the entire process by executing the `init.sh` script in the main folder:

```sh
./init.sh
```

### **5. Run Unit Tests**
To ensure the scripts are working correctly, run:

```sh
python3 -m unittest
```

## **Notes**
- Ensure all dependencies in `requirements.txt` are installed before running the scripts.
