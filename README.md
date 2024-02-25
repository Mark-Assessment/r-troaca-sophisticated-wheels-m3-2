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
      - [**Bugs and fixes**](#bugs-and-fixes)
    - [**Testing After Development**](#testing-after-development)
      - [**Validators**](#validators)
      - [***HTML*** - https://validator.w3.org/nu/](#html---httpsvalidatorw3orgnu)
      - [***CSS*** - https://jigsaw.w3.org/css-validator/](#css---httpsjigsaww3orgcss-validator)
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
- As a new user I want to be able to view the site without logging in.
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