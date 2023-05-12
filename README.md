# Case Based Reaoner For Recommending Covid-19 Policies

Our case-based reasoner provides policy recommendations related to Covid-19, such as lockdown, mask, and vaccine policies. The system is built using FastAPI and React. The reasoner allows decision-makers to create cases, view them, and submit queries, which are processed by the backend API. The API returns policy recommendations and the top three most similar cases by utilizing a Postgres database, which stores the cases. The frontend is served through the backend, creating a seamless user experience. Overall, our system is designed to help decision-makers make informed choices about Covid-19 policies with ease.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need to have python 3 and postgres server installed on your machine.

### Installing

## Backend

To install the project, clone the repository and run the following command in the project directory:

- ## Create a virtual environment

```
python -m venv venv
```

- ## Activate virtual environment

```
./venv/Scripts/activate
```

- ## Install requirements

```
pip install -r requirements.txt
```

## Client

- ## Navigate to client directory

```
cd client
```

- ## Install npm packages

```
npm install
```

- ### Build the project

```
npm run build
```

## DB and env setup

---

## Create a empty database with any suitable name. Edit the .env.example with your db credentials.

### Running the project

To run the project, run the following command in the project directory:

```
uvicorn main:app --reload
```

Test the project by going to http://localhost:8000/ in your browser.

## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - backend
- [React](https://reactjs.org/) - frontend

## Author

- **Sudan Upadhaya** - [sudan94](https://github.com/sudan94)
- **Shehab Shalan** - [shehabshalan](https://github.com/shehabshalan)

## License

This project is licensed under the MIT License.
