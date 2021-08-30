# Contributors page

## Get started

### Environment variables

`HOST`, default : 0.0.0.0

`PORT`, default : 80

### Develop

To run the app in debug mode :

- Install deps : `pip3 install -r requirements.txt`
- Run the run with hot reloading : `cd app/ && uvicorn main:app --reload`

### Architecture

Architecture reference: [Click here !](https://fastapi.tiangolo.com/tutorial/bigger-applications/)

```
.
├── app                  # "app" is a Python package
│   ├── __init__.py      # this file makes "app" a "Python package"
│   ├── main.py          # "main" module, e.g. import app.main
│   ├── dependencies.py  # "dependencies" module, e.g. import app.dependencies
│   └── downloaders          # "downloaders" is a "Python subpackage"
│   │   ├── __init__.py  # makes "downloaders" a "Python subpackage"
│   │   ├── download.py     # "items" submodule, e.g. import app.downloaders.items
│   │   └── users.py     # "users" submodule, e.g. import app.routers.users
│   └── filesManagers         # "filesManagers" is a "Python subpackage"
│       ├── __init__.py  # makes "filesManagers" a "Python subpackage"
│       └── utils.py     # "admin" submodule, e.g. import app.filesManagers.admin
```
