# Makefile

# generate migrations
makemigrations:
	alembic revision --autogenerate -m

# apply migrations
migrate:
	alembic upgrade head

# more helpful shell with autoimports, something like django's shell_plus which is super convenient
shell_plus:
	python shell_plus.py