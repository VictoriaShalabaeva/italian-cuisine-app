# Buon Appetito Website

View the live project [Here](https://italian-cuisine-app.herokuapp.com/)

*Buon Appetito* is an interactive website that allows to collect and share recipes of Italian cuisine meal.

The website is designed to be responsive and accessible on a range of devices, making it easy to navigate through.

![Responsive Design](static/images/responsive-design.jpg)

## User Experience (UX)

### User stories

  - **As a user:**

    - I want to see 
      
### Design

  - **Colour Scheme**

    The main colours used are ....

  - **Typography**

    The Roboto and Yanone Kaffeesatz (Navbar heading) fonts are the main fonts used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. Roboto is a clean font used frequently in programming, so it is both attractive and appropriate.

  - **Imagery**
     
    The large background images are designed to be striking and catch the user's attention demonstrating...

### Wireframes

  - *Home* page - [View](static/pdf/home-page.pdf)

  - *All Recipes* page - [View](static/pdf/all-recipes.pdf)

  - *Profile* page - [View](static/pdf/profile.pdf)

  - *Add New Recipe* page - [View](static/pdf/add-new-recipe.pdf)

  - *Log In* page - [View](static/pdf/log-in.pdf)

  - *Register* page - [View](static/pdf/register.pdf)

## Features

### Existing Features

- The website is responsive on many device sizes (down to 280 px).



- The *Home* page:

  - contains an appealing background image and a Bootstap jumbotron-style component that catch the user's attention. 
  
 

### Features Left to Implement

- a *Search Bar* through which a user can search content of their concern within the website.



## Technologies Used

### Languages Used

- HTML5

- CSS3

- JavaScript

### Frameworks, Libraries & Programs Used

1. [Bootstrap 4.1.3:](https://getbootstrap.com/docs/4.1/getting-started/introduction/)

   Grid System to make the site responsive,

   Navbar to make a responsive navigation header,

   Jumbotron-style component for calling extra attention to featured content or information.

2. [Google Maps JavaScript API:](https://developers.google.com/maps/documentation/javascript/overview)   

   Google Maps JavaScript API was used to integrate an interactive Google map with built in features such as markers and info windows to provide additional information.

3. [EmailJS:](https://www.emailjs.com/)

   EmailJS was used to connects the contact form to an email service.

4. [OpenWeather API:](https://openweathermap.org/api)

   OpenWeather API was used to display a current weather in Moscow.
   
5. [Google Fonts:](https://fonts.google.com/)

   Google fonts Roboto and Yanone Kaffeesatz were used on all pages throughout the project.

6. [jQuery:](https://jquery.com/)

   jQuery was used in JavaScript codes for the media query and detection of iOS devices; within Bootstrap to make the navbar responsive.

7. [Git:](https://git-scm.com/)

   Git was used for version control. 

8. [GitPod:](https://www.gitpod.io/)

   GitPod was used as an IDE platform for website realization.

9. [GitHub:](https://github.com/)

   GitHub is used to store the project code after being pushed from GitPod.

10. [Balsamiq:](https://balsamiq.com/)

    Balsamiq was used to create wireframes during the design process.

11. [Squoosh:](https://squoosh.app/editor)

    Squoosh image editor was used to reduces file size of the images.

12. [Am I responsive?](http://ami.responsivedesign.is/)

    Am I responsive? was used to show how the website looks on different devices.

13. [AutoPrefixer:](https://autoprefixer.github.io/)

    AutoPrefixer was used to add vendor prefixes to a CSS code.

14. [Beautifier:](https://beautifier.io/) 

    Beautifier was used to format code in a consistent and readable way.

15. [W3C Markup Validator](https://validator.w3.org/)

    W3C Markup Validator was used to check the markup validity of Web documents in HTML.

16. [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
 
    W3C CSS Validator was used to check the markup validity of Web documents in CSS.

17. [JSHint](https://jshint.com/)

    JSHint was used to detect errors and potential problems in JavaScript code.

18. [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

    Chrome DevTools was used to inspect and modify the website code.

19. [Lighthouse](https://developers.google.com/web/tools/lighthouse)

    Lighthouse was used to assess performance, accessibility, SEO and best practices.

## Testing

The W3C Markup Validator, W3C CSS Validator and JSHint Services were used to validate HTML, CSS and JS code, respectively, to ensure no syntax error.

- [W3C Markup Validator](https://validator.w3.org/). Please see Figure S1 in [Supp Info](supp-info.md) for the results.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/). Please see Figure S2 in [Supp Info](supp-info.md) for the results.
- [JSHint](https://jshint.com/) did not detect any potential problem in JavaScript codes.

### Testing User Stories from User Experience (UX) Section

Please see [Here](testing_user_stories.md) to find the user stories testing with corresponding screenshots.

### Testing Functionality, Usability and Responsiveness

The manual testing is described [Here](manual-testing.md).

### Further Testing

- The website was checked for performance in [Lighthouse](https://developers.google.com/web/tools/lighthouse) in Chrome DevTools (see results in Figure S3 in [Supp Info](supp-info.md)).

- The Website was tested on Google Chrome, Mozilla Firefox and Microsoft Edge browsers.

- The screen sizes and devices tested in Chrome DevTools include:

    - 1920 x 1080 
    - 1600 x 992
    - 1440 x 900
    - 1366 x 768
    - 1280 x 800
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
    - Galaxy Fold (280 x 653)

- Devices physically tested include:

  - Desktop 
  - Laptop
  - iPhoneXR 
  - Huawei Mate 20 
    
### Bugs

#### Fixed bugs

1. 

#### Existing bugs

1. 
        
## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/).

2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.

3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
    
4. Under "Source", click the dropdown called "None" and select "Master Branch".
    
5. The page will automatically refresh.
    
6. Scroll back down through the page to locate the now published site link in the "GitHub Pages" section.

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



## Credits

### Content

#### Images

- Favicon image from [Iconduck](https://iconduck.com/icons/114143/moscow)

- Background image on *Home* page from [Unsplash](https://unsplash.com/photos/40OJLYVWeeM)

- Bucatini all'Amatriciana image from [BigOven](https://www.bigoven.com/recipe/bucatini-allamatriciana/2435565)

- Spaghetti alla carbonara image from [Recepten.be](https://recepten.be/recept/authentieke-spaghetti-carbonara/)

- Pizza Margherita image from [Indoindians](https://www.indoindians.com/so-simple-and-so-good-pizza-margherita/)

- Tiramisu image from [La Rosiere](https://www.larosiere.net/tiramisu-recette/)



#### Recipes

- Bucatini all'Amatriciana recipe was taken from [Bon Appétit](https://www.bonappetit.com/recipe/bucatini-all-amatriciana-2)

- Spaghetti alla carbonara recipe was taken from [Food Network](https://foodnetwork.co.uk/recipes/spaghetti-alla-carbonara/?utm_source=foodnetwork.com&utm_medium=domestic)

- Pizza Margherita recipe were taken from [Cooking](https://cooking.nytimes.com/recipes/1014332-pizza-margherita)

- Tiramisu recipe was taken from [AllRecipes](https://www.allrecipes.com/recipe/21412/tiramisu-ii/)


- The present README file was written following the [template](https://github.com/Code-Institute-Solutions/SampleREADME) provided by Code Institute. Some parts (like Deployment section) were copied and pasted as they describe exactly the same procedure that was employed for the realization of this project.

### Code

- The code for handling error 404 was taken from [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/)

- The code for handling error 500 was taken from [Flask documentation](https://flask.palletsprojects.com/en/2.0.x/errorhandling/)

- Approach to identify 

- Approach to change 

- Approach to align 

### Acknowledgements

- My mentor Sandeep Aggarwal for continuous helpful feedback.

- Tutor support at Code Institute for their help and support.