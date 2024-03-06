# Flask REST API

Simple API CRUD with Flask


#### Installation

* Clone repo
```
git clone https://github.com/MukhtarSarsenbay/API-CRUD.git
```

* 2 - Install Docker 
https://www.docker.com/products/docker-desktop/

* 3 - Run Docker on the terminal
```
docker compose up -d --build
```

* 4 - Enjoy
  Program Requires very simple authorisation: Username: admin, Password: secret,
  for every step.
  Program was tested on Postman.

#### Features
* Create document
* Read document
* Update document details
* Delete document

#### GET:
This is a GET request and it is used to "get" data from an endpoint. There is no request body for a GET request, but you can use query parameters to help specify the resource you want data on (e.g., in this request, we have id=1).
A successful GET response will have a 200 OK status, and should include some kind of response body - for example, HTML web content or JSON data.

```
curl --location ':8080/documents/1' \
--header 'Authorization: Basic YWRtaW46c2VjcmV0'
```
#### POST:
This is a POST request, submitting data to an API via the request body. This request submits JSON data, and the data is reflected in the response.
A successful POST request typically returns a 200 OK or 201 Created response code.

```
curl --location 'http://localhost:8080/documents' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic YWRtaW46c2VjcmV0' \
--data '{
	"title": "third post data",
    "content": "short story",
    "status": "okay"
}'
```
#### PUT:
This is a PUT request and it is used to overwrite an existing piece of data. For instance, after you create an entity with a POST request, you may want to modify that later. You can do that using a PUT request. You typically identify the entity being updated by including an identifier in the URL (eg. id=1).
A successful PUT request typically returns a 200 OK, 201 Created, or 204 No Content response code.

```
curl --location --request PUT 'http://127.0.0.1:5000/documents/2' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic YWRtaW46c2VjcmV0' \
--data '{
  "title": "Third document",
  "content": "Updated content of the document."
}'
```
#### DELETE:
This is a DELETE request, and it is used to delete data that was previously created via a POST request. You typically identify the entity being updated by including an identifier in the URL (eg. id=1).
A successful DELETE request typically returns a 200 OK, 202 Accepted, or 204 No Content response code.

```
curl --location --request DELETE 'http://127.0.0.1:5000/documents/2' \
--header 'Authorization: Basic YWRtaW46c2VjcmV0' \
--data ''
```

#### Tech Stack
* Flask
* flask-migrate
* flask-restful
* flask-sqlalchemy
* PostgreSQL
* Docker


Code: by Mukhtar Sarsenbay
