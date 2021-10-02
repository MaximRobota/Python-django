Learning the Django framework

### Plan
- [x] Install Django
- [x] Install Admin https://docs.djangoproject.com/en/3.2/intro/tutorial07/
- [x] Install JET admin plugin https://pypi.org/project/django-3-jet/
- [x] Create Admin templates
- [x] Add Auth0
- [ ] REST Api

### Preparing
1. Make sure you have `python`, `pip` installed.
    `pip3 install -r requirements.txt`
2. Rename `.env.example` to `.env` and populate it with the client ID, domain, secret.
3. Register `http://localhost:8000/complete/auth0` as `Allowed Callback URLs` and `http://localhost:8000`
as `Allowed Logout URLs` in your app settings (https://manage.auth0.com/).

### Start
    python3 manage.py migrate
    python3 manage.py runserver

http://127.0.0.1:8000/ - View

http://127.0.0.1:8000/admin  - Admin


*For additional info please see commands.txt