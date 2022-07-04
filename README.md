# Secret Santa Program

## About
This program will send an email to everyone signed up for Secret Santa with the name of the person they will be getting a gift for as well as some rules.

## Access Instructions
* Only needs to be done once when setting up the program

1. Sign in to your gmail that contains the calendar you will use.

2. Navigate to [Google Console](https://console.cloud.google.com)

3. To the right of Google Cloud Platform, click New Project

4. Go through the steps to make a project.

5. Go to your project's dashboard.

6. Click the navigation menu in the top left corner.

7. Click APIs & Services --> Library.

8. Search for Calendar and click on Gmail API.

9. Click Enable.

10. Go back to the navigation menu in the top left corner.

11. Click APIs & Services --> Credentials.

12. Click Create Credentials at the top of the screen.

13. Click OAuth client ID.

14. You will now have to go through the steps to create an OAuth consent screen. In the Scopes section, add the following scope: 
    * https://www.googleapis.com/auth/gmail.send

15. When you are done with that, click Create Credentials at the top of the screen.

16. Click OAuth client ID.

17. Go through the steps of making an OAuth client ID.

18. When you are done, navigate to the Credentials dashboard.

19. Under OAuth 2.0 Client IDs, you should see the ID you just made.

20. Under Actions, you should see a download button.

21. In the popup screen that appears, click Download JSON.

22. In your downloads, rename the file to client_secret.json.

23. Move client_secret.json to this directory.

24. You are good to move on to the next steps below.


## Local Change Instructions
* Only needs to be done once when setting up the program

1. In example.csv, update the contents to be the names and emails of all participants (note: you can have more than three)
    * For instance, suppose Example was the name of a participant and example@gmail.com was their email. I would update Person1Name to Example and person1email to example@gmail.com

2. Rename example.csv to names.csv

3. Update line 5 of message.py to include your specific rules

4. Make sure that Python3 is downloaded and up-to-date

5. Open Terminal (Mac) or Command Prompt (Windows)

6. Navigate to this directory using cd commands

7. Run the following command in Terminal/Cmd: ```pip install -r requirements.txt ```

## How to Run the Program
1. Open Terminal (Mac) or Command Prompt (Windows)
2. Navigate to this directory using cd commands
3. Run the following command in Terminal/Cmd: ```python3 app.py```

## Files
* .gitignore contains all the files that Github should not commit (it is important that you do not commit your client_secret.json or secrets.csv files)
* app.py is the application that verifies credentials and calls the other files' functions
* client_secret.json contains your Google OAuth client secrets
* emails.py handles working with the Gmail API and sending messages
* example.csv is an example CSV file for what names.csv should look like
* message.py handles getting the body and subject of each participant's email
* names.csv contains all the participants' names and email addresses
* README.md is this file you're reading right now
* requirements.txt contains all the requirements you will need for this program

## Sources
* [Gmail Send Example](https://stackoverflow.com/questions/37201250/sending-email-via-gmail-python
)

