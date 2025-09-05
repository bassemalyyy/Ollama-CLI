from setuptools import setup, find_packages

setup(
    name='ollama-cli',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
        'langchain',
        'langchain_openai',
        'langchain_community',
        'requests',
        'geocoder',
        'pytz',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'ollama_cli = ollama_cli.cli:main',
        ],
    },
    author='Bassem Mohamed Ali',
    description='A CLI tool for interacting with Ollama local models with custom tools.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
)