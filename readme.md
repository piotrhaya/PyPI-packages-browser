PyPI packages browser
======

This application allows You to store data about new PyPI packages into elasticsearch and search stored data using API.
Data from https://pypi.org/rss/packages.xml is being stored once a day at 12:30 PM.

<h3>Main Libraries:</h4>
<br>Django v4.1.1
<br>Djangorestframework v3.14.0
<br>Elasticsearch v7.17.6
<br>Elasticsearch-dsl v7.4.0

<h3>Enviroments Variables configuration</h3>

* In Your application directory (/packages_browser) create .env file and fullfill it with Your correct configuration
  data

<h4>Django secret key</h4>

```shell 
SECRET_KEY='your Django secret key'
```

<h4>Pagination in the Web browsable API</h4>

```shell 
DRF_PAGE_SIZE='Number of results on the single page'
```

<h4>Database settings</h4>

```shell 

DATABASE_ENGINE=
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=
```

If you do not have any database system, simply fill in the data as below:

```shell 
DATABASE_ENGINE=django.db.backends.sqlite3
DATABASE_NAME=db.sqlite3
```

<h4>Elasticsearch settings</h4>

```shell 
ES_HOSTS='Your host:port'
ES_HTTP_AUTH_USER='elasticsearch user'
ES_HTTP_AUTH_PASS='password'
ES_VERIFY_CERTS='use True if You want to verify certificates or False if not'
ES_CA_CERTS='directory to Your certificate, if You dont have any leave this option empty'
```

It is highly recomended to use certificate verification You create the connection to elasticsearch!

<h3>Application configuration</h3>

* First step: Install require libraries.

```shell 
pip install -r requirements.txt
```

* Second step: Migrate models into Your database. Migration is already created in the project.

```shell 
python manage.py migrate
```

* Third step: Populate the Elasticsearch index and mapping.

```shell 
python manage.py search_index --rebuild
```

All the data is being stored in the database, in case of loss elasticsearch index You can rebuild it
again with command above.

User Guide
====================================
When Your application server and elasticsearch are running, You will be able to search in Your data.
Defaultly server is running on http://127.0.0.1:8000

* Main endpoint:
  http://127.0.0.1:8000/drf/es/

* Search by terms in the title: http://127.0.0.1:8000/drf/es/?search=title:search_term
* Search by terms in the link url: http://127.0.0.1:8000/drf/es/?search=link:search_term
* Search by terms in the description: http://127.0.0.1:8000/drf/es/?search=description:search_term
* Search by terms in the author: http://127.0.0.1:8000/drf/es/?search=author:search_term
* Search by data in the publication date: http://127.0.0.1:8000/drf/es/?search=pubDate:search_term

<h5>Multisearch browser</h5>

Application has functionality to search data according to words in the title, description and author at once:

* Search module: http://127.0.0.1:8000/search/
