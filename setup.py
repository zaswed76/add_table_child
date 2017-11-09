from os.path import join, dirname

import add_table
from setuptools import setup, find_packages

setup(
        name="add_table",
        # в __init__ пакета
        version=add_table.__version__,
        packages=find_packages(
                exclude=["*.exemple", "*.exemple.*", "exemple.*",
                         "exemple"]),
        include_package_data=True,
        long_description=open(
                join(dirname(__file__), 'README.rst')).read(),
        install_requires=[],
        entry_points={
            'console_scripts':
                ['add_table = add_table.main:Main']
        }

)

