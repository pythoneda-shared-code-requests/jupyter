"""
pythoneda/shared/code_requests/jupyter/jupyter_code_request.py

This file defines the JupyterCodeRequest class.

Copyright (C) 2023-today rydnr's pythoneda-shared-code-requests/jupyter

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import nbformat
from pythoneda.shared.code_requests.code_request import CodeRequest
from pythoneda.value_object import primary_key_attribute

class JupyterCodeRequest(CodeRequest):

    """
    Jupyter-based code requests.

    Class name: JupyterCodeRequest

    Responsibilities:
        - Model code requests using Jupyter notebooks.

    Collaborators:
        - pythoneda.shared.code_requestscode_request.CodeRequest
    """
    def __init__(self):
        """
        Creates a new JupyterCodeRequest instance.
        """
        super().__init__()
        self._notebook = nbformat.v4.new_notebook()

    @property
    @primary_key_attribute
    def notebook(self):
        """
        Retrieves the notebook instance.
        :return: Such instance.
        :rtype: nbformat.v4.notebook.Notebook
        """
        return self._notebook

    def append_markdown(self, txt: str):
        """
        Appends a new Markdown cell.
        :param txt: The text to add.
        :type txt: str
        """
        super().append_markdown(str)
        self.notebook.cells.append(nbformat.v4.new_markdown_cell(txt))

    def append_code(self, pythonCode: str):
        """
        Appends a new code cell.
        :param pythonCode: The Python code to add.
        :type pythonCode: str
        """
        super().append_code(pythonCode)
        self.notebook.cells.append(nbformat.v4.new_code_cell(pythonCode))

    def write(self, file):
        """
        Writes the code request to a file.
        :param file: The file to write.
        :type file: File
        """
        nbformat.write(self.notebook, file)
