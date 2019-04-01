from setuptools import setup

setup(name='grpc_testauth_api',
    version='0.0.1',
    packages=['grpc_testauth_api'],
    install_requires = [
        'grpcio',
        'googleapis-common-protos'
    ],
    zip_safe = False
)
