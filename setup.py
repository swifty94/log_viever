from setuptools import setup

setup(
    name='LogViewer',
    version='1.0',
    long_description=__doc__,
    packages=['log_viewer'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'waitress']
)