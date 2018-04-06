[![License](http://img.shields.io/badge/license-MIT-yellowgreen.svg)](MIT_LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/markfink/metrics.gitinfo.svg?maxAge=2592000)](https://github.com/markfink/metrics.gitinfo/issues)


# installation

to install:

``` bash
$ pip install metrics.pytest-cov
```

to uninstall:

``` bash
$ pip uninstall metrics.pytest-cov
```

for details please see the documentation of metrics.


# metrics.pytest-cov

The **metrics.pytest-cov** package is a plugin for the metrics package. 

Basically what this plugin does is it extract the data you get from running 
"$ coverage report -m" on the command line.

We assume that you run your pytest tests (incl. pytest-cov) before your run
metrics. In case your test execution fails you should fix your code and rerun the
tests prior to running metrics with this plugin.

The metrics.pytest-cov plugin picks up the .coverage file from your successful test run. 
If you must know, we could run the tests but decided not to.

Please note that in case a .coverage file from a testrun is not available we silently do nothing.


# Acknowledgements

Carsten for a recipe on how to load the .coverage file programmatically
https://stackoverflow.com/questions/35224643/how-do-i-access-coverage-py-results-programmatically


# License

Copyright (c) 2018 Mark Fink and others.
metrics is released under the MIT License (see MIT_LICENSE).
