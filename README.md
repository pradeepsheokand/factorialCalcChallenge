# factorialCalcChallenge
Complete Solution Details are provided in the attached confluence link. 
https://pradeepksheokand.atlassian.net/wiki/spaces/SWISSBORG/pages/262145/Factorial+Calculator+-Test+Plan

Instructions to Run the Python Testing Framework:
1) Clone the GitHub Repo: https://github.com/pradeepsheokand/factorialCalcChallenge to your local directory
2) If not already installed, Install Python version > 3.5
3) Create a virtual env using this python command: python -m venv c:\path\to\myenv
4) Activate above virtual env: \path\to\myenv\Scripts\activate
5) Install dependencies using this command (requirements.txt file below has complete dependencies for this project): pip install -r /path/to/requirements.txt
requirements.txt
6) Set working directory as PYTHONPATH so that if you have modules in sub-directories then pytest can identify: set PYTHONPATH=C:\VSO\Sifchain\sorting_testing_challenge;%PYTHONPATH%
7) Run this command to execute tests: pytest -vv testfactorialcalculator.py --html=reports/testreport.html --durations=0
