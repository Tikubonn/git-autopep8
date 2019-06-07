
from setuptools import setup, find_packages

with open("README.md", "r") as stream:
    long_description = stream.read()

setup(
    name="git-autopep8",
    version="1.0.0",
    description="this package add a command that apply PEP8 code style to your codes that add to Git.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="tikubonn",
    author_email="https://twitter.com/tikubonn",
    url="https://github.com/tikubonn/git-autopep8",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "autopep8",
    ],
    dependency_links=[],
    entry_points={
        "console_scripts": [
            "git-autopep8 = git_autopep8_script.git_autopep8:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        'License :: OSI Approved :: MIT License',
    ]
)
