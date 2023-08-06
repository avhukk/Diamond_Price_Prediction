## This is an End to End ML project

### Step 1: Creating and activating a virtual environment
```
conda create -p venv python==3.8

conda activate venv/
```

### Step 2: Creating requirements.txt for downloading required dependencies
```
pip install -r requirements.txt
```

### Step3: Create setup.py (To convert the project into a packages (folders -> packages))
```
pip intall -r requirements.txt

or 

python setup.py install
```

### Step4: Create folder src (consisting of entire lifecycle of the project) and create the following : 
1. Folder called Components:
2. Components/data_ingestion.py
3. Components/data_transformation.py
4. Components/model_trainer.py
5. Folder called pipeline:
6. pipeline/training
7. pipeline/test or prediction
### Step5: Create folder notebooks for EDA, feature engineering and so on 
1. logger.py
2. exception.py
3. utils.py (for general functionalities)
### Step 6: Create .gitignore