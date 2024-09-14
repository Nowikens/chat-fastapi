# Migrations
[Alembic](https://alembic.sqlalchemy.org/en/latest/) is used for migrations. As a shortcut there are two Makefile's tasks:
```bash
# generating migrations

make makemigrations
```
```bash
# applying migrations

make migrate
```

# Shell plus
Django has a great library dedicated to making life easier called [django-extensions](https://django-extensions.readthedocs.io/en/latest/), part of which is shell_plus which is a python terminal but with automatic models imports, suggestions etc.
Thanks to [this Austin Riba's article](https://www.pedaldrivenprogramming.com/2021/01/shell-plus-for-sqlalchemy/) I added something that acts like django's shell_plus.
```bash
# using python

python shell_plus.py

# using Makefile's task
make shell_plus
```