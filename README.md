ABSTRACT

In this world, a human being suffers from many different diseases. Diseases can have a physical, but also a psychological impact on people. Some diseases are cured after treatment, but in some cases they become incurable. Also, many people are unable to afford medical tests. This leads to degradation of health. So, it is always important to detect and treat disease at an early stage.
The purpose of the Disease Detection System is to automate the existing manual system using computerized equipment and full-fledged software. The required software and hardware are easily available and easy to work with. The Disease Detection System can lead to error free, secure, reliable, and fast detection systems. It can assist the user to concentrate on conducting further tests and curing the disease rather than concentrating on diagnosing the disease. Thus, it will help organizations in better utilization of resources. Basically, the project helps to provide better interface and better services to the clients.
1.1: OBJECTIVE
The objective of the Disease Detection System is to automate the existing manual system of disease diagnosis using computerized equipment and fully-fledged software.
The user will give the symptoms to the system as input and then the system will provide the result i.e., the diagnosed disease based on the symptoms given by the user as output.
1.2: EXISTING SYSTEM
Traditionally the disease was detected by going to hospitals and conducting various tests to diagnose the disease which takes a lot of time and money. As a result, the delay caused in this process leads to making the impact of the disease worse in the body and can be very dangerous to health.
Following are the limitations of the existing disease detection system:
•	Money and time-consuming process.
In the traditional system people used to visit hospitals to conduct various medical tests which were time consuming. Also, the cost of the tests are high and are unaffordable for many.
•	Delay in treatment
The traditional system was time consuming which leads to delay in treatment of the disease which can be dangerous for health.
1.3: PROPOSED SYSTEM
The project to be deployed is the ‘Disease Detection System’ which is built using machine learning. The system will diagnose the disease based on the symptoms given to the system as input from the user. The list of diseases and their symptoms are divided into training and testing datasets, and they are implemented using machine learning algorithms.
Below is the description of the datasets and algorithms used in Disease Detection System:
1.3.1: Datasets
A dataset is a collection of data in which data is arranged in some order. A dataset can contain any data from a series of an array to a database table. A tabular dataset can be understood as a database table or matrix, where each column corresponds to a particular variable, and each row corresponds to the fields of the dataset. The most supported file type for a tabular dataset is “Comma Separated File,” or CSV. There are two types of datasets:
Training Dataset
A training dataset is a dataset of examples used during the learning process and is used to fit the parameters (e.g., weights) of, for example, a classifier. For classification tasks, a supervised learning algorithm looks at the training dataset to determine, or learn, the optimal combinations of variables that will generate a good predictive model. The goal is to produce a trained (fitted) model that generalizes well to new, unknown data. The fitted model is tested using the test dataset to estimate the model’s accuracy and in classifying new data.
Testing dataset
A test dataset is a dataset that is independent of the training dataset, but that follows the same probability distribution as the training dataset. A test set is therefore a set of examples used only to assess the performance (i.e., 10 generalization) of a fully specified classifier. To do this, the final model is used to predict classifications of examples in the test set. Those predictions are compared to the examples’ true classifications to assess the model’s accuracy.
Both the training and testing datasets for the Disease Detection System model are imported from Kaggle.com and saved in this system as ‘training.csv’ and ‘testing.csv’. From Kaggle.com we were able to get clean dataset for our system, so we didn’t need to do the cleaning of data.
1.3.2: Algorithm
Machine Learning algorithms are the programs that can learn the hidden patterns from the data, predict the output, and improve the performance from experiences on their own. Different algorithms can be used in machine learning for different tasks.
One of the machine learning algorithms used in the Disease Detection System used is ‘Naïve Bayes’ algorithm. It is a supervised learning algorithm, which is based on Bayes theorem and used for solving classification problems. It is mainly used in text classification that includes a high-dimensional training dataset. Naïve Bayes Classifier is one of the simple and most effective Classification algorithms which helps in building the fast machine learning models that can make quick predictions. It predicts on the basis of the probability of an object.
Working of the Naïve Bayes Algorithm:
1.	Convert the given dataset into frequency tables.
2.	Generate Likelihood table by finding the probabilities of given features.
3.	Now, use Bayes theorem to calculate the posterior probability.
Advantages:
o	Naïve Bayes is one of the fast and easy ML algorithms to predict a class of datasets.
o	It is the most popular choice for text classification problems.
Disadvantages:
o	Naive Bayes assumes that all features are independent or unrelated, so it cannot learn the relationship between features.
1.4: MODULE
A module is a collection of source files and build settings that let you divide your project into discrete units of functionality. Your project can have one or many modules, and one module can use another module as a dependency. You can independently build, test, and debug each module.
Following is the module of the Disease Detection System 
                       Figure-1: Module of the Disease Detection System










