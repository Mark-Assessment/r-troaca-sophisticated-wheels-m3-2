# **Sophisticated Wheels**

## **Site Overview**

[View the live project here.](https://sophisticated-wheels-1ab4360cc753.herokuapp.com/)


Discover the epitome of automotive excellence in Leicester at Sophisticated Wheels. Immerse yourself in our exclusive collection of prestigious vehicles, meticulously curated for the discerning driver. Indulge your automotive desires with our diverse array of luxury cars, conveniently showcased in our state-of-the-art showroom. At Sophisticated Wheels, we understand that your quest for the perfect vehicle is a journey, and we're here to accompany you every step of the way. Our commitment to excellence extends beyond aesthetics. Whether you crave the thrill of a sports car or the old school feel of a classic car, we stand ready to guide you to your ideal automotive companion in Leicester. As a fully approved service center, our dedication to quality assurance ensures that your confidence in us is well-placed. When you choose us, you're not just buying a car; you're investing in a seamless and reassuring experience.

![Website responsiveness](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/amiresponsive.png?raw=true)

## Table of contents

- [**Sophisticated Wheels**](#sophisticated-wheels)
  - [**Site Overview**](#site-overview)
  - [Table of contents](#table-of-contents)
  - [**Planning stage**](#planning-stage)
    - [**Target Audiences:**](#target-audiences)
    - [**User Stories:**](#user-stories)
    - [**Site Aims:**](#site-aims)
    - [**How Will This Be Achieved:**](#how-will-this-be-achieved)
    - [**Design:**](#design)
    - [**Wireframes:**](#wireframes)
    - [**Color Scheme:**](#color-scheme)
    - [**Typography:**](#typography)
    - [**Technologies Used:**](#technologies-used)
      - [**Design Tools**](#design-tools)
      - [**Front-End**](#front-end)
      - [**Back-End**](#back-end)
  - [**Current Features Common to all pages**](#current-features-common-to-all-pages)
    - [**Header Element**](#header-element)
    - [**Footer**](#footer)
  - [**Individual Page Content features**](#individual-page-content-features)
    - [**Home Page Content:**](#home-page-content)
    - [**About Us Page Content:**](#about-us-page-content)
    - [**Our Fleet Page Content:**](#comedour-fleet-page-content)
    - [**Sell Your Car Page Content**](#sell-your-car-page-content)
    - [**Account Page Content**](#account-page-content)
    - [**Login Page Content**](#login-page-content)
    - [**Register Page Content**](#register-page-content)
    - [**Contact Page Content**](#account-page-content)
    - [**404 Error Page Content**](#404-error-page-content)
  - [**Future-Enhancements**](#future-enhancements)
  - [**Testing Phase**](#testing-phase)
    - [**Testing During Development**](#testing-during-development)
      - [**Manual Testing**](#manual-testing)
      - [**User Story Testing**](#user-story-testing)
      - [**Functionality testing**](#functionality-testing)
    - [**Testing After Development**](#testing-after-development)
      - [**Validators**](#validators)
      - [***HTML*** - https://validator.w3.org/nu/](#html---httpsvalidatorw3orgnu)
      - [***CSS*** - https://jigsaw.w3.org/css-validator/](#css---httpsjigsaww3orgcss-validator)
      - [***JSHint*** - https://jshint.com/](#jshint---httpsjshintcom)
      - [***Python linter*** - https://pep8ci.herokuapp.com/](#pythonlinter---httpspep8ciherokuappcom)
      - [**Lighthouse Scores**](#lighthouse-scores)
  - [**Deployment**](#deployment)
  - [**Credits**](#credits)
    - [**General reference:**](#general-reference)
    - [**Content:**](#content)

## **Planning stage**

### **Target Audiences:**

- Users looking to buy a luxury car.
- Users that want to sell their own luxury cars.
- Users that want to be able to easily access the website from their mobile device as well as their other devices.

### **User Stories:**

- As a user I want to see the subject matter of the page.
- As a new user I want to be able to register an account.
- As a user I want to be able to create, read, update and delete a listing of my own car.
- As a luxury car enthusiast, I want to be able to view the fleet of high end cars available in this showroom.
- As a mobile user, I want the website to be responsive and all the sections of the website to be easily accessible and functional on my smartphone or tablet, ensuring a seamless experience regardless of the device I'm using.

### **Site Aims:**

- To inform the user what the website is about.
- To insure the user that the website is fluid and can be navigated at ease every step of their experience.
- To allow the user to easily create, read, update and delete a listing of their own car.
- To inform the user on what the luxury car showroom has in its fleet.
- To allow the user to be able to contact the showroom without any trouble.

### **How Will This Be Achieved:**

- The landing page of the website provides the user a short description of what he can find in the showroom. The user can also read more about the website in the About section.
- The site provides information about the fleet of cars it has in stock and details of each car.
- The site provides the user a form to register and login, so that they can sell their private luxury car.
- The users are able to create their own listing and it will be displayed in their account, where they can update their listing or delete it whenever they decide.
- The users are able to contact the showroom through a form where they can send a message or if they prefer, there is a email adress displayed as well as a phone number.

### **Design:**
 * Below is the schema design for the database that will hold and handle Users and the non-relational database handled by MongoDB which uses primary and foreign keys from each table in order to relate entries to eachother.

![Schema design](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/dbschema.png?raw=true)

 * And this is the flowchart of the website.

 ![Flowchart](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/flowchart.png?raw=true)

### **Wireframes:**

- Mobile Wireframes:
  - Home page

![Home page]()
  - About Us page
  
![About Us]()
  - Our Fleet page
  
![Our Fleet page]()
  - Sell Your Car page
  
![Sell Your Car page]()
  - Account page
  
![Account page]()
  - Contact page
  
![Contact page]()
  - Login page
  
![Login page]()
  - Register page
  
![Register page]()

- Desktop Wireframes:
  - Home page

![Home page]()
  - About Us page
  
![About Us]()
  - Our Fleet page
  
![Our Fleet page]()
  - Sell Your Car page
  
![Sell Your Car page]()
  - Account page
  
![Account page]()
  - Contact page
  
![Contact page]()
  - Login page
  
![Login page]()
  - Register page
  
![Register page]()

### **Color Scheme:**

When deciding the color scheme I wanted a dark road background with grey or white text for the contents for a good contrast. The color palette was created using [https://coolors.co/]

![Color Palette](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/palette.png?raw=true)


I also created this color contrast grid using [https://contrast-grid.eightshapes.com/](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23191919%0D%0A%233C4146%0D%0A%236B6464%0D%0A%23ACA0A0%0D%0A%23FCFAFA&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp), to check the contrast scored and ensure the text remains visible across the entire website and that the site is accessible to everyone.

![Color Contrast Grid](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/contrast.png?raw=true)

### **Typography:**

I decided on using a Google font, called Montserrat, for its clean and bold look.

![Typography](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/typography1.png?raw=true)

While for the logo of the website, in the left corner, I chose a Google font called because it looks stylish and fit for the name of the website.

![Typography](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/typography2.png?raw=true)

### **Technologies Used:**

* Cloud developer platform from [Gitpod](https://www.gitpod.io/).
* IDE integrated into Gitpod from [Visual Studio Code](https://code.visualstudio.com/).
* Debugging assisted by [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/).
* Version control integrated into Gitpod from [Git](https://git-scm.com/).

### **Design Tools:**

* Icon library and toolkit from [Font Awesome 5](https://fontawesome.com/).
* Favicon created on [favicon.cc](https://www.favicon.cc/).
* Showcasing the site on different devices by [Bytes](https://ui.dev/amiresponsive)
* Paint from [Microsoft](https://apps.microsoft.com/store/detail/paint/9PCFS5B6T72H?hl=en-us&gl=us)
* Flowchart by [diagrams.net/draw.io](https://www.diagrams.net/)
* AI created car pictures from [Microsoft Copilot](https://create.microsoft.com/en-us/features/ai-image-generator)

### **Front-End:**

- ![HTML5](https://img.shields.io/static/v1?label=HTML&message=5&color=E34F26&logo=html5&logoColor=ffffff)
    - [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) as the base for markup text.
- ![CSS3](https://img.shields.io/static/v1?label=CSS&message=3&color=1572B6&logo=css3&logoColor=ffffff)
    - [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS) for custom styling the site.
- ![Javascript](https://img.shields.io/badge/logo-javascript-blue?logo=javascript&logoColor=f5f5f5)
    - [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) for JavaScript functionality.

### **Back-End:**

- ![Python](https://img.shields.io/static/v1?label=Python&message=3.12.2&color=blue&logo=python&logoColor=ffffff)
    - [Python 3.12.2](https://www.python.org/) is a high-level, general-purpose programming language.
- ![Flask](https://img.shields.io/static/v1?label=Flask&message=3.0.2&color=yellow&logo=flask)
    - [Flask 3.0.2](https://flask.palletsprojects.com/en/3.0.x/) is a micro web framework written in Python.
- ![Jinja](https://img.shields.io/static/v1?label=Jinja&message=2&color=E34F26&logo=jinja)
    - [Jinja2](https://palletsprojects.com/p/jinja/) for templating with Flask.
- ![Werkzeug](https://img.shields.io/static/v1?label=Werkzeug&message=2.3.x&color=orange&logo=werkzeug)
    - [Werkzeug 2.3.x](https://werkzeug.palletsprojects.com/en/2.3.x/) for password hashing, authentication and authorisation.
- ![Heroku](https://img.shields.io/static/v1?label=Heroku&message=PaaS&color=430098&logo=heroku)
    - [Heroku](https://www.heroku.com) is used as *"Platform as a Service"* (PaaS) for app hosting.
- ![MongoDB](https://img.shields.io/static/v1?label=MongoDB&message=6.0&color=brightgreen&logo=mongodb&logoColor=ffffff)
    - [MongoDB Atlas 6.0](https://www.mongodb.com/atlas) is used as a non-relational database plugin via Heroku.

### **Validation and Evaluation:**

* HTML validation from [W3C](https://validator.w3.org/#validate_by_input).
* CSS validation from [Jigsaw (W3C)](https://jigsaw.w3.org/css-validator/).
* Python validation from [CI Python Linter](https://pep8ci.herokuapp.com/).
* Javascript validation from [JSHint](https://jshint.com/).
* Web page quality improvements assisted by [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)


## **Current Features Common to all pages**

### **Header Element**

* The navigation bar appears on all pages (including the 404 and 500 page).
* In the left corner there is the logo of the website.
* Contains links to the Home, About Us, Our Fleet, Sell Your Car, Login, Register and Contact page for quick navigation around the website. 
* The navbar also has a hover effect, which highlights the link that the cursor is hovering on top of.
* On mobile the navbar transforms into a togglable hamburger button.

![Header](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/navbar.png?raw=true)

## **Footer**

* Placed at the bottom of the page, it includes useful links, account links and contact information as well as the address of the car showroom.
* The footer includes a copyright notice at the bottom and has the same dark background as the navbar. The footer also includes a function that automatically updates the date.

![Footer](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/footer.png?raw=true)

## **Individual Page Content features**

### **Home Page Content:**
* This page contains three short paragraphs that give a short description about the car showroom. All three have a scroll animation while scrolling down the page, they pop up from left to right. The animation was used from [https://michalsnik.github.io/aos/].
  
![Home section1](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/section1.png?raw=true)

![Home section2](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/section2.png?raw=true)

![Home section3](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/section3.png?raw=true)

### **About Us Page Content:**
* At the top of the page there is a heading that contains the title of the page.
* This page contains a wider description of what you can find in this luxury car showroom as well as some AI created images of the showroom. They also have a scrolling animation as the ones on the home page.
  
![About Us section1](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/absection1.png?raw=true)

![About Us section2](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/absection2.png?raw=true)

![About Us section3](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/absection3.png?raw=true)

### **Our Fleet Page Content:**
* At the top of the page there is a heading that contains the title of the page and a short paragraph about the cars in stock.
* This page contains all the cars available in the showroom. Every car has an image and a description that pops up when you hover on top of each of them. Underneath each car there is an enquire about this car button that redirects the user to the contact form.
  
![Our Fleet section1](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/fleet1.png?raw=true)

![Our Fleet section2](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/fleet2.png?raw=true)

### **Sell Your Car Page Content:**
* If the user is not logged in, the page will display a message that informs the user that they need to be logged in to be able to sell a car or to register if he has not done that previously.
  
![Sell Your Car section1](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/sell1.png?raw=true)

* If the user is logged in, a selling form is being displayed.
![Sell Your Car section2](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/sell2.png?raw=true)

### **Account Page Content:**
* If the user is not logged in, the page will display the login page.
  
![Account section1](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/login.png?raw=true)

* If the user is logged in, but has no selling forms the page will display a message that informs the user there are no cars available.

![Account section2](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/account1.png?raw=true)

* If the user is logged in and has previously filled a selling form, the car will display in the users account.

![Account section2](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/account2.png?raw=true)

### **Login Page Content:**
* The page displays a form for the user to login.

![Login](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/login.png?raw=true)

### **Register Page Content:**
* The page displays a form for the user to register a new account.

![Register](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/register.png?raw=true)

### **Contact Page Content:**
* At the top of the page there is a heading that contains the title of the page and a short paragraph where the user is informed that they can feel free to contact the showroom in any manner displayed.
* The user is offered several possibilities to contact the venue. By contact form, email or mobile phone. The address of the showroom is also displayed on this page.
* The contact form has 3 required fields and a submit button:
    * The first field requires the user to input their name.
    * The second field requires the email address of the user.
    * The third field has a required text area, in which the user can input their questions to the showroom, feedback or whatever they choose.

![Contact](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/contact.png?raw=true)

### **404 Error Page Content**
* The page displays a message to inform the user that the page that they were looking for is unavailable.
* Under the message displayed, there is a button that sends the user back to the Home page.

![404 Error](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/404.png?raw=true)

## **Future-Enhancements**
* Provided I would have had sufficient time, I would have added a few extra features to enhance the website's functionality. One of these would be to allow the user to upload their own image to the selling form.
* I would also like to add a search bar at the top of the website, so the user can find a specific car that they are looking for. These enhancements would make the website more user-friendly and accesible.

***
## **Testing Phase**

### **Testing During Development**

During the development process, I have been constantly testing the website in the following ways:

1. Manually testing each element of the page for responsiveness and accesibility via a live server opened using GitPod.

2. Published the page via GitHub pages and shared with friends and family to receive feedback.

3. Made use of Developer Tools from different Internet browsers, to continuously identify and troubleshoot any problems I encountered.

#### **Manual Testing**

**Principles:**

1. **Exploratory Testing:** Manual testing is excellent for exploratory testing, where testers actively explore the application to discover unforeseen issues and usability problems.

2. **User Experience (UX) Testing:** Manual testers can assess the application's user-friendliness, usability, and overall user experience, providing valuable insights.

3. **Ad Hoc Testing:** In situations where test cases aren't well-defined or documented, manual testers can perform ad hoc testing to identify issues.

4. **Non-Functional Testing:** Tests related to subjective criteria like aesthetics, layout, and overall look and feel are often better suited for manual testing.

**When to Deploy Manual Testing:**

- **Usability Testing:** To evaluate the user interface and overall user experience.
- **Exploratory Testing:** When new features are introduced or when test cases are not yet well-defined.
- **Complex Test Scenarios:** For intricate and multi-step test cases where human intuition is required.
- **Non-Functional Testing:** Assessing subjective aspects like aesthetics, accessibility, and human factors.

* While testing the website, I have used 4 different browsers to make sure that it is cross-compatible. The desktop browsers I have used for the tesing were:

  - Firefox
  - Google Chrome
  - Microsoft Edge
  - DuckDuckGo

- I have also asked other people to test the website, using their personal iPhones and Macbooks using Safari, since I don't have access to these devices. To which they reported that they have not encountered any bugs.

#### **Automated Testing**

**Principles:**

1. **Repeatability:** Automated tests can be executed repeatedly without any variation in their steps and expected outcomes.

2. **Consistency:** Automated tests perform the same steps and checks each time, eliminating human errors and ensuring consistent results.

3. **Efficiency:** Automated tests can run quickly and efficiently, covering a large number of test cases in a short time.

4. **Regression Testing:** Automated tests are particularly useful for regression testing, where previously tested functionality is retested to ensure that new changes have not introduced defects.

5. **Data-Driven Testing:** Automation allows for data-driven testing, where tests are executed with different sets of data to verify various scenarios.

6. **Continuous Integration/Continuous Deployment (CI/CD):** Automated tests can be integrated into the CI/CD pipeline, allowing for immediate feedback on code changes and ensuring that only high-quality code is deployed.

**When to Deploy Automated Testing:**

- **Regression Testing:** Automated tests are ideal for regularly checking existing functionality after code changes.
- **Highly Repetitive Tests:** Tasks like data validation, login/logout procedures, and API testing can be automated for efficiency.
- **Load and Performance Testing:** Automated tools can simulate a large number of users to test system performance under heavy loads.
- **Cross-Browser and Cross-Platform Testing:** Automated frameworks can be used to test web applications on different browsers and platforms.

Automated testing can be a powerful tool for catching bugs early on and ensuring that the application is working as expected. While I fully acknowledge the benefits of automated testing and the value it adds to the overall development process, due to time constraints, implementing and maintaining Jest for automated testing was not possible.

#### **User Story Testing**

During my manual testing, I have tested every user story, to ensure that the needs of the users are met.

- As a user I want to see the subject matter of the page.
  - Issue: there was no description of what the page is on the landing page.
  - Resolution: I added a brief but comprehensive description of what you can find in the showroom.

![Home section1](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/section1.png?raw=true)

![Home section2](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/section2.png?raw=true)

![Home section3](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/section3.png?raw=true)

- As a new user I want to be able to register an account.
  - Issue: the user had to be registered to be able to sell their own luxury car.
  - Resolution: added a Register page and registration form.
  
![Register](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/register.png?raw=true)

- As a user I want to be able to create, read, update and delete a listing of my own car.
  - Issue: the user could not list a car to sell.
  - Resolution: added the Register page so they can register an account, added the Sell Your Car page where users with a registered account could create their own listing. In the Account page the user is able to view his own listing and they are able to edit the listing as well as delete it, whenever they want.

![Sell Your Car section2](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/sell2.png?raw=true)

![Account section2](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/account2.png?raw=true)

- As a luxury car enthusiast, I want to be able to view the fleet of high end cars available in this showroom.
  - Issue: the user could not find the available cars on the landing page.
  - Resolution: added the Our Fleet page, where users can see what the showroom has in stock.

![Our Fleet section1](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/fleet1.png?raw=true)

![Our Fleet section2](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/fleet2.png?raw=true)
  
- As a mobile user, I want the website to be responsive and all the sections of the website to be easily accessible and functional on my smartphone or tablet, ensuring a seamless experience regardless of the device I'm using.
  - Issue: the user could not see some of the pages properly.
  - Resolution: I modified some of the CSS rules, as to ensure that it is responsive on all devices.

![Mobile](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/mobile1.png?raw=true)

![Mobile](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/mobile2.png?raw=true)

![Mobile](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/mobile3.png?raw=true)

#### **Functionality testing**

- Tested on Samsung Galaxy S24 Ultra

| Home page |Result|Comments|
|-------|-------|-------|
|Website loads fully|Pass|No delay encountered|
|Layout appearance is correct (visibility of text, all images load, no overlaps)|Pass|N/A|
|Hovering over each link has the desired response from the navbar|Pass|N/A|
|Input fields work correctly, validate and accept data|Pass|N/A|
|Home takes the user to the Home page as expected|Pass|N/A|
|About Us takes the user to the About Us page as expected|Pass|N/A|
|Sell Your Car takes the user to the Sell Your Car page as expected|Pass|N/A|
|Account takes the user to the Account page as expected|Pass|N/A|
|Login takes the user to the Login page as expected|Pass|N/A|
|Register takes the user to the Register page as expected|Pass|N/A|
|Contact takes the user to the Contact page as expected|Pass|N/A|

- Tested on desktop

| Home page |Result|Comments|
|-------|-------|-------|
|Website loads fully|Pass|No delay encountered|
|Layout appearance is correct (visibility of text, all images load, no overlaps)|Pass|N/A|
|Hovering over each link has the desired response from the navbar|Pass|N/A|
|Input fields work correctly, validate and accept data|Pass|N/A|
|Home takes the user to the Home page as expected|Pass|N/A|
|About Us takes the user to the About Us page as expected|Pass|N/A|
|Sell Your Car takes the user to the Sell Your Car page as expected|Pass|N/A|
|Account takes the user to the Account page as expected|Pass|N/A|
|Login takes the user to the Login page as expected|Pass|N/A|
|Register takes the user to the Register page as expected|Pass|N/A|
|Contact takes the user to the Contact page as expected|Pass|N/A|

* All the links, buttons and forms work as expected, with no errors.

### **Testing After Development**

#### **Validators**

#### ***HTML*** - <https://validator.w3.org/nu/>

- All pages return no error.

#### ***CSS*** - <https://jigsaw.w3.org/css-validator/>

- All pages tested, no issues found.
- CSS validator errors due to aos.css, this is out of my control and an issue with the resource.
![CSS validator badge](https://jigsaw.w3.org/css-validator/images/vcss)

#### ***JSHint*** - <https://jshint.com/>

![JSHint results](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/jshint.png?raw=true)

#### ***Python linter*** - <https://pep8ci.herokuapp.com/>

![Python linter results](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/pep8compliance.png?raw=true)

#### **Lighthouse Scores**

- All lighthouse tests have been made while in incognito mode to avoid any browser extensions interference.
- I have asked several people to run lighthouse tests from their own devices as well, and they were getting similar scores.

![ Lighthouse score](https://github.com/RazvanTr10/Sophisticated-Wheels/blob/main/static/images/documentation/lighthouse.png?raw=true)
***

## **Deployment**

### **Local Deployment**

To run the project locally, install:
- [Python3](https://www.python.org/downloads) to run the app
- [PIP](https://pip.pypa.io/en/stable/installation/) to install all app requirements
- [Microsoft Visual Studio Code](https://visualstudio.microsoft.com/)
- [GIT](https://www.atlassian.com/git/tutorials/install-git) for version control
- [MongoDB Atlas](https://www.mongodb.com/atlas) to develop the database

For local deployment:

- Clone this GitHub repository by clicking the green `Code` button and `Download ZIP` to download a copy of the project as a zip-file

- Unzip the file

- Navigate to the correct file location after unpacking the files
    - `cd <path to folder>`

- Create a `env.py` file with your credentials. 

- Install all requirements from the requirements.txt file using this command:
    - `sudo -H pip3 -r requirements.txt`

- Sign up for a free account on [MongoDB](https://www.mongodb.com/Atlas) and create a new Database called **sophisticated_wheels**. The *Collections* (tables) in that database should be as follows:

**cars**
```
_id: <ObjectId>
fname: <string>
lname: <string>
brand: <string>
model: <string>
body_type: <string>
year: <string>
fuel: <string>
colour: <string>
mileage: <string>
price: <string>
email: <string>
telephone: <string>
```

**users**
```
_id: <ObjectId>
username: <string>
password: <string>
```

- Launch the app typing the following command in the terminal:
    - `flask run`
- The app should run on *localhost* on an address similar to `http://127.0.0.1:5000`. More information [here](https://code.visualstudio.com/docs/python/tutorial-flask).

### **Remote Deployment**

This site is currently deployed on [Heroku](https://www.heroku.com/) using the **main** branch on GitHub. To implement this project on Heroku, the following steps were taken:

1. Create a **requirements.txt** file so Heroku can install the required dependencies to run the app.
    - `sudo pip3 freeze --local > requirements.txt`

2. Create a **Procfile** to tell Heroku that this is a Python app
    - `echo web: python app.py > Procfile`

	- Make sure there are no blanks lines at the end of the file!

3. Sign up for a free [Heroku](https://www.heroku.com/) account

    - Create a new app

    - Click the **Deploy** tab 

    - Go to Deployment Method section and click *Connect GitHub*

    - Make sure your GitHub profile is displayed and add the repository name. Once your repository is found, click to connect

    -  Select **Enable Automatic Deploys** button 

4. Click on **Settings** tab, then click on **Reveal Config Vars**. 

- Now we can securely tell Heroku which variables are required by the env.py file. 
Configure the environmental variables as follows:

    - **IP** : 0.0.0.0
    - **PORT** : 5000
    - **SECRET_KEY** : <your_own_secret_key>
    - **MONGO_URI** : <link_to_your_MongoDB>
    - **MONGO_DBNAME** : sophisticated_wheels
    - **DEBUG** : False

5. Go back to **Deploy** tab and navigate to **Deploy a GitHub branch**. Click **Deploy Branch** button. Once the app has been built, you can **View** it.

## **Credits**

### **General reference:**

Heroku deployment instructions from Code Institute video tutorial

Readme styling from Tim Nelson's project [Unicorn Attractor](https://github.com/TravelTimN/ci-milestone05-fsfw)

Markdown Cheatsheet from [Adam Pritchard](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#html)

### **Content:**

Background from [Jan Kroon](https://www.pexels.com/photo/grayscale-photo-of-road-1038935/) on Pexels

Animation from [Michal Snik](https://michalsnik.github.io/aos/)

Dropdown menu from [HowToCodeSchool](https://www.youtube.com/watch?v=eKo1NV1qxbc) on Youtube

Cards tutorial from [Web Lang](https://youtu.be/NG-g11zUSck?si=6oY1MgJtW3bklYAA) on Youtube

Selling form from [RajeshHDN](https://codepen.io/RajRajeshDn/pen/QWwypRy) on CodePen


