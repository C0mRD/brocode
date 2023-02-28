<p align="center">
  <a href="" rel="noopener">
 <img width=300px height=100px src="brocode.jpg" alt="Project logo"></a>
</p>

<h3 align="center">BroCode</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/C0mRD/broCode/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/C0mRD/broCode/pulls)

</div>

---

<p align="center"> A tiny programming language based on inside jokes
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
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
```

### Installing

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
