Title: Another Post on Pelican
Date: 2018-09-11 13:20
Category: Notes

# Automating Pelican builds with Travis-CI

Make sure to escape special characters for bash. The format $"GITHUB_TOKEN" is appropriate for this case.

![Here are the formats I tried. Notice that GITHUB_TOKEN also passes successfully, but we need the $ for build success in bash.](images/EnvVars.png)
