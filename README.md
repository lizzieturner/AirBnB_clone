# AirBnB Clone

![air bnb clone](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJIMMWEC6CH2PXSCQ%2F20180610%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20180610T222756Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4d16d04066eccf8a6a7bd8f44c3e0148ab5c3fcb1fabd4f99e34c96c2acb2df4)


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
