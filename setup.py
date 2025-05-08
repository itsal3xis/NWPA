from setuptools import setup, find_packages

setup(
    name="nwpa",
    version="0.1.0",
    description="NHL Win Prediction Analyst",
    author="Alexis Bernard",
    author_email="alexxqc2006@gmail.com",
    url="https://github.com/itsal3xis/nwpa",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'nwpa = nwpa.nwpa:main',
        ],
    },
    python_requires='>=3.7',
    install_requires=[
        "requests"
        "argparse"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
