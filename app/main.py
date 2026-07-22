from fastapi import FastAPI

from app.bootstrap import ApplicationBootstrap

bootstrap = ApplicationBootstrap()

context = bootstrap.build()

app = FastAPI()

app.state.context = context