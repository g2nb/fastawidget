import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setup_args = dict(
    name='fastawidget',
    version='1.0.0',
    packages=['fastawidget'],
    url="https://github.com/g2nb/fastawidget",
    author="Thorin Tabor",
    author_email="tmtabor@cloud.ucsd.edu",
    description="A user-friend widget for JupyterLab that accepts a FASTA file and displays it within a notebook.",
    license="BSD-3-Clause",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "jupyterlab>=3.0",
        "ipywidgets>=7.0.0",
    ],
    zip_safe=False,
    include_package_data=True,
    python_requires=">=3.7",
    platforms="Linux, Mac OS X, Windows",
    keywords=['fasta', 'bioinformatics', 'genomics', 'visualization', 'Jupyter', 'JupyterLab', 'JupyterLab3'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Jupyter",
    ],
    data_files=[("share/jupyter/nbtools", ["nbtools/fastawidget.json"])],
)


if __name__ == "__main__":
    setuptools.setup(**setup_args)
