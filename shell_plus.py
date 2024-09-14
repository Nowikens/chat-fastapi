"""
This gives django's shell_plus like functionalities with ipython and autoimports
Associated article: https://www.pedaldrivenprogramming.com/2021/01/shell-plus-for-sqlalchemy/
"""
from importlib import import_module

from IPython import embed

from sql import Base


class IpythonAutoImporter:

    # message that's displayed when entering Ipython
    banner = 'Additional imports:\n'

    def import_models(self):
        """Auto imports all models that uses Base.

        This does not really auto imports, it gets all model classes from
        sqlalchemy's registry of model classes and makes it global variables
        which is essentially equivalent to import.
        """
        for clzz in Base.registry._class_registry.values():
            if hasattr(clzz, '__tablename__'):
                globals()[clzz.__name__] = clzz
                import_string = f'from {clzz.__module__} import {clzz.__name__}\n'
                self.banner += import_string

    def import_others(self):
        """Auto imports whatever else is necessary.

        Check import_models docstring for extra info.
        """
        # Add any imports that are needed
        other_imports = [
            # schema:
            # module, what's imported
            ("main", "app"),  # this essentialy gives: from main import app
            ("sql", "get_db")
        ]

        for imp in other_imports:
            module, imported = imp
            # get module, and get from it whatever you want to import: function, class etc.
            globals()[imported] = getattr(import_module(module), imported)
            import_string = f'from {module} import {imported}\n'
            self.banner += import_string


auto_importer = IpythonAutoImporter()
auto_importer.import_models()
auto_importer.import_others()

embed(colors='neutral', banner2=auto_importer.banner)
