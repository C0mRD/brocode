from flask import Flask, request
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)
   
@app.route("/interpret", methods=['POST'])
def interpret():
    if request.method == 'POST':
        code = request.get_data().decode('utf-8')
        with open('code.bro', 'w+') as f:
            f.write(code)
        f.close()
        p = subprocess.Popen(["python","broCodeInterpreter.py","code.bro"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = p.communicate()
        return output.decode()
        
    
if __name__ == "__main__":
    app.run()
