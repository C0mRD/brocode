<p align="center">
  <a href="" rel="noopener">
<<<<<<< Updated upstream
 <img width=300px height=100px src="brocode.jpg" alt="Project logo"></a>
</p>

<h3 align="center">BroCode</h3>
=======
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Project Title</h3>
>>>>>>> Stashed changes

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
<<<<<<< Updated upstream
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/C0mRD/broCode/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/C0mRD/broCode/pulls)
=======
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
>>>>>>> Stashed changes

</div>

---

<<<<<<< Updated upstream
<p align="center"> A tiny programming language based on inside jokes
=======
<p align="center"> Few lines describing your project.
>>>>>>> Stashed changes
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
<<<<<<< Updated upstream
- [Documentation](#documentation)
- [TODO](#todo)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

BroCode is a tiny programming language built using Antlr4 Python3 runtime, it includes all the essential features of any modern day programming language. But what sets broCode apart is its use of regional language(bengali) words as tokens. BroCode is available for you to explore and if you want to build your own programming language, brocode is perfect to take the inspiration.


## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites <a name = "prerequisites"></a>

Python3 is need to be pre-installed to run brocode. Also install requirements via pip.

```
pip install -r requirements.txt
=======
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

Write about 1-2 paragraphs describing the purpose of your project.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
Give examples
>>>>>>> Stashed changes
```

### Installing

<<<<<<< Updated upstream
Install brocode binary release from <a href="https://github.com/C0mRD/broCode/releases/tag/v1.0">here.</a>

To get the source code for development purpose clone this repository via git or download as a zip file from github.

```
git clone https://github.com/C0mRD/broCode
```

<b>Windows</b>

Download the brocode binary release for windows first. Run brocode.exe file with the input filename as an argument.

```
brocode code.bro
```

<b>Linux</b>

Install all the [prerequisites](#prerequisites) first. Download zip file for linux from the release. Give the brocode file permission to execute.

```
chmod +x brocode
```

Run brocode file in terminal with the input filename as an argument.

```
brocode code.bro
```

To get more brocode example files see the example folder.

## 🎈 Documentation <a name="documentation"></a>

### General

```start bro``` is the entrypoint for the program and all program must end with ```stop bro``` . Anything outside of it will be ignored.

```
start bro

stop bro
```

### Built-ins

Use ```bol bro``` to print anything to console.

```
start bro
 bol bro 'Hello World';
stop bro
```

### Variables

Variables can be declared or assigned using ```->``` operator.

```
start bro
 a -> 10;
 b->12;
 a->b;
stop bro
```

### Types

Supports  ```int``` , ```float``` , ```string``` types.

```
start bro
 a->10;
 b->8.5;
 c-> 'hello';
stop bro
```

### Conditionals

BroCode supports if-else-if ladder construct , ```jodi bro``` will execute if condition, ```jodi na bro``` equivalet to elseif and ```na hole bro``` equivalent to else.

```
start bro
a -> 12;
b -> 10;
jodi bro a<b{
  bol bro 'less';
}
jodi na bro a==b{
  bol bro 'equal';
}
na hole bro{
  bol bro 'greater';
}
stop bro
```

### Loops

Statements inside ```jotokhon bro``` blocks are executed as long as a specified condition evaluates to true.

```
start bro
a -> 12;
b -> 20;
jotokhon bro a<b{
  bol bro a;
  a -> a+1;
}
stop bro
```

## 🚀 Todo <a name = "todo"></a>

- [x] Variables (int, float, string)
- [x] Binary operations
- [x] Conditionals
- [x] Loops
- [x] Output to console

- [ ] I/O Operations
- [ ] Functions
- [ ] User-defined data types
- [ ] Import statements


## ⛏️ Built Using <a name = "built_using"></a>

- [Antlr4](https://www.antlr.org/) - Lexer & Parser
- [Python3](https://www.python.org/) - Interpreter
- [React.js](https://reactjs.org/) - Website frontend
- [Flask](https://flask.palletsprojects.com/) - Backend server

## ✍️ Authors <a name = "authors"></a>

- [@c0mrd](https://github.com/c0mrd) - Idea & Initial work
=======
A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo.

## 🔧 Running the tests <a name = "tests"></a>

Explain how to run the automated tests for this system.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## 🎈 Usage <a name="usage"></a>

Add notes about how to use the system.

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [MongoDB](https://www.mongodb.com/) - Database
- [Express](https://expressjs.com/) - Server Framework
- [VueJs](https://vuejs.org/) - Web Framework
- [NodeJs](https://nodejs.org/en/) - Server Environment

## ✍️ Authors <a name = "authors"></a>

- [@kylelobo](https://github.com/kylelobo) - Idea & Initial work

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
>>>>>>> Stashed changes
