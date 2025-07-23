# Documentation

## Sphinx
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
To locally start a web server and view the documentation, run the following command and then open `http://localhost:8000` in a browser.
```bash
> cd build/
> python3 -m http.server 8000
```

## Read the Docs
[Read the Docs](https://about.readthedocs.com) is a convenient platform to automatically compile and deploy documentation, with support for Sphinx. Each time a new commit is published to the watched branches on GitHub, ReadtheDocs will automatically start another build of the documentation. Git tags can also be added as versions, so it is easy to go back to previous releases of the program and read the documentation for a specific version.  
The ReadtheDocs project has the following configuration:
```
Name: SBCRunControl
Repository URL: https://github.com/SBC-Collaboration/SBC-RunControl.git
Connected repository: No connected repository
Language: English
Default version: stable
URL versioning scheme: Multiple versions without translations (/<version>/<filename>)
Default branch: develop  # This is the branch that "latest" version points to.
Path for .readthedocs.yaml: docs/.readthedocs.yaml
Programming Language: Python
```
To set up automatic builds based on GitHub commits, visit Building -> Integrations -> GitHub incoming webhook, and note down **Webhook URL** and **Secret**. Then go to GitHub repository page for **RunControl**, go to Settings -> Code and automation -> Webhooks -> Add webhook, and enter the following configuration:
```
Payload URL: [Webhook URL]
Content type: application/json
Secret: [Secret]
SSL verification: Enable SSL verification
Which events would you like to trigger this webhook?: Just the push event.
Active: Enabled
```