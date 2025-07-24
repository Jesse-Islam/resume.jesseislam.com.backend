from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from firebase_admin import initialize_app, firestore

app = Flask(__name__)
# allow CORS on all routes
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
initialize_app()

db      = firestore.client()
doc_ref = db.collection('page_views').document('resume')

@app.route('/', methods=['POST','OPTIONS'])
@cross_origin()
def view_count():
    if request.method == 'OPTIONS':
        # preflight: no increment, no body
        return ('', 204)
    # only POST from here on
    doc_ref.set({'view_count': firestore.Increment(1)}, merge=True)
    count = doc_ref.get().to_dict()['view_count']
    return jsonify({'view_count': count})

