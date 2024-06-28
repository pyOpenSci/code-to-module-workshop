# pyOpenSci: Code to module workshop -- Create your first Python package

![pyOpenSci Logo](pyopensci-logo-dark-mode.png)

## About

Creating code that can be shared and reused is the pinnacle of open science.
But tools and skills to share your code can be tricky to learn. In this
hands-on tutorial, you’ll learn how to turn your code into an installable
Python module that can be shared with others. To get the most out of this
tutorial, you should be familiar with writing Python code, Python environments
and functions.

You will leave this tutorial understanding how to:

* Create code that can be installed into different environments
* Use Hatch as a workflow tool, making setup and installation of your code easier
* Use Hatch to publish your package to (test) PyPI

## What this repo contains

This is a public repo that contains the scripts and information used in the
code-to-module training.

[Click here to see a detailed overview of the workshop agenda.](#TODO-link-to-jesse-post)

## What you need to install

For this workshop, you’ll need the following installed on your computer prior
to attending:

* Python
* An environment manager
* [Hatch](https://www.pyopensci.org/python-package-guide/tutorials/get-to-know-hatch.htmlhttps://www.pyopensci.org/python-package-guide/tutorials/get-to-know-hatch.html)
* A terminal or shell where you can call Python and enter terminal commands such as `hatch --version` (see below)
* A code editor where you can edit `.py` files.
* Optional: download / clone this workshop repository

Your instructor will be teaching using VSCode with the Python extension installed. Vscode has an integrated terminal. You do not need to use VScode to be successful in 
this training! 

## Download (or clone) our example code repo

You should download or clone
[this repo](https://github.com/pyOpenSci/code-to-module-workshop) which
contains sample code for you to use during the
workshop. If you are not comfortable with using Git / GitHub you can download a
zip file of the code-to-module repo from GitHub (see image below).

## Hatch & Python

If you already have a working version of Python on your computer, then you are in good shape!**If you don’t have Python installed on your computer, then Hatch will install Python for you when you install it following the instructions below.**

## Install Hatch

_These instructions were adapted from the [Introduction to hatch](https://www.pyopensci.org/python-package-guide/tutorials/get-to-know-hatch.html) section of the [pyOpenSci Python Packaging Guide](https://www.pyopensci.org/python-package-guide/)._

### For Mac users

_These instructions are for installing Hatch using the GUI installer. If you’d prefer to use the Command line installer, please see the [Hatch documentation](https://hatch.pypa.io/latest/install/#command-line-installer)._

1. In your browser, download the `.pkg` file: [hatch-universal.pkg](https://github.com/pypa/hatch/releases/latest/download/hatch-universal.pkg)
2. Run the downloaded file and follow the on-screen instructions to install Hatch.
3. Restart your terminal if it is already open.
4. To verify that shell can find and run the `hatch` command, run:
    1. `hatch --version` (in your Terminal / shell).

### For Linux users

_For linux users, the easiest way to install Hatch is to use pipx which can be installed using apt install. Note: if you prefer to use a tool other than pipx, please refer to the [Hatch documentation](https://hatch.pypa.io/latest/) for more information_

* Install hatch from the command line using [pipx](https://pipx.pypa.io/stable/):  

```bash
# First install pipx using apt install
>> apt install pipx
# Then use pipx to install hatch
>> pipx install hatch
```

### For Windows users

_These instructions are for installing Hatch using the GUI installer. If you’d prefer to use the Command line installer, please see the [Hatch documentation](https://hatch.pypa.io/latest/install/#command-line-installer_1)._

1. In your browser, download the `.msi` file: [hatch-x64.msi](https://github.com/pypa/hatch/releases/latest/download/hatch-x64.msi)
2. Run your downloaded file and follow the on-screen instructions.
3. Restart your terminal if it was already open.
4. To verify that the shell can find and run the `hatch` command in your `PATH`, in your terminal run:
    1. `hatch --version`

### Configure Hatch (all systems)

After installing Hatch, it’s useful to customize the Hatch configuration. The
configuration allows you to specify things like the default name and email to
use in your package’s metadata. If you don’t configure Hatch, you can always
edit files later! However your Hatch package outputs might look a bit different
than the ones in the workshop. (This is ok!)

Hatch stores your configuration information in a `config.toml` file.

While you can update the `config.toml` file through the command line, it might
be easier to look at it and update it in a text editor if you are using it for
the first time.

1. Open and edit your `config.toml` file by either:
    1. Running `hatch config explore` in your shell, which will open up a directory window that will allow you to double click on the file and open it in your favorite text editor.
    2. Alternatively, you can retrieve the location of the Hatch config file by running `hatch config find` in your shell.
2. Update your email and name
    3. Once the file is open, update the [template] table of the `config.toml` file with your name and email. This information will be used in any `pyproject.toml` metadata files that you create using Hatch.
3. Set tests to `false`

    _While tests are important, setting the tests configuration in Hatch to true will create a more complex pyproject.toml file. We won’t be creating tests in this workshop._

    Set tests to `false` in the `[template.plugins.default]` table.

Your config file should look something like this:

```toml
mode = "local"
project = ""
shell = ""

[dirs]
project = []
python = "isolated"
data = "/Users/leahawasser/Library/Application Support/hatch"
cache = "/Users/leahawasser/Library/Caches/hatch"

[dirs.env]

[projects]

[publish.index]
repo = "main"

[template]
name = "Leah Wasser"
email = "leah@pyopensci.org"

[template.licenses]
headers = true
default = [
    "MIT",
]

[template.plugins.default]
tests = false
ci = false
src-layout = true

[terminal.styles]
info = "bold"
success = "bold cyan"
error = "bold red"
warning = "bold yellow"
waiting = "bold magenta"
debug = "bold"
spinner = "simpleDotsScrolling"
```

Note: for future packages you may want to enable both CI and tests. This
configuration is to simplify things for our beginner-friendly tutorial.

4. Close the config file and run `hatch config show`

    `hatch config show`

This command prints out the contents of your config.toml file in your shell.
Look at the values and ensure that your name and email are set and also make
sure that `tests=false`.

## Useful Commands

### Conda environments

* **Create environment:** `conda create -n env_name python=3.11`
* **Activate environment:** `conda activate env_name`
* **Leave environment:** `conda deactivate`

### Venv environments

Create environment

* `python -m venv env_name`
* Activate_windows: `env_name\Scripts\activate`
* Activate MAC / LINUX: `source env_name/bin/activate`
* Leave environment: `deactivate`
