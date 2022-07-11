# Stage Name Generator
## Ashley Alphonso
### Project Introduction
___
The purpose of this project was to produce an application consisting of four microsevices, which interact with one another to generate objects based off of developer designed logic. The project is to be fully integrated with a CI/CD pipeline.

The minimum requirements of the project are:

- An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
- An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine
- If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
- The project must follow the Service-oriented architecture that has been asked for.
- The project must be deployed using containerisation and an orchestration tool.
- As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
- The project must make use of a reverse proxy to make your application accessible to the user.

### Idea and Design
___

The application randomly allocates artist stage names to the user using the four services
`Service 1`
> This is the front-end application that generates the stage name and suggests a genre based on the nmae outputted.

`Service 2`
> This service randomly generates the prefix part of the stage name.

`Service 3`
> This service randomly generates the suffix part of the stage name.

`Service 4`
> This service takes the output from service 2 and service 3 and based on that generates a suggested genre to be provided to the front end.

`Service 5`
> Nginx reverse proxy, This services main role was to run as a reverse proxy between port 80 and port 5000 for the front-end service.

The following diagram illustrates how a user and the services interact with one another. 
<p><img src="https://github.com/AlpaPhono/SecondProject/blob/nameGenerator/imagesAndDocs/user%20services%20diagram.png" alt="test" width="1000" height="450"></p>

### The app
___
The font-end user interface uses a very basic layout. It displays the randomly generated stage name and a genre suggestion. Upon refreshing the page a new name would be generated with a different genre suggestion
<p><img src="https://github.com/AlpaPhono/SecondProject/blob/nameGenerator/imagesAndDocs/service%201.png" alt="test" width="1000" height="450"></p>

### Project Tracking 
___
To fit one of the requirements I used a trello for my project tracking. Tasks were assigned that would aid in meeting the acceptance criteria for the project.. The MOSCOW principle was used with colour coding.
<p><img src="https://github.com/AlpaPhono/SecondProject/blob/nameGenerator/imagesAndDocs/trello%20board.png" alt="test" width="1000" height="450"></p>

### Risk Assesment
At the start of the project a risk assesment was carried out. The diagram below contains some of the possible risks that could occur during the process of creating the application. The likelihood of the risks occuring are colour coded to match levels given in a supplimented Key. Red being high risk and green being unlikely. A section for mitigations was created to seperate from things that were currently implimented to things that could be considered further along the project.
<p><img src="https://github.com/AlpaPhono/SecondProject/blob/nameGenerator/imagesAndDocs/namegen%20risk.png" alt="test" width="1000" height="450"></p>

## Project Pipeline
[insert image]
### Development Process
During the entire development of the app, Github was used for version control. Github is useful as as works as both remote storage for my work but also as a webhook that can trigger new builds within my jenkins pipeline.
The web application was written in python, using the micro-framework Flask.

### Unit Testing
> I carried out unit tests against the 4 of my services. Each service had its own uniquely defined tests. The tests were run via a test.sh script. Below are the test results of the current build of the project can be viewed.
***Service_1 test***
<p><img src="https://github.com/AlpaPhono/SecondProject/blob/nameGenerator/imagesAndDocs/service%201%20tesr.png" alt="test" width="1000" height="450"></p>
***Service_2 test***
<p><img src="https://github.com/AlpaPhono/SecondProject/blob/nameGenerator/imagesAndDocs/service%202%20tesr.png" alt="test" width="1000" height="450"></p>
***Service_3 test***
<p><img src="https://github.com/AlpaPhono/SecondProject/blob/nameGenerator/imagesAndDocs/service%203%20tesr.png" alt="test" width="1000" height="450"></p>
***Service_4 test***
<p><img src="https://github.com/AlpaPhono/SecondProject/blob/nameGenerator/imagesAndDocs/Service4%20test.png" alt="test" width="1000" height="450"></p>

## Project Pipeline
___

### Build and Deploy##
The code was built using docker, a containerisation tool. Then deployed onto different vm's using the orchestration tool docker swarm.

### Automation
___
This project runs on a CI/CD pipeline using jenkins installed on a vm. Jenkins allows for webhooks to be attached to the nameGenerator branch of my git repo. When code is pushed to the repository it will trigger a new build inside jenksins.
Ansible was used to configure swarm worker vm's by installing docker and adding them to the swarm.




 

### Current Imporvements
- Using a feature branch model to better organise the version control of my web app. A development branch was made however a seperate branch wasn't implimented when adding a new feature. This is an important approach to adopt as it allows a developer to build upon thier code with confidence that their last working commit is safe in within another branch.












