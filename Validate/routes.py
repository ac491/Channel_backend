from flask import Flask , request , jsonify, Response
from app import app , mongo
import json

@app.route('/blogs', methods = ['GET'])
def get_all_blogs():
    blogs = mongo.db.docs
    output = []
    for blog in blogs.find():
        t = dict(blog)
        output.append({'title' : t['title'], 'content' : t['content']})
    return jsonify({'result' : output})

@app.route('/blogs/upload', methods = ['POST'])
def upload_blogs():
    title = request.form.get('title')
    content = request.form.get('content')

    mongo.db.docs.insert({'title': title, 'content' : content})

    msg = {"status" : { "type" : "success" ,   "message" : "Blog uploaded successfully"}}
    return jsonify(msg)
