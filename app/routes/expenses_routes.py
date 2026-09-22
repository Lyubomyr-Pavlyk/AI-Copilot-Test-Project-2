from flask import jsonify, request, Blueprint
from app import db
from app.models import Expense

expenses_bp = Blueprint('expenses_bp', __name__)

# Create - Add an expense for a destination
@expenses_bp.route('/expenses', methods=['POST'])
def create_expense():
    data = request.json
    destination_id = data['destination_id']
    expense = Expense(destination_id=destination_id, category=data['category'], amount=data['amount'])
    db.session.add(expense)
    db.session.commit()
    return jsonify({'message': 'Expense added successfully'})

# Read - Get all expenses for a specific destination
@expenses_bp.route('/expenses/<int:destination_id>', methods=['GET'])
def get_expenses(destination_id):
    expenses = Expense.query.filter_by(destination_id=destination_id).all()
    expense_list = []
    for expense in expenses:
        expense_dict = {
            'id': expense.id,
            'category': expense.category,
            'amount': expense.amount
        }
        expense_list.append(expense_dict)
    return jsonify(expense_list)

# Update - Update a specific expense by ID
@expenses_bp.route('/expenses/<int:expense_id>', methods=['PUT'])
def update_expense(expense_id):
    expense = Expense.query.get(expense_id)
    if expense is not None:
        data = request.json
        expense.category = data['category']
        expense.amount = data['amount']
        db.session.commit()
        return jsonify({'message': 'Expense updated successfully'})
    return jsonify({'message': 'Expense not found'}, 404)

# Delete - Delete a specific expense by ID
@expenses_bp.route('/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    expense = Expense.query.get(expense_id)
    if expense is not None:
        db.session.delete(expense)
        db.session.commit()
        return jsonify({'message': 'Expense deleted successfully'})
    return jsonify({'message': 'Expense not found'}, 404)
