# <span style="color: #4f9aff">Online Scout Manager</span>

---

![[15th Dartfords Online Scout Manager]](assets/documentation/am-i-responsive.png)


## Introduction

The focus of this site was to implement the django framework and python on the back-end in order to create a user-friendly site. The site is a badge manager for the 15th Dartford scout group where the group can use the blog page to ask questions and post comments, the leaders can add, edit and delete badges along with manage the scouts and their patrols. While scouts can request to earn specific badges and choose to feature up to three badges on their dashboard. These features follow the CRUD(Create, edit, update and delete) ideology where badges, posts and comments can be edited, deleted or updated. The site has an admin panel with all the above features along with the feature to add/delete patrols and users.

---

<a id=contents></a>

## CONTENTS

- [User Experience](#ux)
  - [User Stories](#user-stories)

- [Design](#Design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
  - [Site Functionality Flow Diagram](#siteflow)
  - [Game Logic Overview](#gameplay)
  - [Wireframes](#wireframes)
    - [Mobile Wireframes](#mobile-frames)
    - [Tablet Wireframes](#tablet-frames)
    - [Desktop Wireframes](#desktop-frames)
  - [Features](#features)
      - [Site Pages](#site-pages)
        - [Home Page](#the-home-screen)
        - [Scout Dashboard](#the-scout-dashboard)
        - [Leader Dashboard](#the-leader-dashboard)
        - [Badges Page](#the-badges-page)
        - [Badge Detail Page](#the-badge-detail-page)
        - [Add Badge Page](#the-add-badge-page)
        - [Edit Badge Page](#the-edit-badge-page)
        - [Blog Page](#the-blog-page)
        - [Blog Post Page](#the-blog-post-page)
        - [Create Post Page](#the-create-post-page)
        - [Manage Scouts Page](#the-manage-scouts-page)
        - [Login Page](#the-login-page)
        - [Signup Page](#the-signup-page)
        - [Logout Page](#the-logout-page)
      - [Future Features](#future-implementations)

-[Database]

* [Technologies Used](#technologies)

  - [Languages Used](#languages)
  - [Frameworks, Libraries & Programs Used](#frameworks)

* [Deployment & Local Development](#deployment-development)

  - [Deployment](#development)
  - [Local Development](#local-development)
    - [How to Fork](#fork)
    - [How to clone](#clone)

* [Testing](#testing-readme)

  - [Solved Issues & Bugs](#solved-issues)
  - [Known Issues & Bugs](#known-issues)

* [Credits & Inspiration](#credits&inspiration)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgement](#acknowledgement)

---

<a id=ux></a>

## User Experience (UX)

The site has been designed soley for the 15th Dartford scout troop. The site offers a simple, modern and proffesional design along with an easy to use interface. The clean UI ensures seamless navigation and accessibility for both Scouts and Leaders.

<hr>

<a id=user-stories></a>

### User Stories

#### First-time visitor goals

- As a new site user, I want to have a clear and accessible way to navigate through different sections such as a list of badges that can be aquired and my own dashboard without difficulty.
- As a new site user, I want to be able to signup easily so that I can start looking at badge requirements.

#### Returning visitor goals

- As a returning site user, I want to be able to see my earned badges so that I can keep up to date with my progress.
- As a returning site user, I want to be able to request new badges so that I can continue to show my progression to my peers and leaders.

#### Frequent user goals

- As a frequent site user, I want a blog page where I can ask questions and comment on others posts so that I can help other scouts with earning new badges.

All user stories can found in the linked GitHub project [here](https://github.com/users/Ryan-ford25/projects/7/views/1?layout=board&visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Linked+pull+requests%22%2C%22Sub-issues+progress%22%2C%22Labels%22%5D)

---

<a id=Design></a>

## Design

<a id=colour-scheme></a>

### Colour Scheme

The primary colours for the site are:
- `#445261` (Charcoal Blue) – This grounded dark blue is easy on the eyes and is usually associated with trust and reliablity, two qualities that all scouts should have. The color is also modern and proffesional which is why I have used it as the footer as the proffesionalism and modernity aligns with my design for the website.

- `#188181` (Teal): The colour I have chosen as the main colour for the buttons and tags on the webpage is sophisticated and offers a sense of innovation and creative thinking, this aligns well with scouting in general as these are considered core 'Skills for life' which is what scouting gives to young people.

- `#E84610` (Molten orange): Used for the 'Delete' buttons in the webpage as the high saturation orange has signs of caution and alertness making the user aware that the button would be destructive.

This colour scheme presents a modern and proffesional aesthetic aligning perfectly with the ideals of scouting and specifically the 15th Dartford scout troop.

<details>
<summary>- Toggle the arrow to view the colour swatches</summary>

<img src="assets/documentation/color-swatch.png" width="750" alt="Hex colour pallette">

</details>

<br>
<hr>

<a id=typography></a>

### Typography

Google Fonts was used to import the selected fonts for the site, ensuring high-quality and easily accessible typography.

- The font [Lato](https://fonts.google.com/specimen/Lato?query=lato&categoryFilters=Feeling:%2FExpressive%2FBusiness) is what I decided to use for the website as it comes across as professional and modern, the font also presents seriousness and warmth which was perfect for the scout troops website.

<img src="assets/documentation/Lato-font.png" width="750" alt="Lato Font example text">

<br>
<hr>

<a id=wireframes></a>

### Wireframes

Using [Balsamiq](https://balsamiq.com/), wireframes were developed for mobile, tablet, and desktop views. These wireframes played a crucial role in outlining the site’s structure and layout, ensuring a smooth user experience across different devices. The design process prioritized responsive adjustments to create an intuitive interface that adapts seamlessly to various screen sizes.

<a id=mobile-frames></a>

#### Mobile Wireframes

<details>
<summary> Click here to see the Mobile Wireframes </summary>

|                Home Screen Wireframe                         |                Signup Wireframe                             |                   Login Wireframe                                |
| :-----------------------------------------------:            | :-------------------------------------------------:         | :-------------------------------------------------------------:  |
| ![Home](assets/documentation/home-page-wireframe-mobile.png) | ![Signup](assets/documentation/signup-wireframe-mobile.png) | ![Login](assets/documentation/signin-wireframe-mobile.png)       |

|                   Leader Dashboard Wireframe                                    |               Scout Dashboard Wireframe                                       |               Blog Screen Wireframe                     |
| :-----------------------------------------------------------:                   | :-----------------------------------------------:                             |  :---------------------------------------:              |
| ![Leader Dashboard](assets/documentation/leader-dashboard-wireframe-mobile.png) | ![Scout Dashboard](assets/documentation/scout-dashboard-wireframe-mobile.png) | ![Blog](assets/documentation/blog-wireframe-mobile.png) |

|           Create Post Wireframe                                     |        Badge List Wireframe                                           |          Badge Detail Wireframe                                         |
| :-------------------------------------------------------:           | :-------------------------------------:                               | :-------------------------------------:                                 |
| ![Create Post](assets/documentation/createpost-wireframe-mobile.png)| ![Badge List](assets/documentation/badges-wireframe-mobile.png)       | ![Badge Detail](assets/documentation/badge-detail-wireframe-mobile.png) |

|           Edit Badge Wireframe                                      |        Create Badge Wireframe                                          |          Manage Scouts Wireframe                                          |
| :-------------------------------------------------------:           | :-------------------------------------:                                | :-------------------------------------:                                   |
| ![Edit Badge](assets/documentation/edit-badge-wireframe-mobile.png) | ![Create Badge](assets/documentation/create-badge-wireframe-mobile.png)| ![Manage Scouts](assets/documentation/manage-scouts-wireframe-mobile.png) |

|          Logout Wireframe                                      |              Blog post Wireframe                               |
| :-------------------------------------------------------:      | :-------------------------------------------------------:      |
| ![Logout](assets/documentation/logout-wireframe-mobile.png)    | ![Logout](assets/documentation/blog-post-wireframe-mobile.png)    |



</details>

<a id=tablet-frames></a>

#### Tablet Wireframes

<details>
<summary> Click here to see the Tablet Wireframes </summary>

|                Home Screen Wireframe                         |                Signup Wireframe                             |                   Login Wireframe                                |
| :-----------------------------------------------:            | :-------------------------------------------------:         | :-------------------------------------------------------------:  |
| ![Home](assets/documentation/home-page-wireframe-tablet.png) | ![Signup](assets/documentation/signup-wireframe-tablet.png) | ![Login](assets/documentation/signin-wireframe-tablet.png)      |

|                   Leader Dashboard Wireframe                                    |               Scout Dashboard Wireframe                                       |               Blog Screen Wireframe                     |
| :-----------------------------------------------------------:                   | :-----------------------------------------------:                             |  :---------------------------------------:              |
| ![Leader Dashboard](assets/documentation/leader-dashboard-wireframe-tablet.png) | ![Scout Dashboard](assets/documentation/scout-dashboard-wireframe-tablet.png) | ![Blog](assets/documentation/blog-wireframe-tablet.png) |

|           Create Post Wireframe                                     |        Badge List Wireframe                                           |          Badge Detail Wireframe                                         |
| :-------------------------------------------------------:           | :-------------------------------------:                               | :-------------------------------------:                                 |
| ![Create Post](assets/documentation/createpost-wireframe-tablet.png)| ![Badge List](assets/documentation/badges-wireframe-tablet.png)       | ![Badge Detail](assets/documentation/badge-detail-wireframe-tablet.png) |

|           Edit Badge Wireframe                                      |        Create Badge Wireframe                                          |          Manage Scouts Wireframe                                          |
| :-------------------------------------------------------:           | :-------------------------------------:                                | :-------------------------------------:                                   |
| ![Edit Badge](assets/documentation/edit-badge-wireframe-tablet.png) | ![Create Badge](assets/documentation/create-badge-wireframe-tablet.png)| ![Manage Scouts](assets/documentation/manage-scouts-wireframe-tablet.png) |

|          Logout Wireframe                                      |              Blog post Wireframe                               |
| :-------------------------------------------------------:      | :-------------------------------------------------------:      |
| ![Logout](assets/documentation/logout-wireframe-tablet.png)    | ![Logout](assets/documentation/blog-post-wireframe-tablet.png.png)    |

 </details>

<a id=desktop-frames></a>

#### Desktop Wireframes

<details>
<summary> Click here to see the Desktop Wireframes </summary>
<br>

- Home Screen Wireframe

![Home](assets/documentation/home-page-wireframe.png)

- Signup Wireframe

![Signup](assets/documentation/signup-wireframe-desktop.png) 

- Login Wireframe

![Login](assets/documentation/signin-wireframe-desktop.png)

- Leader Dashboard Wireframe

![Leader Dashboard](assets/documentation/leader-dashboard-wireframe-desktop.png)

- Scout Dashboard Wireframe

![Scout Dashboard](assets/documentation/scout-dashboard-wireframe-desktop.png)

- Blog Screen Wireframe

![Blog](assets/documentation/blog-wireframe-desktop.png)

- Blog Post Wireframe

![Blog Post](assets/documentation/blog-post-wireframe-desktop.png)

- Create Post Wireframe

![Create Post](assets/documentation/createpost-wireframe-desktop.png)

- Badge List Wireframe

![Badge List](assets/documentation/badges-wireframe-desktop.png) 

- Badge Detail Wireframe

![Badge Detail](assets/documentation/badge-detail-wireframe-desktop.png)

- Edit Badge Wireframe

![Edit Badge](assets/documentation/edit-badge-wireframe-desktop.png)

- Create Badge Wireframe

![Create Badge](assets/documentation/create-badge-wireframe-desktop.png)

- Manage Scouts Wireframe

![Manage Scouts](assets/documentation/manage-scouts-wireframe-desktop.png)

- Logout Wireframe

![Logout](assets/documentation/logout-wireframe-desktop.png) 
 
 </details>
<br>
<hr>

<a id=features></a>

## Features

The website consists of multiple pages that the user can navigate to or are redirected to dependant on what the user has interacted with(i.e clicking a badge will redirect to the badges detail page).

All Pages on the website are responsive and have:

- A favicon in the browser tab.

<details>
<summary> Click here to view the favicon </summary>

![favicon](assets/documentation/favicon.ico)

</details>

<a id=site-pages></a>

### Site Pages

---

<a id=home-page-features></a>

#### The home screen

<details>
<summary> Click here to view the home screen </summary>

![Home Page screenshot](assets/documentation/home-screen-ss.png)

</details>

- What it does:
  - Welcomes the user with a straight forward welcome message : "Welcome to 15th Dartford Scout Group's Online Scout Manager".
  - Gives a quick and simple brief explanation of what can be done on the site: "Track badges, manage scouts, and celebrate achievements - all in one place".
- User Benefits:
  - Gets straight to the point meaning the user instantly understands what the site is for.
  - Simple design means that there is no unnecessary clutter.
  - The transparency of the site means that the user will start looking for a 'login' or 'signup' button with a specific purpose in mind (i.e managing scouts or tracking a badge).
- Interactive Elements:
  - Login button: Allows the user to sign in with an account they have previously created.
  - Signup button: The user can create an account if they haven't got one already.

The homepage is a quick and simple message of what can be done on the site. The lack of clutter and guided ui elements such as the "Login" button takes the user directly to the core functions of the site such as 'Tracking badges'.

---

<a id=scout-dashboard-features></a>

#### The Scout Dashboard

<details>
<summary> Click here to view the Scout Dashboard </summary>

![Scout Dashboard screenshot](assets/documentation/scout-dashboard-ss.png)

</details>

- What it does:
  - Displays the users 'Earned badges'.
  - Displays 'Featured badges' that are chosen by the user.
- User benefits:
  - Keeps the user up to date with badges that they have earned.
- Interactive Elements:
  - Feature button: Allows the user to select a badge to place in their 'Featured badges', the button then changes to 'Unfeature' on badges that are currently featured so they can be swapped in and out.

  The Dashboard is like the default page of the site, once logged in or after signing up the scouts are taken straight to their dashboard which is where any earned badges will be displayed and the Scout can choose to feature these badges in the 'Featured badges' section. Initially these sections are blank but as they progress through scouts the badges will soon rack up and will remind them of the progress they're making. By using this as the 'default' page after logging in the Scout will be able to instantly see what badge to work on next, acting as a map for continuous growth.

---

<a id=leader-dashboard-features></a>

#### The Leader Dashboard

<details>
<summary> Click here to view the Leader Dashboard </summary>

![Leader Dashboard sceenshot](assets/documentation/leader-dashboard-ss.png)

</details>

- What it does:
  - Displays a section for 'Badge Requests' allowing the Leader to approve or reject requests.
  - Displays the scouts in the troop and the patrol that they are assigned to.
  - Allows the Leader to add/edit or delete badges.
- User Benefits:
  - Keeps the Leaders up to date with which patrol a scout is currently assigned to.
  - Leaders can keep the badge database up to date with new badges, updated requirements or remove older badges.
- Interactive Elements:
  - 'Accept' or 'Reject' buttons: Displayed once a Scout makes a badge request.
  - 'Edit' and 'Delete' buttons: On badges that are currently in the database.
  - 'Add Badge' button: So that the Leader can create a new badge to add to the database.

  The Leaders Dashboard much like the Scout dashboard is their default page once logged in they are redirected to the page, however due to their role being 'Leader' they aren't able to display or feature earned badges but are instead given a list of the scouts in the troop and the patrols they are assigned to; the badges that are currently in the database and options to edit or delete them; the ability to approve or reject badge requests from scouts; and the option to add new badges to the database with a front-end form. By allowing leaders to edit/delete and add new badges with a front-end form means that the badges are always tailored and up to date with the troops needs.

---

<a id=badges-page-features></a>

#### The Badges Page

<details>
<summary> Click here to view the Badges Page </summary>

![Badges page screenshot](assets/documentation/badges-ss.png)

</details>

- What it does:
  - Displays the Badges from the database with clear images and text.
  - Displays them in a simple grid format.
- User Benefits:
  - The grid format makes it easy for the user to find a specific badge quickly.
- Interactive Elements:
  - Each badge can be interacted with to take the user to its own page which displays the requirements for the badge.

The Badge page follows the simplistic and modern design from the rest of the website and displays each badge clearly with its name and image in a grid format which will accommodate for growth as more badges are added without the page becoming an endless and tiring vertical list. It shows proffesionalism and structure aligning well with the scout troops needs.

---

<a id=badge-detail-features></a>

#### The Badge Detail Page

<details>
<summary> Click here to view the Badge detail Page </summary>

![Badge detail screenshot](assets/documentation/badge-detail-ss.png)

</details>

- What it does:
  - Displays a specific badge with its name, description, image and requirements.
- User Benefits:
  - Easy to read.
  - No exccessive amounts of text.

The Badge Detail page yet again follows the simple design and gets straight to the point displaying only the necessary information needed for each badge, this ensures the user can immediately understand the net steps and get to work on achieving the badge.

---

<a id=add-badge-page-features></a>

#### The Add Badge Page

<details>
<summary>Click here to view the Add Badge Page</summary>

![Add Badge Page screenshot](assets/documentation/create-badge-ss.png)

</details>

- What it does:
  - Presents a front-end form that the user can use to fill out necessary fields in order to add a new badge to the database.
- User Benefits:
  - Simple form layout with clear field labels makes the process easy for the leader to complete the form.
- Interactive Elements:
  - Text field areas: Used to fill out the form.
  - Image upload field: The user can upload an image of the badge which will be used for other pages.
  - 'Add requirement' button: The user can interact with this button to add a new text field for badges that require more requirements.
  - 'delete' checkbox: Can be selected in order to delete the requirement and prevent it from being assigned to the badge after the badge is created.
  - 'Create Badge' button: Once the form has been filled out the user can click on this button to complete the process and add the badge to the database.

The Add Badge form page continues to follow the simple design along with the rest of the site, the fields are clearly labeled so that the User specifically users with a 'Leader' role understand what information to enter and where.

---

<a id=edit-badge-page-features></a>

#### The Edit Badge Page

<details>
<summary>Click here to view the Edit Badge Page</summary>

![Edit Badge Page screenshot](assets/documentation/edit-badge-ss.png)

</details>

- What it does:
  - Presents the user with a pre-filled form of the badge they want to edit.
  - Allows the user to change the information in fields and delete requirements if necessary.
- User Benefits:
  - Using the same layout means the design is consistent and the form appears familiar to the user.
  - The process of editing each field can be done swiftly.
- Interactive Elements:
  - Text field areas: Used to fill out the form.
  - Image upload field: The user can upload an image of the badge which will be used for other pages.
  - 'Add requirement' button: The user can interact with this button to add a new text field for badges that require more requirements.
  - 'delete' checkbox: Can be selected in order to delete the requirement and prevent it from being assigned to the badge after the badge is created.
  - 'Save changes' button: Once the form has been edited to the users liking the button can be used to update the changes to the database.

The edit badge form page is identical to that of the 'add badge' form page, doing this means that the design is consistent and 'familiar'. By not changing the layout of the fields the Leader can edit a badge quickly and efficiently as they would know what needs changing and where the field is.

---

<a id=blog-page-features></a>

#### The Blog Page

<details>
<summary> Click here to view the Blog page </summary>

![Blog page screenshot](assets/documentation/blog-ss.png)

</details>

- What it does:
  - Displays the posts that have been uploaded by other users.
  - Clearly displays the title of the post, author, date and time of when it was posted and a brief description.
- User Benefits:
  - Easy to read.
  - Having the name of the author displayed allows the user to know who wrote the post so they can address the person directly if they choose to write a comment.
  - The clear display of the title and brief description gives the user an idea of what the post is about.
- Interactive Elements:
  - Each post can be interacted with to redirect the user to the post itself showing the entire content.
  - 'Create Post' Button: Allows the user to create their own post to be uploaded to the page.

The blog design is built for speed and connection. Adding the author's name makes the page feel more personal—like a conversation rather than a noticeboard. I used clear titles and short previews so users don't have to guess what a post is about. They can quickly scan the feed, find a topic they are knowledgeable in, and dive in to help without having to click on each post first.

---
<a id=blog-post-page-features></a>

#### The Blog Post Page

<details>
<summary> Click here to view the Blog Post page </summary>

![Blog Post page screenshot](assets/documentation/blog-post-ss.png)

</details>

- What it does:
  - Displays the entire content of the post.
  - Displays a counter for comments.
  - Displays all current comments.
- User Benefits:
  - Gives the user the full content of the post.
  - Confirms the users ability to help.
- Interactive Elements:
  - The user can leave a comment in the text field provided.
  - 'Submit' button: can be used once the user has filled out the text field.

The Blog Post page provides the full details of a post that has been interacted with from the previous Blog page, this means the user can now read the full post and leave helpful comments to the author.

---

<a id=create-post-page-features></a>

#### The Create Post Page

<details>
<summary> Click here to view the Create Post Page </summary>

![Create Post page screenshot](assets/documentation/create-post-ss.png)

</details>

- What it does:
  - Displays a form which can be used to create a post.
- User Benefits:
  - Each field is labeled clearly which helps the user to understand what to put in them.
- Interactive Elements:
  - Text fields: Used to enter information into the field.
  - 'Post' button: Can be used to add the post to the blog page.

The Create post page is a clear and easy to read form. Very similar to that of the badge forms used to add and edit badges. The simple design follows the design of the entire website and creates consistency across all the pages.

---

<a id=manage-scouts-page-features></a>

#### The Manage Scouts Page

<details>
<summary>Click here to view the Manage Scouts Page</summary>

![Manage Scouts Page screenshot](assets/documentation/manage-scouts-ss.png)

</details>

- What it does:
  - Displays a Table with the Scouts names and patrols.
  - The Leader can assign the scout to a different patrol if they want to.
- User Benefits:
  - Easy to read table.
  - The feature allows for a quick and easy way to change a scouts patrol.
- Interactive Elements:
  - Drop down menu: For each scout there is a drop down menu that provides a list of patrols to select from.
  - 'Save' button: Used to save the newly appointed patrol to the scout in the database.

The Manage Scouts Page also follows the simplistic modern design with an easy to read table. In the table is a column labeled 'Assign Patrol' which provides the Leader with an easy to use dropdown list of patrols, the leader can select one of the patrols and interact with the 'Save' button to save the new value assigning the Scout to their new Patrol. This is also then updated on the leaders dashboard aswell so that the data is consistent accross the website.

---

<a id=login-page-features></a>

#### The Login Page

<details>
<summary>Click here to view the Login Page</summary>

![Login Page screenshot](assets/documentation/login-screen-ss.png)

</details>

- What it does:
  - Displays a 'Login' form that existing users can use to log into the site.
  - There are two simple input fields for the username and password.
  - Has a warm welcoming message 'Welcome back to 15th Dartford Scout groups online badge manager".
- User Benefits:
  - Having just the two fields makes it quick and easy for the user to login to the site.
- Interactive Elements:
  - Input fields: Used to enter the users credentials so they can sign in.
  - 'Login' button: Once interacted with the user is redirected to their dashboard.
  - 'Remember me' checkbox: Used by the user to remain logged in the next time they load up the site to save time and not have to re-enter their credentials.
  - 'signup' link: This link allows users that have misclicked the login button or dont have an account to be redirected to the signup page.

The Login page is a straightforward page with a welcome back message which acts as a 'digital handshake' between the site and the user making them feel seen and encorouges repeat visits. The form that has just two input fields can be filled out by the user with their credentials(that they created on signing up) and once they click the 'Login' button they will be redirected to their dashboard. This gets the user straight into the action, however if they misclicked the login button from the homepage and don't have an account just yet then they can click the 'signup' link that is placed within the welcome message to be redirected to the signup page where they can create a new account.

---

<a id=Signup-page-features></a>

#### The Signup Page

<details>
<summary>Click here to view the Signup Page</summary>

![Signup Page screenshot](assets/documentation/signup-screen-ss.png)

</details>

- What it does:
  - Displays a front-end form which the user can fill out to create an account.
  - Asks the user a question: 'Already have an account?' which prevents duplicate accounts and helps users that landed on the page by accident..
- User Benefits:
  - Easy to read.
  - Clear labels.
- Interactive Elements:
  - 'Signup' button: Once the form has been filled out the button can be used to redirect the user to their dashboard.
  - 'Login' link: Used to redirect the user to the login page.

The Signup Page is a clear and concise form that the user can fill out to create a new account. The form is short, simple and follows a clean design(along with other forms on the site) keeping the site design consistent. Using a short form encourages users to fill it out as they view it as a quick process. On the signup page is a question 'Already have an account?' with  a link to the login page, this is for users that may have landed on the page by accident such as from a search engine or by misclicking the 'Signup' button on the home page, the link redirects them to login page.

---

<a id=Logout-page-features></a>

#### The Logout Page

<details>
<summary>Click here to view the Logout Page</summary>

![Logout Page screenshot](assets/documentation/logout-ss.png)

</details>

- What it does:
  - Displays a message to confirm the user wants to logout.
- User Benefits:
  - Quick and easy message.
  - No clutter straight to the point.
- Interactive Elements:
  - 'Signout' Button: Used to confirm the users to choice to logout, once clicked the user is redirected to the homepage.

The signout page is possibly the most simplistic page within the entire site it displays a clean and precise message 'Are you sure you want to sign out?'. The clear message gives the user a chance to ask themselves if they are done with the tasks they set out to achieve, if so they can click the signout button to end their session and be redirected to the homepage keeping their accounts secure so that no one else uses it. If they are not done and decide they don't want to logout just yet they can click on one of the nav bar buttons be redirected and get to finishing their tasks.

---

<a id=user-actions></a>

### User Actions

---

<a id=signing-up></a>

#### Sign Up

The User can fill out the fields in the form, once submitted it will create a user object in the database and automatically secure the users sensitive information such as their password. Currently the only non-required field in the form is the email address as email verification is not on but will be in a future update to crete a more secure experience.

<details>
<summary>Click to view the signup form</summary>

![signup form screenshot](assets/documentation/signup-screen-ss.png)

</details>

---

<a id=signing-in></a>

#### SignIn

Users who have made an account can quickly and easily log in to their account in order to access the login-required functionality of the site.

<details>
<summary>Click to view the Signin form</summary>

![signin form screenshot](assets/documentation/login-screen-ss.png)

</details>

---

<a id=logging-out></a>

#### Logout

Users who are logged in can easily log out in order to stop access to their account-based information and functionality.

<details>
<summary>Click to view the Logout Screen</summary>

![Logout Screen screenshot](assets/documentation/logout-ss.png)

</details>

---

<a id=role-dependant-features></a>

### Role Dependant Features

---
<a id=role-dependant-navigation-bar></a>

#### Scout vs Leader Navigation bar

Users who have created their account with the role of 'Scout' will have the 'Manage Scouts' tab removed from their naviation bar as this feature is only used by users with the role of 'Leader' as they are permitted to view the list of scouts within the troop.


![Leader Navigation bar screenshot](assets/documentation/leader-nav-ss.png)

![Scout Navigation bar screenshot](assets/documentation/scout-nav-ss.png)

---
<a id=role-dependant-dashboard></a>

#### Scout vs Leader Dashboard

Much like the Navigation bar the dashboard is also different depending on the role of the user. Due to Leaders needing the ability to manage their scouts, the patrol they're assigned to and the badges each scout has earned. The dashboard could be classed as less 'fun' and more admin style giving the user access to Accept and reject badge requests, view scouts and the patrol they are in, adding, editing and deleting badges from the database. While the Scouts get a dashboard with a more achievement approach allowing them to view and keep track of earned badges, and feature their favourite badges.

Scout Dashboard 
<br>
<img src="assets/documentation/scout-dashboard-ss.png" width=500 alt="Scout dashboard screenshot"></img>

Leader Dashboard
<br>
<img src="assets/documentation/Leader-dashboard-ss.png" width=500 alt="Leader dashboard screenshot"></img>

---

<a id=future-implementation></a>

## Future Implementations

To ensure the website remains engaging and functional for users, in future implementations I would like to:

1. **Profile** – All Users should be assigned a Profile that would display their name, username, patrol and featured badges when interacted with by other Users.
2. **Customise Dashboard** - Add options to customise the dashboard such as background color/image, gives the users more customisation and creative freedom.
3. **Patrol badges automatically updated** - When a scout is assigned to a patrol they should be given the patrols badge on their profile and the badge should update automatically if their patrol changes.
4. **Email validation login** - Add email verification for login and make it a requirement for signing up.
5. **Add New Patrol** - The Leaders should be given the ability to add Patrols.
6. **Delete scouts from troop** - Leaders should be able to delete users that are no longer in the troop so that their sensitive information is deleted from the database and the scouts list is accurate.
7. **Add checklist to requirements for badges** - Adding checklist boxes to the requirements for each badge means scouts would be able to track their progress for a specific badge and see what they need to do next.
8. **Edit account info** - The users should be able to edit their account information after signing up such as name, username and password.
9 **Request Form** - Rather than a simple request badge button it should redirect the scouts to a form that they can fill out and provide evidence of the requirements being met which a leader can then review and accept or reject the request.

---

<a id=database-design></a>

## Database Design

I designed my database using [Lucidchart](https://www.lucidchart.com). I created my Entity Relationship Diagram(ERD) to visualise the relationship between my database models.

<img src="assets/documentation/database-diagram.png" width=750></img>

---
<a id=agile-development-process></a>

## Agile Development Process

### GitHub Projects 

[Github Projects](https://github.com/users/Ryan-ford25/projects/7/views/1) was utilised as an Agile design tool throughout this project. Using the right tags, issues and assignments, it served to promote efficient and effective Agile design principles.
User issues were created and issues and tasks were planned and referred back to over the course of the project using this Kanban Board.

<img src="assets/documentation/project-ss.png" width=750></img>

---
<a id=testing-readme></a>

## Testing

> [!NOTE]
> Please refer to [TESTING.md](TESTING.md) file for all testing carried out.
---

<a id=technologies></a>

## Technologies Used

<a id=languages></a>

### Languages Used

- [HTML](https://en.wikipedia.org/wiki/HTML) - Used for the main site content.

- [CSS](https://en.wikipedia.org/wiki/CSS) - Used for the main site design and layout.

- [CSS Grid](https://www.w3schools.com/css/css_grid.asp) - Used for an enhanced responsive layout.

- [JavaScript](https://www.javascript.com) - Used for user interaction on the site.

- [Python](https://www.python.org) - Used as the back-end programming language.

<a id=frameworks></a>

### Frameworks, Libraries & Programs Used

- [Balsamiq](https://balsamiq.com/) - Used to create wireframes.

- [LucidCharts](https://www.lucidchart.com/) - Used to create the flow diagrams.

- [Git](https://git-scm.com/) - For version control.

- [Github](https://github.com/) - To save and store the files for the website.

- [Visual Studio Code](https://code.visualstudio.com/) - Code editor used to create the site.

- [Am I Responsive?](http://ami.responsivedesign.is/) - The site was used to show my pages responsiveness on multiple screen sizes.

- [Google Fonts](https://fonts.google.com/) - To import the fonts used on the website.

- [Google Developer Tools](https://developers.google.com/web/tools) - To troubleshoot and test features, solve issues with responsiveness and styling.

- [Bootstrap](https://getbootstrap.com/) - To apply styling to buttons without having to worry about doing all the css myself allowing me to focus on the JavaScript.

- [BrowserStack](https://live.browserstack.com/) - To test my website on other browsers used by other operating systems such as the MacOs and safari.

- [Django](https://www.djangoproject.com/) - Used as the Python framework for the site.

- [PostgreSQL](https://www.postgresql.org) - Used as the relational database management.

- [Heroku](https://www.heroku.com) - Used for hosting the deployed site.

- [Gunicorn](https://gunicorn.org/) - Used for WSGI server.

- [Sycopg2](https://pypi.org/project/psycopg2/) - Used as a PostgreSQL database adapter.

- [Cloudinary](https://cloudinary.com) - Used for online static file storage.

---

<a id=deployment></a>

## Deployment

The deployed application can be found on [Heroku](https://online-scout-badge-manager-63d33c684e7e.herokuapp.com/).

<a id=heroku-deployment></a>

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | user's own value |

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

---

<a id=local-development></a>

## Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:
- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

<a id=clone></a>

### How to Clone

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/Ryan-ford25/Milestone_project3)
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/Ryan-ford25/Milestone_project3`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Ryan-ford25/Milestone_project3)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).


<a id=fork></a>

### How to Fork

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Ryan-ford25/Milestone_project3)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!
---

<a id=credits></a>

>
### Code
 * Another README guide was provided by the Slack community [Youtube video](https://www.youtube.com/watch?v=l1DE7L-4eKQ)
 * I used [stackoverflow](https://stackoverflow.com/questions/75045074/how-are-adapters-used-in-django-allauth) to learn about allauth adapters. In my case I made a custom adapter to redirect users with role of Scout to the scout dashboard template.
 * [Django documentation](https://docs.djangoproject.com/en/6.0/) had been used to explain inline formsets and how a parent and child model can be linked within a single form.

### Content

 * All content was written by the developer.
 * [Color contrast checker](https://coolors.co/contrast-checker/112a46-acc8e5) was used to check if the color scheme chosen would work well.

## Acknowledgements
 * Discord Community for encouragement and information.
 * My teacher Kevin provided me with help along the way.
 * The Discord community helped with providing examples of README files.