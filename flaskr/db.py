from flaskext.mysql import MySQL

import click
from flask import current_app, g
from flask.cli import with_appcontext

mysql = MySQL()

def get_db():
    if 'db' not in g:
        g.db = mysql.get_db()

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        cursor = db.cursor()
        pass


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

    
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    mysql.init_app(app)