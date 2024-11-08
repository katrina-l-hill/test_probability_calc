# Development of a Diagnostic Test Probability Calculator

## Author: Katrina Hill

## Description
Design and implement an application that allows a user to input the prevalence of a disease, the sensitivity of a diagnostic test, and the specificity of the test. The application will then compute and display the probability of the disease given the test result.

## Features
- User-friendly Input Prompts: The program guides the user through inputting the prevalence, sensitivity, and specificity, making it easy for non-technical users.
- Real-time Calculations: Instantly computes probabilities using the input data.
- Comprehensive Results: Outputs both the probability of disease given a positive test and a negative test for complete analysis.
- Error Handling: Provides clear feedback for invalid inputs, ensuring correct data entry.

## Files
- `app.py`: The main program that performs the probability simulations.
- `test.py`: The test file to check the functionality of the application.

## Requirements
- Python 3.11

## How to Run
1. **Clone the repository** (or download the files):
   - git clone https://github.com/katrina-l-hill/test_probability_calc
   - cd into the repository directory
2. **Run the Main program**:
   - run python app.py to run the program
   - the first prompt will be to enter the prevalence of the disease
     - press enter after entering the number
   - the second prompt will be to enter the sensitivity of the test
     - press enter after entering the number
   - the third prompt will be to enter the specificity of th the test
     - press enter after entering the number
3. **Run the tests**:
   - run python -m pytest tests.py to run the tests