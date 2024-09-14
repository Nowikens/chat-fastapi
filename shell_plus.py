"""
This gives django's shell_plus like functionalities with ipython and autoimports
Associated article: https://www.pedaldrivenprogramming.com/2021/01/shell-plus-for-sqlalchemy/
"""
from IPython import embed

from sql import Base

banner = 'Additional imports:\n'
from main import app

banner = f'{banner}from app.main import app\n'

for clzz in Base.registry._class_registry.values():
    if hasattr(clzz, '__tablename__'):
        globals()[clzz.__name__] = clzz
        import_string = f'from {clzz.__module__} import {clzz.__name__}\n'
        banner = banner + import_string

embed(colors='neutral', banner2=banner)