from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Happiness Program',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 2500'
  },
  {
    'id': 2,
    'title': 'Sri Sri Yoga',
    'location': 'Delhi, India',
    'salary': 'Rs. 2500'
  },
  {
    'id': 3,
    'title': 'Utkarsh Yoga',
    'location': 'Remote',
  },
  {
    'id': 4,
    'title': 'Advanced Meditation Program',
    'location': 'San Francisco, USA',
    'salary': '$200'
  }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='The Art of Living')

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)