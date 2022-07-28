
# testrepoforpr

testrepoforpr (Test Repo For github PR-Pull Requests)  is a Python code snippet for calculating the merge time of pulls requests.

## Installation

Create a github token as described in this link
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

For organizations with SSO, the token needs to be authorized as described in this link
https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-saml-single-sign-on/authorizing-a-personal-access-token-for-use-with-saml-single-sign-on 

## Usage:
Before executing the python script, set the following parameters
username = 'xxxx' {github username}
orgname = 'sovrn' {organization}
token = 'xxx' {token for the github username}
repos = ['testrepoforpr', 'helloWorld'] {List of repos}
pulldate = '2022-07-01' {Pull Date: Fetch pull requests that are open as of this date}

At the unix command line :::: python3 testrepoforpr