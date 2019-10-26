from flask_restful import Resource, reqparse
from models.quote import QuoteModel


class Quote(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('_id', type=int, required=True, help="The ID of the quote.")

    def get(self, _id):
        quote = QuoteModel.find_by_id(_id)
        if quote:
            return quote.json()
        return {'message': 'Quote not found, meatbag!'}, 404