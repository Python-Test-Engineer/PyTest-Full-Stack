

https://pypi.org/project/pytest-docker/


pip install pytest-docker

NB By default this plugin will try to open docker-compose.yml in the root of the tests directory.
 
If you need to use a custom location, override the docker_compose_file fixture inside your conftest.py file:

```
import os
import pytest

@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    return os.path.join(str(pytestconfig.rootdir), "tests/docker", "docker-compose.yml")
```

My initial 70_docker folder name causes error as it does not like numbers at start of folder name.