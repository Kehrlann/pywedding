# pywedding
## Intro
Minimalist wedding website, with gift list, accommodation list and two static pages. It uses
Google Spreadsheet as a back-end database for both lists. It is free of use, published under 
the MIT license.

## Live demo
Check the live version [here](http://pywedding.garnier.wf).

## Usage
  * First, install the "database" by copying the appropriate [spreadsheet template](https://drive.google.com/previewtemplate?id=1YYrHsejzTj1sbwCx5hIKupQkVMisa-Cu3iuk4f-apU8&mode=public).
  * Publish that spreadsheet to the web (File > Publish to the web).
  * Get the key (which is in the url, right after the /d/, and looks like like `1YYrHsejzTj1sbwCx5hIKupQkVMisa-Cu3iuk4f-apU8`.
  * Edit the config.py file, and put the key.
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
