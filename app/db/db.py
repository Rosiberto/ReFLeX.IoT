import sqlite3

import click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES            
            )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    conexao = g.pop('db', None)

    if conexao is not None:
        conexao.close()



def init_db():
    conexao = get_db()

    with current_app.open_resource('./db/schema.sql') as f:
        conexao.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


#inicializar o banco de dados
#dentro da pasta app, executar:
# flask --app app init-db

    


