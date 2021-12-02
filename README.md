# TestingGithubProject
**PythonTestAutomationFramework**

**Description**

Test Automation Framework for web automation of "https://github.com" using Selenium and Python with the below features:

* Framework is based on Page Object Model. 
* Reporting using Allure report.
* Logging to external file.
    
The project is being developed during the iTechArt internship.

# How to install it

Make sure you have python3 installed on your machine by typing in cmd ``python3 --version`` if not - go to https://realpython.com/installing-python/#step-1-download-the-python-3-installer.

1) Clone the repository to any local path.

``$ git clone https://github.com/EgorSolenok/TestingGithubProject.git``

2) Install dependencies in python3 from requirements.txt:

``pip3 install -r requirements.txt``

3) Add your own credentials (**USERNAME** and **PASSWORD**) for logging to github.com in ``utils/credentials.py``:

**class Credentials**
* USERNAME = ``'type here'``
* PASSWORD = ``'type here'``

# How to run it

To run the test cases in feature "Guest login actions on the main page" and create report:

``pytest -v -m "guest_actions" --alluredir=report_data/``

To run the test cases in feature "User main actions with repository" and create report:

``pytest -v -m "main_actions" --alluredir=report_data/``


To run the test cases in feature "User additional actions with repository" and create report:

``pytest -v -m "addition_actions" --alluredir=report_data/``

To run required tests from PythonInternship_Task0 use in brackets following marks:
* Correct user is logged in - "sign_in"
* Create repository - "create_repository"
* Rename repository - "rename_repository"
* Add README - "add_readme"
* Delete repository - "delete_repository"

To create **Allure report** and open it type in cmd being located in the folder path:

``allure serve report_data``

**How to logging**

To read logs you should to read or copy file ``logging_data.log`` to your machine after every test run. 
File will be overwritten after starting the next test.
The ability to append logs in file will be added in next version of the framework.
