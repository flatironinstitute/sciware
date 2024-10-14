# Python Packaging Demo

This demo is intended to show how you can adapt existing code (in this case, in
the form of a Jupyter notebook) into a `pip`-installable package. The notebook
contains some code which performs useful computations we want to make re-usable,
and some data munging and plotting we don't. We will keep the notebook in a
working state as we create our new package.

The notebook is by way of [Dan Foreman-Mackey's
blog](https://dfm.io/posts/autocorr/).

Like any good cooking show, we have a pre-prepared example of what we want at
the end of the demo in the `pre-baked-cake/` folder.

## Getting Started

To run this locally, you may need to install some additional packages.
Run the following commands from inside this directory (`sciware/34_PyPackaging/demo/`).

If you are a conda user, you can run

```shell
$ conda env create --prefix ./env --file environment.yml
$ conda activate ./env/
```

If not, a virtual enviroment can be used:

```shell
$ python -m venv --system-site-packages env/
$ source ./env/bin/activate
$ python -m pip install -r requirements.txt
```

Then, run `jupyter lab` to launch Jupyter and follow along.

### Google Colab
You can follow along most of the tutorial using Google Colab instead, to avoid
any local installation being necessary. Note that this will be a slightly
different UI than the presenter will be using, so some parts may be slightly
harder to follow along.

[Click Here](https://colab.research.google.com/github/flatironinstitute/sciware/blob/main/34_PyPackaging/demo/Demo.ipynb) to launch a Colab session

You will need to uncomment and run the first cell of the notebook which says
"Google Colab: uncomment and run this next line!"
