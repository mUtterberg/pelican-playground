Title: Getting Started with Pelican on GitHub Pages
Date: 2018-09-11 10:20
Category: Notes

# Deploying a Pelican site to GitHub Pages

If your change was on GitHub in the browser, run `git pull origin master` first. Otherwise, initiate the new build with `pelican content -o output -s publishconf.py`

### A note on deployment
Pelican settings are split between pelicanconf.py and publishconf.py - the latter of which is essentially the production settings file. [This thread on Stack Overflow](https://stackoverflow.com/questions/20817192/what-is-the-difference-between-pelicanconf-and-publishconf-when-using-pelican) provides some insight from the contributor of that feature ("bifurcated settings").

We pip installed ghp-import specifically for GitHub Pages, so run `ghp-import output -b gh-pages` next. And because our Pelican source is hosted on branch master, `git push origin gh-pages` to ensure we aren't over-writing the generator. The project page can publish from either, but we selected gh-pages in our project's settings to enable hosting both branches on GitHub.
