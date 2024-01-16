# vim: set fileencoding=utf-8
"""
pythoneda/shared/code_requests/jupyterlab/jupyterlab_code_request_nix_flake.py

This file defines the JupyterlabCodeRequestNixFlake class.

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
from .jupyterlab_code_request import JupyterlabCodeRequest
from path import Path
from pythoneda.shared.code_requests import CodeRequestNixFlake
from pythoneda.shared.nix_flake.licenses import Gpl3
from typing import List


class JupyterlabCodeRequestNixFlake(CodeRequestNixFlake):

    """
    Nix flake for managing code requests using Jupyterlab.

    Class name: JupyterlabCodeRequestNixFlake

    Responsibilities:
        - Wrap a code request in a Nix flake that launches Jupyterlab.

    Collaborators:
        - pythoneda.shared.code_requests.jupyterlab.JupyterlabCodeRequest
    """

    def __init__(self, codeRequest: JupyterlabCodeRequest, version: str, inputs: List):
        """
        Creates a new JupyterlabCodeRequestNixFlake instance.
        :param codeRequest: The code request.
        :type codeRequest: pythoneda.shared.code_requests.jupyter.JupyterCodeRequest
        :param version: The version of the flake.
        :type version: str
        :param inputs: The resolved dependencies as NixFlakes.
        :type inputs: List
        """
        super().__init__(
            codeRequest,
            "jupyterlab-code-request",
            version,
            f"github:rydnr/nix-flakes/jupyterlab-{version}?dir=jupyterlab",
            inputs,
            "Jupyterlab code request",
            "https://github.com/pythoneda-shared-code-requests/jupyter",
            Gpl3.license_type(),
            ["rydnr <github@acm-sl.org>"],
            2023,
            "rydnr",
        )

    @classmethod
    def empty(cls):
        """
        Builds an empty instance. Required for unmarshalling.
        :return: An empty instance.
        :rtype: pythoneda.shared.ValueObject
        """
        return cls(None, None, [])

    def generate_files(self, flakeFolder: str):
        """
        Generates the files.
        :param flakeFolder: The flake folder.
        :type flakeFolder: str
        """
        super().generate_files(flakeFolder)
        self.generate_notebook(flakeFolder)

    def generate_notebook(self, flakeFolder: str):
        """
        Generates the code-request.ipynb from a template.
        :param flakeFolder: The flake folder.
        :type flakeFolder: str
        """
        with open(Path(flakeFolder) / "code-request.ipynb", "w", encoding="utf-8") as f:
            self.code_request.write(f)

    def git_add_files(self, gitAdd):
        """
        Adds the generated files to git.
        :param gitAdd: The GitAdd instance.
        :type gitAdd: pythoneda.shared.git.GitAdd
        """
        super().git_add_files(gitAdd)
        self.git_add_notebook(gitAdd)

    def git_add_notebook(self, gitAdd):
        """
        Adds the generated code-request.ipynb file to git.
        :param gitAdd: The GitAdd instance.
        :type gitAdd: pythoneda.shared.git.GitAdd
        """
        gitAdd.add("code-request.ipynb")

    def _set_attribute_from_json(self, varName, varValue):
        """
        Changes the value of an attribute of this instance.
        :param varName: The name of the attribute.
        :type varName: str
        :param varValue: The value of the attribute.
        :type varValue: int, bool, str, type
        """
        if varName == "code_request":
            self._code_request = JupyterlabCodeRequest.from_dict(varValue)
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
        if varName == "code_request":
            result = self._code_request.to_dict()
        else:
            result = super()._get_attribute_to_json(varName)
        return result
