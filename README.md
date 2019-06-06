# MathContestClassification

This repository contains a project to classify math competition problems into subjects, ideally as granular as identifying the main technique used to solve the problem (e.g. a "power of a point" class etc.). Besides serving a pedadogical purpose of e.g. making it easy to construct problem sets surrounding a specific topic, in principle it should be a helpful tool in solving an unknown problem.

## Runbook

### Problem retrieval

Problems are retrieved via scraping [AoPS](artofproblemsolving.com) contest collections. You will need a couple of packages:

```
py -m pip install selenium
py -m pip install bs4
```

After this you can run the main file via `py main.py`. **This will take several hours**. Periodic progress will be evident by `problem<x>.txt` files appearing in the main directory. All in all there are almost 50k problems, so you should expect about 100 files (50 text files and 50 pickle files). Obviously, the pickle files are used for future programmatic work in classification; the text files are more for human curiosity.

Note that it is strongly recommended to modify `constants.py` to dump every 10 problems or so as a test run before running the full program. This will allow you to catch any incompatabilities quickly.
