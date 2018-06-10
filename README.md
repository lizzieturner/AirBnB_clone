# AirBnB Clone - The Console

![air bnb clone](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png)


## Table of Contents

* [Description](#description)
* [Purpose](#purpose)
* [Requirements](#requirements)
* [File Structure](#file-structure)
* [Usage Examples](#usage-examples)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)


## Description

description here

## Purpose

The purpose of this project is to understand how to:   
* create a Python package   
* create a command interpreter using the `cmd` module   
* serialize and deserialize a Class   
* write and read a JSON file   
* manage `datetime`   
* use `*args` and `**kwargs`   
* handle named arguments in a function   

## Requirements

### PYTHON SCRIPT REQUIREMENTS  
   * allowed editors: `vi`, `vim`, `emacs`   
   * the first line of all files should be exactly `#!/usr/bin/python3`   
   * all code should use the `PEP8` style (version 1.7.*)   
   * all files must be executable   
   * all files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)   

### PYTHON TEST CASE REQUIREMENTS    
   * all test files should be in the folder `tests`   
   * all test files should be text files (extension: `.txt`)   
   * all test files should be executed using the command `python3 -m doctest ./tests/*`   
   * all modules should have documentation `python3 -c 'print(__import__("my_module").__doc__)'`   
   * all functions (inside and outside of classes) should have documentation `python3 -c 'print(__import__("my_module").my_funct\
ion.__doc__)'`   

## File Structure

* [AUTHORS](AUTHORS) - list of contributors   
* []() -   
* []() -   
* []() -   

## Usage Examples

### Interactive Mode

```python3
~/me$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
~/me$
```

### Non-Interactive Mode

```python3
~/me$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)

~/me$ cat test_help
help
~/me$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
~/me$
```

## Bugs

At this time, there are no known bugs.


## Authors

Lizzie Turner | [GitHub](https://github.com/lizzieturner) | [Twitter](https://twitter.com/_lizzieturner_)   
Sonia Chevli | [GitHub](https://github.com/SoniaChevli) | [Twitter](https://twitter.com/SuperSaiyanSone)

## License

**AirBnB Clone** is open source and free to download and use
