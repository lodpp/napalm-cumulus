"""setup.py file."""
from setuptools import find_packages, setup

__author__ = 'Arthur Halet <arthur.halet@orange.com>'


# Read the requirements from the file
with open("requirements.txt", encoding="utf-8") as f:
    reqs = f.read().splitlines()

setup(
    name="napalm-cumulus",
    version="0.5.8+lodpp.0.3a3",
    packages=find_packages(),
    include_package_data=False,
    package_data={
        "napalm_cumulus": [
            "templates/*.j2",
            "utils/textfsm_templates/*",
        ],
    },
    author="Arthur Halet",
    author_email="arthur.halet@orange.com",
    description="Network Automation and Programmability Abstraction Layer with Multivendor support",
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/napalm-automation/napalm-cumulus",
    install_requires=reqs,
)
