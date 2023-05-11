import subprocess
import sys
import os

# Check if the virtual environment is already active
if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
    print("Virtual environment is already active.")
else:
    print("Virtual environment is not active. Creating virtual environment...")

    # Create virtual environment
    subprocess.run(["python", "-m", "venv", "env", "--prompt", "env", "--python=python3.8"])

    # Activate virtual environment
    if sys.platform.startswith('win32'):
        activate_script = os.path.join("env", "Scripts", "activate")
    else:
        activate_script = os.path.join("env", "bin", "activate")

    subprocess.run(["source", activate_script], shell=True)

# Install PySpark
subprocess.run(["pip", "install", "pyspark"])

# Install data science packages
packages = [
    "numpy",
    "pandas",
    "matplotlib",
    "scikit-learn",
    "seaborn",
    "statsmodels",
    "tensorflow",
    "keras",
    "nltk",
    "pyarrow",
    "dask",
    "confluent-kafka",
    "apache-airflow",
    "apache-beam",
    "sqlalchemy",
    "scipy"
]

for package in packages:
    subprocess.run(["pip", "install", package])

print("Setup completed successfully.")