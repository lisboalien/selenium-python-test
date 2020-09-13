# selenium-python-test
This repository contains the merge of the ideas learned in 
*Introduction to Selenium WebDriver with Python* course
and *Behavior-Driven Python with pytest-bdd* course
taught by [Andrew "Pandy" Knight](https://twitter.com/AutomationPanda)
on [Test Automation University](https://testautomationu.applitools.com/)

So it is basicaly a project using BDD and page steps tests using Python and Selenium Webdriver.

# Setup Instructions

## Python Setup

This project requires Python 3.8 or higher.
You can download the latest Python version from [Python.org](https://www.python.org/downloads/).

This project also requires [pipenv](https://docs.pipenv.org/).
To install pipenv, run `pip install pipenv` from the command line.

## WebDriver Setup

For Web UI testing, you will need to install the latest versions of
[Google Chrome](https://www.google.com/chrome/)
and [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/).
You can use other browsers with Selenium WebDriver, but the project will use Chrome and Firefox.

You will also need to install the latest versions of the WebDriver executables for these browsers: [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for Chrome
and [geckodriver](https://github.com/mozilla/geckodriver/releases) for Firefox.
Each test case will launch the WebDriver executable for its target browser.
The WebDriver executable will act as a proxy between the test automation and the browser instance.
Please use the latest versions of both the browsers and the WebDriver executables.
Older versions might be incompatible with each other.

ChromeDriver and geckodriver must be installed on the
[system path](https://en.wikipedia.org/wiki/PATH_(variable)).

### WebDriver Setup for Windows

To install ChromeDriver and geckodriver on Windows:

1. Create a folder named `C:\Selenium`.
2. Move the executables into this folder.
3. Add this folder to the *Path* environment variable. (See [How to Add to Windows PATH Environment Variable](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/).)

### WebDriver Setup for *NIX

To install ChromeDriver and geckodriver on Linux, macOS, and other UNIX variants,
simply move them to the `/usr/local/bin/` directory:

```bash
$ mv /path/to/ChromeDriver /usr/local/bin
$ mv /path/to/geckodriver /usr/local/bin
```

This directory should already be included in the system path.
For troubleshooting, see:

* [Setting the path on macOS](https://www.cyberciti.biz/faq/appleosx-bash-unix-change-set-path-environment-variable/)
* [Setting the path on Linux](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix)

### Test WebDriver Setup

To verify correct setup on any operating system, simply try to run them from the terminal:

```bash
$ ChromeDriver
$ geckodriver
```

You may or may not see any output.
Just verify that you can run them without errors.
Use Ctrl-C to kill them.

## Project Setup

1. Clone this repository.
2. Run `cd selenium-python-test` to enter the project.
3. Run `pipenv install` to install the dependencies.
4. Run `pipenv run python -m pytest` to verify that the framework can run tests.
5. Create a branch for your code changes. (See *Repository Branching* below.)

## About the Author

This project is made by **Aline de Farias Lisboa** or "lisboalien" in social media.

* Twitter: [@Lisboalien](https://twitter.com/Lisboalien)
* LinkedIn: [Aline Lisboa](https://www.linkedin.com/in/alinelisboa/)
