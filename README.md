# django-postgis-example

This repository is the example code for the blog post [Dockerizing Django with PostgreSQL, PostGIS and GeoDjango for Location Search](https://aaronnotes.com/2023/10/dockerizing-django-with-postgresql-postgis-and-geodjango-for-location-search/)

To run the application, add `.env` in `postgres` and `djproject/djsite`, and run the following command:

```
cd postgres
docker compose -f compose.postgis.yml up
cd ../djproject/djsite
docker build -f dockerfile.base -t dj_base .
docker compose up
```

Add test data in `http://localhost:1024/admin`; test location search in `http://localhost:1024/djapp/search`
