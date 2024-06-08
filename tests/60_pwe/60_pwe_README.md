These test are based on articles at pytest-with-eric.com

Videos are available at: [PyTest With Eric](https://www.youtube.com/playlist?list=PLsszRSbzjyvm5meFiH-rDU-YiC5kcOLcK)

These are for my own development and also to add the tests to PyTest Full Stack.

pip installs required to date:

- `pip install pytest-html`
- `pip install typer`
- `pip install PyYAML`
- `pip install pytest-mock`
- `pip install tox`

Because of the nature of conftest.py seemingly unble to read src/task_manager based on its location here, the src files, as it were, are placed in 60_pwe/task_manager.

This might be different if the test suite had src and tests folders in root rather than all these sub folder which we are using for test structure  purposes.