import os
from typing import Sequence, Tuple

from nbconvert import HTMLExporter
import nbformat
from traitlets.config import Config

from pelican import signals
from pelican.readers import BaseReader
from pelican.utils import pelican_open


class JupyterReader(BaseReader):

    enabled = True
    file_extensions = ['ipynb']

    @staticmethod
    def _write_outputs(outputs: dict, source_dir: str) -> None:
        images_dir = os.path.join(source_dir, 'images')
        if not os.path.exists(images_dir):
            os.makedirs(images_dir)
        for output in outputs:
            dest = os.path.join(source_dir, output)
            with open(dest, 'wb') as fh:
                fh.write(outputs[output])

    @staticmethod
    def add_filename_prefix_to_content(outputs: Sequence[dict], body: str) -> str:

        def add_pelican_static_prefix(body: str, src_value: str) -> str:
            body_w_prefix = body.replace(src_value, '{static}%s' % src_value)
            return body_w_prefix

        for output in outputs:
            body = add_pelican_static_prefix(body, output)

        return body

    def read(self, source_path: str) -> Tuple[str, dict]:

        source_dir = os.path.dirname(source_path)

        with pelican_open(source_path) as text:

            notebook_node = nbformat.reads(text, as_version=4)

            c = self.settings.get('NBCONVERT_CONFIG', Config())
            html_exporter = HTMLExporter(c)
            (body, resources) = html_exporter.from_notebook_node(notebook_node)

            outputs = resources['outputs']
            if outputs:
                self._write_outputs(outputs, source_dir)
                body = self.add_filename_prefix_to_content(outputs, body)

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
