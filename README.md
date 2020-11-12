<p align="center">
  <img src="https://pbs.twimg.com/profile_banners/1168677863442268160/1580499452/1500x500">
</p>


PhageAI is an AI-driven software platform using advanced Machine Learning and Natural Language Processing techniques for deeper understanding of the bacteriophages genomics.


[![Travis CI](https://travis-ci.com/ProteonPharmaceuticals/phageai.svg?branch=main)](https://travis-ci.com/github/ProteonPharmaceuticals/phageai)
[![codecov](https://codecov.io/gh/ProteonPharmaceuticals/phageai/branch/master/graph/badge.svg)](https://codecov.io/gh/ProteonPharmaceuticals/phageai)
[![Documentation Status](https://readthedocs.org/projects/phageai/badge/?version=stable)](https://phageai.readthedocs.io/en/stable/?badge=stable)
[![PyPI version](https://img.shields.io/pypi/v/phageai.svg)](https://pypi.org/project/phageai/)
[![PyPI license](https://img.shields.io/pypi/l/phageai.svg)](https://pypi.python.org/pypi/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/phageai.svg)](https://pypi.python.org/pypi/phageai/)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Downloads](https://static.pepy.tech/badge/phageai)](https://pepy.tech/project/phageai)
[![Twitter Follow](https://img.shields.io/twitter/follow/phageai.svg?style=social)](https://twitter.com/phageai) 


## Table of Contents

[Framework modules](https://github.com/ProteonPharmaceuticals/phageai#framework-modules) | [Documentation](https://github.com/ProteonPharmaceuticals/phageai#documentation) | [Installation](https://github.com/ProteonPharmaceuticals/phageai#installation-and-usage) | [Community and Contributions](https://github.com/ProteonPharmaceuticals/phageai#community-and-contributions) | [Have a question?](https://github.com/ProteonPharmaceuticals/phageai#have-a-question) | [Found a bug?](https://github.com/ProteonPharmaceuticals/phageai#found-a-bug) | [Team](https://github.com/ProteonPharmaceuticals/phageai#team) | [Change log](https://github.com/ProteonPharmaceuticals/phageai#change-log) | [License](https://github.com/ProteonPharmaceuticals/phageai#license) | [Cite](https://github.com/ProteonPharmaceuticals/phageai#cite)

## Framework modules

`lifecycle` - set of methods related with bacteriophage lifecycle research (exploration, prediction);  
`taxonomy` - set of methods related with bacteriophage taxonomy research (TBA);  
`repository` - set of methods related with PhageAI bacteriophage repository (TBA); 

## Documentation

The official technical documentation is hosted on ReadTheDocs: https://phageai.readthedocs.io

## Installation and usage

#### PhageAI user account (1/3)
Create a free user account in [the PhageAI web platform](https://phage.ai) or use an existing one. If you had to create new one, activate your account by activation link which was sent on your mail inbox. After that, log into the platform successfully and click "My profile" on menu (left sidebar). From the "API access" section copy the access token (string) and keep it for the steps below.

#### PhageAI package (2/3)

_PhageAI_ requires Python 3.8.0+ to run and can be installed by running:

```
pip install phageai
```

Alternatively, you also can use the Conda ecosystem:

```
conda install -c conda-forge phageai
```

If you can't wait for the latest hotness from the develop branch, then install it directly from the repository:

```
pip install git+git://github.com/ProteonPharmaceuticals/phageai.git@develop
```

#### PhageAI execution (3/3)

```python
from phageai.lifecycle.classifier import LifeCycleClassifier

lcc = LifeCycleClassifier(access_token='<PASTE_YOUR_ACCESS_TOKEN_HERE>')
lcc.predict(fasta_path='<PASTE_YOUR_FASTA_PATH_HERE>')
```

Expected output for `MG945357.fasta` bacateriophage sample:
```json
{
    "model_class_label": "Virulent",
    "prediction_accuracy": "98.94",
    "gc": "39.47",
    "sequence_length": 4915
}
```

We shared numerous examples of using the framework in Jupyter Notebook format (*.ipynb).

## Community and Contributions

Happy to see you willing to make the PhageAI better. Development on the latest stable version of Python 3+ is preferred. As of this writing it's 3.8. You can use any operating system.

If you're fixing a bug or adding a new feature, add a test with *[pytest](https://github.com/pytest-dev/pytest)* and check the code with *[Black](https://github.com/psf/black/)* and *[mypy](https://github.com/python/mypy)*. Before adding any large feature, first open an issue for us to discuss the idea with the core devs and community.

## Have a question?

Obviously if you have a private question or want to cooperate with us, you can always reach out to us directly by mail.

## Found a bug?

Feel free to add a new issue with a respective title and description on the [the PhageAI repository](https://github.com/ProteonPharmaceuticals/phageai/issues). If you already found a solution to your problem, we would be happy to review your pull request.

## Team

Core Developers and Domain Experts who contributing to PhageAI:

* Piotr Tynecki
* Joanna Kazimierczak
* Arkadiusz Guziński
* Bogusław Zimoń

## Change log

The log's will become rather long. It moved to its own file.

See [CHANGELOG.md](https://github.com/ProteonPharmaceuticals/phageai/blob/master/CHANGELOG.md).

## License

The PhageAI package is released under the under terms of [the MIT License](https://github.com/ProteonPharmaceuticals/phageai/blob/master/LICENSE).

## Cite

> **PhageAI - Bacteriophage Life Cycle Recognition with Machine Learning and Natural Language Processing**  
>
> Tynecki, P.; Guziński, A.; Kazimierczak, J.; Jadczuk, M.; Dastych, J.; Onisko, A.
>
> Bioinformatics 2020, DOI: [10.1101/2020.07.11.198606](https://doi.org/10.1101/2020.07.11.198606)
