# Testing for GHIT Restaurant

## Issues and BUGS Throughout Development

Issues encountered during the development process was mainly the learning curve of trying to have my URLS and Views setup correctly.
This was eventually fixed, with the help of fellow students and Tutor support. Pointing me in the right direction of how to link up my URLS and views properly.

Other minor issues faced when first building out website was trying to convert all static files with Django.
Once the appropriate {{static ''}} tags  were assigned to the correct images these issues eventually cleared up.

First had issues with deployment to Heroku as well. 
![herokucrash 3](https://user-images.githubusercontent.com/65243328/176644389-f1fadd8a-b36a-4357-b294-790617ddf2cd.JPG)
The H10 ERROR was indicating that it was because of my PROCFILE. I then rectified this by making sure my procfile was changed to that of
something similar to the Django Blog project. This then worked afterwards.

After that I then had issues loading up Static files on Heroku Deployed app. As it was not able to pull static files from Cloudinary.
I troubleshooted this by making some changes to settings.py file thanks To Scott at Tutor Support.

![clouindary error1](https://user-images.githubusercontent.com/65243328/176645228-bf756a86-030a-4d29-ba20-39064d5c80ef.JPG)

## Validator Testing

### LightHouse

Testing was achieved through Google Chrome Lighthouse. Initially had to make sure that testing was done in Incognito browser as
my extensions were interfering with the testing giving the site low scoring.

•Website works on browsers such as Edge, Firefox, Safari and Google Chrome.

•Website content is easy to read and follow.

•Links between pages work harmoniously.

![lighthouse test](https://user-images.githubusercontent.com/65243328/176645805-81882a92-bc96-4fee-bc31-73465c3112b7.JPG)

### W3C MARKUP TOOLS

No major visible Errors where shown for Nu HTML validator, mainly just errors and warnings for spaces and duplicate <img> tags and <tabs>
This could not be helped as of the Bootstrap elements within the Code. Other than this no major issues found while testing.
 
  Home page:
 ![w3c html validator](https://user-images.githubusercontent.com/65243328/176647111-40a6e7c3-af06-42eb-b993-dd1de7ffd828.JPG)
  
  Menu page:
  ![w3c html validator menu](https://user-images.githubusercontent.com/65243328/176647467-f0983951-f6c3-42df-8804-d2fbc4735bdc.JPG)
  
  Booking page:
  ![w3c html validator booking](https://user-images.githubusercontent.com/65243328/176647515-c71d8db9-6227-42cc-a6cb-7237ed6fb179.JPG)
  


## Python Validator PEP8
  
  Hardly any errors discovered for Python testing but pretty much the same as W3C Validator, mainly blank line space errors and line too long errors
  however that could not be helped due to the code/ imports executed in order to make code work. Other than that everything came back clean.
  
  Admin.py:
  ![admin test](https://user-images.githubusercontent.com/65243328/176648420-f980aa1c-f0b8-45ac-8ad5-b619be41c7f2.JPG)
  
  Apps.py:
![apps test](https://user-images.githubusercontent.com/65243328/176648423-0f0e196e-80ad-4292-a04a-c35462cea7a7.JPG)
  
  Booking.views.py:
![booking view test](https://user-images.githubusercontent.com/65243328/176648427-067ccf92-725e-4ac0-aea0-17e4834f1736.JPG)
  
  models.py:
![models test](https://user-images.githubusercontent.com/65243328/176648429-690820ce-332b-42ef-8d5a-84acfc919895.JPG)
  
  Reservation.views.py:
![reservation view](https://user-images.githubusercontent.com/65243328/176648430-f208a01b-afb0-44c2-af91-2e12ddada1d7.JPG)
  
  Urls.py:
![urls test](https://user-images.githubusercontent.com/65243328/176648433-f20c5984-4134-48bf-a72f-30b0ca441a63.JPG)
  
  wsgi.py:
![wsgi test](https://user-images.githubusercontent.com/65243328/176648437-f862e96d-b6d0-455e-81cc-780b3ecabd9b.JPG)

  
 ## User Story testing
  
  ### Admin
As a Site Admin I can approve or disapprove Reservations so that I can avoid clashes with other customers.

As a Site Admin I can create, read, update and delete Reservations so that I can manage Bookings sent in by users.

As a Site Admin I can approve Reservations before it is published so that the users are able to see their Approved Reservations once logged in.
![admin testing](https://user-images.githubusercontent.com/65243328/176649580-87797a1e-bb08-499d-bf32-3248f3220171.JPG)

   ### User
  As a Member User I can register an account so that I can manage my reservations, so I can update, delete and create new reservation requests.
  ![userregistertesting](https://user-images.githubusercontent.com/65243328/176650555-a4a947c0-9b9b-453b-83bb-bac61d17981f.JPG)
![usersignintesting](https://user-images.githubusercontent.com/65243328/176650559-ca4d9d2a-2516-41f0-8752-3abee5005833.JPG)
![update delete reservations](https://user-images.githubusercontent.com/65243328/176649989-38b3978c-f049-4262-bcb1-e34cfbb8d114.JPG)
  
 ### General Browser User
  As a General user I can browse the site, view the menu and also make a booking via the bookings page. This will enable me to fill out a form with Date/Time
  and contact information that will be sent to the GHIT Staff's mailbox.
  ![booking test 1](https://user-images.githubusercontent.com/65243328/176651312-a6f3d57a-89f4-4e56-8f16-9a7a8c8cd8a4.JPG)
![booking test 2](https://user-images.githubusercontent.com/65243328/176651316-6f13b3d8-947d-4018-b4ef-f89507e03d24.JPG)

  
 ## Responsiveness
  
 Site performs well across all different platforms.
  
  Mobile:
  ![responsive mobile](https://user-images.githubusercontent.com/65243328/176651692-7ee0689a-8d39-4f19-afc2-c44209436553.JPG)
  
  Tablet:
![responsive tablet](https://user-images.githubusercontent.com/65243328/176651696-ebef4a23-973b-4de2-b0f9-0b306c9e8c49.JPG)
  
  Desktop:
![responsive desktop](https://user-images.githubusercontent.com/65243328/176651699-ad485f01-70b3-46f6-af9d-de8c35d14a04.JPG)

  
[Back to Readme]([https://mikacodez.github.io/mellowte/](https://github.com/MikaCodez/GHITrestaurant#readme))
