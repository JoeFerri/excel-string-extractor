import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="exsextractor",
    version="1.0.0",
    author="Giuseppe Ferri",
    author_email="jfinfoit@gmail.com",
    description="exsextractor is a Python script that scans Excel and CSV files, extracting all strings from every cell and consolidating them into one or more output files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoeFerri/excel-string-extractor",
    packages=setuptools.find_packages(),
    py_modules=['esextractor'],
    install_requires=[
      'openpyxl',
    ],
    classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)