# Cottage Delights - Cottagecore Themed Afternoon Tea E-Commerce App

### About the Project:
---


- [Live Preview](https://cottagedelights.herokuapp.com/)
- [Github Repository](https://github.com/digimori/CottageDelights)

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
As a developer, my goal was to make an E-Commerce app with secure payment functionality and to give the user the ability to save their information such as shipping address and order history into a personal profile. 
I also wanted to implement a contact form (in case on questions or issues with orders) and a newsletter model so that the user could sign up to be emailed promotional offers and new products.


### User Stories:
---
I have compiled the Agile User Stories in a Google Sheets document for easy reading and copying in the link below:  

[User Story Google Sheets](https://docs.google.com/spreadsheets/d/1655crCqeP7uN0QqolqXEPqaM7uZFYanWhCC3R0CrUDM/edit?usp=sharing)


### Design Choices (Fonts, Colours and images, cards and hamburger menus):
---
#### Font and Colours:

* Fonts: 
For the fonts, I chose and mix of 
I eventually opted to disregard the cursive fonts aside from large titles and logo fonts as they are very difficult for those with dyxlexia to read and I wanted to maintain accessibility.

* Colours:
As with previous projects, I went for a beige theme and found the default AntiqueWhite CSS to be perfect for it. Cottagecore is based in a lot of neutral and muted colours, embodying vintage themes and simple living, so I wanted to take that idea of keeping it simple and integrate it into my design.
The button colours are a muted purple as I found it to be a nice contrast that wasn't too harsh on the eyes to read. 

* Offcanvas Navigations:
I chose to use Offcanvas for my mobile navigation as it doesn't have an effect on the overall content of the page and positioning compared to a collapsible nav. This makes media queries easier to separate out from a developer standpoint and gave me somewhere to comfortably put the search bar and account links without compromising the site's design.

* Home page images:
I choose images of tea, cakes and cottage themed aesthetics to continue the theme of a cottagecore themed afternoon tea. 


### Wireframes
---

<details>
  <summary>Wireframes (Adobe Photoshop):</summary>

 ####  Desktop, Mobile

 I have chosen to only include desktop vs mobile views here as the tablet versions are just sized down versions of the desktop views.

- Index page:
![Index - Home Page](/static/readmeimages/cottagedelightshomewireframe.png)

- Products page:
![Products page](/static/readmeimages/cottagedelightsproducts.png)

- Product Details page:
![Product details](/static/readmeimages/cottagedelightsproductsdetail.png)

- Profile Page (Once Logged in, cannot be accessed prior to login):
![Profile - Logged in](/static/readmeimages/userprofile.png)

- Add-Products page (Superuser/Admin must be logged in):
![Add Products]()

- Edit Products page(Superuser/Admin must be logged in):
![Edit Products]()

- Delete Modal check(Superuser/Admin must be logged in):
![Delete Modal]()

- Shopping Cart page:
![Shopping Cart](/static/readmeimages/cottagedelightsshoppingcart.png)

- Payment Page:
![Payment page](/static/readmeimages/checkoutform.png)

- Order Confirmation page:
![Order Confirmation]()

- Newsletter Signup:
![Newsletter signup](/static/readmeimages/newsletter.png)

- Contact Form:
![Contact Form](/static/readmeimages/contactform.png)

</details>

---

### Database Schema
---
Models:
<details>
<summary>Products</summary>

class Product model:

| id | Name | Properties | Primary/Foreign Key |
| ----------- | ----------- | ----------- | ----------- |
| 1 | category | 'category', null=True, blank=True, on_delete=models.SET_NULL | Foreign |
| 2 | sku | CharField, max_length | Primary |
| 3 | name | CharField, max_length, null=True, blank=True | Primary |
| 4 | description | TextField | Primary | 
| 5 | ingredients | CharField, max_length | Primary |
| 6 | weight | CharField, max_length, null=True, blank=True | Primary |
| 7 | storage | TextField, null=True, blank=True | Primary |
| 8 | price | DecimalField, max_digits, decimal_places | Primary |
| 9 | rating | DecimalField, max_digits, decimal_places, null=True, blank=True | Primary |
| 10 | image_url | URLField, max_length, null=True, blank=True | Primary |
| 11 | image | ImageField | null=True, blank=True |
</details>

<details>
<summary>Categories</summary>

class Category model:

| id | Name | Properties | Primary/Foreign Key |
| ----------- | ----------- | ----------- | ----------- |
| 1 | name | CharField, max_length | Primary |
| 2 | friendly_name | CharField | max_length, null=True, blank=True | Primary |

There is also a Meta class inside this mode, where Category can become "Categories" in the instance of plurals. 

</details>

<details>
<summary>Checkout</summary>

class OrderRecord model:  

| id | Name | Properties | Primary/Foreign Key |
| ----------- | ----------- | ----------- | ----------- |
| 1 | order_number | CharField, max_length, null=False, editable=False | Primary |
| 2 | userprofile | ForeignKey, UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' | Foreign |
| 3 | full_name | CharField, max_length, null=False, blank=False | Primary |
| 4 | email | CharField, max_length, null=False, blank=False | Primary |
| 5 | phone_number | CharField, max_length, null=True, blank=True  | Primary |
| 6 | address_line_1 | CharField, max_length, null=False, blank=False  | Primary |
| 7 | address_line_2 | CharField, max_length, null=True, blank=True  | Primary |
| 8 | town_city | CharField, max_length, null=False, blank=False | Primary |
| 9 | county | CharField, max_length, null=True, blank=True  | Primary |
| 10 | country | CountryField, blank_label='Country *', null=False, blank=False | Primary |
| 11 | postcode | CharField, max_length, null=False, blank=False | Primary |
| 12 | shopping_cart | TextField, null=False, blank=False, default='' | Primary |
| 13 | order_total | DecimalField, max_digits, decimal_places, null=False, default=0 | Primary |
| 14 | delivery_cost | DecimalField, max_digits, decimal_places, null=False, default=0 | Primary |
| 15 | grand_total | DecimalField, max_digits, decimal_places, null=False, default=0 | Primary |
| 16 | date | DateTimeField, auto_now_add=True | Primary |
| 17 | stripe_pid | CharField, max_length, null=False, blank=False, default='' | Primary | 


class OrderLineItem model:

| id | Name | Properties | Primary/Foreign Key |
| ----------- | ----------- | ----------- | ----------- |
| 1 | order | ForeignKey, OrderRecord, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems | Foreign |
| 2 | product | ForeignKey, Product, null=False, blank=False, on_delete=models.CASCADE | Foreign | 
| 3 | quantity | IntegerField, null=False, blank=False, default=0 | Primary |
| 4 | lineitem_total | DecimalField, max_digits, decimal_places, null=False, blank=False, editable=False | Primary | 


</details>

<details>
<summary>User Profile</summary>

class UserProfile model:

| id | Name | Properties | Primary/Foreign Key |
| ----------- | ----------- | ----------- | ----------- |
| 1 | user | OneToOneField, User, on_delete=models.CASCADE | Primary |
| 2 | default_phone_number | CharField, max_length, null=True, blank=True | Primary |
| 3 | default_address_line_1 | CharField, max_length, null=True, blank=True | Primary |
| 4 | default_address_line_2 | CharField, max_length, null=True, blank=True | Primary |
| 5 | default_town_city | CharField, max_length, null=True, blank=True | Primary |
| 6 | default_county | CharField, max_length, null=True, blank=True | Primary |
| 7 | default_postcode | CharField, max_length, null=True, blank=True | Primary |
| 8 | default_country | CountryField, blank_label='Country *', null=True, blank=True | Primary |


</details>

<details>
<summary>Contact Form</summary>

class ContactForm model:

| id | Name | Properties | Primary/Foreign Key |
| ----------- | ----------- | ----------- | ----------- |
| 1 | name | CharField, max_length | Primary |
| 2 | email | EmailField, null=False, blank=False | Primary |
| 3 | order_number | CharField, max_length | Primary |
| 4 | description | TextField, null=False, blank=False | Primary |

</details>

<details>
<summary>Newsletter</summary>

class Newsletter model:

| id | Name | Properties | Primary/Foreign Key |
| ----------- | ----------- | ----------- | ----------- |
| 1 | email | EmailField, null=True | Primary |
| 2 | date | DateTimeField, auto_now_add=True | Primary |

class MailMessage model:
| id | Name | Properties | Primary/Foreign Key |
| ----------- | ----------- | ----------- | ----------- |
| 1 | title | CharField, max_length, null=True | Primary |
| 2 | message | TextField, null=True | Primary |


</details>



### Features and Navigation
---

#### Login/Logout/Register


<details>
<summary>Logged In Index and Registration</summary>

The registration page is adapted from the built in AllAuth templates and modified to match the rest of the UX design.

![Registration Page](/static/readmeimages/signup.png)  

If the user is logged in as a superuser, it will display the "Product Management tab", otherwise, this will be missing with the user only able to Logout or view their Profile.  

![Logged in Superuser Nav-bar - Index](/static/readmeimages/ifsuperusermyaccount.png) 

</details>

<details>
<summary>Logout page</summary>

I implemented a logout page as a stopping point in case the user accidentally clicked and wanted to remain logged in.

![Logout](/static/readmeimages/confirmsignout.png)

</details>

#### Profile

<details>
<summary>Profile Page</summary>

The profile layout has two functions:
 - To display Shipping details saved by user and allow them to update them:  

![Full Profile Page](/static/readmeimages/defaultdelivery.png)

- To view the order history of products the user has purchased:

User's order history:
![Order History](/static/readmeimages/orderhistory.png)
</details>


<details>
<summary>Search Bar</summary>

The search bar is simple and filters by product name and description.  
There is also a section that tells the user how many results were found.

![Search Bar](/static/readmeimages/searchfunction.png)

</details>

<details>
<summary>Product Cards</summary>

![Product Details]()

</details>


### Adding Products

<details>
<summary>Add Product Form</summary>

The implementation of the Add Product form was created with the idea in mind that the Superuser can add and modify the products and their details from the live site itself without having to explicitly log into the backend Django admin.

![Add Product Form](/static/readmeimages/productmanagementform.png)  

The image upload allows for either image url input or direct upload from the admin's device.

![Image upload](/static/readmeimages/productmanagementimage.png)

</details>


### Editing Products

<details>
<summary>Edit Form for Product Management</summary>

The implementation of the Edit Product form was created with the idea in mind that the Superuser can modify the products and their details from the live site itself without having to explicitly log into the backend Django admin.

![Edit Product](/static/readmeimages/editingproductform.png)

The image upload allows for either image url input or direct upload from the admin's device whilst also showing what the current uploaded image is.

![Edit image](/static/readmeimages/editproductimage.png)

</details>


#### Deleting Products

<details>
<summary>Product Deletion</summary>

I included the implementation of defensive programming in the form of a modal in order to make sure the user/admin wanted to delete what they had clicked.

![Delete Modal](/static/readmeimages/deletionmodal.png)

</details>

#### Navigation compression on mobile
<details>
<summary>Off-Canvas navigation </summary>

For the Off-Canvas I chose to have all of the navigation compressed onto it, including the search bar and My Account functions.  
This just made it overall easier to manage, especially with Media Queries and aside from the toggler, they don't interfere too much with the site's layout otherwise.

![Offcanvas compressed/closed](/static/readmeimages/offcanvasclosedmobile.png)

When opened, it reveals the search, account options, shopping cart and site navigation.  

![Offcanvas Opened](/static/readmeimages/offcanvasopen.png)

</details>


### Testing and Validation:
--- 

###  Validation (HTML, CSS, JSHint, Python PEP8)
---
<details>
<summary>HTML</summary>

[HTML Validation using W3 Validator](https://validator.w3.org/)
![Home page](/static/readmeimages/homevalidate.png)
![Products page](/static/readmeimages/productsvalidated.png)
![Product Details page]()
![Shopping cart page]()
![Checkout page]()
![Checkout Success page]()
![Newsletter page](/static/readmeimages/newslettervalidated.png)
![Contact Form](/static/readmeimages/contactformvalidated.png)
![Account Sign in](/static/readmeimages/signinvalidated.png)
![Account Sign up](/static/readmeimages/accountsvalidated.png)
![User Profile page]()
![Add Products page]()
![Edit Products]()

</details>

<details>
<summary>CSS, JavaScript and jQuery</summary>

[CSS Validation using Jigsaw](https://validator.w3.org/)
![CSS Validation](/static/readmeimages/cssvalidation.png)  

[jQuery and JavaScript Validation using JSHint](https://jshint.com/)
- I decided to put all of it into one document to save space in the readme.  
- Stripe being an "undefined variable" is incorrect as it is pulled from the Stripe module
  
![jQuery]()

</details>

<details>
<summary>Python PEP8</summary>

[PEP8 Validation using CI's Linter](https://pep8ci.herokuapp.com/)

- Home Views:  

![Home views](/static/readmeimages/homelinted.png)

- Cart views:  

![Cart views](/static/readmeimages/cartlinted.png)

- Product views:  

![Products views](/static/readmeimages/productslinted.png)

- Checkout views:  
![Checkout views](/static/readmeimages/checkoutlinted.png)

- Webhook Handler:  

![Webhook Handler](/static/readmeimages/webhookhandlerlinted.png)

- Webhooks:  

![Webhooks](/static/readmeimages/webhooklinted.png)

- Newsletter views:  

![Newsletter views](/static/readmeimages/newsletterlinted.png)

- Contact Form views:  

![Contact Form views](/static/readmeimages/contactformlinted.png)

- User profile views:  

![User profile views](/static/readmeimages/userprofilelinted.png)


</details>


#### Manual Testing - User Testing

| Test | Expectation | Pass/Fail |
| ----------- | ----------- | ----------- |
| User Registration | User is able to register account | Pass |
| Registration Confirmation | Confirmation Email sends to user | Pass |
| User Sign in/Out | User is able to sign in and sign back out to end session | Pass | 
| Adding to cart | User is able to add products to cart, adjusting quantity on product page before doing so | Pass |
| Updating cart | User is able to update and delete products from their cart page | Pass | 
| User checkout | User is able to securely checkout using Stripe payments | Pass |
| Order confirmation | User receives a confirmation email with order details | Pass |
| Retain details in user account | User is able to save default shipping information to their profile page | Pass |
| Order History | User is able to access a record of their order history | Pass |
| Toasts | Toasts pop up throughout the site, informing the user of their actions such as adding to cart | Pass |
| Newsletter | User is able to signup to a newsletter list - Detail stored in backend admin | Pass |
| Newsletter message | Admin is able to compose and send newsletter to users stored in mailing list | Pass |
| Contact Form | User is able to send an email to the admin as a method of contact | Pass | 




### Media Queries

I used the Chrome Dev tools to implement changes in real time before performing a final commit on the code itself.  
This was also used to test the responsiveness as I could change the breakpoints as I edited each line of code.


### Bugs and Fixes
---
| Bug/Issue | Explanation | Fix Implemented |
| ----------- | ----------- | ----------- |
| Product Redirection | Once a product has been added by the admin, the views do not seem to correctly redirect back to the product itself if an image was not uploaded, despite a placeholder being present.  | This was a typo error, I had added a link to the if statement that linked back to the product image, which if none is going to be there aside a placeholder, it will error. Fixed. |
| SMTP Security Changes | SMTP security changes from Google now make the App password unable to link in as a third party so sending e-mails now takes too long to respond to the server in order to send | Fixed by adding Logging into settings.py | 
| Registration Confirmation Email | Does not send to user, SMTP/AllAuth Issue | Fixed by adding Logging to settings.py |
| Validation Issue with Offcanvas | Does not accept unordered lists inside the offcanvas divs as valid | Fixed - De-nested lists in Offcanvas | 
| User Registration | User is able to register an account when running through Gitpod but not Heroku | PostgreSQL migration issue, remigrated database to Heroku - Fixed | 
| Toast close | Toast close button will not close the toast notification | - |



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

#### Workstation setup and installation:
<details>
<summary>Initial Setup and Migrations</summary>

In Terminal:
```
pip3 install Django==4.2.2 (This is the current LTS and is what is used in this project)
```
  
In settings.py:
```
ALLOWED_HOSTS=['8000-YOUR-GITPOD-WORKSPACE', localhost, 'HEROKU-APP-URL']
```

Create a .gitignore file via terminal:
```
touch .gitignore
```

In the .gitignore file, ensure the code has the following:
```
*.sqlite3
*.pyc
__pycache__/
```
  
Freeze requirements.txt via terminal:
```
pip3 freeze > requirements.txt
```

Run Initial Migrations via terminal:
```
pip3 manage.py makemigrations  
pip3 manage.py migrate
```

Create superuser for admin access and follow the instructions in the terminal:
```
python3 manage.py createsuperuser
```

Install AllAuth package in terminal:
```
pip3 install django-allauth==0.41.0
```

Install Pillow in terminal:
```
pip3 install pillow
```

Install unicorn in terminal:
```
pip3 install gunicorn
```

In the Procfile, set the following:
```
web: gunicorn cottagedelights.wsgi:application
```

Install Django Crispyforms in terminal:
```
pip3 install django-crispy-forms==1.14.0
```

Install Django countries:
```
pip3 install django-countries==7.2.1
```

Install fixtures from models:
```
python3 manage.py loaddata categories
python3 manage.py loaddata products
```

* NOTE: MAKE SURE CATEGORIES ARE ALWAYS LOADED FIRST.

Make migrations again via terminal as before:
```
pip3 manage.py makemigrations  
pip3 manage.py migrate
```

* Remember to freeze requirements whenever a new app or library is installed!
* Note - Due to Heroku backport errors, please ensure that in the requirements.txt file, that the backport reads as follows:
```
backports.zoneinfo==0.2.1;python_version<"3.9"
```

</details>

#### Stripe Deployment:
<details>
<summary>Stripe and Webhook installation</summary>

- Create an account on the [Stripe Website]()
- Test API keys
- Doumentation
- Accept Payment

Install Stripe in your workspace terminal:
```
pip3 install Stripe
```

In your Workspace environment variables, create the following variables:

These can be found in the Developer tab > API keys 

| Variable name | Value |
| ------ | ------ |
| STRIPE_PUBLIC_KEY | YOUR_STRIPE_PUBLIC_KEY |
| STRIPE_SECRET_KEY | YOUR_STRIPE_SECRET_KEY |


Add the variables, if not already cloned, to your settings.py files as the following:
```
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
```

To install the webhooks, navigate to the following:
- Stripe dashboard > Developers > Webhooks > Add Endpoint

In the endpoint URL, if using Gitpod, input your Gitpod URL as follows:
```
https://8000-YOUR-GITPODWORKSPACE.gitpod.io/checkout/wh/
```

If using a live deployed site, such as Heroku:
For Live:
```
https://YOUR-LIVE-APP-URL/checkout/wh/
```

Once the Webhook has been created, navigate back to the created Webhook  
Reveal the "Signing Secret" found underneath the endpoint URL and copy it
Add this to your environment variables under:

| Variable name | Value |
| ------- | ------- | 
| STRIPE_WH_SECRET | YOUR_SIGNING_SECRET |


Then, ensure the following is in your settings.py file:
```
STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
```

In the terminal:
```
export STRIPE_WH_SECRET=<YourSigningSecret>
```

And finally, start the server:  
```
python3 manage.py runserver
```

</details>

#### Postgres Setup - ElephantSQL database:

<details>
<summary>Creating and setting up the database via ElephantSQL</summary>

- Create an account with [ElephantSQL](https://www.elephantsql.com/) using the "TinyTurtle" plan.
- Login with your Github account (The one you used to clone this project)

In the Create new team form:
- Add a team name (your own name is fine)
- Read and agree to the Terms of Service
- Select Yes for GDPR
- Provide your email address
- Click “Create Team”

Creating the Database:
- Navigate to your dashboard
- Click the "Create new instance" button

Set up your plan  
- Give your plan a Name (this is commonly the name of the project)
- Select the Tiny Turtle (Free) plan
- You can leave the Tags field blank
- In "Select Region", select the region closest to you
- Click "Review"
- Double check your inputted data
- Click "Create instance" to proceed
- Return to the ElephantSQL dashboard and click on the database instance name for this project
- In the URL section, copy this URL and save it for later - You will need it for setting up your Heroku app
</details>

<details>
<summary>Connecting the Database to your local IDE</summary>

- In the terminal, install dj_database_url and psycopg2, both of these are needed to connect to your external database:
```
pip3 install dj_database_url==0.5.0 psycopg2
```

- Update your requirements.txt file with the newly installed packages**:
```
pip freeze > requirements.txt
```

** Note: Make sure to update the backports as previously mentioned as each time you freeze requirements, it will overwrite it.

- In settings.py, find the DATABASE object and alter it as follows:
```
DATABASES = {
     'default': dj_database_url.parse('your-database-url-here')
 }
 ```

 DO NOT COMMIT YOUR DATABASE YET.

 - In the terminal, run the showmigrations command to confirm you are connected to the external database:
 ```
  python3 manage.py showmigrations
 ```

- Migrate your database models to your new database:
```
python3 manage.py migrate
```

- Load in the fixtures. Please note the order is very important here. We need to load categories first and then the products:
```
python3 manage.py loaddata categories
python3 manage.py loaddata products
```

- If you have not created a superuser yet, this must be done now (See initial setup)

- Finally, in settings.py, ensure that the following code is there:
```
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     }
 }
```

</details>


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
| STRIPE_PUBLIC_KEY | Your Stripe public API key | API key for access |
| STRIPE_SECRET_KEY | Your Stripe secret API key | API key for access |
| STRIPE_WH_SECRET | Your Stripe Signing Secret key | Key for Webhook access |
| SECRET_KEY | Any secret key | A password for access |
| DATABASE_URL | Postgres URL | Connection to Database |
| USE_AWS | TRUE | Use AWS for static storage |
| AWS_SECRET_ACCESS_KEY | Your AWS Secret Access Key | API key for access | 
| AWS_ACCESS_KEY_ID | Your AWS Public Access Key | API key for access |
| EMAIL_HOST_PASS | Your app password | Allows scure access to SMTP |
| EMAIL_HOST_USER | youremail@example.com | Email you wish to send emails from | 
| DEVELOPMENT | FALSE | Turns the workspace off of the development state |
| DEBUG | FALSE | Turns the Debugger off for the workspace |


- Once those are saved, navigate to the Deploy tab
- On Deployment method", click "Github"
- Search the Repo (In this case, for this particular project, type in 'CottageDelights' and select the repo.)
- Enable Automatic deploys
- on Manual Deploy, select the Main branch and click "Deploy Branch"


#### Connecting your Database to Heroku:

- Temporarily disable collectstatic in the terminal:
```
heroku config:set DISABLE_COLLECTSTATIC=1 --app APP_NAME_HERE
```

- Push to both Github and Heroku main branches

- Create a two Django Secret keys using [this link](https://miniwebtool.com/django-secret-key-generator/)

- Add one to your Environment variables and one to your Heroku Config vars (detailed above) under SECRET_KEY


#### AWS S3 bucket Deployment:

- Create an account at [Amazon Web Services](https://aws.amazon.com/)
- Log in to the service once account has been created and verified
- Search through "Find Services" for S3
- Click "Create Bucket"
- It is recommended that the names for this bucket also match your deployed app name
- Select Region closest to you, as with Heroku and Postgres
- Allow public access to bucket
- Click Create bucket

Once the bucket has been created, Go to the following settings (These are conveniently on one page, just scroll):
- Object Ownership - This needs to have ACLs enabled and Object Ownership preferred.
- Properties - Turn on Static web hosting

Under Permissions:
- Paste the following into the CORS configuration:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```

In the Bucket Policy tab:
- Select "Policy Generator" (Open it in a new tab, you will need to come back to this page)
- The policy type will be "S3"
- In the "Principles" input field, place an asterisk (*) to select all
- Action dropdown - Select "Get Object"
- Back in the bucket policy, copy the ARN and paste it into the ARN box on the Policy generator page
- Click "Add Statement"
- Click "Generate policy" and copy the code that opens in the modal
- Paste this into the Bucket Policy tab and add /* to the end of your app URL found in the code

The ACLS:
In the access control list, check the following boxes:
- Bucket Owner - List, Read, Write
- Everyone - List

Identify and Access Management (IAM):



#### SMTP Gmail setup:


### Credits
--- 
#### Code and libraries
