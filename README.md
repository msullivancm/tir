# tir
Projetos TIR. Automação Protheus.
TIR - Test Interface Robot

GitHub release (latest by date)

TIR is a Python module used to create test scripts for web interfaces. With it, you can easily create and execute test suites and test cases for any supported web interface systems, such as Protheus Webapp.
Current Supported Technologies

    Protheus Webapp
    APW

Table of Contents

Documentation
Installation
Config
Usage
Samples
Contact Us
Contributing
Documentation

Our documentation can be found here:

    TIR Documentation

    TIR Technical Documentation

This project has a docs folder with Sphinx files.

Our create_docs.cmd script handles the installation of dependencies and creates the offline documentation on doc_files/build/html folder.
Installation

The installation is pretty simple. All you need as a requirement is Python 3.7.9 (Mozilla Firefox) installed in your system.

There are three ways of installing TIR:
1. Installing and Upgrade from PyPI

TIR can ben installed via pip from Pypi

pip install tir_framework --upgrade

2. via Terminal(Deprecated For The Branch Master)

You can install TIR via terminal. Make sure your Python and Git are installed and run this command:

pip install git+https://github.com/totvs/tir.git --upgrade

It will install the last release of TIR in the active Python instance.
Config

The environment must be configured through a config.json file. You can find one to be used as a base in this repository. To select your file, you can either put it in your workspace or pass its path as a parameter of any of our classes' initialization.
Config options

Here you can find all the supported keys: Config.json keys
Custom config path

Just pass the path as a parameter in your script:
Protheus WebApp Class example:

#To use a custom path for your config.json
test_helper = Webapp("C:\PATH_HERE\config.json")

Usage

After the module is installed, you could just import it into your Test Case. See the following Protheus WebApp Class example:

# Import from our package the class you're going to use
from tir import Webapp

test_helper = Webapp()
test_helper.Setup('SIGAGCT','10/08/2017','T1','D MG 01 ','05')
test_helper.Program('CNTA010')

test_helper.SetButton('Cancelar')
test_helper.AssertTrue()

test_helper.TearDown()

Samples

We have a repository with different samples of TIR scripts:

TIR Script Samples
Contact

Gitter
Contributing

To contribute be sure to follow the Contribution guidelines.

Also, it's important to understand the chosen architecture.
