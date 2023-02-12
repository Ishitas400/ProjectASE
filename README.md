# ProjectASE
Advanced Software Engineering 

A) ETHICAL HACKING

To protect ourselves from unethical hackers, employment of ethical hackers has become very important nowadays. Python uses inbuilt libraries and modules which makes our job much easier to code using python.In this exercise, I have focussed on how common passwords can be converted to hashed digested words using md5 and SH1 methods. The python code for the same can be found here - https://github.com/Ishitas400/ProjectASE/blob/main/EthicalHack.py .
This code would also need a website where we can directly convert our passwords into md5 and SH1 hashed versions without any problem - https://www.md5hashgenerator.com .
Also, I have used my set of passwords for testing and debugging the program which can be found here - https://github.com/Ishitas400/ProjectASE/blob/main/password.txt . (This list is completely customizable) The output of the code is as follows - https://github.com/Ishitas400/ProjectASE/blob/main/output1.PNG  and https://github.com/Ishitas400/ProjectASE/blob/main/output2.PNG .



B)EXERCISES FOR ADVANCED SOFTWARE ENGINEERING COURSE


 1.GIT

For GIT,I have used frequent push,pull,commit and other frequently used commands in this repo.I have randomly used a few commmands that may have just been for practice that were not necessarily asked in the exercises. I have attached my Git command history here- https://github.com/Ishitas400/ProjectASE/blob/main/.bash_history A few of the other not so related to the project commits are https://github.com/Ishitas400/ProjectASE/blob/main/hotel1.txt , https://github.com/Ishitas400/ProjectASE/blob/main/houses.txt , https://github.com/Ishitas400/ProjectASE/blob/main/rollno.txt , https://github.com/Ishitas400/ProjectASE/blob/main/surnames.txt . 


2. UML

For the second task, I have created 3 UML diagrams.

  a)The first is the Sequence diagram https://github.com/Ishitas400/ProjectASE/blob/main/hack1.PNG which represents the sequence of messages that are shared or exchanged between the objects represented in the diagram.
  
  b)For the second diagram I have shown a Use Case diagram https://github.com/Ishitas400/ProjectASE/blob/main/hack2.PNG which graphically represents a user's possible interractions with a system.
  
  c) Finally, for the third case, I have chosen the Activity diagram https://github.com/Ishitas400/ProjectASE/blob/main/hack3.PNG which represents the behavior of the components in a system.It gives us an overview of how the workflows.
  
  
  3.DDD
  
  For the DDD, I decided to go for another domain since my domain was too small to be represented and broken into sub-domains. I chose the banking system as it seemed very intersting to me to learn as well as document the relationship between the numerous sub domains involved in the same. I have drawn a diagram which depicts the different sub domains of the banking domain and the relationships between them- https://github.com/Ishitas400/ProjectASE/blob/main/DDD.PNG .
  
4. METRICS
For the Metrics, I have chose Pylint which is a very well known metrics and Bandit. 
Pylint checks code in the static mode,which means that it analyses code without actually running it. Although I did not get a very good result using it, it was probably because I used many elif and if statements in order to fit 2 codes of a similar nature together. Here I have attached the snapshot of the same. https://github.com/Ishitas400/ProjectASE/blob/main/pylint.PNG
   
For the second metrics, I have chosen Bandit which checks for the security of a code. Here bandit has shown a high level severity of 2 which is common in codes involving hashing algorithms like md5 and SH1. https://github.com/Ishitas400/ProjectASE/blob/main/bandit.jpg  is the link to the output.
    
5. CLEAN CODE DEVELOPMENT
  
  For CCD, I have made a Python cheat sheet which includes a few tips that I like to follow while writing Python codes for clean codes https://github.com/Ishitas400/ProjectASE/blob/main/Python%20Cheatsheet.pdf .
    The source code can be used here for reference. https://github.com/Ishitas400/ProjectASE/blob/main/EthicalHack.py#L1-L30 .
  Here I have marked the 5 clean code snippets.
  For clean code 1: I have imported hashlib which is a module which implements many secure md5 and SH1 message encrption calculations and makes performing operations easier instead of writing huge chunks of codes.
  For clean code 2: Instead of writing a huge line of code I have broken it into 3 different lines so that it is more readable and compact.
  For clean code 3: Instead of using 'xyz' or some random variables, I have used a variable called password_found which is quite self explanatory and avoiuds unnecessary confusion.
  For clean code 4: For input as a string,I have used double quotes instead of single quote in order to avoid confusion with apostrophe.
  For clean code 5: I have use try and except so that even if the file is not found in the mentioned directory,it should not throw an error and abend the program. Instead, the program runs with code 0 successfully even if the file path is given incorrectly.
  
