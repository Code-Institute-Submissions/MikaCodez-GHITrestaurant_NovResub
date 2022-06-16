# GHIT Restaurant
GHIT Restaurant is a Fusion of Ghanaian and Italian cuisine based in London to dine in.


<img width="356" alt="Ghitreadme" src="https://user-images.githubusercontent.com/65243328/173249709-8e49068c-f163-4cc3-b701-93245fb6fec4.PNG">


## UX
### Users
The user should be able to interact with the website freely and be able to visit the menu, book and reserve a table with a date/time of their choice. They will be able to also Sign up and login with an authenticated account that allows them to interact with their booking and write about their dietary requirements such as allergies etc.

### Admins
The Admins should be able to manage the bookings of the User, being able to approve, delete requests that are receieved from the booking.

### User Stories
| iD | Story | Resolution |
| --- | --- | --- |
| #1 | Account registration | Admin App |
| #2 | Site Pagination | Web App |
| #3 | View Menu | Menu Section |
| #4 | Make A booking | Booking Section |
| #5 | View Booking | Reservation App |
| #6 | Cancel booking | Reservation App |
| #7 | Send an email request for special booking/special requirements | Booking section |
| #8 | Admin can manage user account | Admin App |
| #9 | Admin can manage user booking | Admin App |
| #10 | Admin can delete user account/booking | Admin App |

### Purpose
The Application is designed as a restaurant website which will be the first introduction to the user of what they can expect to find and enjoy their restaurant experience. The site provides an idea of the dishes available, the location of the restaurant and allows the user to be able to Manage their booking and reservation.

  
### Wireframes

Wireframes where designed in Figma with rough concept in mind.
Each pages wireframes includes mobile(small screen) & desktop(large screens).

![ghit wireframes 1](https://user-images.githubusercontent.com/65243328/173871566-ee33e486-a93f-4ad9-9f98-ea1f6fc27278.JPG)
![ghit wireframes 2](https://user-images.githubusercontent.com/65243328/173871576-5a6b8f42-7d14-47c1-acc9-1a9921e25239.JPG)
![ghit wireframes 3](https://user-images.githubusercontent.com/65243328/173871583-92e04afc-e638-46dc-b45e-b524f160f050.JPG)

### Colors


![coolors ghit](https://user-images.githubusercontent.com/65243328/174058277-86a93d21-2654-4ed0-a6f1-d3cf6e754b8a.JPG)

#000002 Rich Black used for the Gradient for the main bulk of the site. To give the clean aesthetic.


#59CBCF Dark Turquoise for the Buttons on the site to help them stand alone.


#DED9D9 Gainsboro for the intermediary positions of the site to help create balance.


#D4CE91 Medium Champagne on the menu sections of the website to help the food and drinks stand out.


#446D03 Dark Olive Green on some of the vegetables of the website.


#25252F Raisin Black on the Gradien of the main bulk of the site.


#FCFBF8 Baby powder on the intermediary positions of the site to help create balance.



## Features
Home Page

The home page has an attractive layout to keep the user engaged and enticed for whats to come when they eventually visit the restaurant . The page has a Navigation bar that links to other sections of the site and buttons on the page that link straight to the booking. If the user is not registered user and not logged in. The navbar has a login/register options and the button to take user to the login page.

![ghit homepage 1](https://user-images.githubusercontent.com/65243328/173861087-271f5dea-b433-496e-af98-14ff760ebd47.JPG)
![ghit homepage 2](https://user-images.githubusercontent.com/65243328/173861110-80353367-fc31-4db5-a7bb-75092602b769.JPG)

Menu Page

The Menu Page has an eye-catching layout to keep the user engaged and enticed for whats to come when they eventually visit the restaurant displaying a various amount of options for the user to choose from.


![ghit menu page](https://user-images.githubusercontent.com/65243328/173861128-5b934c14-537e-46d2-9702-c3a8d0fead54.JPG)
![ghit menu page 2](https://user-images.githubusercontent.com/65243328/173861118-ec841d7e-45ed-4255-9323-93df870a2980.JPG)

Booking Page

The Booking Page is where the user can input the date and time they want to visit the restaurant. There is also a form to leave their details for the Restaurant so the admin is aware of the user's requirements.

The Booking page also has a Google maps location of the Restaurant to help assist users in locating the restaurant for when they show up.

![ghit booking page 1](https://user-images.githubusercontent.com/65243328/173861149-75f4f125-76f1-4f06-92e5-1d80bb7cb37c.JPG)
![ghit booking page 2](https://user-images.githubusercontent.com/65243328/173861157-cde02af1-7dc9-43c1-8395-16844474867a.JPG)
![ghit booking page 3](https://user-images.githubusercontent.com/65243328/173861164-4330d63d-68f4-4a9f-9cb8-f80c16dc265d.JPG)


## Future Features

Login Page / Sign up Page

Allowing new users to sign up to site to manage reservations and existing users to log in and manage their reservations also.

Manage Reservation page

Allowing existsing users to View and Manage their reservations that have been approved by the Admin.

Edit a Reservation

Allowing existsing users to make changes to their approved existing reservation.

Delete a Reservation

Allowing existsing users to delete their approved existing reservation.

## Testing
### Bugs


## Deployment
The site was deployed to Heroku. The below steps were carried out to deploy.

Deployment steps add the list of requirements by writing in the terminal "pip3 freeze > requirements.txt"

Git add and git commit the changes made

Log into Heroku or create a new account and log in

top right-hand corner click "New" and choose the option Create new app, if you are a new user, the "Create new app" button will appear in the middle of the screen

Write app name - it has to be unique, it cannot be the same as this app

Choose Region - Europe selected in this instance

Click "Create App"

The page of your project opens. 8. Choose "settings" from the menu on the top of the page 9. Go to section "Config Vars" and click button "Reveal Config Vars"

Go to git pod and copy the content of "creds.json" file

In the field for "KEY" enter "CREDS" - all capital letters

Paste the content of "creds.json" and paste to field "VALUE" Click button "Add"

Add another key "PORT" and value "8000"

Go to section "Build packs" and click "Add build pack"

in this new window - click Python and "Save changes" click "Add build pack" again in this new window - click Node.js and "Save changes" take care to have those apps in this order: Python first, Node.js second, drag and drop if needed Next go to "Deploy" in the menu bar on the top

Go to section "deployment method", choose "GitHub"

New section will appear "Connect to GitHub" - Search for the repository to connect to

type the name of your repository and click "search"

once Heroku finds your repository - click "connect"

Scroll down to the section "Automatic Deploys"

Click "Enable automatic deploys" or choose "Deploy branch" and manually deploy

Click "Deploy branch"

Once the program runs: you should see the message "the app was sussesfully deployed" 23. Click the button "View"

Forking the GitHub repository By forking out of this repository you will be able to view and edit the code without affecting the original repository.

Locate the GitHub repository. Link can be found here: GHIT Restaurant Click the button in the top right-hand corner "Fork" This will take you to your own repository to a fork that is called the same as the original branch.

Making a local clone Locate the GitHub repository. Link can be found here. Next to the green Gitpod button you will see a button "code" with an arrow pointing down You are given the option to open with GitHub desktop or download zip You can also copy https full link, go to git bash and write git clone and paste the full link


## Credits

SCOPE code credits to Code Institute, Django Blog Walkthrough Project. HTML template credit to Lucian Tartea. I have ammended the code to my Restaurant sites specification.

Credits also due to Code Institute staff for helping in slack Mentor Anthony.
