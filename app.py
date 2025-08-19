from flask import Flask, request, jsonify, render_template, redirect, url_for
from datetime import datetime, timedelta
import uuid

app = Flask(__name__)

# In-memory storage for links
links = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_link', methods=['POST'])
def create_link():
    data = request.json
    content = data.get('content')
    alias = data.get('alias', None)

    if not content:
        return jsonify({'error': 'Content is required'}), 400

    # Generate a unique link ID
    link_id = alias if alias else str(uuid.uuid4())
    links[link_id] = {
        'content': content,
        'clicks': 0,
        'created_at': datetime.now()
    }

    # Return the public link
    public_link = url_for('get_link', link_id=link_id, _external=True)
    return jsonify({'link': public_link}), 201

@app.route('/link/<link_id>', methods=['GET'])
def get_link(link_id):
    link_data = links.get(link_id)
    if link_data is None:
        return jsonify({'error': 'Link not found'}), 404

    # Increment click count
    link_data['clicks'] += 1

    return render_template('link_detail.html', link=link_id, content=link_data['content'], clicks=link_data['clicks'])

if __name__ == '__main__':
    app.run(debug=True)
