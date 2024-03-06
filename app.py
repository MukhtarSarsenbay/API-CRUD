from flask import Flask, request, jsonify, make_response
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
auth = HTTPBasicAuth()
#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@document-db/mydatabase'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app,db)
# In-memory database simulation
documents = {
    1: {'title': 'Sample Document', 'content': 'This is a sample.'}
}

users = {
    "admin": generate_password_hash("secret")
}

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Document {self.title}>"

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

@app.route('/documents', methods=['GET'])
@auth.login_required
def get_documents():
    documents = Document.query.all()
    return jsonify([{'id': doc.id, 'title': doc.title, 'content': doc.content, 'status': doc.status} for doc in documents])

@app.route('/documents/<int:doc_id>', methods=['GET'])
@auth.login_required
def get_document(doc_id):
    document = Document.query.get(doc_id)
    if document is None:
        return make_response(jsonify({'error': 'Document not found'}), 404)
    return jsonify({'id': document.id, 'title': document.title, 'content': document.content, 'status': document.status})

@app.route('/documents', methods=['POST'])
@auth.login_required
def create_document():
    if not request.json or 'title' not in request.json or 'content' not in request.json or 'status' not in request.json:
        return make_response(jsonify({'error': 'Bad request'}), 400)
    new_document = Document(title=request.json['title'], content=request.json['content'], status=request.json['status'])
    db.session.add(new_document)
    db.session.commit()
    return jsonify({'id': new_document.id, 'title': new_document.title, 'content': new_document.content, 'status': new_document.status}), 201

@app.route('/documents/<int:doc_id>', methods=['PUT'])
@auth.login_required
def update_document(doc_id):
    document = Document.query.get(doc_id)
    if document is None:
        return make_response(jsonify({'error': 'Document not found'}), 404)
    document.title = request.json.get('title', document.title)
    document.content = request.json.get('content', document.content)
    document.status = request.json.get('status', document.status)
    db.session.commit()
    return jsonify({'id': document.id, 'title': document.title, 'content': document.content, 'status': document.status})

@app.route('/documents/<int:doc_id>', methods=['DELETE'])
@auth.login_required
def delete_document(doc_id):
    document = Document.query.get(doc_id)
    if document is None:
        return make_response(jsonify({'error': 'Document not found'}), 404)
    db.session.delete(document)
    db.session.commit()
    return jsonify({'result': True})


print('test')
with app.app_context():
    db.create_all()
    print("Database tables created.")
app.run(port=8080, host="0.0.0.0")
