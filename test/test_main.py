# tests/test_main.py

import os
import subprocess
import pytest

@pytest.fixture
def input_files():
    input_dir = os.path.join(os.path.dirname(__file__), '../input')
    return [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith('.txt')]

@pytest.fixture
def answer_files():
    answer_dir = os.path.join(os.path.dirname(__file__), '../output')
    return [os.path.join(answer_dir, f) for f in os.listdir(answer_dir) if f.endswith('.txt')]

def test_main_script(input_files, answer_files):
    total_tests = len(input_files)
    passed_tests = 0
    failed_tests = 0

    for input_file, answer_file in zip(sorted(input_files), sorted(answer_files)):
        with open(input_file, 'r') as file:
            input_content = file.read()
        
        result = subprocess.run(['python', './execute/main.py'], input=input_content, capture_output=True, text=True)
        
        with open(answer_file, 'r') as file:
            expected_content = file.read().strip()
        
        if result.stdout.strip() != expected_content:
            print(f"Failed for file: {input_file}")
            failed_tests += 1
        else:
            print(f"Test case passed for file: {input_file}")
            passed_tests += 1
    
    print(f"Total test cases: {total_tests}")
    print(f"Passed test cases: {passed_tests}")
    print(f"Failed test cases: {failed_tests}")




