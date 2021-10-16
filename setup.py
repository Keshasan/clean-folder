from setuptools import setup

setup(
    name='clean-folder',
    version='1.0.0',
    description='Script sorting tree folders',
    url='https://github.com/Keshasan/clean-folder',
    author='Aleksandr Holoborodko',
    author_email='kesha3084@gmail.com',
    license='',
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean_folder:clean_folder_func']}
)