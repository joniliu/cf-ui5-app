
### Introduction

A simple SAPUI5 app (skeleton) runnable from local machine using Python Flask, and deployable to Cloud Foundry.
Basically serving SAPUI5 web app content via Flask. The typical `webapp` folder of SAPUI5 is also renamed to `templates` as that's standard Python Flask folder naming convention for storing web content.

### Instructions

Do `git clone` this repository, you should have `cf-ui5-app` folder.

##### Cloud Foundry

Login to your Cloud Foundry account.

> $ cd cf-ui5-app

> $ cf push

Navigate to CF App Route to access this UI5 app.


##### Local Machine

Do `git clone` this repository, you should have `cf-ui5-app` folder.

> $ cd cf-ui5-app

> $ python app.py

Navigate to `http://localhost:5000/` to access this UI5 app.







