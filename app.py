from math import gcd
from flask import Flask, request, jsonify, render_template
from flask_ngrok import run_with_ngrok
app = Flask(__name__, static_url_path='/static')
run_with_ngrok(app)
@app.route("/")
def index():
    return render_template("index.html")

def totient(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    count_coprime = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            count_coprime += 1
    
    return count_coprime

def find_primitive_roots(N):
    phi = totient(N)
    divisors = [i for i in range(1, phi + 1) if phi % i == 0]
    primitive_roots = []
    
    possible_roots = [i for i in range(N) if gcd(i, N)==1]

    for i in possible_roots:
        for j in divisors:
            if pow(i, j, N) == 1:
                break
        
        if j == phi:
            primitive_roots.append(i)
    
    return primitive_roots

@app.route("/find_primitive_roots", methods=["POST"])
def calculate_primitive_roots():
    data = request.get_json()
    N = data.get("N")

    if N is None or N <= 0:
        return jsonify({"success": False, "error": "Please enter a valid positive number."})
    
    primitive_roots = find_primitive_roots(N)

    if primitive_roots:
        return jsonify({"success": True, "primitive_roots": primitive_roots})
    else:
        return jsonify({"success": False, "error": "No primitive roots found for N."})

if __name__ == "__main__":
    app.run()
