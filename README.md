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
> Nginx reverse proxy

The following diagram illustrates how a user and the services interact with one another. 
[insert diagram]

### The app
___
The font-end user interface uses a very basic layout. It displays the randomly generated stage name and a genre suggestion. Upon refreshing the page a new name would be generated with a different genre suggestion
[insert screen shot of front end]

### Project Tracking 
___
To fit one of the requirements I used a trello for my project tracking. Tasks were assigned that would
[insert trello board]
### Risk Assesment
At the start of the project a risk assesment was carried out. The diagram below contains some of the possible risks that could occur during the process of creating the application. The likelihood of the risks occuring are colour coded to match levels given in a supplimented Key. Red being high risk and green being unlikely. A section for Mitigations was created to seperate from things that were currently implimented to things that could be considered further along the project.
[insert risk assesment]

## Project Pipeline

### Development Process
During the entire development of the app, Github was used for version control. Github is useful as as works as both remote storage for my work but also as a webhook that can trigger new builds within my jenkins pipeline.
The web application was written in python, using the micro-framework Flask.

### Unit Testing
___
> I carried out unit tests against the 4 of my services. Each service had its own uniquely defined tests. The tests were run via a test.sh script. Below the test results of the current build of the project can be viewed.











