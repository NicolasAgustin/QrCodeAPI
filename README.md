# QrCodeAPI
API for generate and decode qr codes 


## Dependencies

Install mongodb from this link 

https://www.mongodb.com/try/download/community




## Run Locally

Clone the project

```bash
  git clone https://github.com/NicolasAgustin/QrCodeAPI.git
```

Go to the project directory

```bash
  cd QrCodeAPI
```

Create env

```bash
  python -m virtualenv venv
```

Install dependencies

```bash
  pip install -r requirements/requirements.txt
```

Start the API

```bash
  flask run
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`

`DB_PORT`

`DB_IP`

`DB_NAME`


## Authentication
The authentication endpoint is `/auth` with method POST.
The request must have the header `Content-Type: application/json` and in the body
of the request the values:
```json
    {
        "user": "your-username",
        "password": "your-password"
    }
```

This will output something like this:

```json
{
    "data": "token",
    "message": "Successfully fetched auth token"
}
```

The fetched token must be passed in each request to any endpoint.
The request must have Authorization Bearer for token. 
## Making requests
To create a QR code based on text, the request must be pointed to `/encode/<your text>` with GET method.
Also the parameters for generating the QR code can be parameterized with a POST request to `/encode` that contains a json in the body:
```json
    {
        "text": "this will be converted to qr code",
        "fill_color": "squares color",
        "back_color": "background color"
    }
```

To read QR code based on an image the request must be pointed to `/decode` with a POST method. 
