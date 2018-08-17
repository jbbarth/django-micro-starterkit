Your App Name
=============

An app that rocks!


Install
-------

This project is developed in Python. You may want to use a virtualenv
if you have multiple Python projects on a single machine.

You'll also need a recent pip (at least >8.0 ; the 1.5.x version that
ships with MacOSX is *not* suitable for pip-tools, which is itself
mandatory to install the project).

If needed, install a specific pip version with:
```
curl -s https://bootstrap.pypa.io/get-pip.py | python - "pip==8.1.1"
```

Also ensure you have a recent version of setuptools:
```
pip install -U setuptools
```

You may want to In a virtualenv of your choice:
```
pip install pip-tools
./script/pip-sync
```


Develop
-------

    python app.py runserver_plus

