# pywedding
## Intro
Minimalist wedding website, with gift list, accommodation list and two static pages. It uses
Google Spreadsheet as a back-end database for both lists. It is free of use, published under 
the MIT license.

## Live demo
Check the live version [here](http://pywedding.garnier.wf).

## Usage
  * First, install the "database" by copying the appropriate [spreadsheet template](). It is higly recommended 
that you create a new google account, such as 'pyweddingcalvinsuzie@gmail.com', share your spreadsheet with
this new account.
  * Edit the config.py file, and put in the login + password of said account.
  * Modify all the appropriate values in config.py to replace the default texts with you own content.
  * Install the dependencies with pip : `$ pip install Flask gdata`.
  * Run runserver.py, your site should be available on http://localhost:2706.
You can use an external tool to  publish it, such as [ngrok](https://ngrok.com/).

## Advanced usage (virtualenv, wsgi server)
  * It is a flask app, and that can be used with a WSGI server. For more info about this kind of deployment, 
check out [Flask's doc](http://flask.pocoo.org/docs/0.10/deploying/uwsgi/).
  * It is recommended that you install the app in a [virtualenv](https://virtualenv.pypa.io/en/latest/).
All the dependencies should be installed.
  * If you do so, the config.py can be copied anywhere on your filesystem. Just add an environment 
variable `PYWEDDING_CONFIG` pointing to it.
  * Should you decide to publish the site using uwsgi + nginx, you will find config samples in the `config-samples`
directory. Your can then run `uwsgi --ini /PATH/TO/YOUR/uwsgi.ini`.
  * Everything under pywedding/static can be served statically via your webserver.
