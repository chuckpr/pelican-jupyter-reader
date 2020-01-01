import json
import nbformat
from nbconvert import HTMLExporter
from pelican import signals
from pelican.readers import BaseReader
from pelican.utils import pelican_open
from typing import Tuple


class JupyterReader(BaseReader):

    enabled = True
    file_extension = ['ipynb']

    def read(self, source_path: str) -> Tuple[str, dict]:

        with pelican_open(source_path) as text:

            notebook_node = nbformat.reads(text, as_version=4)

            html_exporter = HTMLExporter()
            html_exporter.template_file = 'basic'

            (body, resources) = html_exporter.from_notebook_node(notebook_node)

            content = body

        metadata = notebook_node['metadata'].get('pelican', {})

        parsed_metadata = {}
        for key, value in metadata.items():
            parsed_metadata[key] = self.process_metadata(key, value)


        return content, parsed_metadata


def add_reader(readers) -> None:
    readers.reader_classes['ipynb'] = JupyterReader


def register() -> None:
    signals.readers_init.connect(add_reader)
