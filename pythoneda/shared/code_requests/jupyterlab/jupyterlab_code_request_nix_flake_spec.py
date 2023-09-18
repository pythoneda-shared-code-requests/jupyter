"""
pythoneda/shared/code_requests/jupyterlab/jupyterlab_code_request_nix_flake_spec.py

This file declares the JupyterlabCodeRequestNixFlakeSpec class.

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
from pythoneda.shared.code_requests import CodeRequestNixFlakeSpec
from typing import List

class JupyterlabCodeRequestNixFlakeSpec(CodeRequestNixFlakeSpec):
    """
    Specifies Jupyterlab Nix flakes wrapping a code request.

    Class name: JupyterlabCodeRequestNixFlakeSpec

    Responsibilities:
        - Provides conditions on Jupyterlab Nix flakes wrapping code requests.

    Collaborators:
        - pythoneda.shared.code_requests.CodeRequestNixFlakeSpec
        - pythoneda.shared.code_requests.jupyterlab.JupyterlabCodeRequest
    """

    def __init__(
            self,
            codeRequest: JupyterlabCodeRequest,
            versionSpec: str = None,
            inputSpecs: List = []):
        """
        Creates a new JupyterlabCodeNixFlakeSpec instance.
        :param codeRequest: The code request.
        :type codeRequest: pythoneda.shared.code_requests.jupyterlab.JupyterlabCodeRequest
        :param name: The name of the flake.
        :type name: str
        :param versionSpec: The version of the flake.
        :type versionSpec: str
        :param url: The url.
        :type url: str
        :param inputSpecs: The flake specs.
        :type inputSpecs: List[pythoneda.shared.nix_flake.NixFlakeSpec]
        """
        super().__init__(
            codeRequest,
            "jupyterlab-code-request",
            versionSpec,
            f"github:rydnr/nix-flakes/jupyterlab-{versionSpec}?dir=jupyterlab",
            inputSpecs)

    def _set_attribute_from_json(self, varName, varValue):
        """
        Changes the value of an attribute of this instance.
        :param varName: The name of the attribute.
        :type varName: str
        :param varValue: The value of the attribute.
        :type varValue: int, bool, str, type
        """
        if varName == 'code_request':
            self._code_request = JupyterlabCodeRequest.from_dict(varValue)
        else:
            super()._set_attribute_from_json(varName, varValue)
