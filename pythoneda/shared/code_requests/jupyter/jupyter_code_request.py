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
from datetime import datetime
import json
import nbformat
from pythoneda.shared.code_requests.code_request import CodeRequest
from pythoneda.shared.code_requests.jupyter import JupyterNixFlake
from pythoneda.value_object import primary_key_attribute
import tempfile
from typing import Dict, List

class JupyterCodeRequest(CodeRequest):

    """
    Jupyter-based code requests.

    Class name: JupyterCodeRequest

    Responsibilities:
        - Model code requests using Jupyter notebooks.

    Collaborators:
        - pythoneda.shared.code_requests.CodeRequest
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

    def append_markdown(self, txt:str):
        """
        Appends a new Markdown cell.
        :param txt: The text to add.
        :type txt: str
        """
        super().append_markdown(txt)
        self.notebook.cells.append(nbformat.v4.new_markdown_cell(txt))

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

    def to_dict(self) -> Dict:
        """
        Converts this instance into a dictionary.
        :return: Such dictionary.
        :rtype: Dict
        """
        return {
            "notebook": str(nbformat.writes(self._notebook, version=4))
        }

    @classmethod
    def from_dict(cls, dict:Dict): # CodeRequest
        """
        Creates a new instance with the contents of given dictionary.
        :param dict: The dictionary.
        :type dict: Dict
        :return: A JupyterCodeRequest instance.
        :rtype: pythoneda.shared.code_requests.jupyter.JupyterCodeRequest
        """
        result = cls()
        result._notebook = nbformat.reads(dict["notebook"], as_version=4)
        return result

    def to_json(self) -> str:
        """
        Serializes this instance as json.
        :return: The json text.
        :rtype: str
        """
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, jsonText: str): # -> JupyterCodeRequest
        """
        Reconstructs a CodeRequest instance from given json text.
        :param jsonText: The json text.
        :type jsonText: str
        :return: The JupyterCodeRequest instance.
        :rtype: pythoneda.shared.code_requests.jupyter.JupyterCodeRequest
        """
        result = cls.from_dict(json.loads(jsonText))
        return result

    async def run(self):
        """
        Runs this notebook.
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            await JupyterNixFlake(self, "code_request", datetime.now().strftime("%Y%m%d%H%M%S"), temp_dir, "A nix flake to run a code request").run()