6.BUILD MANAGEMENT

  For Build Management, I have chosen Pybuilder as a built management tool. Previously, I have used Maven in Eclipse for Java project build. the build file can be found here- https://github.com/Ishitas400/ProjectASE/blob/main/build.py  and the setup file here- https://github.com/Ishitas400/ProjectASE/blob/main/setup.py . I have also added a snippet of my terminal to prove that the build ran successfully- https://github.com/Ishitas400/ProjectASE/blob/main/pybuild.PNG . The coverage files are available here https://github.com/Ishitas400/ProjectASE/blob/main/ase.coverage .
  
7. UNIT TESTS


8.CONTINUOUS DELIVERY


9.IDE

 For the IDE, I have chosen Pycharm. Previously I used to use Jupyter Notebook religiously for Data Science and Machine Learning codes. This was the first time that  I used Pycharm for an entire project. I can say that I thoroughly enjoyed using it and would definitely use it more often in the future. It is a great IDE as it allows us to view the source code very easily. Also it is similar to the Eclipse IDE used for JAVA programming and allows us to easily debug and gfind errors in our code because of the yellow and red balloon icons which alos provide us with probable one click solutions. The shortcuts that I liked in Pycharm are as follows-
 
 shift+F10 for running a code, https://github.com/Ishitas400/ProjectASE/blob/main/run1.PNG
 shift+F9 for debugging a code, https://github.com/Ishitas400/ProjectASE/blob/main/debug.PNG
 F9 for resuming program execution,
 alt+HOME to jump to the Navigation Bar,
 alt+ctrl+L for reformating code,
 F2 for Navigating to the next highlighted error in the active editor, https://github.com/Ishitas400/ProjectASE/blob/main/EthicalHack.py#L36
 ctrl+C and ctrl+V for copying and pasting to and from the clipboard and 
 shift+Tab for unindent selection. 
 
 
10.DSL
  
 For DSL(Domain Specific Language), I have chosen SQL which is the Structured Query Language which is mostly used to communicate with a database. For our task, I have refactored my code from another subject taught by our university(pdds). The data set was provided by the professor- https://github.com/Ishitas400/ProjectASE/blob/main/zuwendungen-berlin.csv.gz . The code was written in Jupyter Notebook so that along with the SQL language I  could also use a few python commands so that the main idea of this project being a python project is not diverted from. The notebook can be found as foolows - 
https://github.com/Ishitas400/ProjectASE/blob/main/ASE.ipynb .

11.FUNCTIONAL PROGRAMMING

For functional programming, I have attached the relevant code snippets here-
a)Final data structure-I have used finally in my code here https://github.com/Ishitas400/ProjectASE/blob/main/Functional.py#L28 . 
The output is as https://github.com/Ishitas400/ProjectASE/blob/main/finally.PNG ,

b)For side effect free functions and the rest of the the functional programming requirements,I have made a small python code which depicts 
different aspects of functional programming- https://github.com/Ishitas400/ProjectASE/blob/main/SideEffect.py#L1-L11 .

c)For the use of higher order functions,I have used "sorted" which sorts a list from ascending to descending - https://github.com/Ishitas400/ProjectASE/blob/main/SideEffect.py#L13-L15

d)For functions as parameters and return values, we defined 3 functions as herbivorous,carnivorous and omnivorous and passed the functions 
as arguments - https://github.com/Ishitas400/ProjectASE/blob/main/SideEffect.py#L18-L35 .

e)For closures in python,I have defined variables outside the inner function and have nested the anonymous function 
and then called both the inner and outer functions- https://github.com/Ishitas400/ProjectASE/blob/main/SideEffect.py#L38-L52 .

The output for (b);(c);(d) and (e) parts are found here - https://github.com/Ishitas400/ProjectASE/blob/main/op.PNG .



 
 
 


  
  
  
