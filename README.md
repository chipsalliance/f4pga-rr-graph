# SymbiFlow Routing Resources Graph (`rr-graph`) Python Libraries

[![License](https://img.shields.io/github/license/SymbiFlow/symbiflow-rr-graph.svg)](https://github.com/SymbiFlow/symbiflow-rr-graph/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/SymbiFlow/symbiflow-rr-graph)](https://github.com/SymbiFlow/symbiflow-rr-graph/issues)
![PyPI](https://img.shields.io/pypi/v/rr-graph)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rr-graph)
![PyPI - Downloads](https://img.shields.io/pypi/dm/rr-graph)


This repository contains a Python library and utilities for working with
["Routing Resource Graph" (`rr-graph`) files](https://docs.verilogtorouting.org/en/latest/vpr/file_formats/#routing-resource-graph-file-format-xml)
used by [SymbiFlow](https://symbiflow.github.io) and
[Verilog to Routing](https://verilogtorouting.org).

It supports both the [XML](https://en.wikipedia.org/wiki/XML) and
[Cap'n'Proto](https://capnproto.org/) formats of `rr-graph` files.
The Cap'n'Proto schema is generated from the
[XML schema @ `vtr-verilog-to-routing/vpr/src/route/rr_graph.xsd`](https://github.com/verilog-to-routing/vtr-verilog-to-routing/blob/master/vpr/src/route/rr_graph.xsd)
using the [uxsdcxx tool](https://github.com/SymbiFlow/uxsdcxx).

For information on the schema generation can be found in the
[`SCHEMA_GENERATOR.md` file in Verilog to Routing](https://github.com/verilog-to-routing/vtr-verilog-to-routing/blob/master/vpr/src/route/SCHEMA_GENERATOR.md).

# Contributing

A full contribution guide can be found in [`docs/contributing.md`](./docs/contributing.md).

A few important points;
 * All contributions should be sent as
   [GitHub Pull requests](https://help.github.com/articles/creating-a-pull-request-from-a-fork/).

 * By contributing you agree to the [code of conduct](./docs/code-of-conduct.md).

 * **All** commits are required to include a
   [DCO](./docs/developer-certificate-of-origin) sign off line.


# License

All software (code, associated documentation, support files, etc) in this
repository is licensed under the very permissive
[ISC Licence](https://opensource.org/licenses/ISC).

A copy can be found in the [`LICENSE`](LICENSE) file.

All new contributions must also be released under this license.