1.5: USER INTERFACE
The user interface refers to a feature which allows user to interact with the software running on a server through web browser. The aim to create a user interface is to create an interface in such a way users find convenient to use. Here the user acts as a client.

In the Disease Detection System, the ‘home page’ is the first page to be seen by the user where the user is required to enter the symptoms to diagnose the disease by the system. The Disease Detection system requires 5 symptoms from the user. After entering the symptoms then the user is required to click the ‘Submit’ button to submit the symptoms as input to the system. At the beginning of the home page the instructions are also provided for the user on how to use the system for the user’s convenience.

After clicking the ‘Submit’ button the user will be directed to the result page where the name of the disease will be displayed to the user based on the symptoms given to the system

There are other useful links provided in the system for the user such as ‘Blog’ and ‘Home Remedy’ which provides information regarding healthy lifestyle and home remedies to cure ailments.

   
Figure-2: Home Page

After clicking the ‘submit’ button the user will be directed to the result page where the result of the input i.e., the name of the disease will be displayed on the system based on the inputs i.e., the symptoms entered by the user.
 Figure-3: Result Page

1.6: BENEFITS
The following are the benefits of Disease Detection System:
•	Saves Time and Money
The Disease Detection System reduces the time and money to visit a hospital and conduct analysis to diagnose the disease. The user can detect the disease using this system and then they just is required to conduct a final test for the medical confirmation of the disease.

•	Helps to Cure the Disease Early
Disease Detection System helps to diagnose the disease in less time. So the process to cure the disease can begin early so that the disease can be cured before it worsens the health as in some cases the disease becomes incurable due to delay in treatment.




1.7: LIMITATIONS
The Disease Detection System, however, is subjected to some limitations. The limitations provide the complete understanding of the system and can be improved in the future.
The Disease Detection System requires the following limitations:
•	Less number of disease diagnosis
There are a lot of diseases in present time but for now the disease detection system has data of 40 diseases i.e., it can detect 40 diseases which are provided in its datasets.The dataset needs to be improved to add more disease into the system for better performance and accuracy in disease diagnosis.

•	Less number of services provided
Disease Detection System includes only getting the symptoms and providing the result in the present time and doesn't provide any other features. This can be improved by adding more features such as Virtual Assistant, Medicine, and Test Suggestions, etc.
 
CHAPTER-2: REQUIREMENT ANALYSIS
Requirement analysis is a significant and essential activity after elicitation. We analyze, refine, and scrutinize the gathered requirements to make consistent and unambiguous requirements. This activity reviews all requirements and may provide a graphical view of the entire system. After the completion of the analysis, it is expected that the understandability of the project may improve significantly.

2.1:  ANALYSIS STUDY
Analysis Study refers to assessing every expense or problem related to a project before working on it and evaluating the outcome once the work is done. Failing to do so, would mean unexpected challenges, overlooked critical information, or flaws in the work process that manifest as the project unfolds.
Following is the analysis study for Disease Detection System:
•	User friendly interface
Disease Detection System provides a better interface to the user and thus the user can interact easily with the system.

•	Lower installation
Disease Detection System doesn’t require any high configurations and software setup for smooth running of the system. This application is designed with an ease to support any ordinary system having an internet connection. At the server the charges are only for setting up the LAN connections but not the systems.

•	Simple to use and easy to understand
The coding of this system was indeed a tedious job. But it is implemented in such a way that the user needs only the internet and web browser to use this system.

•	Platform independent
This project is done completely in Python language and it is platform independent so, the client systems may have vista, Linux, Mac or any other operating system and they can connect to server easily without any dependencies of Operating System.

2.2: FEASIBILITY STUDY
A feasibility study is a detailed analysis that considers all of the critical aspects of a proposed project in order to determine the likelihood of it succeeding. It
is the test of the System proposal according to its workability, impact on the current System, ability to meet the needs of the current users and effective use of the resources. Its main objective is not to solve the problem, but to acquire its scope.
Feasibility Study in Disease Detection System focuses on the following:

