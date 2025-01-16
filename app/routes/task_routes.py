from flask import Blueprint, request, jsonify
from app import db
from app.models.task import Task

bp = Blueprint('tasks', __name__, url_prefix='/api/tasks')

# TODO: Add pagination for large task lists
# TODO: Implement authentication middleware
@bp.route('', methods=['GET'])
def get_tasks():
    priority = request.args.get('priority')
    completed = request.args.get('completed')

    query = Task.query

    if priority:
        query = query.filter_by(priority=priority)
    if completed is not None:
        completed_bool = completed.lower() == 'true'
        query = query.filter_by(completed=completed_bool)

    tasks = query.all()
    return jsonify([task.to_dict() for task in tasks]), 200

@bp.route('/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify(task.to_dict()), 200

@bp.route('', methods=['POST'])
def create_task():
    data = request.get_json()

    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400

    task = Task(
        title=data['title'],
        description=data.get('description', ''),
        priority=data.get('priority', 'medium')
    )

    db.session.add(task)
    db.session.commit()

    return jsonify(task.to_dict()), 201

@bp.route('/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()

    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.priority = data.get('priority', task.priority)
    task.completed = data.get('completed', task.completed)

    db.session.commit()

    return jsonify(task.to_dict()), 200

@bp.route('/<int:id>/complete', methods=['PATCH'])
def complete_task(id):
    task = Task.query.get_or_404(id)
    task.completed = True
    db.session.commit()

    return jsonify(task.to_dict()), 200

@bp.route('/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()

    return '', 204
