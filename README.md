.. image:: https://travis-ci.org/dominikl/omero-cli-template.svg?branch=master
    :target: https://travis-ci.org/dominikl/omero-cli-template
    
# Basic example for an OMERO CLI plugin

Fork and use this repository to create custom OMERO CLI plugins.

### Provides
- A basic implementation: [src/omero_cli_template.py](src/omero_cli_template.py)
(Change the name to match your plugin name `omero_cli_[PLUGIN].py`)
- "Entry point" for the CLI: [src/omero/plugins/template.py](src/omero/plugins/template.py)
This directory structure `omero/plugins/[PLUGIN].py` is needed for the plugin to be 
discovered by the CLI. (Same here, it's recommended to change the name accordingly to `[PLUGIN].py`)
- A basic integration test (which is run by Travis): [test/integration/clitest/test_template.py](test/integration/clitest/test_template.py)
( -> rename to `test/integration/clitest/test_[PLUGIN].py`)
- Travis integration:
  - [.travis.yml](.travis.yml) Enables automatic Travis builds
  - [.gitmodules](.gitmodules) Pulls in the [omero-test-infra](https://github.com/openmicroscopy/omero-test-infra.git) 
  repository as submodule (runs the integration tests)
- [setup.py](setup.py) and [README.rst](README.rst) so the plugin can be made `pip` installable via [PyPI](https://pypi.org/)

### How to use this repository / best practices
- Fork/Clone it.
- Rename the various files from `...template...` to match your plugin name (see above), `omero_cli_[PLUGIN].py`, 
`omero/plugins/[PLUGIN].py`, `test/integration/clitest/test_[PLUGIN].py`.
- Rename the `TemplateControl` class in [src/omero_cli_template.py](src/omero_cli_template.py) to
`[PLUGIN]Control`.
- Add your plugin implementation to the `[PLUGIN]Control`.
- Make sure your plugin is registered with the CLI with the right name, i. e. replace all occurrences of 
`register("template", ...)` with `register("[PLUGIN]", ...)`

### Further reading
- [OMERO Python language bindings](https://docs.openmicroscopy.org/omero/5.4.6/developers/Python.html)
- [argparse](https://pypi.org/project/argparse/) Used for parsing command line arguments (the CLI uses
version 1.1)
