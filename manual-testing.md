# Testing Functionality, Usability and Responsiveness

Functionality, Usability and Responsiveness of the key website elements were tested manually following the plan:

### Navigation bar:

  - The navbar automatically collapses at the lg (large) breakpoint (992px).

    <img src="static/images/testing/navbar.jpg" alt="The navbar automatically collapses at the lg (large) breakpoint (992px)." width="700px" height="auto">

  - For not registered users, the navbar displays links only to 4 pages: *Home*, *All Recipes*, *Log In* and *Register*.
    The card on *Home* page displays 3 buttons: *View All Recipes*, *Log In* and *Register*.

    <img src="static/images/testing/not-registered-user.jpg" alt="Links for not registered user." width="700px" height="auto">

  - A registered user can view additional buttons: *Profile*, *Add New Recipe*, *Log Out*.
    Buttons *Log In* and *Register* dissapper. 

    <img src="static/images/testing/registered-user.jpg" alt="Links for registered user." width="700px" height="auto">

  - All buttons of the navbar are clickable and open correct pages.

### Pages layout:

  - *Home* page rearranges correctly at certain breakpoints.

    <img src="static/images/testing/home-page-layout.jpg" alt="Home page layout." width="700px" height="auto">

  - *All recipes* and *Profile* pages rearrange correctly at certain breakpoints.

    <img src="static/images/testing/all-recipes-page-layout.jpg" alt="All Recipes page layout." width="700px" height="auto">

  - *Log In* and *Register* pages rearrange correctly at certain breakpoints.

    <img src="static/images/testing/login-page-layout.jpg" alt="Login page layout." width="700px" height="auto">

  - *Add New Recipe* and *Edit Recipe* pages rearrange correctly at certain breakpoints.

    <img src="static/images/testing/add-new-recipe-page-layout.jpg" alt="Add new recipe page layout." width="700px" height="auto">

### *Register*, *Log In* and *Log Out* functionality
  
  - The user name and password should match a specific pattern: numbers, lower and uppercase letters; special characters are not allowed; should contain from 5 to 15 characters. If the input does not match a pattern, a message appears to help users.

    <img src="static/images/testing/pattern-check.jpg" alt="The user name and password should match a specific pattern." width="700px" height="auto">

  - When the account is successfully created, the user is redirected to his *Profile* page. The flash message is correctly displayed.

    <img src="static/images/testing/successful-registration.jpg" alt="User's successful registration." width="700px" height="auto">

  - The users with existing accounts can successfully log in through *Log In* page and be rediracted to their *Profile* page.

    <img src="static/images/testing/successful-login.jpg" alt="User has been successfully logged in." width="700px" height="auto">

  - If the user presses the *Log Out* button on Navbar, the user is redirected to the *Log In* page. The flash message is correctly displayed.

    <img src="static/images/testing/successful-logout.jpg" alt="User has been successfully logged out." width="700px" height="auto">

### All recipes page

  - For not registered users:
      - all recipes are displayes (from all users),
      - there are no *Edit Recipe* and *Delete Recipe* buttons,
      - when clicking the recipe card, the recipe data is displayed, all data fields are proparly displayed.
        <img src="static/images/testing/all-recipes-page-for-not-registered-users.jpg" alt="All recipes page displayed for not registered users." width="700px" height="auto">

  - For registered users (logged in):
      - all recipes are displayes (from all users),
      - there are *Edit Recipe* and *Delete Recipe* buttons,
      - when clicking the recipe card, the recipe data, *Edit Recipe* and *Delete Recipe* buttons are displayed, all data fields are proparly displayed.
        <img src="static/images/testing/all-recipes-page-for-registered-users.jpg" alt="All recipes page displayed for registered users." width="700px" height="auto">

### Flash messages

### Search

