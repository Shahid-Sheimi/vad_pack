from setuptools import setup, find_packages

setup(
    name='my_vad',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'torch>=1.10.0',
    ],
    author='Shahi Hussain',
    author_email='shahieed39@gmail.com',
    description='A package for applying voice activity detection using Silero VAD',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Shahid-Sheimi/vad_pack.git',  
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
