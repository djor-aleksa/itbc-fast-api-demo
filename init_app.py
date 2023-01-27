from fastapi import FastAPI


def init_app():
    app = FastAPI()
    return app


app = init_app()
