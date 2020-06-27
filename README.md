# Jotform Formatter

Replaces the values of every row for the specified columns in the config folder.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Python 3
* Pip


### Installing

Install dependencies with pip

```
pip install -r requirements.txt
```


### Running the GUI

```
python3 src/main.py
```

### Deployment

Create the executable

##### Windows

```
pyinstaller --onefile -w -i logo.ico -n formatter src/main.py
```

##### Mac
```
pyinstaller --onefile -w -i logo.icns -n formatter src/main.py
```

Executable will be created under the 'dist' folder