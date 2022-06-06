
## Vincent Brown
 
### Data Centric and Back Development Project

## Predict Your Sales

### A resource for sales professionals to accurately forecast sales
This is a detailed interactive website implemented with the intention of allowing better work relations and communications between managers and sales professionals. By acting as a form of communication and correspondence between sales professionals and their managers.

As many people know, often sales professionals can have a stressful role. When targets need to be hit, sales need to be made, a lot of pressure is put on the sales person and on their managers to feed back accurate predictions of what revenue is coming in. This application is designed to take a lot of the stress and anxiety out of the equation. This is done by having a simplified platform allowing both the manager and the sales professional different forms of access.

1. The Sales professional: Once they have a conversation / confirmation of a sale being made they can upload this on the Predict Your Sales platform. The purpose of uploading the prospective sale is that each user will be asked to provide the customer name, amount, close date and description. Various companies tend to use different forms or abbreviations for asking these 4 questions so the app can be used by any organisation and most importantly, these are the same 4 questions the manager will ask and require for their own reporting and conversations with management.
2. The Sales Manager: Once the manager logs in to the portal they will have a dashboard which shows an overall view of each sales person in an accordion. When they click on each salesperson, it will bring up a snapshot of the predicted sales. The 4 questions will be answered here which will make it very convenient for reporting purposes.

These are as follows:
1. Name: this is where the account name or customer name will go.
2. Amount: This will have the total value and deal size, to make things easier for forecasting and reporting purposes.
3. Description: Describe the conversation, need and buying process.
4. Time: When is the sale expected to close.


 #### Long Term Strategy:
The long term plan for this would be to continuously add on various features as the apps are used. Including a feedback button at the bottom of the salespersons dashboard, this is where they can highlight what might make the job easier for the person. Inevitably this could help develop the work relationship further and encourage more proactive and creative ideas from all staff members. This would also mean that these ideas have a reference point for who came up with the idea as well which in turn ensures trust but also career development.

My plans for this application would be to test it with my own role and even see if my team members at work would want to use an application for tracking their sales.


#### Site Interface:
The website has been built with a simplistic 3 page layout for those that are not signed in, a four page layout for users and then a 5 page layout for the manager.

##### New User:
When a new user goes to this site they can view the sales but do not have any permissions to edit/ delete or create any sales. They can also view the dashboard to learn about the team structure and also have the ability to then register and create an account.

##### Salesperson/ User:
A User is an active sales member of the team. Once they log in, they have a 4 page layout which is as follows: The Home/ Sales page to view all sales submitted, this is to view their own and colleagues sales. By doing this it demonstrates an open and transparent relationship between the team and encourages healthy sales competition. They do have permissions to create, read, update and delete their own sales from this page. The Third Page is to create an upload a new sale, this information is synced up to the MongoDB so any changes are recognised both on the site and in the database.

##### Manager :
A manager has the most privileges as they have admin access to everything. This is because the app is designed for small teams and to help managers communicate better with sales staff as well as support the reporitng process for Senior Management. They have access to all 4 pages previously mentioned but also an additional page which allows them to create , read, update and delete the users on their team. this too is synced with MongoDB  to enable transparent collection of data as well as allowing the team to grow and be dynamic in size.

### User Stories:
#### Sales Person
This user story will follow a new staff member (Woody) who joins a new company that is already using the Predict Your Sales application. When this new member began, they were instructed to create an account just like the other salespeople will have done. Or if the Sales Manager prefers they can create the account for them. The salesperson can have an amount of previous ability, so the app is available for all levels of experience and is only a tool to help with organising sales pipelines and forecasting.

#### Manager
Admin is an experienced Sales Manager, having worked in 2 of the largest tech organisations prior to this role, they have begun a new company mission which now caters for a smaller team of well trained salespeople to take advantage of some new territories and business opportunities. If successful, the team can grow to a much larger team and therefore each sale is of the utmost importance. Therefore they have decided to use Predict Your Sales in order to track, monitor and guide the team to success in an organised and much less stressful fashion.
 

