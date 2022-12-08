# About

This is a little Django web application that does an [OpenDrift](https://github.com/OpenDrift/opendrift) [Leeway](https://opendrift.github.io/choosing_a_model.html) simulation with a set of provided parameters via a web formular. The result is sent to a user via e-mail.

This is an experimental tool to help Search and Rescue operations. An experimental service is available at [leeway.tuerantuer.org](https://leeway.tuerantuer.org).

Sample output from the leeway tool (100 points, 1km radius, south of Lampedusa):

![Example leeway output](./.github/leeway-simulation-output.png)


# Installation

1. Clone this repository and change into the new directory:
   ```bash
   gh repo clone digitalfabrik/leeway
   cd leeway
   ```
2. Create an virtual environment and activate it:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install the dependencies:
   ```bash
   pip install -e .
   ```
4. Initialize the database:
   ```bash
   cd opendrift_leeway
   python3 manage.py migrate
   python3 manage.py createsuperuser
   ```

# Development Server

1. Switch into the cloned project and then into the `opendrift_leeway` subdirectory.
2. Open two terminals:
   1. In the first terminal run:
      ```bash
      source ../.venv/bin/activate
      python3 manage.py runserver
      ```
   2. In the second terminal run:
      ```bash
      source ../.venv/bin/activate
      celery -A leeway worker -l INFO
      ```


# Packaging

1. Install build dependencies: `python3 -m pip install --upgrade build twine`
2. Build python package: `python3 -m build`
3. Upload target distribution to PyPI: `twine upload ./dist/opendrift-leeway-*.tar.gz`


# Production Server

This details the installation on Debian with Apache2 and mod_wsgi.

1. Create target directory on the production system:
   ```bash
   sudo mkdir /opt/iopendrift-leeway
   sudo chown www-data:www-data /opt/opendrift-leeway
   ```
2. Create the virtual environment:
   ```bash
   sudo -u www-data bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install the application into the virtual environment:
   ```bash
   pip install opendrift-leeway
   ```
4. Install Docker and add the `docker` group to the `www-data` user.
5. Create symlink to facilitate the Apache configuration:
   ```bash
   ln -s $(python -c "from opendrift_leeway.core import wsgi; print(wsgi.__file__)") .
   ```
6. Configure Apache2 according to example.
7. Set up Celery worker with `leeway-celery.service` and start the service.
