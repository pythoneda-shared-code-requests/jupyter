# Jupyter-based code requests

Shared kernel for code requests based on Jupyter.

## How to declare it in your flake

Check the latest tag of the artifact repository: https://github.com/pythoneda-shared-code-requests/jupyter-artifact/tags, and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-shared-code-requests-jupyter = {
      [optional follows]
      url =
        "github:pythoneda-shared-code-requests/jupyter-artifact/[version]?dir=jupyter";
    };
  };
  outputs = [..]
};
```

Should you use another PythonEDA modules, you might want to pin those also used by this project. The same applies to [https://nixos/nixpkgs](nixpkgs "nixpkgs") and [https://github.com/numtide/flake-utils](flake-utils "flake-utils").

The Nix flake is under the [https://github.com/pythoneda-shared-code-requests/jupyter-artifact/tree/main/jupyter](jupyter "jupyter") folder of <https://github.com/pythoneda-shared-code-requests/jupyter-artifact>.

