# Documentation

The documentation of this project is handled using [Sphinx](https://www.sphinx-doc.org/en/master/usage/quickstart.html). The raw files in markdown and reStructuredText (RST) formats are saved in `docs/` folder. A mandatory `conf.py` file stores configuration information for Sphinx, including project title and version, used extensions, and theme. A `toctree` list is created in `index.md` to generate the table of content. Any files not included there will not show up in the documentation.  
Automatic documentation of classes and methods can be generated from docstrings in the `api.rst` file using `autoclass`. The docstring should be in Sphinx format listed [here](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html). Example below.
```python
"""[Summary]

:param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
:type [ParamName]: [ParamType](, optional)
...
:raises [ErrorType]: [ErrorDescription]
...
:return: [ReturnDescription]
:rtype: [ReturnType]
"""
```
To compile the documentation into **.html** files in `docs/html/` folder, run the following command:
```bash
> sphinx-build -M html sourcedir outputdir
```
Specifically for this project, the commands would look something like:
```bash
> conda activate runcontrol
> cd RunControl/docs/
> sphinx-build -M html ./ build/
```