# Python + Playwright + pytest — Intensive 5-Day Learning Plan

> **Goal:** Build the practical foundations needed to read, write, run, and debug browser automation tests in five days.
> 
> **Starting level:** Almost from scratch.
> 
> **Estimated time:** 5–6 hours per day (about 25–30 hours total).
> 
> **Priority:** Project requirements, the Python needed for testing, pytest, and then Playwright.
> 
> **Important:** Five days is enough to learn the basics and create your first working tests, but not to master Python completely. If you already have a repository at work, adapt the exercises to its structure and conventions instead of restructuring the project to match this plan's examples.

---

## Table of Contents

- [How to Use This Plan](#how-to-use-this-plan)
- [Core Resources](#core-resources)
- [Day 1 — Python Fundamentals](#day-1--python-fundamentals)
- [Day 2 — Practical Python and pytest](#day-2--practical-python-and-pytest)
- [Day 3 — Playwright Fundamentals](#day-3--playwright-fundamentals)
- [Day 4 — Test Structure and Debugging](#day-4--test-structure-and-debugging)
- [Day 5 — Implementing Tests in the Target Project](#day-5--implementing-tests-in-the-target-project)
- [Final Skills Checklist](#final-skills-checklist)
- [Glossary](#glossary)
- [Further Resources](#further-resources)

---

## How to Use This Plan

### Guidelines

1. **Write more code than you watch.** Aim for about 30% theory and 70% practice.
2. **Do not copy without understanding.** After working through an example, close the material and recreate it on your own.
3. **Read errors.** Before changing code, find the first meaningful error in the traceback and determine what it means.
4. **Use the documentation as the source of truth.** A video or course can help explain a concept, but the documentation should be authoritative for API details.
5. **Explore the target repository starting on Day 2.** Do not postpone working with real tests until the end of the week.
6. **Do not try to learn everything at once.** First learn the syntax and basic patterns needed for the current task.

### Priority Labels

- **[MUST]** — required to implement basic tests.
- **[SHOULD]** — very useful; cover these once you understand the basics.
- **[LATER]** — postpone if the five-day deadline cannot be extended.

### Suggested Daily Schedule

| Block                   | Time       | How to work                                           |
| ----------------------- | ----------:| ----------------------------------------------------- |
| Theory                  | 45–60 min  | Read the specified sections and take brief notes      |
| Coding with an example  | 45–60 min  | Recreate the example and explain every line           |
| Independent exercises   | 90–120 min | Solve tasks without copying a ready-made solution     |
| Documentation           | 30 min     | Find answers to specific questions                    |
| Review / target project | 60–90 min  | Apply what you learned to the tests you need to write |

You do not need to follow the schedule to the exact minute. If you get stuck on an error, spend time understanding it, but do not spend the entire day on one extra topic.

---

## Core Resources

Use these resources throughout the plan. You do not need to read all of them in full.

### Python

| Resource                                                                                             | What to use it for                                                            |
| ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| [30 Days of Python — GitHub](https://github.com/Asabeneh/30-Days-Of-Python)                          | A course with explanations and exercises. Choose only the topics listed here. |
| [Python Tutorial — official documentation](https://docs.python.org/3/tutorial/)                      | Reference for Python syntax and fundamentals.                                 |
| [Python: Built-in Types](https://docs.python.org/3/library/stdtypes.html)                            | Strings, lists, dictionaries, sets, tuples, and Boolean types.                |
| [Python: Built-in Functions](https://docs.python.org/3/library/functions.html)                       | Functions such as `len()`, `range()`, `type()`, `print()`, and `enumerate()`. |
| [Python: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)                      | Understanding exceptions and error messages.                                  |
| [Python: venv](https://docs.python.org/3/library/venv.html)                                          | Virtual environments.                                                         |
| [Python: Installing Packages](https://packaging.python.org/en/latest/tutorials/installing-packages/) | Installing libraries and the basics of `pip`.                                 |

### pytest

| Resource                                                                                                | What to use it for                      |
| ------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| [pytest — Getting Started](https://docs.pytest.org/en/stable/getting-started.html)                      | First tests and how to run them.        |
| [pytest — Assertions](https://docs.pytest.org/en/stable/how-to/assert.html)                             | Assertions and readable test results.   |
| [pytest — Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)                             | Shared setup and test data preparation. |
| [pytest — Parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html)                       | Testing multiple sets of data.          |
| [pytest — Good Integration Practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html) | Project structure and good practices.   |
| [pytest — How to invoke pytest](https://docs.pytest.org/en/stable/how-to/usage.html)                    | Running files, tests, and options.      |

### Playwright for Python

| Resource                                                                                    | What to use it for                                              |
| ------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| [Playwright Python — Installation / Introduction](https://playwright.dev/python/docs/intro) | Installation and your first pytest test.                        |
| [Playwright — Writing Tests](https://playwright.dev/python/docs/writing-tests)              | Test patterns, assertions, and the basic workflow.              |
| [Playwright — Locators](https://playwright.dev/python/docs/locators)                        | Finding page elements.                                          |
| [Playwright — Assertions](https://playwright.dev/python/docs/test-assertions)               | Verifying expected results.                                     |
| [Playwright — Auto-waiting](https://playwright.dev/python/docs/actionability)               | Waiting for elements to become ready.                           |
| [Playwright — Debugging](https://playwright.dev/python/docs/debug)                          | Debugging tests.                                                |
| [Playwright — Trace Viewer](https://playwright.dev/python/docs/trace-viewer)                | Analyzing test execution and errors.                            |
| [Playwright Python API Reference](https://playwright.dev/python/docs/api/class-page)        | Details of the `Page` object's methods.                         |
| [Playwright — Page Object Model](https://playwright.dev/python/docs/pom)                    | Organizing larger test suites if the project uses this pattern. |

### Video Resources — Optional

Do not watch an entire video course as part of this five-day plan. Choose a segment that covers the topic you are currently struggling with.

- [freeCodeCamp — Learn Python: Full Course for Beginners (YouTube)](https://www.youtube.com/watch?v=rfscVS0vtbw) — a long course covering fundamentals, functions, collections, loops, exceptions, files, and modules.
- [freeCodeCamp — Python for Beginners: Full Course (YouTube)](https://www.youtube.com/watch?v=eWRfhZUzrAc) — an alternative beginner course with exercises.
- [Asabeneh's YouTube channel](https://www.youtube.com/channel/UC7PNRuno1rzYPb1xLa4yktw) — supplementary material for 30 Days of Python.
- ### **[Best Motivational Resource](https://youtu.be/ywjyvKzc8e4)** — How to learn, where to find learning materials, and much more!

**Rule:** If you can complete an exercise on your own, do not watch another video on the same topic. Move on.

---

# Day 1 — Python Fundamentals

## Daily Goal

Understand simple Python code and independently write variables, conditions, loops, collections, and functions. Do not move on to complex object-oriented constructs yet.

## Schedule

| Blok | Time   | What to do                                         |
| ---- | ------:| -------------------------------------------------- |
| 1    | 30 min | Check the Python installation and run a `.py` file |
| 2    | 60 min | Variables, data types, operators, and conditions   |
| 3    | 60 min | Strings, lists, and dictionaries                   |
| 4    | 45 min | Loops `for`, `range()`, `in`                       |
| 5    | 60 min | Funkcje, argumenty i `return`                      |
| 6    | 90 min | Independent exercises and review questions         |

## Required Theory [MUST]

### 1. Variables and Types

Learn:

- `str` — tekst;
- `int` — integers;
- `float` — floating-point numbers;
- `bool` — `True` / `False`;
- `None` — brak values;
- `type()` i basic conversions, np. `int("12")`;
- the difference between assignment `=` a comparison `==`.

Example:

```python
username = "tester"
attempts = 3
is_active = True

if attempts > 0 and is_active:
    print(f"User {username} can continue")
```

You should understand f-strings such as `f"..."`, indentation, comparisons, and the `and`, `or`, and `not` operators.

### 2. Strings and Collections

Learn:

- strings: `strip()`, `lower()`, `split()`, `in`, indeksowanie;
- lists: creation, indexing, `append()`, iteracja;
- dictionaries: klucze, values i odczyt danych;
- `len()`, `range()`, `enumerate()`;
- the difference between a list and a dictionary.

Example:

```python
users = ["anna", "jan", "ola"]

test_user = {
    "username": "anna",
    "active": True,
}

print(users[0])
print(test_user["username"])
```

### 3. Conditions, Loops, and Functions

Learn:

- `if`, `elif`, `else`;
- the `for` loop;
- basic use of `while`;
- `break` i `continue` — przynajmniej rozumienie;
- defining functions with `def`;
- parameters and arguments;
- `return` kontra `print`;
- lokalne variables i values zwracane przez funkcje.

Example:

```python
def is_valid_username(username):
    return len(username.strip()) >= 3


print(is_valid_username("anna"))
```

## Additional Theory [SHOULD]

- tuples (`tuple`) and sets (`set`);
- list comprehensions;
- default parameter values;
- truthiness and falsiness (`truthiness`);
- the difference between `is` and `==`—especially `is None`.

## Day 1 Resources

W `30 Days of Python` cover only these sections:

- [Day 1 — Introduction](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme.md)
- [Day 2 — Variables, Built-in Functions](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/02_Day_Variables_builtin_functions/02_variables_builtin_functions.md)
- [Day 3 — Operators](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/03_Day_Operators/03_operators.md)
- [Day 4 — Strings](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/04_Day_Strings/04_strings.md)
- [Day 5 — Lists](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/05_lists.md)
- [Day 8 — Dictionaries](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/08_Day_Dictionaries/08_dictionaries.md)
- [Day 9 — Conditionals](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/09_Day_Conditionals/09_conditionals.md)
- [Day 10 — Loops](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/10_Day_Loops/10_loops.md)
- [Day 11 — Functions](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/11_Day_Functions/11_functions.md)
- [Python Tutorial — oficjalna documentation](https://docs.python.org/3/tutorial/)

You do not need to complete every extensive course exercise. Choose the ones related to the topics listed here.

## Practical Exercises

Complete these in a separate file `day1_practice.py`.

### Task 1 — User Validation [MUST]

Write a function `is_valid_username(username)` that returns `True` if the name has at least 3 characters after whitespace is stripped. Otherwise, it returns `False`.

Check at least: `"anna"`, `"ab"`, `""`, `"  ola  "`.

### Task 2 — Data Filtering [MUST]

Given a list of usernames, create a new list containing only names that are at least 3 characters long. Do not remove elements from the original list.

### Task 3 — Test Data [MUST]

Create a dictionary representing a user with the fields `username`, `active`, and `role`. Write a function that returns `True` only when the user is active.

### Task 4 — Results List [SHOULD]

Given a list of test results, e.g. `["passed", "failed", "passed"]`, count how many results are `passed` and how many are `failed`.

## Review Questions

Before the end of the day, answer in your own words:

1. What is the difference between `=` od `==`?
2. What is the difference between `return` i `print()`?
3. How do you read the value of `username` from a dictionary?
4. How do you iterate przez wszystkie elementy lists?
5. What does `len("anna")`?
6. Why does indentation matter in Python?
7. What does a function return if it has no `return` statement?
8. How are `None` and `False` different?

## Day Completion Criteria

- [ ] I can write a simple function without copying an example.
- [ ] I can filter a list and read values from a dictionary.
- [ ] I understand conditions and loops.
- [ ] I can explain what every line of my code does.

---

# Day 2 — Practical Python and pytest

## Daily Goal

Prepare a project environment, split code across files, write function tests, and understand fixtures and parametrization.

## Schedule

| Blok | Time   | What to do                       |
| ---- | ------:| -------------------------------- |
| 1    | 30 min | Importy, pliki i traceback       |
| 2    | 30 min | `venv`, `pip`, and dependencies  |
| 3    | 60 min | Pierwsze tests pytest i `assert` |
| 4    | 60 min | Parametryzacja                   |
| 5    | 60 min | Fixtures i `conftest.py`         |
| 6    | 90 min | Exercises, errors, and review    |

## Required Theory [MUST]

### 1. Modules and Imports

Understand:

```python
from validators import is_valid_username
```

- a single `.py` file can be a module;
- an import makes functions and values from another module available;
- file and directory names affect imports;
- `requirements.txt` can describe project dependencies.

### 2. Exceptions and Tracebacks

Learn the basic meaning of:

- `SyntaxError` — a syntax problem;
- `NameError` — an undefined name was used;
- `TypeError` — operacja nie pasuje do typu;
- `ImportError` / `ModuleNotFoundError` — an import problem;
- `AssertionError` — an assertion was not satisfied.

Do not try to handle every exception immediately. First learn to read the message and identify the line it points to.

### 3. Virtual Environments

In Windows PowerShell, in a new practice directory:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pytest
```

If activation is blocked by the PowerShell execution policy, do not change system settings blindly. You can invoke the interpreter directly:

```powershell
.\.venv\Scripts\python.exe -m pip install pytest
.\.venv\Scripts\python.exe -m pytest -v
```

**If you already have a work repository:** use the Python version and dependency installation method specified by the project. Do not install or update global packages unnecessarily.

### 4. pytest Basics

Learn:

- pliki i funkcje testowe o namech rozpoznawanych przez pytest, np. `test_validators.py`, `test_username()`;
- `assert`;
- running `python -m pytest`;
- rozumienie `PASSED`, `FAILED`, `ERROR`;
- `@pytest.mark.parametrize`;
- `@pytest.fixture`;
- podstawy `conftest.py`.

## Additional Theory [SHOULD]

- `try`, `except`, `finally`, `raise`;
- reading and writing JSON files;
- `pathlib`;
- logging basics and diagnostic messages;
- a fixture using `yield` for test cleanup.

## Day 2 Resources

- [Python Day 12 — Modules](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/12_Day_Modules/12_modules.md)
- [Python Day 15 — Python Type Errors](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/15_Day_Python_type_errors/15_python_type_errors.md)
- [Python Day 17 — Exception Handling](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/17_Day_Exception_handling/17_exception_handling.md)
- [Python Day 20 — Python Package Manager](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/20_Day_Python_package_manager/20_python_package_manager.md)
- [Python Day 23 — Virtual Environment](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/23_Day_Virtual_environment/23_virtual_environment.md)
- [pytest — Getting Started](https://docs.pytest.org/en/stable/getting-started.html)
- [pytest — Assertions](https://docs.pytest.org/en/stable/how-to/assert.html)
- [pytest — Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [pytest — Parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html)
- [pytest — Usage](https://docs.pytest.org/en/stable/how-to/usage.html)

## Practice — Your First Project

Create `validators.py`:

```python
def is_valid_username(username):
    return len(username.strip()) >= 3


def is_valid_password(password):
    return len(password) >= 8
```

Create `test_validators.py`:

```python
from validators import is_valid_username, is_valid_password


def test_valid_username():
    assert is_valid_username("tester") is True


def test_invalid_username():
    assert is_valid_username("ab") is False


def test_valid_password():
    assert is_valid_password("password123") is True


def test_invalid_password():
    assert is_valid_password("abc") is False
```

Run:

```powershell
python -m pytest -v
```

Temporarily change one expected value to see a failing test. Restore the correct version after analyzing the result.

### Task 1 — Parametrization [MUST]

Replace separate username tests with one test using `@pytest.mark.parametrize` that checks at least four cases.

### Task 2 — Your Own Function and Tests [MUST]

Write a simple function that checks whether a string resembles an email address. A basic rule is enough, such as the presence of `@` and a dot after it—do not try to implement the entire email-address specification. Write positive and negative tests.

### Task 3 — Fixture [MUST]

Create a fixture that returns sample user data as a dictionary. Use it in at least two tests.

### Task 4 — Diagnostics [MUST]

Trigger each of the following and identify it:

- a syntax error;
- an undefined variable name;
- a failed assertion;
- niepoprawny import.

After each error, explain how you identified it.

## Review Questions

1. Why is `assert` useful in a test?
2. What is the difference between `FAILED` and `ERROR` in pytest output?
3. What does `@pytest.mark.parametrize`?
4. Co to jest fixture i jak test z niej korzysta?
5. What is `conftest.py`?
6. Why is it useful to run `python -m pytest`?
7. Co zapewnia `venv`?
8. How do you find the relevant line in a traceback?

## Day Completion Criteria

- [ ] I can create and use a virtual environment.
- [ ] I can run a single test file.
- [ ] I understand `assert`, fixtures, and parametrization.
- [ ] I can explain the cause of a simple error using its traceback.

---

# Day 3 — Playwright Fundamentals

## Daily Goal

Write a browser test that opens a page, finds elements, performs actions, and verifies the result.

## Schedule

| Blok | Time   | What to do                                  |
| ---- | ------:| ------------------------------------------- |
| 1    | 30 min | Instalacja i uruchomienie exampleowego test |
| 2    | 60 min | `page`, nawigacja i locatory                |
| 3    | 60 min | Akcje i interakcje z formularzem            |
| 4    | 60 min | Asercje Playwright                          |
| 5    | 45 min | Auto-waiting i timeouty                     |
| 6    | 90 min | Samodzielny scenariusz testowy              |

## Required Theory [MUST]

### 1. Installation

In a fresh practice environment:

```powershell
python -m pip install pytest-playwright
python -m playwright install chromium
```

Then run the test:

```powershell
python -m pytest -v
```

Playwright recommends its official pytest integration for end-to-end tests. If the target project already has its own dependencies, follow its configuration instead of automatically installing newer versions.

### 2. Core Objects

Understand the difference between:

- `page` — a browser tab/page;
- `locator` — sposobem wskazania elementu;
- `browser` — a browser instance;
- `context` — an isolated context, e.g. a session with its own cookies;
- fixture `page` — an object provided by the pytest-playwright integration.

### 3. Locators

Learn robust locators first:

```python
page.get_by_role("button", name="Log in")
page.get_by_label("Username")
page.get_by_text("Welcome")
page.get_by_placeholder("Enter username")
page.locator("[data-testid='submit']")
```

Prefer roles, labels, and stable test attributes when available. Avoid fragile selectors based on long DOM paths.

### 4. Actions and Assertions

Common actions:

```python
locator.click()
locator.fill("example")
locator.check()
locator.select_option("option-value")
```

Common assertions:

```python
from playwright.sync_api import expect

expect(locator).to_be_visible()
expect(locator).to_have_text("Welcome")
expect(page).to_have_url("https://example.com/")
```

Playwright assertions generally wait automatically for the expected state within the timeout. This is better than adding fixed delays.

### 5. What to Avoid

- `time.sleep()` jako podstawowej metody synchronizacji;
- clicking an element before confirming that the locator identifies the correct element;
- checking the result only with `print()`;
- using `force=True` without justification;
- basing tests on screen coordinates.

## Additional Theory [SHOULD]

- the difference between `get_by_role()` and `locator()`;
- handling checkboxes, radio buttons, and dropdowns;
- checking the URL, title, text, and visibility;
- screenshot basics;
- opening new tabs, dialogs, and frames—only if they are relevant to your tasks.

## Day 3 Resources

- [Playwright Python — Installation / Introduction](https://playwright.dev/python/docs/intro)
- [Playwright — Writing Tests](https://playwright.dev/python/docs/writing-tests)
- [Playwright — Locators](https://playwright.dev/python/docs/locators)
- [Playwright — Assertions](https://playwright.dev/python/docs/test-assertions)
- [Playwright — Auto-waiting / Actionability](https://playwright.dev/python/docs/actionability)
- [Playwright Python — Page API](https://playwright.dev/python/docs/api/class-page)
- [pytest-playwright — GitHub](https://github.com/microsoft/playwright-pytest)

## Practice — Your First Browser Test

Create `test_browser.py`:

```python
from playwright.sync_api import Page, expect


def test_example_page(page: Page):
    page.goto("https://example.com")

    heading = page.get_by_role("heading", name="Example Domain")

    expect(heading).to_be_visible()
    expect(page).to_have_title("Example Domain")
```

Run:

```powershell
python -m pytest -v
```

In this example, the `page` fixture is provided by pytest-playwright. You do not need to launch or close the browser yourself.

### Task 1 — Navigation and Assertions [MUST]

Write a test that:

1. Otwiera `https://example.com`.
2. Checks the page title.
3. Checks that the heading is visible.
4. Checks the heading text.
5. Checks that the “More information...” link is visible.

### Task 2 — Form [MUST]

Choose a test application that you are authorized to test. Write a scenario that:

1. otwarcie page;
2. finds the form fields;
3. wpisanie danych;
4. clicks the button;
5. checks the message or final state.

Match the locators to the actual HTML and page labels.

### Task 3 — Fix an Error [MUST]

Intentionally enter an incorrect locator name. Run the test and determine:

- which locator failed;
- which element was expected;
- how to confirm the correct element name/role;
- how to fix the test without adding a fixed delay.

### Task 4 — Additional Interactions [SHOULD]

If you have time, test a checkbox or dropdown and verify the element's state using `expect()`.

## Review Questions

1. How are `page` and `locator` different?
2. Why is `get_by_role()` often better than a fragile CSS selector?
3. What does `fill()` do, and how is it different from `click()`?
4. Why is `expect()` used?
5. Co to jest auto-waiting?
6. Why do fixed `sleep` calls often make tests unstable?
7. Where does the `page` fixture come from?
8. How can you determine whether an error concerns the locator or the expected result?

## Day Completion Criteria

- [ ] I can write and run a test using `page`.
- [ ] I can identify an element using a locator.
- [ ] I can perform an action and verify the result with an assertion.
- [ ] I understand basic locator errors and timeouts.

---

# Day 4 — struktura tests, fixtures i debugging

## Daily Goal

Understand how tests are organized in a repository and extend existing code in accordance with the project's conventions.

## Schedule

| Blok | Time   | What to do                                     |
| ---- | ------:| ---------------------------------------------- |
| 1    | 45 min | Review the target repository                   |
| 2    | 45 min | Fixtures i `conftest.py`                       |
| 3    | 45 min | Test data i parametryzacja                     |
| 4    | 60 min | Debugging locators and timeouts                |
| 5    | 45 min | Struktura tests i ewentualny Page Object Model |
| 6    | 90 min | Implementing two scenarios                     |

## Required Theory [MUST]

### 1. Understand the Repository Before Making Changes

If you have an existing project, identify:

- where the tests are located;
- how test files and functions are named;
- how dependencies are installed;
- czy istnieje `pytest.ini`, `pyproject.toml` lub inna konfiguracja;
- where fixtures are defined;
- czy projekt korzysta z Sync API czy Async API;
- how the application URL, login credentials, and other parameters are configured;
- how to run a single test and the full suite.

Do not change the configuration, package versions, or architecture without a reason.

### 2. Fixtures and `conftest.py`

A fixture prepares and shares resources or data between tests. `conftest.py` can make fixtures available to tests within a directory scope.

Learn:

- jak test otrzymuje fixture przez argument funkcji;
- how a fixture's scope works;
- when `yield` is used for resource cleanup;
- why tests should be as independent as possible.

### 3. Debugging

When a test fails, check the following in order:

1. Which test failed?
2. Jaka jest pierwsza istotna linia tracebacku?
3. Does the locator identify the correct element?
4. Has the page reached the expected state?
5. Czy assertion odpowiada wymaganiu biznesowemu?
6. Are the data and session state correct?
7. Does the error recur on the next run?

Do not increase the timeout as your first response. First determine why the element or state did not appear in time.

## Additional Theory [SHOULD]

- Page Object Model—if the project uses it or it helps reduce repeated code;
- logowanie i screenshoty;
- trace viewer;
- running tests by markers;
- configuring settings through environment variables;
- basics of `pathlib` and JSON files for test data.

## Day 4 Resources

- [pytest — Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [pytest — Good Integration Practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html)
- [pytest — Usage](https://docs.pytest.org/en/stable/how-to/usage.html)
- [Playwright — Debugging](https://playwright.dev/python/docs/debug)
- [Playwright — Trace Viewer](https://playwright.dev/python/docs/trace-viewer)
- [Playwright — Page Object Model](https://playwright.dev/python/docs/pom)
- [Playwright — Locators](https://playwright.dev/python/docs/locators)

## Practical Exercises

### Task 1 — Explore the Project [MUST]

In the target repository, find and describe:

- plik konfiguracyjny;
- one existing test;
- one fixture;
- how the application URL is provided;
- the command used to run a single test.

If you do not have a repository yet, complete this exercise in your practice project.

### Task 2 — Two Scenarios [MUST]

Implement two tests for a feature in the application under test, such as login:

- scenariusz pozytywny;
- scenariusz negatywny.

In both cases, assertions should verify a specific result, not merely that a button was clicked.

### Task 3 — Parametrization [SHOULD]

If scenarios differ only in input data and expected results, consider `@pytest.mark.parametrize`. Do not force together cases that require completely different setup.

### Task 4 — Diagnostics [MUST]

Run a test that is intentionally designed to fail, then:

- odczytaj traceback;
- find the cause;
- popraw kod;
- ponownie uruchom test;
- check whether the other tests still pass.

### Task 5 — Test Isolation [SHOULD]

Run tests in a different order or individually. Check whether any test depends on another test having run first.

## Review Questions

1. Why is a fixture better than duplicating setup in every test?
2. What is `conftest.py`?
3. What can cause a timeout in Playwright?
4. Why should you not increase the timeout immediately?
5. What does it mean for tests to be independent?
6. When is parametrization useful?
7. What can the Page Object Model be used for?
8. What information can you get from the Trace Viewer?

## Day Completion Criteria

- [ ] I can find the project's configuration and fixtures.
- [ ] I can add a test without unnecessarily changing the architecture.
- [ ] I can diagnose a failed test.
- [ ] I can run a single test and a larger test suite.

---

# Day 5 — Implementing Tests in the Target Project

## Daily Goal

Complete the required scenarios, run them reproducibly, and explain what each test verifies.

## Schedule

| Blok | Time        | What to do                                   |
| ---- | -----------:| -------------------------------------------- |
| 1    | 30 min      | Przejrzyj wymagania i wypisz scenariusze     |
| 2    | 45 min      | Run existing tests and check the environment |
| 3    | 120–180 min | Implementuj wymagane scenariusze             |
| 4    | 45 min      | Debuguj errors i popraw assertions           |
| 5    | 45 min      | Run the full suite and check reproducibility |
| 6    | 30 min      | Record the result and unresolved issues      |

## Required Theory [MUST]

Do not start a major new topic today. Refer back to these resources when needed:

- [Playwright Locators](https://playwright.dev/python/docs/locators);
- [Playwright Assertions](https://playwright.dev/python/docs/test-assertions);
- [Playwright Debugging](https://playwright.dev/python/docs/debug);
- [pytest Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html);
- [pytest Usage](https://docs.pytest.org/en/stable/how-to/usage.html).

## Execution Plan

### Step 1 — Break Requirements into Scenarios

For each requirement, record:

- **Preconditions** — what state must exist before the test?
- **Input data** — what data will you use?
- **Steps** — what actions will the test perform?
- **Expected result** — what exactly must be verified?
- **Cleanup** — does the test change state that must be restored?

### Step 2 — Prepare the Test

Before coding, determine:

- the correct locator;
- the user action;
- an assertion that matches the requirement;
- the source of test data;
- how to run the test.

### Step 3 — Implement in Small Steps

After adding each scenario:

1. uruchom go samodzielnie;
2. check the result;
3. popraw errors;
4. uruchom ponownie;
5. only then move on to the next one.

### Step 4 — Verify the Test Suite

Check that:

- whether all required tests are discovered;
- whether tests pass individually;
- whether they work as a suite;
- whether they depend on execution order;
- whether they use unnecessary fixed delays;
- whether assertions check actual results;
- whether errors are readable and diagnosable.

### Step 5 — Report

Record:

- the number of passed and failed tests;
- znane errors;
- any environment issues;
- what has been completed;
- co wymaga dalszej pracy.

Do not hide failures by disabling tests or weakening assertions just to get a green result.

## Final Task

For every required scenario, you should be able to answer:

1. What exactly does this test verify?
2. Why wybrano ten locator?
3. Co oznacza assertion?
4. What conditions must be met for the test to pass?
5. What will I do if the test starts failing intermittently?

## Day Completion Criteria

- [ ] All required scenarios have implemented tests or a clearly documented blocker.
- [ ] I can run a single test and the full suite.
- [ ] I understand the assertions and data used in each scenario.
- [ ] I can identify the cause of the most important errors.
- [ ] I have documented execution status and remaining issues.

---

# Final Skills Checklist

Check an item only when you can do it without copying a ready-made solution.

## Python

- [ ] I understand podstawowe typy danych i variables.
- [ ] I can write conditions and loops.
- [ ] I can work with lists and dictionaries.
- [ ] I can write a function and use `return`.
- [ ] I can import functions from another file.
- [ ] I can read basic tracebacks.
- [ ] I understand virtual environments and dependency installation.

## pytest

- [ ] I can write and run a test.
- [ ] I understand `assert`.
- [ ] I can use `@pytest.mark.parametrize`.
- [ ] I understand fixtures i argumenty tests.
- [ ] I know what `conftest.py`.
- [ ] I can run a single test and the full suite.

## Playwright

- [ ] I understand the roles of `page` and `locator`.
- [ ] I can choose a stable locator.
- [ ] I can fill in a form and click a button.
- [ ] I can verify text, visibility, and the URL.
- [ ] I understand auto-waiting.
- [ ] I can recognize a basic locator error or timeout.
- [ ] I can debug a test and explain its result.

## Praca projektowa

- [ ] I can find tests and configuration in the repository.
- [ ] I can add a scenario in accordance with existing conventions.
- [ ] I can run tests after making changes.
- [ ] I can document known issues without hiding failures.

---

# Glossary

| Term            | Meaning                                                        |
| --------------- | -------------------------------------------------------------- |
| Variable        | A name associated with a value                                 |
| Data type       | A kind of value, e.g. text, a number, or a Boolean value       |
| Function        | A reusable block of code that can be called                    |
| Argument        | A value passed when calling a function                         |
| `return`        | Returns a result from a function                               |
| Module          | A Python file that can contain functions and other definitions |
| Exception       | An error or special condition raised while a program runs      |
| `venv`          | An isolated Python environment for a project                   |
| Test            | Code that checks specific behavior                             |
| Assertion       | A check that a result matches expectations                     |
| Fixture         | A shared mechanism for preparing test data or resources        |
| Parametrization | Running a similar test with different data sets                |
| Locator         | A way to identify a page element                               |
| `page`          | An object representing a page/tab in Playwright                |
| Timeout         | The maximum time to wait for an operation or state             |
| E2E             | A test covering a user flow through an application             |
| Trace           | A record of test execution used to analyze failures            |

---

# Further Resources

Study these only when they are needed for your project or after you have mastered the most important topics.

- [Python — Classes and Objects w 30 Days of Python](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/21_Day_Classes_and_objects/21_classes_and_objects.md)
- [Python — Regular Expressions](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/18_Day_Regular_expressions/18_regular_expressions.md)
- [Python — File Handling](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/19_Day_File_handling/19_file_handling.md)
- [Python — List Comprehension](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/13_Day_List_comprehension/13_list_comprehension.md)
- [pytest — parametrized fixtures i zaawansowane fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [Playwright — Authentication](https://playwright.dev/python/docs/auth)
- [Playwright — Network](https://playwright.dev/python/docs/network)
- [Playwright — Screenshots](https://playwright.dev/python/docs/screenshots)
- [Playwright — API testing](https://playwright.dev/python/docs/api-testing)

## What Not to Prioritize During These Five Days

Unless your project requires them, postpone:

- advanced object-oriented programming;
- custom decorators and generators;
- asynchronous programming in depth;
- Pandas, NumPy i data analysis;
- building web applications with Django or Flask;
- advanced algorithms and data structures;
- setting up CI/CD from scratch.

## Final Principle

**Measure progress by working code, not by the number of chapters read.** The most important outcome of these five days is being able to write a test, understand its assertions, run it, and diagnose a failure.
