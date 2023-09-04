"""
pythoneda/shared/code_requests/jupyter/jupyterlab_input.py

This file defines the JupyterlabInput class.

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
from pythoneda.shared.nix_flake import NixFlakeInput, Nixos2305Input, FlakeUtilsInput

class JupyterlabInput(NixFlakeInput):

    """
    Represents the input for Jupyter.

    Class name: JupyterlabInput

    Responsibilities:
        - Represents the information about Jupyter flake.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new JupyterlabInput instance.
        """
        super().__init__("jupyterlab", "github:rydnr/nix-flakes/main?dir=jupyterlab", [ Nixos2305Input(), FlakeUtilsInput() ])
