# web_brute_force-selenium

-  [Clone project](#clone-project)
-  [Install dependencies](#install-dependencies-in-linux)
-  [Setting up selenium](#setting-up-selenium)
-  [Generate passwords](#generate-passwords)
-  [Run selenium script to crack the password](#run-selenium-script-to-crack-the-password)

## Clone project

```
git clone https://github.com/IsuruFerna/web_brute_force-selenium.git

```

## Install dependencies in linux

First we need to create an virtual environment

```
python3 -m venv .venv
```

Activate the virtual environment

```
source .venv/bin/activate
```

Then install dependencies

```
pip install -r requirements.txt
```

## Setting up selenium

In order to run the script you have to find the login form and IDs of the email and password text input. When you found you have to replace on the following names

-  `formBasicEmail`: Id of email input
-  `formBasicPassword`: Id of password input
-  `p.text-red-500 small`: In order to select and control error message I've choosed CSS_SELECTOR.

## Generate passwords

With the below command it will generate a file called `passwords.txt` with the possibilities of 94 x 94 x 94 x 94 x 94 x 94 list of ascii letter passwords(689869781056). It will take hours. so since this is for a testing I wouldn't reccomend to generate all because there's firewall to handle suspicious activities and it will probably Enable Rate Limiting. So this can't be done in real world scenarios

```
python generate_passwords.py
```

## Run selenium script to crack the password

```
python main.py
```

This process is not super fast. It will open your browser and try to simulate login with the list of passwords that you've generated. So the generated passwords are 6 characters long, minimum required password for a web application is 8 so if you think this can be done in realworld, you couldn't done in your lifetime since there're firewalls to handle suspicious activities

This will be the result if you able to find the correct password

```
get env: https://example-site.com/ foo@email.com
Attempt failed: Incorrect email or password, failed password: aaaaaa
Attempt failed: Incorrect email or password, failed password: aaaaab
Attempt failed: Incorrect email or password, failed password: aaaaac
No error message found. Checking if login was successful...
correct password: hello1
```
