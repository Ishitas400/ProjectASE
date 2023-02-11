# ProjectASE
Advanced Software Engineering 

ETHICAL HACKING


EXERCISES FOR ADVANCED SOFTWARE ENGINEERING COURSE


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
  
  
