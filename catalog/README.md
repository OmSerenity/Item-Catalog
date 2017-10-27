# Northern Nevada Desert Plants:  A Catalog Project 

# About

Plants which grow and thrive in the desert climate of Northern Nevada are cataloged here.  This application provides a list of items, in this case, plants, within a variety of categories as well as a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

# Inner Workings of this Project
  - Python
  - Flask
  - SQLAlchemy
  - OAuth
  - Google Login
  - Facebook Login
  - HTML5
  - CSS3
  - Bootstrap

# You will need these to run the program:

  - Python 3
  - Vagrant
  - Virtualbox
  - patience (just kiddling!)
  - Google Dev Account (to obtain app/client id and secret for oAuth2)
  - Facebook Dev Account (to obtain app/client id and secret for oAuth2)

# Obtain OAuth Credentials
  - Go to https://console.developers.google.com/apis and https://developers.facebook.com/
  - Obtain app/client ids and client secrets
  - Copy and paste your unique values in 'client_secrets.json' and 'fb_client_secrets.json'
  - Be sure to replace your data client id where indicated in 'login.html'
  
# How to run the project

 First, create the sample database:
> python create_database.py
 
 Second, populate the sample database:
 > python generate_dbinfo.py
 
 Third, run the server
 > python server.py
 
Enjoy!

 ##  Issues/Known Bugs:
None.   
_If you find any, please let me know :)_

##  Frequently Asked Questions:

1.   How can I log in?
*After you've pasted your developer info / client IDs for Google and Facebook in the login.html file, and run the program in your browser, click on the Google or Facebook login icons and you should be able to login*

 2.  What can I do after I log in?
 *After you are authorized as a user, you will be able to create, add, edit, or delete the different categories and entries.*

Attributions

User Icon and plant icons designed by Chanut is Industries from Flaticon (https://www.flaticon.com).

Plant info from: https://www.unce.unr.edu/publications/files/ho/2007/sp0712.pdf, http://www.onlinenevada.org/articles/nevada-vegetation-overview, and https://www.desertusa.com/

License
---- 

MIT - open source!
*Please see the License.txt file for details.*
