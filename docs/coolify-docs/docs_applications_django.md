Skip to content
Menu
Return to top
# Django ​
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
## Requirements ​
  1. Set the base directory where your `requirements.txt` and `manage.py` files are located.


> In the example repository, it is `/coolify`.
  1. Add `gunicorn` to the `requirements.txt` file, official docs.
  2. Add `localhost` and your `domain` to `ALLOWED_HOSTS` in `settings.py` file,  official docs.


> `Localhost` is required for health checks to work properly.
