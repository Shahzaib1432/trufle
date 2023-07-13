from setuptools import setup

setup(
    name='trufle',
    version='1.0.0',
    author='Muhammad Ahmad',
    description='A Python GUI framework',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Shahzaib1432/trufle',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    packages=['trufle'],
    install_requires=[
        'PyQt5',
        'random',
        'string',
        'os',
        'sys',
        'typing',
        'pathlib',
    ]
)
