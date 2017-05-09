# Demo Blog
## Prerequisites
- Ubuntu server (*app was tested using 16.04, other versions could work as well*)
- Python 3.5 (*other versions compatibility is not guaranteed*)
- (*optional*) [virtualenv](https://virtualenv.pypa.io/en/stable/installation/ )  
## Instalation
1. Clone the repo sowhere and `cd` into it.
2. Run `pip install -r requirements.txt` to install dependencies.
4. Cd into `/demoblog` folder
5. Run `manage.py migrate` to migrate DB schema
6. Run `manage.py createsuperuser` and follow instructions to create an admin user

## Runnung the app
1. Run `manage.py runserver`
2. Go to `host:port/admin` and login with admin user
3. Create Blog posts
4. Go to `host:port/blog`
5. Enjoy!

## Roadmap (things that are never gonna get done)

- Create tests
- Create better templates
- Add functionality with the tags
- Add custom 404 page
- Fix bugs in issues