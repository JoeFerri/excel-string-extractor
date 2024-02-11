:: JF
:: recursively removes python cache files
:: see https://bobbyhadz.com/blog/python-remove-pycache-folders-and-pyc-files#remove-__pycache__-folders-and-pyc-files-in-python-project

python -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
python -Bc "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]"
