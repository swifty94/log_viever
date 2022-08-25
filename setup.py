from setuptools import setup

setup(
    name='LogViewer',
    version='1.3',
    long_description=__doc__,
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'waitress']
)