•	Technical Feasibility
Technical feasibility is the process of figuring out how you're going to produce your product or service to determine whether it's possible to launch or deploy or not. Technical feasibility deals with whether the project will be executed with existing software technologies and system configurations.

The Disease Detection System is implemented in such a way to make it as technically feasible as possible. The primary technical requirement includes the availability of Windows 7 or higher versions of operating Systems installed in the network. Visual Studio Code was required to implement the code for this system which is available. Flask framework was required for the system’s front end development which was also available. Thus, through all the ends technical feasibility was met. 

•	Economical Feasibility
The purpose of economic analysis is to determine whether there is an economic case for the investment decision. This assessment goes beyond the items typically included in a financial analysis. It deals with whether the project is cost effective or not.

The Disease Detection System is economically feasible. The hardware installation cost was low as the hardware required for this system is pre installed. The softwares loaded for this project (Visual Studio Code and Flask Framework) were installed for implementing other applications as well so the cost of the software setup was also low. As student trainees were developing the application, there were no major personnel costs associated.

Moreover, the technical requirements were already available so there was no further expenditure for buying software packages. 

•	Operational Feasibility
The operational feasibility assessment focuses on the degree to which the proposed development project fits in with the existing business environment and objectives with regard to development schedule, delivery date, corporate culture and existing business processes. It deals with the analysis of whether the project has sufficient support for the management and the users.

The Disease Detection System is operationally feasible. This application provides the necessary information to the user such as how to enter the symptoms and click on ‘submit’ button to get to know the result. The system is implemented in such a way that no prior knowledge is required by the user to work on the system. The user just needed to have the basic knowledge of computers. 

2.3: TECHNOLOGIES:
Languages:
Front-end: 
1.	HTML:
The HyperText Markup Language or HTML is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets (CSS) and scripting languages such as JavaScript.
Web browsers receive HTML documents from a web server or from local storage and render the documents into multimedia web pages. HTML describes the structure of a web page semantically and originally included cues for the appearance of the document.

2.	CSS:
Cascading Style Sheets (CSS) is a style sheet language used for describing the presentation of a document written in a markup language such as HTML or XML  CSS is a cornerstone technology of the World Wide Web, alongside HTML and JavaScript. CSS is designed to enable the separation of content and presentation, including layout, colors, and fonts.[3] This separation can improve content accessibility; provide more flexibility and control in the specification of presentation characteristics; enable multiple web pages to share formatting by specifying the relevant CSS in a separate .css file, which reduces complexity and repetition in the structural content; and enable the .css file to be cached to improve the page load speed between the pages that share the file and its formatting. 

3.	JavaScript:
JavaScript is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS. JavaScript is a high-level, often just-in-time compiled language that conforms to the ECMAScript standard.[10] It has dynamic typing, prototype-based object-orientation, and first-class functions. It is multi-paradigm, supporting event-driven, functional, and imperative programming styles. It has application programming interfaces (APIs) for working with text, dates, regular expressions, standard data structures, and the Document Object Model (DOM).




Back-end: 
1.	Python (v- 3.11.1)
Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[33]
Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.
Python was created in the late 1980s, and first released in 1991, by Guido van Rossum as a successor to the ABC programming language. Python 2.0, released in 2000, introduced new features, such as list comprehensions, and a garbage collection system with reference counting, and was discontinued with version 2.7 in 2020. Python 3.0, released in 2008, was a major revision of the language that is not completely backward-compatible and much Python 2 code does not run unmodified on Python 3. With Python 2's end-of-life, only Python 3.6. and later are supported, with older versions still supporting e.g., Windows 7 (and old installers not restricted to 64-bit Windows).

Framework:
•	Flask (v- 2.2.2)
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.[2] It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools. 
Applications that use the Flask framework include Pinterest and LinkedIn.


2.4: TOOLS USED
Platform (Source Code Editor):
•	Visual Studio Code 2022 (v- 17.4.2) 
Visual Studio Code, also commonly referred to as VS Code,[10] is a source-code editor made by Microsoft with the Electron Framework, for Windows, Linux and macOS. Features include support for debugging, syntax highlighting, intelligent code completion, snippets, code refactoring, and embedded Git. Users can change the theme, keyboard shortcuts, preferences, and install extensions that add additional functionality.
In the Stack Overflow 2021 Developer Survey, Visual Studio Code was ranked the most popular developer environment tool among 82,000 respondents, with 70% reporting that they use it.

