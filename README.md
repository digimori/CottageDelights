# Cottage Delights - Cottagecore Themed Afternoon Tea E-Commerce App

### About the Project:
---


- [Live Preview]()
- [Github Repository]()

***

[AmIResponsive]()
![Image for AmIResponsive]()   



### Table of Contents  
- [About The Project](#about-the-project)  
- [Technologies Used](#technologies-used)   
- [Developer Goals](#developer-goals)
- [User Stories](#user-stories)
- [Design Choices](#design-choices-fonts-colours-and-images-cards-and-hamburger-menus)
- [Wireframes](#wireframes)
- [Database Schema](#database-schema)
- [Features](#features-and-navigation)
- [Navigation](#navigation)
- [Testing And Validation](#testing-and-validation)
- [Deployment](#deployment-github-and-heroku)
- [Credits](#credits)


***

### Technologies used:
---
- HTML
- CSS (Bootstrap 5 library)
- JavaScript (jQuery)
- Django Frameworks
- Python3 (Back-end application)
- PostgreSQL (Relational Database)

### Developer Goals:
---


### User Stories:
---
PORT THESE OVER FROM YOUR EXCEL SPREADSHEET!


### Design Choices (Fonts, Colours and images, cards and hamburger menus):
---
#### Font and Colours:

### Wireframes
---

<details>
  <summary>Wireframes (Adobe Photoshop):</summary>

 ####  Desktop, Tablet, Mobile

- Index page (Not Logged in and Registration page are laid out the same):
![Index - Not logged in/Registration](/readmeimages/Wireframesprelogin.jpg)

- Profile Page (Once Logged in, cannot be accessed prior to login):
![Profile - Logged in]()

- Add-Products page (Superuser/Admin must be logged in):
![Add Products]()
</details>

---

### Database Schema
---


### Features and Navigation
---

#### Login/Logout/Register


<details>
<summary>Logged In Index and Registration</summary>

![Logged in Nav-bar - Index]() 
![Registration Page]()

</details>

<details>
<summary>Logout page</summary>

![Logout]()

</details>

#### Profile

<details>
<summary>Profile Page</summary>

![Full Profile Page]()
</details>


<details>
<summary>Search Bar</summary>


![Search Bar]()
![No Results]()

</details>

<details>
<summary>Product Cards</summary>

</details>


### Adding books

<details>
<summary>Add Product Form</summary>

</details>


### Editing Products

<details>
<summary>Edit Form for Product Management</summary>


</details>


#### Deleting Products

<details>
<summary>Product Deletion</summary>

</details>

### Testing and Validation:
--- 

###  Validation (HTML, CSS, Python PEP8)
---
<details>
<summary>HTML</summary>


</details>

<details>
<summary>CSS, jQuery and Python PEP8</summary>

[CSS Validation using Jigsaw](https://validator.w3.org/)
![CSS Validation]()

[PEP8 Validation using CI's Linter](https://pep8ci.herokuapp.com/)
![Python PEP8]()

[jQuery Validation using JSHint](https://jshint.com/)
![jQuery]()
</details>


#### Manual Testing - User Testing

| Test | Expectation | Pass/Fail |
| ----------- | ----------- | ----------- |
|  | |  |


### Media Queries

I used the Chrome Dev tools to implement changes in real time before performing a final commit on the code itself.  
This was also used to test the responsiveness as I could change the breakpoints as I edited each line of code.


### Bugs and Fixes
---
| Bug/Issue | Explanation | Fix Implemented |
| ----------- | ----------- | ----------- |
||  | |


### Deployment (Github and Heroku):
---

#### Github into Gitpod/Local Code Editor/IDE:

#### To deploy and run locally via an IDE:

- Use the Chrome browser
- Create a Gitpod account at [this link](https://www.gitpod.io/)
- Download and install the Gitpod browser extension for Google Chrome.
- Restart browser after installation has completed.
- Log into Gitpod using your Github username and password. If you don't already have a GitHub account, [create one here](https://github.com/signup?source=login)
- Navigate into your desired Gitpod repository 
- This project's repository can be found both at the top of this README, [and here](https://github.com/digimori/CottageDelights)
- Click the green "Gitpod" button on the top right of the repository file section.
[image goes here]

- This will open the project into a Gitpod workspace and can then be worked on in a local setting, such as VSCode.

#### Clone and Fork:

-Follow [This link](https://github.com/digimori/CottageDelights) back to the Github project respository.
- Select the menu item above the repository files labelled "Code".
- To clone: Select the appropriate url or open to Git Desktop.
- To view on a web IDE: Click the dropdown labelled "Open in Web IDE" on the top right of the repository, and choose the appropriate IDE.
- This dropdown can also be used to clone the code into VSCode IDE.
- To clone into the Local IDE - in the terminal, type 'git clone' followed by the URL that can be copied from the aforementioned Code URL.
- To fork - Follow the instructions as outlined in the Github Docs here.


#### To deploy to Heroku:

Create an account with [Heroku](https://id.heroku.com/login)
Login with username/password (This requires multi-factor authentication through an external device such as the [Salesforce app](https://www.salesforce.com/solutions/mobile/app-suite/security/))
- Click on "New" > "Create App"
- Use "Europe" as the host
- Implement a distinct name for the app
- Click "Create App"
- Click on the app's name to open the settings and deployment section

- Open the Settings tab and find the section "Config Vars"
- Click "Reveal Config Vars"
- Input the following Key-Value Pairs (This is an example sample set and can be found under 'example.py' in this repository, you will need to configure it with your own settings placed inside the angle brackets - Remove the angle brackets once the information is placed inside them): 

| Key | Value | Explanation |
| ----------- | ----------- | ----------- |
| IP | 0.0.0.0 | Local IP |
| PORT | |  |
| SECRET_KEY | Any secret key | A password for access |
|  |  | Connection to Database |
|  | <database_name> | Database name |
| DEVELOPMENT | FALSE | Turns the workspace off of the development state |
| DEBUG | FALSE | Turns the Debugger off for the workspace |


- Once those are saved, navigate to the Deploy tab
- On Deployment method", click "Github"
- Search the Repo (In this case, for this particular project, type in 'CottageDelights' and select the repo.)
- Enable Automatic deploys
- on Manual Deploy, select the Main branch and click "Deploy Branch"


### Credits
--- 
#### Code and libraries
