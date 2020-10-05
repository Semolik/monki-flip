import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='monki-flip',
    version='1.0.0',
    author='n0spaces, Semolik',
    description="'monki flip' video generator",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Semolik/monki-flip',
    packages=setuptools.find_packages(),
    package_data={'gsbl': ['media/*.*']},
    entry_points={'console_scripts': ['monk=gsbl.__main__:main']},
    install_requires=['pylsd-nova>=1.2.0', 'numpy', 'Pillow', 'moviepy'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
