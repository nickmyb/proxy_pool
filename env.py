import environs


class EnvMixin:
    def __init__(self: 'EnvMixin') -> None:
        self.env: environs.Env = environs.Env()
        self.env.read_env()


DOT_ENV: EnvMixin = EnvMixin()
