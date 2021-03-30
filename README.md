# Mailing service

This service has been created using Python 3.7 and smtplib library to enable you to engage customers across the channel email.
The application was deployed in Heroku and actually is used in a large number of service cells of eva conversational flows.

## Prerequisites

- 	Python 3.7+
- 	Postman
- 	Cloud account (Azure, GCP, Heroku, etc)

## Local testing
- Run the file app.py 
- Send this cURL with your fauvorite rest service client (I prefer Postman)

```json
curl --location --request POST '[URL]' \
--header 'Content-Type: application/json' \
--data-raw '{
    "plaintext":"[plaintext]",
    "asunto":"[asunto]",
    "sender":"[sender]"
}'
```

Where:
- 	[URL]: Refers to the service endpoint
- 	[asunto]: Refers to the subject of the message
- 	[plaintext]: Refers to the content of the message
- 	[sender]: Refers to the mail sender name

## Considerations when deploying GCP
- 	To the main file you have to put main
- 	You have to indicate the first function that should run
- 	This function must be passed as a parameter self
- 	You have to extend the app's permissions

## Permission extension
- 	Go t- o the Google Cloud Console
- 	Click the checkbox next to the role you want to grant access to.
- 	Click Show dashboard in the upper right corner to bring up the Permissions tab
- 	Click Add Member
- 	In the New Members field, type allUsers
- 	Select the Cloud Functions function> Cloud Functions Invoker from the Select a function drop-down menu
- 	Click Save

## Configuring SMTP mail
•	Go to the https://myaccount.google.com/security
•	Go to item "Seguridad"

![image](https://user-images.githubusercontent.com/68356488/113006532-d78f4e80-914b-11eb-9eea-a9b6e4e10ac8.png)


•	And open the two steps verify

![image](https://user-images.githubusercontent.com/68356488/113007416-951a4180-914c-11eb-989b-652d854f6709.png)


•	Follow the steps wizard

![image](https://user-images.githubusercontent.com/68356488/113007592-ba0eb480-914c-11eb-9545-d6d4dacbfb7e.png)


•	Add an app password

![image](https://user-images.githubusercontent.com/68356488/113008362-589b1580-914d-11eb-89b0-be106e1debf7.png)


•	Take note of the new app password

![image](https://user-images.githubusercontent.com/68356488/113008491-75cfe400-914d-11eb-873d-138f20f115ff.png)

#### Note: this email and app password must be added to the line 33 in app.py fileNote: this email and app password must be added to the line 33 in app.py file
