# Django College Management System (beta)
This is a Simple College Management System Developed for Educational Purpose using Python (Django).
Feel free to make changes based on your requirements.

I've created this project while learnging Django and followed tutorial series from **SIBTC**

And if you like this project then ADD a STAR ⭐️  to this project 👆

## Features of this Project

## Support Developer
2. Add a Star 🌟  to this 👆 Repository


## How to Install and Run this project?

### Pre-Requisites:
1. Install Git Version Control
[ https://git-scm.com/ ]

2. Install Python Latest Version
[ https://www.python.org/downloads/ ]

3. Install Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]

*Alternative to Pip is Homebrew*

### Installation
**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```

Activate Virtual Environment

For Windows
```
$  source venv/scripts/activate
```

For Mac
```
$  source venv/bin/activate
```

**3. Clone this project**
```
$  git clone https://github.com/akanmu01/collegemanagementsystem.git
```

Then, Enter the project
```
$  cd collegemanagementsystem
```

**4. Install Requirements from 'requirements.txt'**
```python
$  pip install -r requirements.txt
```

**5. Add the hosts**

- Got to settings.py file 
- Then, On allowed hosts, Add [‘*’]. 
```python
ALLOWED_HOSTS = ['*']
```
*No need to change on Mac.*

**6. Database hosting Link **
``` python
**MYSQL**
	https://railway.app/project/29f816f2-41ac-4f11-9409-bdaafc1ee033/plugin/9dd56272-fe0a-4f19-ad81-7daeff7cabe3/Data
**Postgre**
	https://railway.app/project/2b8cf46d-b2d8-4e32-9283-50b91ac588b5/plugin/b4bf9297-6559-4d62-a966-54721910a9ff/Data
```
**7. Now Run Server**

Command for PC:
```python
$ python manage.py runserver
```

Command for Mac:
```python
$ python3 manage.py runserver
```

**8. Login Credentials**

Create Super User (Root Admin)
```
$  python manage.py createsuperuser
```
Then Add Email, Username and Password

**or Use Default Credentials**

*You can change password for Admin*
```
$  python manage.py changepassword admin
```
*You can change password for Teacher*
```
$  python manage.py changepassword Teacher
```

*You can change password for Student*
```
$  python manage.py changepassword Student
```

## For Sponsor or Projects Enquiry
1. Email - petrjoe02@gmail.com
2. Whatsapp - https://wa.me/+2348133643937
3. FaceBook - https://fb.me/coin09o
