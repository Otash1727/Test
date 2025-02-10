The program was created using Django + Postgresql + Rest Api.

----------------------------------------------------------------------------------------------
- Url to view the given assignment
- https://docs.google.com/document/d/1TFLX3MqYcfAVTbExSqEHuyrKE9CKE4VDzWuRjlcRwVw/edit?tab=t.0 
----------------------------------------------------------------------------------------------

---------------------------- To run the project without Docker ---------------------------

1. Activate the env. Command to activate 
    ---- source env/bin/activate or .\.env\Scripts\Activate -----

2. Install the dependencies in requirements.txt on your OS. 
    ---- pip install -r requirements.txt -----

3. Enter your information to the database of Postgresql 
    e.g. settings.py  To reach .env: cd ---- app/base/settings.py ----    
    Reminder:  All the information is included in this file. The code to connect all the migration with the database is \
    --------- python manage.py makegrations-----------
    --------- python manage.py migrate --------------

4. Command of creating Django admin
    --------  python manage.py createsuperuser -------

5.	The command to run Django is
    ------ python manage.py runserver --------
    after this command you see Django online on console. 
    
    --->>PS C:\Users\user\Desktop\your_project> python manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    January 24, 2025 - 21:48:51
    Django version 5.1.5, using settings 'base.settings' 
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK. <<--------


To get more information about Django project here: https://docs.djangoproject.com/en/5.1/intro/tutorial01/

------------------------------ To use API------------------------------------
You can’t use the API directly to GET or POST information. To do this, you have to use token. 

how get Token

![Image](https://github.com/user-attachments/assets/b16cfd85-72be-4c01-90fa-9e94b4b1863f)

