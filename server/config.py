TORTOISE_ORM = {
    "connections": {"default": "sqlite://database/data.db"},
    "apps": {
        "models": {
            "models": ["models.user"],
            "default_connection": "default",
        },
    },
}
