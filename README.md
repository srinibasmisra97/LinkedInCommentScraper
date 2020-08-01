# LinkedIn Comment Scraper

## Setup

Tools required:
1. Python3 (https://realpython.com/installing-python/)
2. Pip3 for Python3 (https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/)
3. Virtualenv
4. Google Chrome
5. Chromium Driver

If any Python IDE, such as PyCharm is installed, then points 1-4 can be ignored, as they would already be present.

Download or clone the code from github. Open a command prompt or terminal(normal linux terminal or in PyCharm) and go to the downloaded folder.

To setup `virtualenv`:
```
virtualenv -p python3 venv
```

To activate virtualenv:
```
source ./venv/bin/activate
```

Run the following command to install python dependencies:
```
pip3 install requirements.txt
```

To download the chromium driver:
1. Go to https://chromedriver.chromium.org/
2. Download the driver for your specific version of chrome. To check that:
    1. Open chrome.
    2. Go to chrome://version .
    3. Check the major version, i.e. for a version `84.0.4147.105`, the major version is `84`.
3. Extract the zip folder, and note the path to the executable, i.e. the file you'll extract.
4. Update the path in `scraper.py` in the variable `CHROME_DRIVER_PATH`.

## Run the script

```
python3 scraper.py
```

Enter the filename (w/ .csv at the end) where the data will be stored.

Enter the link to the LinkedIn post.

Enter username and password.

Wait and watch.

***PLEASE DO NOT INTERFERE WITH THE PROCESS***

You can check the number of comments parsed in the execution terminal.