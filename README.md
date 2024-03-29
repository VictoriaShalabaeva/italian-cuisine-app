# Buon Appetito Website

View the live project [Here](https://italian-cuisine-app.onrender.com)

*Buon Appetito* is an interactive website that allows to collect and share recipes of Italian cuisine meal.

The website is designed to be responsive and accessible on a range of devices, making it easy to navigate through.

![Responsive Design](static/images/responsive-design.jpg)

## User Experience (UX)

### User stories

  - **As a user:**

    - I want to search for different recipes and get inspiration to try something new.
    - I want to be able to create my own recipes and store them in my profile. 
    - I want to organize my recipes (to create, edit and delete recipes).
    - I want to share my own recipes with others.
      
### Design

  - **Colour Scheme**

    The main colours used are dark grey #212121, white #FFFFFF and grey #424242.

  - **Typography**

    The Roboto, Dancing Script (Navbar heading) and Courgette (titles) fonts are the main fonts used throughout the whole website with Sans Serif and cursive as the fallback fonts in case for any reason the font isn't being imported into the site correctly. Roboto is a clean font used frequently in programming, so it is both attractive and appropriate.

  - **Imagery**
     
    The large background image is striking and catches the user's attention. All other images on the site are the image URLs added by users when creating their recipes.

### Wireframes

  - *Home* page - [View](static/pdf/home-page.pdf)

  - *All Recipes* page - [View](static/pdf/all-recipes.pdf)

  - *Profile* page - [View](static/pdf/profile.pdf)

  - *Add New Recipe* page - [View](static/pdf/add-new-recipe.pdf)

  - *Log In* page - [View](static/pdf/log-in.pdf)

  - *Register* page - [View](static/pdf/register.pdf)

## Features

### Existing Features

- The website is responsive on many device sizes (down to 320 px).

- The website allows users to Create, Read, Update and Delete recipes. This displays full CRUD functionality.

- Any user can:

  - register an account,
  - log in as an existing user,
  - log out,
  - view his profile page with a list of recipes that have been added,
  - view, edit and delete recipes,
  - search recipes,
  - see which user has created any particular recipe.

### Features Left to Implement

- Recipes rating.

- The possibility to leave a comment on a recipe.

- Admin login functionality to edit or delete recipes added by other users (in case of incorrect or inappropriate information). At the moment, the recipes correction of other users are done by accessing the data in MongoDB.

- Advertisement integration (to promote any branded product in the recipes description).

- A *Scroll to top* button.

- *Contact* page.

## Technologies Used

### Languages Used

- HTML5

- CSS3

- Python3

- JavaScript

### Frameworks, Libraries & Programs Used

1. [Materialize:](https://materializecss.com/)

   Grid System to make the site responsive,

   Navbar to make a responsive navigation header,

   Cards components for displaying recipes.

2. [MongoDB:](https://www.mongodb.com/)

   MongoDB was used to store recipes and users data.

3. [Heroku:](https://id.heroku.com/login)

   Heroku was used to deploy and run the application.
   
4. [Flask:](https://flask.palletsprojects.com/en/2.0.x/)

   Flask was used as a framework to develop a web application.

5. [Jinja:](https://jinja.palletsprojects.com/en/3.0.x/)

   Jinja was used to render templates.

6. [PyMongo:](https://pymongo.readthedocs.io/en/stable/)

   PyMongo was used to work with MongoDB from Python.

7. [Werkzeug:](https://pypi.org/project/Werkzeug/)

   Werkzeug was used to generate and check password hash.

8. [jQuery:](https://jquery.com/)

   jQuery was used in JavaScript codes to add functionality to materialize components.

9. [Git:](https://git-scm.com/)

   Git was used for version control. 

10. [GitPod:](https://www.gitpod.io/)

    GitPod was used as an IDE platform for website realization.

11. [GitHub:](https://github.com/)

    GitHub is used to store the project code after being pushed from GitPod.

12. [Google Fonts:](https://fonts.google.com/)

    Google fonts Roboto, Dancing Script and Courgette were used on all pages throughout the project.

13. [Balsamiq:](https://balsamiq.com/)

    Balsamiq was used to create wireframes during the design process.

14. [Squoosh:](https://squoosh.app/editor)

    Squoosh image editor was used to reduces file size of the images.

15. [Am I responsive?:](http://ami.responsivedesign.is/)

    Am I responsive? was used to show how the website looks on different devices.

16. [Font Awesome:](https://fontawesome.com/)

    Font Awesome was used to add icons.

17. [AutoPrefixer:](https://autoprefixer.github.io/)

    AutoPrefixer was used to add vendor prefixes to a CSS code.

18. [Beautifier:](https://beautifier.io/) 

    Beautifier was used to format code in a consistent and readable way.

19. [W3C Markup Validator](https://validator.w3.org/)

    W3C Markup Validator was used to check the markup validity of Web documents in HTML.

20. [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
 
    W3C CSS Validator was used to check the markup validity of Web documents in CSS.

21. [JSHint](https://jshint.com/)

    JSHint was used to detect errors and potential problems in JavaScript code.

22. [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

    Chrome DevTools was used to inspect and modify the website code.

23. [PEP8 online](http://pep8online.com/)

    PEP8 online was used to check a code for PEP8 requirements.

24. [Black Playground](https://black.vercel.app/)

    Black Playground was used to format the Python code.

25. [Render:](https://render.com/)

    After Heroku has ended their free tier offerings for deployment, the present project was migrated to a different free service on an alternative platform Render.

## Testing

The W3C Markup Validator, W3C CSS Validator, JSHint and PEP8 Online services were used to validate HTML, CSS, JS and Python code, respectively, to ensure no syntax error.

- [W3C Markup Validator](https://validator.w3.org/) did not detect any problem in the HTML code on *Home*, *All Recipes*, *Log In* and *Register* pages:

  <img src="static/images/testing/w3c-markup-validator.jpg" alt="Results in W3C Markup Validator." width="500px" height="auto">

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) did not detect any problem in the CSS code:

  <img src="static/images/testing/w3c-css-validator.jpg" alt="Results in W3C CSS Validator." width="500px" height="auto">

- [JSHint](https://jshint.com/) did not detect any problem in the JavaScript code:

  <img src="static/images/testing/jshint.jpg" alt="Results in JSHint." width="500px" height="auto">

- [PEP8 online](http://pep8online.com/) did not detect any problem in the Python code:

  <img src="static/images/testing/pep8-online.jpg" alt="Results in PEP8 online validator." width="500px" height="auto">

### Testing User Stories from User Experience (UX) Section

Please see [Here](testing_user_stories.md) the user stories testing with corresponding screenshots.

### Testing Functionality, Usability and Responsiveness

The manual testing is described [Here](manual-testing.md).

### Further Testing

- The Website was tested on Google Chrome, Mozilla Firefox and Microsoft Edge browsers.

- The screen sizes and devices tested in Chrome DevTools include:

    - 1920 x 1080 
    - 1600 x 992
    - 1440 x 900
    - 1366 x 768
    - Nexus 10 (800 x 1280)
    - iPad (768 x 1024)
    - Surface Duo (540 x 720)
    - iPhone 6/7/8 Plus (414 x 736)
    - Pixel 2 (411 x 731)
    - iPhone 6/7/8 (375 x 667)
    - Nexus 4 (384 x 640)
    - iPhone X (375 x 812)
    - Galaxy S5 (360 x 640)
    - iPhone 5/SE (320 x 568)

- Devices physically tested include:

  - Desktop 
  - Laptop
  - iPhoneXR 
  - Huawei Mate 20 
    
### Bugs

#### Fixed bugs

1. On *Edit Recipe* page, the *ingredients* and *preparation steps* sections were displayed as lists of items (see example in the image below) with additional left-side spaces and new lines (undesired). That was introducing further issues with the correct editing of data in the database.

    The initial code was rewritten using `join()` function and hyphen signs. `join()` function returns a string as a concatenation of strings in a sequence with a chosen separation (new line separation in our case). Hyphen signs (-) added to the start or end of a block remove the whitespaces before or after that block.

    Initial code:
      ```
      {% for ingredient in recipe.ingredients %}
        {{ ingredient }}
      {% endfor %}
      ```
      <img src="static/images/bugs/edit-recipe-bug.jpg" alt="Edit Recipe page bug." width="700px" height="auto">

    Final code:
      ```
      {{- recipe.ingredients|join('\n') -}}
      ```
      <img src="static/images/bugs/edit-recipe-bug-solution.jpg" alt="Correct Edit Recipe page." width="700px" height="auto">

2. The two elements, indicated with red errors (search fields and buttons) in the image below, have *Materialize* classes *s12* and should have occupied two rows in mobile devices. Instead they were placing in one row.

    Initial code:
      ```
      <div class="row valign-wrapper center-align">
        <div class="input-field col s12 l6 xl8">
            <i class="fas fa-search prefix grey-text text-lighten-1"></i>
            <input type="text" name="query" id="query" minlength="3" class="validate" required>
            <label for="query">Search Recipes</label>
        </div>
        <div class="col s12 l6 xl4">
            <button type="submit" class="white-text grey darken-3 waves-effect waves-light btn">
                <i class="fas fa-search left"></i> Search
            </button>
            <a href="{{ url_for('get_recipes') }}" class="white-text orange darken-4 waves-effect waves-light btn">Reset</a>
        </div>
      </div>
      ```
      <img src="static/images/bugs/search-bar-bug.jpg" alt="Search field bug." width="200px" height="auto">
    
    Final code:

      The delition of `valign-wrapper` class in the outer div solved the issue:

      <img src="static/images/bugs/search-bar-bug-solution.jpg" alt="Search field bug solution." width="200px" height="auto">


#### Existing bugs

1. The form input autocomplete field has a white background that does not match well with the page styling. I did not manage to target that particular element to change the colour. However, the background colour of the form input in general has been modified successfully: when the input is introduced for the first time and autocomplete does not work, the background is transparent (as it meant to be).

    <img src="static/images/bugs/autocomplete-white-bug.jpg" alt="Autocomplete form input background." width="700px" height="auto">

2. The background image on real mobile devices has issues:
    
    - On Huawei Mate 20, the background image slightly jumps due to an appearing/disappearing address bar. 

    - On iPhone XR, the background image (instead of jumping) creates white spaces when the address bar appears/disappears. 
    
      <img src="static/images/bugs/background-image-bug.jpg" alt="Background image bug on physically tested mobile devices." width="200px" height="auto">
      
      Secondly, the background image on *All Recipes* and *Profile* pages is stretched out taking all the page length which makes the image have poor resolution. In Chrome DevTools mobile simulations, the background image is fixed while scrolling and takes the height of the view port.

3. The fallback image for recipes cards takes a few seconds to load.
        
## Deployment

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/).
    
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.

3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/).
    
2. Under the repository name, click "Clone or download".
    
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
    
4. Open Git Bash.
    
5. Change the current working directory to the location where you want the cloned directory to be made.
    
6. Type `git clone`, and then paste the URL you copied in Step 3.

    ```
    $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
    ```

7. Press Enter. Your local clone will be created.

   ```
   $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
   > Cloning into `CI-Clone`...
   > remote: Counting objects: 10, done.
   > remote: Compressing objects: 100% (8/8), done.
   > remove: Total 10 (delta 1), reused 10 (delta 1)
   > Unpacking objects: 100% (10/10), done.

Click [Here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

### Create database in MongoDB

1. Create an account at [MongoDB](https://www.mongodb.com/).
2. Create a Cluster, select a Cloud provider (e.g. AWS), select the closest region to you, choose a Cluster Tier (e.g. the M0 Tier, which is the 'free forever' tier), scroll down to the bottom and select 'Cluster Name'. Finally, click on the *Create Cluster* button.
3. In order to create database user credentials, click on *Database Access* under the *Security* section on the left. Click on *Add New Database User*, make sure that the user privileges are set to *Read and Write to the Database*, and then click *Add User*.
4. Click on *Network Access* within the *Security* menu, click *Add IP Address* and select *Allow Access From Anywhere*.
5. Go back to the *Clusters* tab, click on the *Collections* button.
6. In the *Collections* tab, click *Create Database* and enter the database name and the name of initial collection, press *Create* button. 
7. Create other collections.
8. Fill in your database: in each collection click on *Insert Document* button.

### Deployment to Heroku

1. In the terminal:

    - Type `pip3 freeze --local > requirements.txt`. It will update the list of requirements needed to run the application.
    - Type `echo web: python app.py > Procfile` to create the Procfile.

2. Create application:

    - Create an account at [Heroku.com](https://dashboard.heroku.com).
    - Click on the *New* button.
    - Select *Create new app*.
    - Enter the name of your application.
    - Select your region.

3. Set up connection to Github Repository:

    - Click the *Deploy* tab and select *GitHub-Connect to GitHub* in the *Deployment method* section.
    - A prompt to find a Github repository to connect to will then be displayed.
    - Enter the repository name and click search.
    - Once the repository name has been found, click *Connect*.

4. Set environment variables:

    - Click the *Setting* tab and then click *Reveal Confid Vars*.
    - Insert your variables:
      - IP: 0.0.0.0
      - PORT: 5000
      - database name you want to connect to
      - database url (this url can be found on MongoDb: go to the *Overview* tab, click *Connect* button, select *Connect your application*, select you driver and version (e.g. *Python* and *3.6 or later*), then copy the string to the clipboard and paste it for the MONGO_URI variable)
      - secret key which is required whenever using the flash() and session() functions of Flask

5. Enable automatic deployment:

    - Click the *Deploy* tab and scroll to the *Automatic deploys* section.
    - Choose the branch you want to deploy from, then click *Enable Automation Deploys*.

6. View your application:

    - You can view the application by clicking on the *Open app* button located at the top right corner.

7. After Heroku has ended their free tier offerings for deployment, the present project was migrated to a different free service on an alternative platform [Render](https://render.com/).

## Credits

### Content

#### Images

- Favicon image was taken from [Iconduck](https://iconduck.com/emojis/15944/slice-of-pizza)

- Background image was taken from [Unsplash](https://unsplash.com/photos/40OJLYVWeeM)

- Bucatini all'Amatriciana image was taken from [BigOven](https://www.bigoven.com/recipe/bucatini-allamatriciana/2435565)

- Spaghetti alla carbonara image was taken from [Recepten.be](https://recepten.be/recept/authentieke-spaghetti-carbonara/)

- Tiramisu image was taken from [La Rosiere](https://www.larosiere.net/tiramisu-recette/)

- Cannoli Siciliani image was taken from [Home Cooking Adventure](https://www.homecookingadventure.com/recipes/cannoli-siciliani)

- Vitello tonnato image was taken from [LINDENHOFF](https://www.lindenhoff.nl/recepten/vitello-tonnato/)

- Lasagna alla Bolognese image was taken from [PASTAFICIO](https://www.pastaficio.nl/alles-wat-je-moet-weten-over-lasagne/)

- Saltimbocca alla Romana image was taken from [Cibovagare](https://www.cibovagare.it/ricette/saltimbocca-alla-romana-1036.html)

- Risotto ai funghi porcini image was taken from [Galfrè Antipasti d'Italia](https://www.ghiottogalfre.it/it/primi/24-risotto-ai-funghi-porcini.html)

- Spaghetti alle vongole porcini image was taken from [ELLE](https://www.elle.com/nl/eten/recepten/a32915157/recept-spaghetti-alle-vongole-spaghetteria/)



#### Recipes

- Bucatini all'Amatriciana recipe was taken from [GREAT ITALIAN CHEFS](https://www.greatitalianchefs.com/recipes/bucatini-all-amatriciana-recipe)

- Spaghetti alla carbonara recipe was taken from [GREAT BRITISH CHEFS](https://www.greatbritishchefs.com/recipes/spaghetti-carbonara-recipe?_ga=2.47408039.1629710258.1636143312-85067904.1636143312)

- Tiramisu recipe was taken from [GREAT ITALIAN CHEFS](https://www.greatitalianchefs.com/recipes/tiramisu-recipe?_ga=2.210897045.1629710258.1636143312-85067904.1636143312)

- Cannoli Siciliani recipe was taken from [GREAT ITALIAN CHEFS](https://www.greatitalianchefs.com/recipes/sicilian-cannoli-recipe?_ga=2.210460693.1629710258.1636143312-85067904.1636143312)

- Vitello tonnato recipe was taken from [GREAT BRITISH CHEFS](https://www.greatitalianchefs.com/recipes/vitello-tonnato-recipe)

- Lasagna alla Bolognese recipe was taken from [GREAT ITALIAN CHEFS](https://www.greatitalianchefs.com/recipes/lasagne-alla-bolognese-recipe?_ga=2.47866919.1629710258.1636143312-85067904.1636143312)

- Saltimbocca alla Romana recipe was taken from [Jamie Oliver](https://www.jamieoliver.com/recipes/beef-recipes/saltimbocca-alla-romana/)

- Risotto ai funghi porcini recipe was taken from [Jamie Oliver](https://www.jamieoliver.com/recipes/chicken-recipes/baked-chicken-porcini-risotto/)

- Spaghetti alle vongole recipe was taken from [GREAT ITALIAN CHEFS](https://www.greatitalianchefs.com/recipes/spaghetti-alle-vongole-recipe?_ga=2.65817127.884526670.1636361549-85067904.1636143312)

- The present README file was written following the [template](https://github.com/Code-Institute-Solutions/SampleREADME) provided by Code Institute. Some parts (like Deployment section) were copied and pasted as they describe exactly the same procedure that was employed for the realization of this project.

### Code

- The code was written following the Code Institute tutorials.

- The code for handling error 404 was taken from [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/).

- The code for handling error 500 was taken from [Flask documentation](https://flask.palletsprojects.com/en/2.0.x/errorhandling/).

### Acknowledgements

- My mentor Sandeep Aggarwal for continuous helpful feedback.

- Tutor support at Code Institute for their help and support.