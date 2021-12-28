# TestingGithubProject
**PythonTestAutomationFramework**

**Description**

Test Automation Framework for web automation of "https://github.com" using Selenium and Python with the below features:

* Framework is based on Page Object Model. 
* Reporting using Allure report.
* Logging to external file.
    
The project is being developed during the iTechArt internship.

# How to install it

Make sure you have python3.10 installed on your machine by typing in cmd ``python3 --version`` if not - go to https://realpython.com/installing-python/#step-1-download-the-python-3-installer.

1) Clone the repository to any local path.

``$ git clone https://github.com/EgorSolenok/TestingGithubProject.git``

2) You have to install allure command line and add the allure folder installation into system environment variable: https://docs.qameta.io/allure/#_installing_a_commandline

3) Make sure you have pipenv  by typing in cmd ``pipenv --version``. If not - you have to install pipenv for creation virtual environment and installation packages: https://pipenv.pypa.io/en/latest/  

``$ pip install --user pipenv``

4) Install dependencies:

``pipenv install``

5) To set your own credentials as default type them to (**USERNAME** and **PASSWORD**) for signin in to github.com in ``config.py``:

**class Credentials**
* USERNAME = ``'type here'``
* PASSWORD = ``'type here'``

# How to run it

**For all tests runs you should to type commands in folder ``tests``.**

**If you don't set your own creds in config.py - you should type your actual credentials to commandline as  `` --user=< USERNAME > `` and `` --password=< PASSWORD > ``in every case (without brackets).**




To run the test cases in feature "Guest login actions on the main page" and create report:

``pytest -v -m "guest_actions" --alluredir=report_data/``

To run the test cases in feature "User main actions with repository" and create report:

``pytest -v -m "main_actions" --alluredir=report_data/``


To run the test cases in feature "User additional actions with repository" and create report:

``pytest -v -m "addition_actions" --alluredir=report_data/``

To run required tests from PythonInternship_Task0 use in brackets following marks:
* Correct user is logged in -  ``pytest -v -m "sign_in" --alluredir=report_data/``
* Create repository -  ``pytest -v -m "create_repository" --alluredir=report_data/``
* Rename repository -  ``pytest -v -m "rename_repository" --alluredir=report_data/``
* Add README -  ``pytest -v -m "add_readme" --alluredir=report_data/``
* Delete repository -  ``pytest -v -m "delete_repository" --alluredir=report_data/``



To create **Allure report** and open it type in cmd being located in the folder path:

``allure serve report_data``

**How to logging**

To read logs you should to read ``logging_data.log`` . 

