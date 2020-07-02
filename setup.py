import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='logic-joaovictorvi',
    version='0.0.4',
    description='lib de lógica para a cadeira de Lógica para computação',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    author='João Victor Duarte Viana',
    author_email='jv.duarte.viana@gmail.com',
    keywords=['atoms', 'formula', 'truth_table'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url='https://github.com/JoaoVictorViana/logic',
    python_requires='>=3.6',
)