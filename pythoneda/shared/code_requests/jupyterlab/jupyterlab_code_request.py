"""
pythoneda/shared/code_requests/jupyterlab/jupyterlab_code_request.py

This file defines the JupyterlabCodeRequest class.

Copyright (C) 2023-today rydnr's pythoneda-shared-code-requests/jupyterlab

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
from pythoneda import primary_key_attribute
from pythoneda.shared.code_requests import CodeRequest, CodeRequestNixFlakeSpec
from pythoneda.shared.nix_flake import NixFlakeSpec
from typing import List

class JupyterlabCodeRequest(CodeRequest):

    """
    Jupyterlab-based code requests.

    Class name: JupyterlabCodeRequest

    Responsibilities:
        - Model code requests using Jupyter notebooks.

    Collaborators:
        - pythoneda.shared.code_requests.CodeRequest
    """
    def __init__(self):
        """
        Creates a new JupyterlabCodeRequest instance.
        """
        super().__init__()
        self._notebook = nbformat.v4.new_notebook()

    @classmethod
    def empty(cls):
        """
        Builds an empty instance. Required for unmarshalling.
        :return: An empty instance.
        :rtype: pythoneda.ValueObject
        """
        return cls()

    @property
    @primary_key_attribute
    def notebook(self):
        """
        Retrieves the notebook instance.
        :return: Such instance.
        :rtype: nbformat.v4.notebook.Notebook
        """
        return self._notebook

    def append_markdown(self, txt:str):
        """
        Appends a new Markdown cell.
        :param txt: The text to add.
        :type txt: str
        """
        actual_text = '\n'.join(line.lstrip() for line in txt.split('\n'))
        super().append_markdown(actual_text)
        self.notebook.cells.append(nbformat.v4.new_markdown_cell(actual_text))

    def append_code(self, pythonCode:str, dependencies:List):
        """
        Appends a new code cell.
        :param pythonCode: The Python code to add.
        :type pythonCode: str
        :param dependencies: The dependencies.
        :type dependencies: List[pythoneda.shared.code_requests.Dependency]
        """
        super().append_code(pythonCode, dependencies)
        self.notebook.cells.append(nbformat.v4.new_code_cell(pythonCode))

    def write(self, file):
        """
        Writes the code request to a file.
        :param file: The file to write.
        :type file: File
        """
        nbformat.write(self.notebook, file)

    def _set_attribute_from_json(self, varName, varValue):
        """
        Changes the value of an attribute of this instance.
        :param varName: The name of the attribute.
        :type varName: str
        :param varValue: The value of the attribute.
        :type varValue: int, bool, str, type
        """
        if varName == 'notebook':
            self._notebook = nbformat.reads(varValue, as_version=4)
        else:
            super()._set_attribute_from_json(varName, varValue)

    def _get_attribute_to_json(self, varName) -> str:
        """
        Retrieves the value of an attribute of this instance, as Json.
        :param varName: The name of the attribute.
        :type varName: str
        :return: The attribute value in json format.
        :rtype: str
        """
        result = None
        if varName == 'notebook':
            result = nbformat.writes(self._notebook)
        else:
            result = super()._get_attribute_to_json(varName)
        return result

    @property
    def nix_flake_spec(self):
        """
        Retrieves the specification for the Nix flake.
        :return: Such specification.
        :rtype: pythoneda.shared.nix_flake.NixFlakeSpec
        """
        from .jupyterlab_code_request_nix_flake_spec import JupyterlabCodeRequestNixFlakeSpec
        return JupyterlabCodeRequestNixFlakeSpec(self)