Operating System: 
•	Windows 11
Windows 11 is the latest major release of Microsoft's Windows NT operating system, released in October 2021. It is a free upgrade to its predecessor, Windows 10 (2015), and is available for any Windows 10 devices that meet the new Windows 11 system requirements.

•	Processor - x64-based processor




2.5:USER AND SYSTEM REQUIREMENTS
2.5.1: OBJECTIVE
The objective of the Disease Detection System is to automate the disease diagnosis process using computerized software. The system involves the user specifying the symptoms in the system and gets the name of the disease diagnosed as a result. This will reduce time and money of the users which was spent on undergoing various tests for diagnosis. By using this system and getting the result of the diagnosis, the user is required to undergo a medical test for the confirmation of the disease. 

2.5.2: INTRODUCTION
People having health issues are now very common around the globe. Poor lifestyle and diet are one of the main reasons for this. Even children and young adults are facing major health issues such as diabetes, hypertension, etc. It is observed in some cases that many people facing health issues are not able to afford medical expenses. Also, some hospitals charge heavy fees for treatment and particularly when the patients have insurance policy/cover and thus delays the testing and diagnosis process which further degrades their health.

The Disease Detection System aims to automate the existing system using computerized equipment and full-fledged softwares. In this system the user has to enter the symptoms and after clicking the ‘submit’ button then the user will be directed to the result page where the name of the disease will be displayed. 

In the Disease Detection System, the symptoms are well connected to the disease. Some helpful links are provided for the convenience of the user such as ‘Blog’ which provides information regarding healthy lifestyle. ‘Home Remedy’ link provides information about home remedies to cure ailments. ‘Connect with Doctors’ link provides information about the doctors and how to connect with them. The system is developed in such a manner to make it more user friendly. 

2.5.3: PURPOSE
The Disease Detection System is designed in such a way to make a user-friendly interface. The instructions are provided in the home page on how to enter their symptoms and get to know their result. Also, some links are provided which can be convenient for the user. The only requirement from the user side is that the user should have basic computing skills and an internet connection.

2.5.4: INTENDED USER
Intended user means the users that are intended to use Software, features or functions of the Software, as described in the Specifications for such Software.
In the Disease Detection System, anyone with basic computing skills and internet connection can use this system with great efficiency. 


2.5.5: PROJECT SCOPE
The scope of the project is a part of project planning that involves determining and documenting a list of specific project goals, deliverables, features, functions, tasks, etc. in other words, it is what needs to be achieved and the work that needs to be done to deliver the project. It defines the limitations and the future expectations from the project.

The disease Detection System was initiated to provide a computerized and more convenient approach to detect their diseases based on the symptoms they provide to the system as input. First they will enter five symptoms and after clicking the ‘submit’ button they will be directed to the result page where the name of the disease will be displayed to the user.

The scope of this project is to increase the details of the disease into the system and provide more functionalities like virtual assistant, medicine and test suggestions, etc. Also there is always a scope to improve the accuracy of the detection in the system.

The overall scope of the project is that new features and functionalities can be established. The limitations can be rectified, and the overall productivity of the project will be increased. 


2.5.6: LIMITATIONS 
The limitations provide a better understanding of the project and explains the scope of improvement of the project.
This Disease Detection System is however, subjected to following limitations:
•	Can detect limited number of disease
The system as of now can detect only forty diseases as of now. This limitation can be improved by adding more data into the dataset. 
•	Provides limited services
More services can be added into the system such as virtual assistant, test and medicine suggestions, etc
Also, there is always scope to improve the accuracy of the detection of the disease.

2.5.7: OVERALL DESCRIPTION
The overall description of a project provides a high-level overview of the project. The document explains a project's objectives and its essential qualities.
Overall Description of the Disease Detection System
Product Perspective
•	To provide a platform to the user to detect their disease on their own.
The Disease Detection System provides a platform where the user can provide symptoms to the system and get to know about the name of the disease.

•	To provide more feasible approach to monitor one’s own medical condition.
This system helps the user to detect the disease on their own without visiting to the hospitals.

