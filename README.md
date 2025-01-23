# airflow-dbt-snowflake
The repo provides the steps for initial setup of airflow and to run the dbt-snowflake job via airflow scheduler


Sure! Here’s the entire content formatted as a single `README.md` file:

```markdown
# airflow-dbt-snowflake

This repository provides the steps for the initial setup of Apache Airflow and to run the DBT-Snowflake job via the Airflow scheduler.

## AirFlow-DBT-Snowflake Integration on a Local Machine (Windows)

### Step 1: Install WSL on Windows

Open your command prompt and run:

```bash
C:\Users\psara>wsl --install
```

### Step 2: Launch Ubuntu

Once WSL is installed, launch Ubuntu and follow the prompts to create a default UNIX user account.

```bash
Please create a default UNIX user account.
Enter new UNIX username: shrovan
New password:
Retype new password:
passwd: password updated successfully
```

### Step 3: Update Linux

```bash
shrovan@LAPTOP-3U4JI4R2:/mnt/c/Users/psara$ sudo apt update
```

### Step 4: Install Python and Pip

Install Python and pip for creating a virtual environment:

```bash
shrovan@LAPTOP-3U4JI4R2:/mnt/c/Users/psara$ sudo apt install python3 python3-pip
```

### Step 5: Install Venv and Create a Python Virtual Environment

Install the venv package and create a virtual environment:

```bash
shrovan@LAPTOP-3U4JI4R2:/mnt/c/Users/psara$ sudo apt-get install python3-venv
shrovan@LAPTOP-3U4JI4R2:~$ mkdir airflow_project
shrovan@LAPTOP-3U4JI4R2:~$ cd airflow_project/
shrovan@LAPTOP-3U4JI4R2:/mnt/c/Users/psara/shrovandbtairflow$ python3 -m venv airflow_venv
shrovan@LAPTOP-3U4JI4R2:/mnt/c/Users/psara/shrovandbtairflow$ source airflow_venv/bin/activate
```

### Step 6: Install Apache Airflow in the Virtual Environment

Set the Airflow version and install:

```bash
(airflow_venv) shrovan@LAPTOP-3U4JI4R2:
AIRFLOW_VERSION=2.10.1
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONTRAINT_URL}"
```

### Step 7: Set Airflow Home and Initialize the Database

```bash
(airflow_venv) shrovan@LAPTOP-3U4JI4R2:/mnt/c/Users/psara/shrovandbtairflow$ export AIRFLOW_HOME=~/airflow
(airflow_venv) shrovan@LAPTOP-3U4JI4R2:/mnt/c/Users/psara/shrovandbtairflow$ airflow db init
```

### Step 8: Start the Web Server

```bash
(airflow_venv) shrovan@LAPTOP-3U4JI4R2:/mnt/c/Users/psara/shrovandbtairflow$ airflow webserver --port 8080
```

### Step 9: Start the Scheduler

In a new terminal, activate the virtual environment and start the scheduler:

```bash
shrovan@LAPTOP-3U4JI4R2:/mnt/c/Users/psara$ cd shrovandbtairflow/
shrovan@LAPTOP-3U4JI4R2:/mnt/c/Users/psara/shrovandbtairflow$ source airflow_venv/bin/activate
(airflow_venv) shrovan@LAPTOP-3U4JI4R2:/mnt/c/Users/psara/shrovandbtairflow$ airflow scheduler
```

### Step 10: List Current Users

In a new terminal, list the users:

```bash
(airflow_venv) shrovan@LAPTOP-3U4JI4R2:/mnt/c/Users/psara/shrovandbtairflow$ airflow users list
```

### Step 11: Create a New User with Admin Role

Create an admin user:

```bash
(airflow_venv) shrovan@LAPTOP-3U4JI4R2:/mnt/c/Users/psara/shrovandbtairflow$ airflow users create --username admin --firstname shrovan --lastname p --role Admin --email admin@anyname.com
```

### Step 12: Check User Information

Verify the user details:

```bash
(airflow_venv) shrovan@LAPTOP-3U4JI4R2:/mnt/c/Users/psara/shrovandbtairflow$ airflow users list
```

### Step 13: Create a DAG Folder

Open the Airflow installation folder in VSCode and create a `dags` folder. Add a new Python script in this folder and activate the virtual environment.

```bash
(airflow_venv) shrovan@LAPTOP-3U4JI4R2:/mnt/c/Users/psara/shrovandbtairflow$ source /mnt/c/Users/psara/shrovandbtairflow/airflow_venv/bin/activate
```

### Step 14: Run the Python Script

Execute your DAG script:

```bash
(airflow_venv) shrovan@LAPTOP-3U4JI4R2:~/airflow/dags$ python3 hello_world.py
```

### Step 15: Create a `requirements.txt`

Create a `requirements.txt` file for the required packages:

```bash
(airflow_venv) shrovan@LAPTOP-3U4JI4R2:~/airflow$ cat requirements.txt 
apache-airflow
dbt-core
dbt-snowflake
```

### Step 16: Install Requirements

Run the requirements file:

```bash
(airflow_venv) shrovan@LAPTOP-3U4JI4R2:~/airflow$ pip install -r requirements.txt 
```

### Step 17: Create a Python Script for DBT Model

Create a Python script to run a DBT model from Airflow.

### Step 18: Execute the Script

Run your script and check the task in Airflow.
```

You can copy this content into a file named `README.md` in your repository. Let me know if you need any more help!

Step17:- Create a Python script to run a DBT Model from Airflow.


Step 18: Execute the Script and check the task in Airflow.

