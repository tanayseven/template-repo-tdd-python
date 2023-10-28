# TDD workshop template repository

## How to set up the repository

1. Install latest [Python (3.12 as of writing this)](https://www.python.org/)
2. Make sure the commands `python` and `pip` works from the command line/terminal
3. If the above commands are not working, make sure you [add it to the path](https://realpython.com/add-python-to-path/)
4. Install [Git](https://git-scm.com/)
5. Clone this repository run in cmd/terminal `git clone https://github.com/tanayseven/template-repo-tdd-python.git`
6. Install an IDE/Text Editor, [VSCode](https://code.visualstudio.com/) with [Python Extension](https://code.visualstudio.com/docs/languages/python) or install [Pycharm Community Edition](https://www.jetbrains.com/pycharm/)
7. Open the cloned directory in cmd/terminal `python -m venv venv`
8. Activate the above created virtual environment `. ./venv/bin/activate` for Linux/Mac OS and run `\venv\Scripts\activate` for Windows
9. Install the dependencies `pip install -r requirements.txt`
10. Then run the tests `pytest`
11. If the above command works, you should get an output similar to the following, then you should be set to go

```text
================================================================================================== test session starts ===================================================================================================
platform linux -- Python 3.11.5, pytest-7.4.3, pluggy-1.3.0
rootdir: /home/tanay/repos/template-repo-tdd-python
collected 1 item                                                                                                                                                                                                         

test/test_main.py .                                                                                                                                                                                                [100%]

=================================================================================================== 1 passed in 0.01s ====================================================================================================
```