•	To provide other useful links 
The Disease Detection System provides the following links as of now:
o	‘Blogs’
This link provides information regarding healthy lifestyle.

o	‘Home Remedy’
This link provides information regarding home remedies to cure ailments.

o	‘Connect with Doctors’
This link provides information regarding the doctors and how to connect with them.

Product Features
•	Home page
The home page is the first page that the user will see. In this page the user will provide the symptoms to the system and after clicking the ‘submit’ button, the user will be directed to the result page.



•	Result page
The result page is where the user will be directed to after providing the symptoms to the system. This page will be displaying the result i.e., the name of the disease to the user based on the symptoms the user has entered.

•	Blog page
This page directs the user to a blog page which provides information regarding a healthy lifestyle which can be very helpful to the user.

•	Home Remedy Page
This page directs the user to a page which provides home remedies to cure ailments.

•	Page to connect with doctors
In case if the patient is detected with any disease, then the user is provided with a link which will direct the user to a site where the user can connect with the doctors. The name of the doctor, along with contact details is mentioned in this page.

2.6: OPERATING ENVIRONMENT
Operating environment refers to the environment which is suitable to run the application software. An operating environment is not a full operating system but is a form of middleware that rests between the OS and the application. 

Operating System:
Processor: x64-based processor with 1.30 GHz Clock Speed
RAM: 4GB or more
Hard Disk: 50GB or more
Monitor: 1920 x 1080, 120.04 Hz
Keyboard: 100 keys
Mouse: 2 Buttons / 3 Buttons
Operating System: Windows 8 or more

2.7: USER CLASSES
User classes define the various groups of people intended to use an application. They are divided into three classes namely:
•	user 
The file or directory owner, which is usually the user who created the file. The owner of a file can decide who has the right to read, write and execute it.

•	group
 Members of a group.

•	others
All other users who are not the file owner or group owner.
The user classes for Disease Detection System are:
•	System Owner (User):
The Disease Detection System’s owner/developer. They have complete access on the system.

•	Administrators (Group): 
Have full privilege on the functioning of the system.

•	Public (Others): 
They can view the home page, result page, and other useful links provided in the system. They cannot access the back-end functionalities of the system.

2.8 DESIGN CONSTRAINTS
Design constraints are those constraints that are imposed on the design solution of an application. Though they do not affect the working of the system
The design constraint of the Disease Detection System as of now is that the GUI (Graphical User Interface) of the system will only be in English Language.

2.9: SYSTEM FEATURES
Features are the “tools” you use within a system to complete a set of tasks or actions. Functionality is how those features work to provide you with a desired outcome.

2.9.1: FUNCTIONAL REQUIREMENTS
Functional requirements are product features or functions that developers must implement to enable users to accomplish their tasks.
Functional requirements of the Disease Detection System: 
•	Home page: 
Home page is the first page to be seen by the user. Here the user will provide symptoms to the system. Instructions are provided for the convenience of the user to do the same.
Input: Enter Symptoms

•	Result Page:
After entering the symptoms and clicking the ‘submit’ button, the user will be directed to the result page where the system will display the result of the symptoms added by the user i.e., the disease detected by the system based on the symptoms added by the user.
Output: Disease Detected by the symptoms

•	Blog Page:
The blog link directs the user to a blog page where information is provided regarding health such as healthy lifestyle, nutritional facts, etc.

•	Home Remedy Page:
This link directs to the page where information is provided regarding home remedies for various health issues.
2.9.2: NON-FUNCTIONAL REQUIREMENTS
The non-functional requirements serves as constraints or restrictions on the design of the system.
The non-functional requirements of the disease detection system are:
•	Availability:
Availability describes how likely the system is accessible to a user at a given point in time.
The Disease Detection System is always available, and the user can access it any time. In case of hardware or connection failure then a page for the same will be displayed. This ensures 24x7 availability.

•	Performance:
This refers to how fast a software system or a particular piece of it responds to certain users’ actions under a certain workload. 
The system is interactive and there are less delays involved. The delay is faced only during the establishment of the connection. Overall, the system is performing very smoothly, and no issues were face as of now. 
•	Reliability: 
Reliability specifies how likely the system or its element would run without a failure for a given period of time under predefined conditions.

As the system provide the right tools for problem solving it is made in such a way that the system is reliable in its operations and for securing the sensitive details. 
