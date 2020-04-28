# RTR108
RTU Computer Studies Repository that will be used in order to upload codes which are going to be developed in classes.

## Structure of Directories

### Python

In python folder we can find many tests and scripts which can help with basics of the language and syntax and general. It is divided in some sub-directories:

1. *basics_of_python* - First steps in the language
2. *diaries* - Diaries of commands in *Idle*
3. *list_exercises* - Practice with lists and functions and python
4. *test_python* - Test done in class

### Circuit Simulation

This folder stores all files and scripts generated by *Qucs* and *ngspice* software simulators.

- Files with *.sch* extension are the ones generated by *gschem* or *Qucs* when you draw a circuit.
- Files with *.net* extension are the ones generated by *gnetlist* in order to simulate numeric values on *ngspice*

Example of *.net* file:
```
v1 0 n0 SIN(0 10 100000Hz)
.INCLUDE ./Simulation.cmd
R1 0 n1 1k
C1 n0 n1 3.3nF
.end
```

### Latex

In Latex folder, we store all the reports developed using *Overleaf* platform. There you can see *.pdf* report and the source *Latex* code developed in order to generate the report.

### Colab Notebooks Python

In this folder you can see some source codes developed in colab notebooks in order to practice Data Analysis using python and some common libraries like **Pandas**, **Numpy**, **seaborn** etc.

One of the tests made until here is a comparision in number of *Covid-19* confirmed cases between three countries (here i suggest to compare the baltic countries).
You can check some results in the public notebook used to develop these studies. Link of dataset used to develop these studies can be found below too:

[Covid-19 Data Analysis (Comparision between countries)](https://colab.research.google.com/drive/1Q1Lw2QAG9CylQ28k2Px7B3YrTXQouAXm)

[Dataset Novel Corona Virus 2019](https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset/tasks?taskId=508)
