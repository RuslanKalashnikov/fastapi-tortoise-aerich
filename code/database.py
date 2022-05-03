from tortoise.contrib.fastapi import register_tortoise

from code import settings

DATABASE_CONFIG = {
    'connections': {'default': settings.DATABASE_URL},
    'apps': {
        'models': {
            'models': ['code.models', 'aerich.models'],
            'default_connection': 'default',
        },
    },
}


def init_tortoise(app):
    register_tortoise(
        app,
        config=DATABASE_CONFIG,
        generate_schemas=True,
        add_exception_handlers=True,
    )
