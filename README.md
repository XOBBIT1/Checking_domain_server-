<h1>Django Project and Docker Compose Readme</h1>

<p>
    This readme file provides instructions on how to launch the Django project using Docker Compose. It also lists the 
    required environment variables and describes the available endpoints. The primary libraries used in the project are also 
    enumerated and selected.
</p>

<h2>Launching the Project</h2>

<p>To launch the Django project using Docker Compose, follow these steps:</p>

<ol>
  <li>Make sure you have Docker and Docker Compose installed on your machine.</li>
  <li>Clone the project repository to your local machine.</li>
  <li>Navigate to the project directory in the terminal.</li>
  <li>Create a <code>.env</code> file in the project directory and set the required environment variables:</li>
</ol>

<pre>
    <code>
        SECRET_KEY="django secret_key"
        POSTGRES_NAME=Name for Postgresql database
        POSTGRES_USER=User for Postgresql database
        POSTGRES_PASSWORD=Password for Postgresql database
        POSTGRES_PORT=Postgresql port
        REDIS_PORT=Redis port
    </code>
</pre>

<ol start="5">
  <li>Run the following command to build and start the Docker containers:</li>
</ol>

<pre><code>docker-compose up --build</code></pre>

<p>Once the containers are up and running, you can access the FastAPI application at <a href="http://localhost:8000">http://localhost:8000</a>.</p>

<h2>Endpoints</h2>

<p>The following endpoints are available in the FastAPI application:</p>

<pre>
    <code>
        GET:  domain/get_all/
        POST: domain/create/
        GET: domain/get/
        POST: domain/chart/
        PUT: domain/put/
        DELETE: domain/delete/
    </code>
</pre>

<p>Please refer to the project code for detailed request/response models and additional information about these endpoints.</p>

<h2>Primary Libraries</h2>

<p>The following libraries are selected as primary dependencies for the auth service:</p>

<ul>
    <li><a href="https://docs.djangoproject.com">Django</a></li>
    <li><a href="https://pypi.org/project/pre-commit/">Pre-commit</a></li>
    <li><a href="https://pypi.org/project/flake8/">Flake8</a></li>
    <li><a href="https://pypi.org/project/drf-spectacular/">Drf-spectacular</a></li>
    <li><a href="https://pypi.org/project/django-rest-swagger/">Django-rest-swagger</a></li>
    <li><a href="https://pypi.org/project/psycopg2/">Psycopg2</a></li>
    <li><a href="https://pypi.org/project/django-celery-beat/">Django-celery-beat</a></li>
    <li><a href="https://pypi.org/project/django-cors-headers/">Django-cors-headers</a></li>
    <li><a href="https://pypi.org/project/django-filter/">Django-filter</a></li>
    <li><a href="https://pypi.org/project/celery/">Celery</a></li>
    <li><a href="https://pypi.org/project/redis/">Redis</a></li>
    <li><a href="https://pypi.org/project/gevent/">Gevent</a></li>
</ul>

<p>Other libraries listed in the <code>Pipfile</code>. File are also mentioned as primary dependencies.</p>
