# GithubActionsExercise

## Overview
The **GithubActionsExercise** project is a demonstration of several essential software development practices, including validation, testing, code linting, and Continuous Integration (CI). The project features:

- Simple code with Pydantic for data validation.
- Testing with Pytest for unit testing.
- Static code analysis with Ruff.
- Code coverage measurement with Coverage.py.
- A GitHub Actions workflow to automate CI, including caching for dependencies to optimize performance.

## Features and Details

### 1. **Pydantic for Data Validation**
The project utilizes **Pydantic**, a data validation library for Python, to ensure that data passed to functions is valid before processing. A simple class, `Numbers`, is created using Pydantic to validate that the input values are integers.

- **`Numbers` Model**: 
  The `Numbers` class holds two integer values `a` and `b`. Pydantic ensures that the values passed into the class are properly typed as integers. If the values are incorrect (e.g., strings instead of integers), Pydantic raises a `ValidationError`.

- **Functions**:
  - `add_numbers`: Adds two integers validated by the `Numbers` model.
  - `substract_numbers`: Subtracts two integers validated by the `Numbers` model.

### 2. **Unit Testing with Pytest**
Testing is performed using **Pytest**, a popular testing framework for Python.

- **Test Cases**:
  - Tests ensure that the addition and subtraction functions return correct results.
  - Tests validate that Pydantic correctly raises `ValidationError` when invalid data (e.g., strings instead of integers) is provided.
  - Additional tests handle edge cases such as negative numbers and zero values.

The tests are structured in a separate file, `tests/test_main.py`, ensuring proper modularization.

### 3. **Static Code Analysis with Ruff**
To maintain clean and readable code, **Ruff** is used as a linter for static code analysis. Ruff enforces various Python standards, including:

- Docstring conventions (PEP 257).
- Code formatting and styling (PEP 8).

By integrating Ruff into the CI pipeline, any stylistic issues or violations of Python standards are caught early, ensuring consistent code quality across the project.

### 4. **Code Coverage with Coverage.py**
To ensure that the tests cover as much of the code as possible, the project includes **Coverage.py**.

- **Coverage Check**:
  - Coverage.py tracks which parts of the code are executed by the tests.
  - The project is configured to enforce a minimum test coverage of 90%, meaning that if less than 90% of the code is covered by tests, the CI pipeline will fail.

This ensures that the project maintains a high level of code coverage, improving code reliability and reducing the likelihood of untested bugs.

### 5. **GitHub Actions CI Pipeline**
The project is integrated with **GitHub Actions** for Continuous Integration (CI). The CI pipeline automates the process of running static code analysis, running tests, and checking coverage whenever code is pushed or a pull request is made.

- **Steps in the CI Pipeline**:
  1. **Checkout Code**: The pipeline checks out the latest code from the repository.
  2. **Dependency Caching**: The pipeline caches dependencies using `actions/cache@v3` to speed up subsequent runs.
  3. **Install Dependencies**: Installs project dependencies, including `pytest`, `ruff`, and `coverage`.
  4. **Run Ruff**: Executes Ruff to ensure that the code meets linting standards.
  5. **Run Unit Tests**: Executes Pytest to verify the correctness of the code.
  6. **Check Coverage**: Runs Coverage.py to ensure that the code is at least 90% covered by tests. If coverage falls below 90%, the pipeline fails.

The caching mechanism speeds up the workflow by avoiding repeated installation of dependencies, thus optimizing the pipeline’s performance.

## Project Structure
```plaintext
GithubActionsExercise/
│
├── code/
│   ├── __init__.py  # Package initialization
│   └── main.py      # Contains the Numbers model and the add/subtract functions
│
├── tests/
│   └── test_main.py # Contains unit tests for the add_numbers and substract_numbers functions
│
├── requirements.txt  # Python package dependencies
├── .github/
│   └── workflows/
│       └── ci.yml   # GitHub Actions CI configuration
├── pyproject.toml    # Ruff and other project configurations
└── README.md         # Project documentation (this file)
```
## How to Run

1. **Install Dependencies**:
   To install the necessary dependencies, run the following command in your terminal:
   ```bash
   pip install -r requirements.txt
2. **Run Tests**:
   To execute the unit tests using Pytest, run the following command:
   ```bash
   pytest
3. **Run Coverage**:
   To check the test coverage of the code using coverage.py, use these commands:
   ```bash
   coverage run -m pytest
   coverage report --fail-under=90
3. **Run Ruff for Static Code Analysis**:
   To lint your code and ensure that it follows proper Python standards using Ruff, run:
   ```bash
   ruff check .

## Conclusion
The **GithubActionsExercise** project demonstrates the integration of data validation, testing, linting, and CI automation. The use of Pydantic ensures robust data validation, while Pytest and Coverage.py ensure high code quality and reliability. GitHub Actions provides a streamlined process for continuous integration with caching, static analysis, and test coverage checks.


## Acknowledgments

This README was written with the assistance of [ChatGPT](https://chat.openai.com/).
