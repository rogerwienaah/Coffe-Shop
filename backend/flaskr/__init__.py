import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

db = SQLAlchemy()

#pagination
def paginate_questions(request, selection):
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE

        questions = [question.format() for question in selection]
        current_questions = questions[start:end]

        return current_questions



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    # set up CORS and Allow '*' for origins 
    CORS(app, resources={'/': {'origins': '*'}})

    
    # CORS Headers
    # Use the after_request decorator to set Access-Control-Allow
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization, true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET, POST, DELETE, PATCH, OPTIONS"
        )

        return response

    
    # An endpoint to handle GET requests for all available categories
    @app.route("/categories", methods=["GET"])
    def get_available_categories():
        if request.method == "GET":
            # get all categories and add to a dict
            categories = Category.query.order_by(Category.id).all()
            my_categories = {}
        
            for category in categories:
                my_categories[category.id] = category.type

            # return 404 error if no categories found
            if len(my_categories) == 0:
                abort(404)

            # return successful response
            return jsonify({
                'success': True,
                'categories': my_categories
            })

        
    
    # an endpoint to handle GET requests for questions
    @app.route('/questions', methods=["GET"])
    def get_paginated_questions():
        if request.method == "GET": 
            # get all questions and paginate
            questions = Question.query.all()
            current_questions = paginate_questions(request, questions)

            # return 404 error if no questions found
            if len(current_questions) == 0:
                abort(404)

            # get all categories and add to dict
            categories = Category.query.all()
            my_categories = {}
        
            for category in categories:
                my_categories[category.id] = category.type

        
            
            return jsonify({
                "success": True,
                "questions": current_questions,
                "total_questions": len(questions),
                "categories": my_categories
            })



    # an endpoint to delete question using a question id
    @app.route('/questions/<int:id>', methods=['DELETE'])
    def delete_question(id):
        if request.method == "DELETE":
            # get question by id
            question = Question.query.filter_by(id = id).one_or_none()

            # return 404 status code if there are no questions
            if question is None:
                abort(404)

            question.delete()

            return jsonify({
                "success": True,
                "deleted": id,
                "total_questions": len(Question.query.all()),
            })

    
    # An endpoint to POST a new question and also get questions based on a search term
    @app.route('/questions', methods=['POST'])
    def create_new_question():
        if request.method == "POST":
            body = request.get_json()

            # get data from json body
            new_question = body.get("question", None)
            new_answer = body.get("answer", None)
            new_category = body.get("category", None)
            new_difficulty = body.get("difficulty", None)

            search_term = body.get('searchTerm', None)

            try:
                if search_term:
                    questions = Question.query.filter(Question.question.ilike(f"%{search_term}%")).all()
                    paginated_questions = paginate_questions(request, questions)
                    
                    return jsonify({
                        'success': True,
                        'questions': paginated_questions,
                        'total_questions': len(paginated_questions)
                    })

                else:    
                    # create new question
                    question = Question(question=new_question, answer=new_answer, category=new_category, difficulty=new_difficulty)
                    question.insert()
                    
                    # get updated questions and paginate response
                    updated_questions = Question.query.order_by(Question.id).all()
                    updated_questions = paginate_questions(request, updated_questions)

                    return jsonify({
                        "success": True,
                        "question_created": question.question,
                        "created": question.id,
                        "questions": updated_questions,
                        "total_questions": len(Question.query.all())
                    })

            except:
                # return 422 status code if there is a problem creating a question
                abort(422)    

    
    # A GET endpoint to get questions based on category
    @app.route('/categories/<int:category_id>/questions', methods=["GET"])
    def get_category_questions(category_id):
        if request.method == "GET":
            # get category by id
            category = Category.query.filter_by(id=category_id).one_or_none()

            if (category is None):
                abort(404)
            
            try:
                # get questions and paginate results
                questions = Question.query.filter_by(category=category.id).all()
                paginated_questions = paginate_questions(request, questions)

                return jsonify({
                    'success': True,
                    'questions': paginated_questions,
                    'total_questions': len(Question.query.all()),
                    'current_category': category.type
                })
            
            except:
                abort(400)

    # play quiz
    @app.route('/quizzes', methods=['POST'] )
    def play_quiz():
        if request.method == "POST":
            try:
                # get data from json body
                body = request.get_json()
                previous_questions = body.get('previous_questions', None)
                category = body.get('quiz_category', None)

                category_id = category['id']
                next_question = None

                # get question based on category id
                if category_id != 0:
                    avail_questions = Question.query.filter_by(category=category_id).filter(Question.id.notin_((previous_questions))).all()
                
                # get questions not categorized by id
                else:
                    avail_questions = Question.query.filter(Question.id.notin_((previous_questions))).all()

                # get random question
                if len(avail_questions) > 0:
                    next_question = random.choice(avail_questions).format()

                return jsonify({
                    'question': next_question,
                    'success': True
                })

            except:
                abort(422)


    # error handlers

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'method not allowed'
        }), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 500

    
    
    """**
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """

    """**
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """

    """**
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """


    """**
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """


    """**
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """



    """**
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """


    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """

    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """

    return app

