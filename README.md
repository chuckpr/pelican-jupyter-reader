`pelican-jupyter-reader`: A Plugin for Pelican
---------------------------------------------

[![PyPI version](https://badge.fury.io/py/pelican-jupyter-reader.svg)](https://badge.fury.io/py/pelican-jupyter-reader)
[![Netlify Status](https://api.netlify.com/api/v1/badges/a92deaef-8ffb-4d11-a941-358ac92e3500/deploy-status)](https://app.netlify.com/sites/peaceful-jang-e394ce/deploys)

This [Pelican](http://docs.getpelican.com/en/latest/index.html) plugin provides a Jupyter Notebook (i.e. `*.ipynb`) reader.
The plugin intends to allow users to simply drop Jupyter notebooks in their
Pelican content directory and have the notebooks rendered (beautifully) in a Pelican
static website.

Installation
------------

This plugin can be installed via:

    pip install pelican-jupyter-reader

Quickstart
----------

- Add the plugin to `pelicanconf.py`:
```python
# ...

from pelican.plugins import pelican_jupyter_reader
PLUGINS = [pelican_jupyter_reader]

# ...
```

- Provide [Pelican post
  metadata](http://docs.getpelican.com/en/latest/content.html#file-metadata) as
  a top-level object with key `pelican` in the Jupyter notebook metadata:
```javascript
{
    "pelican": {
        "date": "2020-04-10",
        "title": "this is a title",
        "tags": "thats, awesome",
        "category": "yeah",
        "slug": "my-super-post",
        "authors": "Alexis Metaireau, Conan Doyle",
        "summary": "Short version for index and feeds"
    },
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    },
//...the rest of the notebook JSON follows.
```

- Drop your Jupyter notebook in the Pelican content directory, build your site,
  and deploy!  :rocket:


Example
-------

The [demo/](https://github.com/chuckpr/pelican-jupyter-reader/tree/master/demo)
directory has a simple post with corresponding configuration in
`pelicanconf.py`. The demo site is deployed
[here](https://peaceful-jang-e394ce.netlify.app).


Notes
-----

The Jupyter nbconvert configuration for
[preprocessors](https://github.com/jupyter/nbconvert/tree/5.x/nbconvert/preprocessors)
and the
[HTMLExporter](https://github.com/jupyter/nbconvert/blob/5.x/nbconvert/exporters/html.py)
are exposed in your Pelican config, `pelicanconf.py`.  This
means you can manipulate notebooks with utilities provided by `nbconvert`.

For example, to use the `basic` template for the `HTMLExporter`, you could add
the following to your `pelicanconf.py`:

```python
from traitlets.config import Config
NBCONVERT_CONFIG = Config()
NBCONVERT_CONFIG.HTMLExporter.template = 'basic'
```

To strip empty cells from the notebook before publishing, you might add this
option to `pelicanconf.py`:

```python
# ...
NBCONVERT_CONFIG.RegexRemovePreprocessor.patterns = ['\\s*\\Z']
```

Other `nbconvert` configuration options can be found
[here](https://nbconvert.readthedocs.io/en/latest/config_options.html#configuration-options).
