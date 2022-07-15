# Trivia API Project
Trivia API is a web application that allows people to test their knowledge through a game (trivia). It uses a webpage to manage the trivia app and play the game.
The following functionality is implemented in the app:

  1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and  can show/hide the answer.
  2. Delete questions.
  3. Add questions and require that they include question and answer text.
  4. Search for questions based on a text query string.
  5. Play the quiz game, randomizing either all questions or within a specific category.

## Getting Started

### Installing Dependencies

  1. ### Python 3.7
   Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

  2. ### Virtual Environment 
   It is recommended to work within a virtual environment for this project. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

  3. ### PIP Dependencies 
    After setting up your virtual environment, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM you will use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension you will use to handle cross-origin requests from the frontend server.

## Setting up the Database

With Postgres running, populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

## Run the server

Run the server from the `backend` directory. This is done by executing:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 


## Testing

To run tests, execute:

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

#### Frontend Dependencies

This project uses NPM to manage software dependecies. From the `frontend` directory, run:

```bash
npm install
```

## Running the Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use `npm start`. You can change the script in the `package.json` file.

Open http://localhost:3000 to view it in the browser. The page will reload if you make edits.

```bash
npm start
```

## API Reference

### Getting Started

- Backend Base URL: http://127.0.0.1:5000/

- Frontend Base URL: http://127.0.0.1:3000/

- Authentication: This project does not require authentication or API keys.

### Error Handling

Errors are returned as JSON in the following format:

```json
   {
    "success": "False",
    "error": 404,
    "message": "Resource not found"
   }
```
The API will return five types of error codes:

- 400 - bad request
- 404 - resource not found
- 422 - unprocessable entity
- 405 - method not allowed
- 500 - internal server error

### Endpoints

### GET '/categories'
- Fetches a dictionary of all available categories.
- Returns an object with a single key, categories, that contains a object of id: category_string key:value pairs. 

- Sample: 
```bash
    `curl http://127.0.0.1:5000/categories`
 ```

```json
       {
        "categories": {
            "1": "Science", 
            "2": "Art", 
            "3": "Geography", 
            "4": "History", 
            "5": "Entertainment", 
            "6": "Sports"
        }, 
        "success": true
    }
```

#### GET '/categories/<int:id>/questions'
- Gets all questions in a specified category by id using url parameters
- Returns a JSON object with paginated questions from a specified category
- Sample: 
```bash
  `curl http://127.0.0.1:5000/categories/3/questions`
```

```json
{
  "current_category": "Geography",
  "questions": [
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 20
}
```

### GET '/questions'

- Returns a list of questions
- Includes a list of categories
- Paginated in groups of 10
- Includes details of question such as category, difficulty, answer and id

- Sample: 
```bash
    `curl http://127.0.0.1:5000/questions
```

```json
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 20
}
```

### DELETE '/questions/<int:id>'

- Deletes a question by id using url parameters
- Returns id of deleted questions if successful

- Sample: 
```bash
    `curl http://127.0.0.1:5000/questions/2 -X DELETE
 ```

```json
      {
      "deleted": 2, 
      "success": true,
      "total_questions": 20
  }
```

### POST '/questions'
- Creates a new question using JSON request parameters in the database

- Sample: 
```bash
      `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question": "which is the champion team of the champions 2020?", "answer": "Bayern", "difficulty": 3, "category": "6" }'`
```

```Created question
  {
      "id": 25,
      "question": "which is the champion team of the champions 2020?",
      "answer": "Bayern", 
      "difficulty": 3,
      "category": 6
  }
```

```JSON response
{
  "created": 25,
  "question_created": "which is the champion team of the champions 2020?",
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 21
}
```

#### POST '/questions'
- Searches for questions using a search term, 
- Returns a JSON object with paginated questions matching the search term
- Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm": "author"}'`
```json
{
  "questions": [
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }
  ],
  "success": true,
  "total_questions": 1
}
```



#### POST '/quizzes'
- Allows user to play the trivia game
- Uses JSON request parameters of a chosen category and previous questions
- Returns JSON object with random available questions which are not among previous used questions
- Sample: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [10, 11], "quiz_category": {"type": "Sports", "id": "6"}}'`

```json
{
  "question": {
    "answer": "Bayern",
    "category": 6,
    "difficulty": 3,
    "id": 25,
    "question": "which is the champion team of the champions 2020?"
  },
  "success": true
}
```

## Authors

- Roger Wienaah build the API, worked on the test suite and this README to integrate with the frontend

- Udacity provided the starter files for this project including the models and frontend.