[View live project here](https://hanks-dog-parlour.herokuapp.com/)

## **Content**

- [**UX (User Experience)**](#ux-user-experience)
  - [**Target Audience**](#target-audience)
  - [**Project Goals**](#project-goals)
  - [**User Goals**](#user-goals)
  - [**Site Owner Goals**](#site-owner-goals)
  
- [**Design Choices**](#design-choices)
  - [**Fonts**](#fonts)
  - [**Colours**](#colours)
  - [**Imagery**](#imagery)
  - [**Logo**](#logo)
  - [**Wireframes**](#wireframes)
  - [**Site Map**](#site-map)
  - [**Database**](#database)

- [**Features**](#features)
  
- [**Testing**](#testing)
  - [**Functionality Testing**](#functionality-testing)
  - [**User Story Testing**](#user-story-testing)
  - [**Performance Testing**](#performance-testing)
  - [**Responsive**](#responsive)
  - [**W3C Validator**](#w3c-validator)

- [**Bugs**](#bugs)

- [**Technologies**](#technologies)
  - [**Languages**](#languages)
  - [**Libraries**](#libraries)
  - [**Tools**](#tools)

- [**Deployment**](#deployment)

- [**Credits**](#credits)
  - [**Code**](#code)
  - [**Content**](#content)
  - [**Images**](#images)
  - [**Videos**](#videos)
  - [**Inspiration**](#inspiration)
  - [**Acknowledgements**](#acknowledgements)
  
  ## **UX (User Experience)**

  [Back to contents](#content)

### **Target Audience**
- Dog lovers
- All ages

[Back to contents](#content)

### **Project Goals**
The primary goal of this project is to create a website that works perfectly, is visually appealing in design, and easy to navigate for a first-time user. It allows users to perform not only the basic functionalities in a website (for example sign up/login, ability to purchase items, and perform payments), but also to ensure that users have a great experience and more interactivity within the site through additional functionalities such as put items into their basket and purchase these items.

### **User Goals**
The user will be looking for:
- A website that is straight forward and intuitive to use, easy to navigate and also make a purchase.
- A website where there is a variety of products that can also be searched individually by the user.

### **Site Owner Goals**
As a site owner, I would like to provide a clear, easy to navigate, eye catching site that users will enjoy visiting and find everything they are looking for. I want to give access to a shop for users to buy items. I would also want the user to gain access to a basket feature which will allow the user to come back to their basket and have the items they have selected ready for when they want to pay. By achieving this, the user will be able to delete and update their basket with no trouble.

[Back to contents](#content)

### **User Stories**
As a shopper I want to be able to:

- I want the main purpose of the site to be clear for when new/exisiting customers visiy.
- I would like the site to be easy to navigate so that the content can be founf quickly and with ease.
- I want to view a list of products and items by searching for individual words.
- I would like to view my total purchases at any time and have the option to update and delete items out of my shopping bag.
- I would like to successfully register for an account and proceed to log in.
- I want to be able to store my shipping details so that it’s easier for me to check out.

[Back to contents](#content)

## **Design Choices**

### **Fonts**

![fonts](ReadMe/media/fonts/font-1.png)
![fonts](ReadMe/media/fonts/font-2.png)
![fonts](ReadMe/media/fonts/font-3.png)
![fonts](ReadMe/media/fonts/font-4.png)
![fonts](ReadMe/media/fonts/font-5.png)
![fonts](ReadMe/media/fonts/font-6.png)

When choosing a font I came across a number of really good fonts to chose from on google font and also dafont just to see if they had anything that google font did not. After a meeting with the client and vigorous testing I decided to go with oswald as this was the most eye catching and was very similar to the original logo that the client had sent me. I also went with san-serif as the backup font just in case my chosen font failed.

### **Colours**

![fonts](ReadMe/media/Color/hanks.png)

The website I used to get my pallet was coolors.com which I uploaded the logo that the client gave me and this generated a pallet for. I chose these colors to have a choice just in case one color collided with another. I only use one three colors from this pallet wich where #000000, #ffffff and #D1A702. 

### **Imagery**

I will create a image for the main home page banner which will feature a random dog parlour. I had to import this image into photoshop to alter a few things so that the image was suitable for my website.

The imagery came straight from the client herself so i never had to search for any images. This made the process of making the website quicker as I never had to look arround for any images to use. The images are located in my static folder. The only image i grabbed from google was a no image sign which was used just incase the user admin did not want a image on there or accidently added a product but forgot the image.

[Back to contents](#content)

### **Logo**

[Back to contents](#content)

### **Wireframes**

Initial Wireframes were produced showing the Products, home page, order summary, Basket and mobile nav layouts.

#### **Web**
![fonts](ReadMe/media/wireframes/home-page.png)
![fonts](ReadMe/media/wireframes/mobile-nav.png)
![fonts](ReadMe/media/wireframes/product-page.png)
![fonts](ReadMe/media/wireframes/basket.png)
![fonts](ReadMe/media/wireframes/order-summary.png)

[Back to contents](#content)

### **Site Map**

![fonts](ReadMe/media/site-map.png)

A Site Map was produced for the first development stage, and is shown above. Note that the the orange squares are the pages that only the admin can access so that no one can delete or edit a product.

### **Database**

![fonts](ReadMe/media/schema.png)

1. Home
- Contact
   - This model contains information relating to messages sent by users to the store.

2. Home
- Contact
   - This model contains information relating to messages sent by users to the store.

3. Checkout
- Order
   - This model contains information relating to messages sent by users to the store.
- OrderLineItem
   - This model contains information the products in the customers order, quantity and total with or without a deliery charge.

4. Products
- Product
   - This model contains information relating to all the products for sale on the site.

- Categories
   - This model contains information about the various different categories of products on the site.

4. Profile
- UserProfile
   - This model contains the default order details saved from customers previous orders which they can use for future orders.

[Back to contents](#content)

## **Features**

### **Landing Page**

1. Navbar
- The navbar contains the main links and navigation throughout the site. it remains consistent at the top of each page.
- The navbar is fully mobile responsive and reacts to changes in screen size. It also allows for collapsible menu on mobile screens.
- The navbar also contains all the categories of products on the site through the various drop downs.
- The search bar disappears on mobile view but still works when the search icon is clicked, my account and bag also work on mobile view.

2. Delivery Message
- The delivery banner provides a clear and concise message to the user about needing to spend 50 pound to get free delivery.
- The delivery information banner appears just below the navbar on each page, it is fully mobile responsive and reacts to the changes in screen size.

3. Home Page
- Navigation bar at the top of the page provides for easy and intuitive navigation throughout the site.
- Distinct image and highlighted section letting the user know exactly what the site is about.
- Search bar at the top ot the page provides for a way for a user to search ther site for a specific item that they are looking for.
- Background image used of a workshop to make it easier to read the text and see the buttons.
- Big shop button ontop of image to direct users straight to the store if needed.

4. Product Page
- The navigation bar at the top of the page displasys all the categories of products on the site for ease of use for the user.
- A user can sort the products throughout the site based on name and price by choosing from the select dropdown at the top of the page.
- When a user searches from the search bar at the top of the page the results are shown on this products page again in paginated format.
- A add or delete function at the bottom of each product for the admin to create, update or delete products.
- Once a product is selected a details page will show stating how many items you would like to purchse and if necessary a dropdown size selector.
- Two big buttons on the bottom of the details page to keep shopping, or to add the item to your basket.

5. Add products
- This page is only available to superusers and can be found by clicking on my account at the top of the page and then selecting product management.
- This page contains a form which a superuser can use to add products to the database and have the products appear on the site when done and form submitted the user gets taken to the products page of the product thehave added and a message appears showing them they have successfully addedthe product to the database.
- Once the amdin has added a product, A message will appear in the top right hand corner stating that the product was successfully added.

6. Edit Products
- This page is only available to superusers and can be found by clicking on my edit link on either the products page or the product details page.
- The edit product page will be a form which is instantiated with the details of the product that a user is editing.
- Once the amdin has edited a product, A message will appear in the top right hand corner stating that the product was successfully edited.

7. Bag
- In the navbar at the thop of the bad on all screen sizes a bag icon will appear, this bag will be turquise and display £0.00 by default. Once a user adds an item to the bag the bag icon will change to a gold color to signify an item in the bag. When a user clicks on the bag icon the will be taken to the bag page.
- When a user clicks on the bag icon when they have no items in the bag the below will be displayed indictaing they have no items in their bag and a keep shopping button to encourage them to add items to their bag.
- When a user clicks on the bag icon when they have items in the bag the below will be displayed the items in their bag and a secure checkout button to encourage customers to move forward to the checkout process and a keep shopping button which encourages them to add more items to their bag.

8. Checkout
- When the user has items in their bag, a secure checkout button will appear, when they click on this secure checkout button on the bag page, they will get taken to the checkout page where they can complete their order and pay for their order via stripe.
- Display order summary of whats in the shopping bag.

9. Profile Page
- Has a profile navigation allowing users to view their information.
- A section with the order they have previousle made.

[Back to contents](#content)

## **Testing**

### **Accessing admin**

- To access the admin the super user is 
  - username - test
  - password - Password@test

### **Make a dummy purchase** 

- To make a dummy purchase, you can use a dummy card number which is:
   - 4242 4242 4242 4242 0424 2424

### **Html Validator**

![fonts](ReadMe/media/test/html.png)
- When testing my html I had a look at the 6 errors that where showing up and my code looks like it is being duplicated but ive gone back through my code and can not see the errors that are showing up.

### **Css Validator**

![fonts](ReadMe/media/test/css/Css.png

### **Javascript Validator**

- Stripe Element ![fonts](ReadMe/media/test/js/stripe-element.png)
- Profile ![fonts](ReadMe/media/test/js/profile.png)

[Back to contents](#content)

## **Bugs**

Bug | Fix
--------|--------
Products_product does not exist | There where no connections in my PostgreSQL on heroku, so I loaded my categories and products in github again and this solved the issue.
Recieving a 500 error and my css was not laoding | I had to change the debug to 'DEVELOPMENT' in os.environ and export the debug to be True so get the css to laod.
Aws no activated |I had some trouble activating my aws account to access the s3/bucket section but the support team at aws helped me sort this out.

[Back to contents](#content)

## **Technologies**

### **Languages**

  - [HTML5](https://en.wikipedia.org/wiki/HTML5). 
    - Used for the main markup language for my game content.
  - [CSS3](https://en.wikipedia.org/wiki/CSS). 
    - Used to style my pages and the content on the game.
  - [JS](https://en.wikipedia.org/wiki/JavaScript). 
    - Used to contact the DOM.
  - [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))

### **Database**
- Development - SQLite
- Deployed site - Heroku PostgreSQL

### **Storage**
- Amazon AWS S3 - used to store static files.

### **Payment**
- Stripe - fully integrated payments platform.

### **Framework**
- Django - web development framework.
- jQuery - to assist with JavaScript coding and DOM manipulation.
- Bootstrap - to assist with responsive design.

### **Libraries**

- coolers.co Color scheme generator.
- Google Fonts Font library.
- Font awesome Icons.
- jQuery JavaScript Library.
- Heroku Cloud platform.
- Website Mockup Generator used to generate responsive screenshot.
- Responsinator.com.
- Imgur.
- psycopg2 - PostgreSQL database adapter for Python. Used as part of the Heroku deployment process.
- flake8-django - Flake8 plug-in for Django, for python code validation.
- pillow - Python imaging library.
- gunicorn - Python WSGI HTTP Server for UNIX. Used as part of the Heroku deployment process.
- django-countries - Django application providing country choices for use with forms etc. Used to populate country choices on the Country dropdowns.
- dj-database-url - Django database configuration utility. Used to configure connection to the Heroku deployed postgres database.
- django-crispy-forms - enables enhanced rendering of Django forms including integration with Bootstrap.
- django-allauth - user authentication and account management.
- dbdiagram - used to plan and visualise the data schema prior to and during development.
- MindMup - used to produce the Site Map.
- DrawSql - shcema database diagram

### **Browser**

- Google Chrome

### **Tools**

- [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
  - [GitHub:](https://github.com/) 
    - GitHub is used to store the projects code after being pushed from Git.
  - Photoshop - Used to edit all my images in my project.

[Back to contents](#content)

## **Deployment**

Once app was setup and ready to go I deployed to Heroku by following the steps below:

* I created an app on the heroku website which i called ms4-fit-as-a-fiddle

    * I clicked on the new button.
    * I then clicked on the create a new app link.
    * I then gave my app the name of ms4-fit-as-a-fiddle and chose europe as my closest region.
    * Finally, I selected to create my app.

* Next, I set up the postgres database.

    * in Heroku,
        * Go to app resources section, search for postgres
        * then I chose to add to project and chose the free plan for my project.
        * In order to use Postgres, I had to install two dependecies in gitpod, dj_database_url and psycopg2
    
    * in Gitpod
        * I installed both dj_database_url and psycopg2 using the command:
            * `pip install`
        * then, using the command: pip3 freeze > requirements.txt, I added the dependencies to the requirements file which is needed by Heroku.
        * Then in settings.py I imported dj_database_url:
            * `import dj_database_url`
        * then, I commented out the current database settings and replaced it with the settings of the postgres database:
        ```
        DATABASES = {
            'default': dj_database_url.parse('DATABASE_URL')
        }
        ```
        * DATABASE_URL above is an environmental variable and as such should not be shown  in version control. The database url can be found from your app config settings in heroku.
        * Once the above method is set up, models need to be migrated to the new database using the command below:
            * `python3 manage.py migrate`
        * I then created a new superuser for my site on heroku using the command below:
            * `python3 manage.py createsuperuser`
        * When that was done I then commited my changes and made sure not to include environmnet variables in the version control.
        * Then, I created an if-else statement in the settings.py to use Postgres if the DATABASE_URL variable is available and otherwise use the default database in gitpod.
        ```
        if "DATABASE_URL" in os.environ:
                DATABASES = {
                    "default": dj_database_url.parse(os.environ.get('DATABASE_URL'))
                }
          else:
                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': BASE_DIR / 'db.sqlite3',
                    }
                }
        ```
        * The postgres database should now be ready for use.

    * Gunicorn
        * For the app to work on heroku we need a way for heroku to tell that the app is a web application, which is where Gunicorn comes in.
        * Installing Gunicorn
            * `pip3 install Gunicorn`
        * A Procfile then needs to be created to tell heroku how to run our app. this is acheieved below:
            * `touch Procfile`
        * In the Procfile we need to tell it to use a webserver, this is achieved by placing the below code in the procfile:
            * `web: gunicorn <appname>.wsgi:application`
    
    * We now need to connect to Heroku in the terminal on gitpod
        * use the following command
            * `heroku login -i`
        * Login using your email and password that you used to create an account with on heroku website.
        * then, I disabled the collection of static files temporarily until AWS has been set up.
            * `heroku config:set DISABLE_COLLECTSTATIC=1 --app <appname>`
            * the --app command is used when you have more than one app in your heroku account
        * Now, in settings I added heroku into my list of allowed hosts, and localhost so the project can still b run locally using the following settings.
            * `ALLOWED_HOSTS = ["<heroku appname>.herokuapp.com", "localhost"]`
        * changes were then pushed to Github
        * Then I needed to set up pushing to heroku achieved below
            * `heroku git:remote -a <heroku appname>`
        * then the project gets pushed to github using:
            * `git push heroku master`
        * Heroku now builds the app.
    
    * On the Heroku Website
        * Go to the deploy section of the app.
        * I searched for the app being used in github
        * When it was found I connected and then clicked on enable Automatic deploys
        * Now any changes pushed to Github will automatically be pushed to Heroku too.
    
    * Amazon AWS
        * Amazon AWS was used to store both static and media files of my project
        * I created an AWS account and worked through the process of signing-in. Once my account was setup I was able to set my project up on aws.
        * first, I needed to create a bucket.
            * search for aws s3 service.
            * click on the Create Bucket button.
            * Give the bucket a unique name and then select the region.
            * uncheck the block public access and acknowledge that the bucket will now be public.
            * click create bucket.
        * Bucket settings
            * Properties
                * Go to the bucket Properties section
                * Turn on static website hosting
                * in the index and error text inputs, add index.html and error.html.
                * then, click save.
        * Permissions
            * Go to the bucket Permissions section.
            * In the cors config paste in the below code:
                * ```
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
                            "ExposedHeaders": [

                            ]
                        }
                    ]
                  ```
            * In the bucket policy, click on the generate policy
        * Policy
            * Select S3 bucket policy
            * Add * to the principal field to select all principals
            * select action to get object
            * Paste in your ARN which can be found on the bucket policy page.
            * click add statement
            * then, click on the generate policy button
            * then, copy and paste the new policy into your bucket policy
            * also, add /* onto the end of the resources key
            * and, click save.
        * Access Control List
            * Go to the Access Control List section.
            * set list objects permission to everyone.
    
    * Create a new user

        * On the admin page for aws search for IAM to add a new user
        * Create a group
            * We need to create a group to put our user in
            * Click create a new group and name it.
            * click through to the end and save the group.
            * create a group policy
                * click policy and the click create policy
                * select the JSON tab and then import managed policies.
                * search s3 and select on Amazons3fullaccess and import.
                * in the resources section, paste in the ARN that was used above.
                * click through to review policy.
                * fill in the name and description and then click generate policy.
            * back into the group, click on permission and attach the policy.
            * find the policy you have just created and attach it.

        * Create the user
            * select users from the sidebar and then click on add user
            * create a username and then select programmatic access then click on next.
            * select the group to add your user too
            * click through to the end and then click create user.
            * Download the CSV file containing the user keys needed to access the app
    
    * Connect bucket to Django
        * first install two packages in the IDE, boto 3 and django storages, seen below:
            * ```
                pip3 install boto3
                pip3 install django-storages
              ```
        * Now we need to add this to our requirements.
            * `pip3 freeze > requirements.txt`
        * storages then needs to be added to installed apps in settings.py
        * an environment variable called USE_AWS needs to be set up to run the code on heroku.
        * The settings needed for the project in the settings.py file are below:
            * ```
                if "USE_AWS" in os.environ:
                    # Bucket configurations
                    AWS_STORAGE_BUCKET_NAME = "<bucket name>"
                    AWS_S3_REGION_NAME = "<bucket region>"
                    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID") # taken from downloaded csv file
                    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY") # taken from downloaded csv file
                    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

                    # static and media files
                    STATICFILES_STORAGE = "custom_storages.StaticStorage"
                    STATICFILES_LOCATION = "static"
                    DEFAULT_FILE_STORAGE = "custom_storages.MediaStorage"
                    MEDIAFILES_LOCATION = "media"

                    # now need to override static and media Urls for production
                    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
                    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
              ```
        * Back in heroku click on settings tab and then click reveal config vars.
        * Then set up the environmental variables as required.
        * Back in the IDE, we need to create a custom storages.py to tell django that in production we want to use Amazon S3 to store our static and media files
        * import S3Boto3Storage at the top of the custom_storages.py file.
        * Set up classes to tell django where to store the files as shown below:
            * ```
                class StaticStorage(S3Boto3Storage):
                    location = settings.STATICFILES_LOCATION
                
                class MediaStorage(S3Boto3Storage):
                    location = settings.MEDIAFILES_LOCATION
              ```
        * push all the changes to Github from the IDE
    
    * Add Media files to AWS
        * in your AWS bucket, create a new folder called media
        * select upload and then upload all your image files
        * select to grant public access
        * finally, click to upload your files.
    
    * Setting the project up locally

        * Find your github repo, on the code dropdown.
        * then choose to extract files to your respository.
        * open the IDE of your choice and open the folder contaoining the code using your IDE.
        * Once this is done, you can now download the requirements needed to run the project using the below command in your IDE terminal:
            * ` pip3 install -r requirements.txt `
        * You can also choose to clone your files from github to your repository in the IDE by again, choosing the code dropdown in tour github repo and copying the HTTPS url that is provided in the dropdown.
        * then when the url has been copied return to your terminal and use the code below:
            * ` git clone https://github.com/Brianconn71/fit-as-a-fiddle.git`
        * once this is done, you then need to set up the below environment variables to use full functionality of the site:
            * DJANGO_SECRET_KEY = your secret key
            * STRIPE_PUBLIC_KEY = your stripe public key
            * STRIPE_SECRET_KEY = your stripe secret key
            * STRIPE_WH_SECRET = your stripe webhook secret
            * IN_DEVELOPMENT = True
            * Your stripe variables which can be found on your stripe dashboard
            * You need a Django secret key which can be found [here](https://miniwebtool.com/django-secret-key-generator/)
        * Then you need to migrate the database models to set up your own database.
            * first check for migrations:
                `python3 manage.py makemigrations --dry-run`
            * then make migrations:
                * `python3 manage.py makemigrations`
            * check to see how migrations will work out:
                * `python3 manage.py migrate --plan `
            * lastly, if all looks good, migrate:
                * `python3 manage.py migrate`
        * Now, a superuser account needs to be created to access the admin section, so follow the step below to create a superuser
            * ` python3 manage.py createsuperuser `
        * enter your own username and password
        * finally, we need to run the project to ensure working order and we are good to go.
            * ` python3 manage.py runserver`

[Back to contents](#content)

## **Credits**

### **Content**
  - https://github.com/LukeSmallman/pure-fitness.git
  - https://codepen.io/trending 
  - https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/9e2f12f5584e48acb3c29e9b0d7cc4fe/579bbf01edaf47938e6a860b8f08f275/
  - Slack

### **Images**
- Beth Moyle - Hanks Dog Parlour

 ### **Acknowledgements**
   - My mentor was a really big help in sorting out bits of code that I kept missing.
   - Student support at code institute for their infomation and support.

[Back to contents](#content)