### View the deployed Project Here
[Visit Live Site Here](https://predictyoursales.herokuapp.com/)

### Business Goals
* To increase the volume of sales.
* To allow every salesperson the right and ability to contribute to the team targets.
* To allow transparency and better communication between salespeople and management.
* To inevitably enable sales professionals to have a much better quality of work life, so they do not feel an abundance of stress and pressure over company goals.


### User Goals:
* To provide a simple yet easy flowing website capable for users of varying tech abilities to get easy access to sales information,e.g. if a new member joined the team and took over some sales/ accounts.
* To encourage the next team members comin on board that this is an organised and structured team that collaborates to success.
* To provide accurate and concise information regarding sales predictions which will put less stress on Senior Management, Middle Management as well as sales teams.
* To provide the user with helpful links and motivational resources.
*
###  Target Market & User Stories:
#### Target Market:
* Any salesperson with an interest in managing their own sales pipeline
* Any manager looking to responsibly and equally manage sales people
* Any company with an interest in accurate forecasting of sales


### UX Design Stages
#### Strategy
My goal for this design was to allow ease of access to information as well as allowing all types of users to upload sales information which means they do not need to remember every single sale/ account off the top of their head.

#### Scope
 For users of the site, I wanted to allow easy navigation across the 3-5 page structure depending on user permissions. This is to enable new members of the team to easily make their way to the register page or sales page if they are already new sales. Or for newcomers to read about how it all works in the dashboard section.

#### Structure
The informational design will be very simple and easy to follow, as this app will have both experienced and non experienced users, I want to appeal to the general audience. The dashboard will have a short about section explaining how and why the app is used. This will provide insight but also encourage new members to utilize the tool if they see colleagues being even more successful from it.

#### Skeleton
The navigation bar shall allow easy access to any page as well as clear instructions for the non-technical visitors to the site. Each page has a clear descriptive title as I wanted any user to have a clear and easy way to either sign up to become a member or to get the information they need to go to an event without having to sign up in case they are not tech savvy.This feature can be seen on many websites and therefore re enforces the functionality of the site.

#### Surface
My aim for this design was to use dark grey and white as the primary contrasting colors to indicate levels of importance to the various sections (navigation bar/ dashboard section/ login/ logout/ register/ manager users and new sales. This is to give a professional, sleek yet practical feel to the site where users are not being overwhelmed with information, they only see what is relevant.

### Wireframe Mockups:
Here are my wireframes for multiple pages of the Predict Your Sales app.

 PDF Attached Here

### Features
#### Home/ Sales Page
* Initially there is a consistent navigation bar across all 3-5 pages allowing access to Home, Dashboard, New Sales, Manage Users, Login/ Out / Register Page.

* There is a page titled "Sales in Progress" as once a sale has been closed won or closed lost the sale will be updated or deleted from the app.
 
* There is a search bar below this giving users a quick way to find a specific sale they may need to update.

* Below this I have created a section with some collapsible components, each component is a sale. If the user created that sale they can also edit that sale or delete the sale. They can view other colleagues sales but do not have permission to edit or change them in any way.

* And finally a footer with a message and disclaimer stating this project is for educational purposes only.

#### Dashboard Page
* Initially there is a consistent navigation bar across all 3-5 pages allowing access to Home, Dashboard, New Sales, Manage Users, Login/ Out / Register Page.

* There is a page titled "Sales Dashboard" positioned at the top.

* Below this created a series of cards to explain the following for the user profile:
##### User Profile Information
1. Role Description
2. Salesperson App Permissions
3. Career Progression
4. Bonuses & Pay

* There are also Sale Manager and Salespeople Resources below each card to provide motivational and organisational support.

* And finally a footer with relevant links to various social media pages of the group.

#### New Sales Page
* Initially there is a consistent navigation bar across all 3-5 pages allowing access to Home, Dashboard, New Sales, Manage Users, Login/ Out / Register Page.

* This page contains a form where both users and admins can create a new sale. Sellers will hopefully be creating new sales regularly whereas the Admin may have to create sales due to a shortage of staff or covering for one of their team members.

* The form contains 5 sections which 4 are required to submit your sales successfully, they are as follows:
1. Customer Name
2. Sale amount
3. Sale Description
4. Close Date
5. This is an optional button to choose whether the sale needs approval especially in cases where a discount may be offered.

* There is defensive programming in place here so if not a user they will be brought to the login page.


* And finally a footer with relevant links to various social media pages of the group.

#### Manage Users Page
* Initially there is a consistent navigation bar across all 3-5 pages allowing access to Home, Dashboard, New Sales, Manage Users, Login/ Out / Register Page.

* There is then Page Title "Manage Users" at the top of the screen

* Below this is a button "Add Users", when clicked this will bring the admin to a new page to add a new user to the team. This is also linked to the MongoDB

* This page contains a series of boxes, one for each user profile. Each User profile can be changed by the Manager, the purpose for this is so that in the case of a team member leaving but the sales need to be transferred to a new member of staff the sales manager can edit the username and password for the new member so the sales data has not been affected.

 * There is defensive programming in place here so if not the admin they will be brought to the login page.

* And finally a footer with relevant links to various social media pages of the group.

#### Login Page
* Initially there is a consistent navigation bar across all 3-5 pages allowing access to Home, Dashboard, New Sales, Manage Users, Login/ Out / Register Page.

* This page contains a form where both users and admins can log into their account.

* There is defensive programming in place here so if not a user they will be brought to the registration page.

* And finally a footer with relevant links to various social media pages of the group.

#### Features to Add in Future
* Adding a CAPTCHA to the login page would reduce the volume of fake accounts or limit hacking.
* Cookie and GDPR compliance page to allow users to have more control of how their data will be used.
* It would be great to set up an FAQ page for this site as with older members of the group there can tend to be regular recurring questions. This could be added to the dashboard page.
* Ideally I would love to add more into the dashboard where users could create a full user profile to include their own career goals and then to set markers with the manager for working towards these goals.


### Technologies
* HTML - Hyper Text Markup Language
* CSS - Cascading Style Sheets
* Materialize (4.2.1) - Mobile Responsive Framework
* Gitpod - Cloud Based IDE linked with Github
* Github - Online repository for hosting site
* Font Awesome - Provided a variety of font styles and icons used in the project
* Auto prefixer - to help structure code when finished - https://autoprefixer.github.io/
* HTML and CSS Validators - https://validator.w3.org/nu/#textarea / https://jigsaw.w3.org/css-validator/validator
* Chrome Developer Tools - Provided continuous learning and development tools to ensure high quality mobile user experience
* Javascript
* Python3
* Flask
* JQuery
* MongoDB
* Heroku


### Defensive Programming
* There are various forms of defensive programming practices in this project used for each page of the site. The main functionality for this is to block anyone from getting access to make changes to sales information uploaded by staff.

#### Sales Page
* All visitors can view sales information as this is to encourage an open transparent workplace as well as allow other sales people to see colleagues' success which will hopefully motivate them to find and upload new sales for themselves.

* Users who are logged in to their own account will then have the option to edit or delete their own sales

#### New Sales
* This page is limited to users who are logged in to their own account. If an admin or user is not logged in then they will be redirected to the login page

* Also if logged in to your own account you can only edit or delete your own sales so there is no chance of one person changing the data on someone else's sales.

#### Manage Users
* Only the admin has access to this page, if a user tries to access this page that is not the user, they will be redirected to login.
* An Admin is the only person who can make changes to user accounts
* They can also delete user accounts from the database

#### Passwords
* In order to hide any password information I have used the Werkzeug hash method to hide each password in a secret key to keep sensitive information from the cookies, website and database.

### Testing
#### Home Page
*  The navigation bar was built in a container using materialize so to ensure this was mobile responsive I used Chrome developer tools regularly to ensure the navbars responsiveness. This was tested with chrome dev tools using Iphone 5, desktop and IMAC sizes.
* This included a title, icon and 3-5 options to navigate throughout the site's pages.
*  When in mobile view the menu would take the burger icon shape and go on the right corner of the screen, when clicked this would become a dropdown for the rest of the menu.  
* The Sales Section is one container, a series of collapsible cards.
- The cards were tested by clicking the element to see if they would open up, if not then I checked the classes to ensure they were Materialize compliant.
- When clicking the sale, it would drop down and you can then see the sale information uploaded on the new sale form.
- In each card when logged in, the user could then see an edit or delete button for each sale. This only shows for the user that created the sale
* The Search option was tested by first creating the function and search bar and then checking the mongo db index page to see if the categories were added correctly. I then went on to search for several items to ensure it was functioning correctly.
* The bottom of the page consists of 4 links to various social media sites to allow the user to easily follow the groups social platforms.
* All links including the main button to get started have been clicked and checked to ensure they are fully functional in mobile and desktop view.
* Lighthouse mobile testing system was used regularly to improve overall UX design and mobile experience.

#### Dashboard Page
* The navigation bar was built in a container using bootstrap so to ensure this was mobile responsive I used Chrome developer tools regularly to ensure the navbars responsiveness.
* This included a title, icon and 3-5 options to navigate throughout the site's pages.
* Each link has been tested by clicking and ensuring that if the link is to another area on the site that it opens in the same tab.
* This page is primarily text based as it is an information and resources page. Therefore I had to carefully structure the cards in the center so they were mobile responsive. Below this I also included a series of helpful links and resources for salespeople and managers. Each link was also clicked to ensure it worked properly in a new tab

* The bottom of the page consists of a disclaimer.
* All links have been clicked and checked to ensure they are fully functional in mobile and desktop view.
* Each link has been tested by clicking and ensuring that if the link is to another area on the site that it opens in the same tab for the navbar.

#### New Sales Page
* The navigation bar was built in a container using bootstrap so to ensure this was mobile responsive I used Chrome developer tools regularly to ensure the navbars responsiveness.
* This included a form where users would submit all sales information required to submit the sale to the app and database.
* Multiple fields are required to limit the amount of poor data being uploaded to the database.
* Each link has been tested by clicking and ensuring that if the link is to another area on the site that it opens in the same tab.
* There is a submit and cancel button below the form.
- When clicking cancel you will be brought back to the sale page
- When clicking submit the data is passed successfully to the DB. This was checked by submitting sales and checking MongoDB.
* The bottom of the page consists of 4 links to various social media sites to allow the user to easily follow the groups social platforms.
* All links have been clicked and checked to ensure they are fully functional in mobile and desktop view.
* Each link has been tested by clicking and ensuring that if the link is to another area on the site that it opens in the same tab.
* The checkbox function is not a required field as the same may not need approval.
*
### Lighthouse Results
Performance = 98%
Accessibility = 92%
Best Practices = 100%
SEO = 91%


### Deployment
* This project was created using the Cloud based IDE Gitpod, I continuously added, committed and pushed my code to Github. This was instructed by Code Institute lessons and by my mentor. In order to deploy my website to github I followed the below steps:

* I began by logging into my Github account
* Then I click repositories section if not already in the top used repositories and click on the link Predict Your Sales
* Once I had opened this file, I then selected the settings option
* At this stage I scrolled down until you saw the Github pages section - this brought me to the dedicated page to deploying your site
* I then clicked a drop-down menu item which was labelled None and selected the Master branch
* The website automatically deployed once I selected the master branch
* I then scrolled back down to the section of Github pages to get the link for the deployed site.
* Scroll back down to the GitHub Pages section to retrieve the link to the deployed website.
github have also now created their own page for the deployment process as well. Visit Live Site Here

_____________________________________

The site was initially deployed on Github while in development but then I chose to deploy this via Heroku. Initially the steps were as follows:
1. Go to Heroku site and create an account.
2. Link my Heroku account with my github account by editing the settings and searching for my github account.
3. Once found, I then continue to search for the repo and select connect to repository.
4. Once connected I will then use the CLI to ensure the site is deploying successfully.

There was also a recent incident which meant the deployment process changed. Since I already had my app set up and created on my Heroku account, I simply had to use the CLI to reconnect the app back to the Heroku account.

I did this by typing the following command into the CLI "heroku git:remote -a Predict_Your_Sales"

After this I used git login -i which then prompted me to submit my email and password
Once accepted I was then able to deploy the app to heroku again by using the following commands:
git add .
git commit -m ""
git push 
git push to heroku

### Bug Fixes:
* The bugs experienced in developing this application were Python related.
* Thankfully I used Python and relied heavily on using print statements as well as getting Jinja feedback.
* This was most helpful when testing if there were any function errors.
* Also a good way for DB testing is to submit various forms and see if the data is received in the DB.
* There were form bugs initially too, although some designs are intentional- the sale amount section does allow letters and numbers which is intentional as some users might want to have an early estimate and give a low and high figure e.g €10,000 low, €50,000 high



#### Form Issues Not Logging in DB
Title: Form Issues
Environment : new_sales.html
Steps to reproduce a Bug: In order to reproduce this bug, simply remove the {% extends "base.html" %}.
Expected Result: Page will not load correctly (missing navbar)
Actual Result: Emails were not sent
Severity/Priority: High priority bug fix as without navbar there would be a very poor UI and lack of navigation
[View bug commit and fix Here](https://github.com/VinBdev/Predict_Your_Sales/commit/38e41c55481f7ecd448bd8344cbf8ea99dc80354)
 
 29th of April 2020
 
#### Passwords not hidden when created by user
Title: Form Issues
Environment : app.py
Steps to reproduce a Bug: In order to reproduce this bug, simply remove hash section from app.py
Expected Result: Passwords will not appear in MongoDB
Actual Result: Passwords will appear in MongoDB
Severity/Priority: High priority bug fix as without user info is not safe
[View bug commit and fix Here](https://github.com/VinBdev/Predict_Your_Sales/commit/c5cedf0e47da177ffb89a801d2229785f5e5b3c5)

#### Manage User page accessible by users
Title: Permissions
Environment : app.py
Steps to reproduce a Bug: In order to reproduce this bug, simply change the edit_user function from app.py
Expected Result: Users cannot edit other users
Actual Result: Users can edit users
Severity/Priority: High priority bug fix as without users can create dummy accounts and mess with data
[View bug commit and fix Here](https://github.com/VinBdev/Predict_Your_Sales/commit/07f152609685896fc5440df5a6af23c1909989eb )
 
26th of April
 
 
#### Validating Code:
All files were put through the following validators:
* https://validator.w3.org/nu/#textarea
* https://jigsaw.w3.org/css-validator/validator
* https://www.jshint.com/
* https://extendsclass.com/python-tester.html

### Credits
#### The Full Stack programme lessons on UX design and Bootstrap.
* I reviewed the previous lessons of the course while typing out the core HTML and CSS structure of this project. I then used the Bootstrap framework to enable site responsiveness for mobile/tablet and desktop users.

#### LMS content on Google maps & Email.js
* For these sections I reflected back on the course to the lessons around functions, event listeners, setting up an api and working with maps/ email.js

#### Youtube tutorials on Python best practices
* The google maps team has their own youtube channel containing lots of videos and documentation to support development and marker clusters. https://www.youtube.com/watch?v=ommyvZnYwe8

#### Stack Overflow
* Stack overflow was a great resource while using this project and navigating through javascript territory it allowed me to relate other developers problems to my own and then to reflect back on my own work using the feedback form other developers.

#### Content
* All content in the about me section was written by me and is fictionally based on my own experiences in sales teams
* The content written in the  app is all fictional especially all users names and info

#### Media
Youtube and other articles referenced are as follows :
*   https://www.salesreadinessgroup.com/blog/how-to-become-a-great-sales-leader
* https://salesdrive.info/key-strategies-for-successfully-managing-a-sales-team/
* https://www.youtube.com/watch?v=9X2fjctfIHs
*  https://www.youtube.com/watch?v=-N45bnTaSss
*  https://www.saleshacker.com/12-tips-on-managing-a-high-performing-sales-team41
* https://www.youtube.com/watch?v=rylwgRSgjG0
* https://www.youtube.com/watch?v=GrhSLf0I-HM
* https://www.richardson.com/sales-resources/defining-consultative-sales/
* https://kapta.com/resources/key-account-management-blog/key-account-management/10-tips-for-successful-key-account-management
* https://blog.hubspot.com/sales/habits-to-become-a-more-effective-salesperson

### Acknowledgements
* I was inspired to create this site after being unsure as to where I can go to help organise my own sales pipelines and give more accurate feedback to management.
* I would often be curious as to what other sales people were doing in terms of performance and what I can learn form them.
* I also received various links and resources from my mentor Brian Macharia

### Disclaimer
* This project is for educational purposes only.

### The Future of Predict Your Sales
* Once I have completed the Full Stack Software Development programme I would like to come back to this project and add on the following two features.

* An option for users to make full interactive accounts in a profile section with images, personalised journey goals and accomplishments.

##### Thank you very much for reading my Readme.md file. I welcome feedback and hope that you have found this file beneficial while researching Predict Your Sales!
