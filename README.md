# Datyy

Datyy is a template for Data Dashboard applications.

## Motivation

This template solves the basic needs of every application, such as:

- Login system
- Logging
- Navbars, sidebars, menus, submenus etc.
- Layouts, components
- Basic UI interaction, hide sidebar, collapse submenu etc.

Since it's a Data Dashboard, it contains examples of how to:

- Preserve application states
- Plot different kinds of graphs/charts
- Interact with components
- Update graphs on dropdown/slider/radioitem selection
- Change states by clicking on a graph etc.

The idea is to speed up the process of creating new Data Dashboards by rearranging, modifying, and styling individual simple components, focusing on logic and building on the simple examples.

## Preview

<p align="center">
  <img src="/preview/datyy.gif?raw=true"/>
</p>

## Technologies

- Flask
- Dash
- Plotly
- SQLAlchemy

## Setup

Set up `pipenv` environment and run:

```
pipenv install --dev
```

Create `.env` file and include the following variables:

```
# Database
# If you are using MySQL (if not, check SQLAlchemy docs):
DBURI=mysql+mysqlconnector://<user>:<pass>@<host>:<port>/<db>

# Logs
LOG_FOLDER=<path-to-log-folder>
```

Check `config.py`, `database.py`, create table, insert user and run `app.py`

### Service + Gunicorn + Nginx Setup

Create `.service` file in `/etc/systemd/system/`:

```
[Unit]
Description=Gunicorn service - Datyy app
After=network.target

[Service]
User=<user>
Group=www-data
WorkingDirectory=<working-filepath>
Environment="PATH=<env-filepath>"
ExecStart=<env-path>/gunicorn --bind unix:<working-filepath>/datyy.sock app:server

[Install]
WantedBy=multi-user.target
```

Create `datyy` in `/etc/nginx/sites-available/` and link it to `sites-enabled`:

```text
server {
    listen 80 default_server;
    server_name domain www.domain;

    location / {
        include proxy_params;
        proxy_pass http://unix:<working-filepath>/datyy.sock;
    }

	location /static {
		alias <working-filepath>/static;
	}
}
```
