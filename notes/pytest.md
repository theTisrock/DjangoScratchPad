https://docs.pytest.org/en/stable/getting-started.html

Install and use Pytest:
- pip install -U pytest OR pipenv install pytest
- check the version: pytest --version
- create a sample pytest file with mock functions. pytest modules must have the "test_" prefix on the file name and the 
function. Be sure to write a FAILING test to see how it catches errors.
  
pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories. 
More generally, it follows standard test discovery rules.

- execute the tests by entering the "pytest" command in the project directory.