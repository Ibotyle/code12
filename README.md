# An API to retrieve Public Information

This project contains a public API that retrieves:
my HNG registered email address, current datetime(ISO 8601 format) and the GitHub URL of the project's codebase.

## Technologies Used
- Python
- Flask
- Git
- Vercel

## Prerequisite
- Python 3.8 or higher
- pip (Python package manager)

## Local Development
1. Clone repo
`git clone https://github.com/Ibotyle/code12.git`

1.1. Change Directory to code12
`cd code12`

3. Create Virtual Environment
   `python -m venv venv`
   
4. Activate Virtual Environment
   `source venv/bin/activate`

5. Install dependencies
`pip install -r requirements.txt`

6. Run the application
`flask run`

API should be running on http://127.0.0.1:5000


## To access Project
Send a get request to https://code12-olive.vercel.app/

## Example Usage

### Request
`curl -X GET https://code12-olive.vercel.app/
`
### Response
`{
"current_datetime":"2025-02-02T09:43:23","email":"ibotyle@gmail.com","github_url":"https://github.com/ibotyle/code12"
}
`

## Deployment
Project url: https://code12-olive.vercel.app/

## Backlink
<a href="https://hng.tech/hire/python-developers">Python Developers</a>

