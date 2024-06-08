pip install pytest-docker

NB By default this plugin will try to open docker-compose.yml in your tests directory. If you need to use a custom location, override the docker_compose_file fixture inside your conftest.py file:

```
import os
import pytest


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    return os.path.join(str(pytestconfig.rootdir), "mycustomdir", "docker-compose.yml")
```

My initial 70_docker folder name causes error as it does not like numbers at start of folder name.