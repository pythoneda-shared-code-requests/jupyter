"""
pythoneda/shared/code_requests/jupyter/jupyter_nix_flake.py

This file defines the JupyterNixFlake class.

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
from .jupyterlab_input import JupyterlabInput
from path import Path
from pythoneda import primary_key_attribute
from pythoneda.shared.code_requests import CodeRequest, PythonedaDependency
from pythoneda.shared.nix_flake import FlakeUtilsInput, NixFlakeInput, Nixos2305Input, PythonedaNixFlake, PythonedaSharedPythonedaBannerInput, PythonedaSharedPythonedaDomainInput
from typing import List

class JupyterNixFlake(PythonedaNixFlake):

    """
    Nix flake for Jupyter-based code requests.

    Class name: JupyterNixFlake

    Responsibilities:
        - Wrap a Jupyter code request in a Nix flake.

    Collaborators:
        - pythoneda.shared.code_requests.jupyter.JupyterCodeRequest
    """
    def __init__(self, codeRequest:CodeRequest, name:str, version:str, outputFolder:str, description:str):
        """
        Creates a new JupyterNixFlake instance.
        :param codeRequest: The code request.
        :type codeRequest: pythoneda.shared.code_requests.CodeRequest
        :param name: The name of the flake.
        :type name: str
        :param version: The version of the flake.
        :type version: str
        :param outputFolder: The output folder.
        :type outputFolder: str
        :param description: The flake description.
        :type description: str
        """
        super().__init__(
            name,
            version,
            self.__class__.dependencies_to_inputs(codeRequest.dependencies),
            outputFolder,
            description,
            "https://github.com/pythoneda-shared-code-requests/jupyter",
            "C",
            "D",
            "D")
        self._code_request = codeRequest

    @classmethod
    def empty(cls):
        """
        Builds an empty instance. Required for unmarshalling.
        :return: An empty instance.
        :rtype: pythoneda.ValueObject
        """
        return cls(None, None, None, None, None)

    @property
    @primary_key_attribute
    def code_request(self) -> CodeRequest:
        """
        Retrieves the code request.
        :return: Such instance.
        :rtype: pythoneda.shared.code_requests.CodeRequest
        """
        return self._code_request

    def generate_files(self, flakeFolder: str):
        """
        Generates the files.
        :param flakeFolder: The flake folder.
        :type flakeFolder: str
        """
        super().generate_files(flakeFolder)
        self.generate_notebook(flakeFolder)

    def generate_notebook(self, flakeFolder:str):
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

    @classmethod
    def dependencies_to_inputs(cls, dependencies:List) -> List:
        """
        Converts given dependencies to a list of NixFlakeInput instances.
        :param dependencies: The dependencies.
        :type dependencies: List[pythoneda.shared.code_requests.Dependency]
        :return: The list of NixFlakeInput instances.
        :rtype: List[pythoneda.shared.nix_flake.NixFlakeInput]
        """
        result = { JupyterlabInput() }
        pythonedaDependencies = [ Nixos2305Input(), FlakeUtilsInput(), PythonedaSharedPythonedaBannerInput() ]
        for dep in dependencies:
            deps = []
            if isinstance(dep, PythonedaDependency):
                deps = pythonedaDependencies
                if dep.name != "pythoneda-shared-pythoneda-domain":
                    deps.append(PythonedaSharedPythonedaDomainInput())
            result.add(NixFlakeInput(dep.name, dep.url, deps))
        return list(result)
