from flask import Flask, request, jsonify

# quiskit no longer has Basic Aer insted has Aersimulator from qiskit_aer
#from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, BasicAer

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile

#import Aersim
from qiskit_aer import AerSimulator

app = Flask(__name__)

def generate_random_bit_string(n):
    """
    Args: n
    return value: str

    n: the length of bit string required
    return_value: the qrng bit string generated
    """


    # Create a Quantum Circuit with one qubit and one classical bit
    qc = QuantumCircuit(1, 1)

    # Apply a Hadamard gate on the qubit to create a superposition
    qc.h(0)

    #measure 
    qc.measure(0, 0)

    # Use BasicAer's qasm_simulator ----- not supported anymore
    #simulator = BasicAer.get_backend('qasm_simulator')

    # use AerSImulator instead
    simulator = AerSimulator()
    
    # Execute the circuit on the qasm simulator --- not supported anymore
    #job = execute(qc, simulator, shots=n)

    # using transpile to achive the same 
    compiled_circuit = transpile(qc, simulator)
    
    # Grab results from the job     ---- not supported anymore
    #result = job.result()
    
    # using simulator.run to get same results
    result = simulator.run(compiled_circuit).result()

    # Get the counts (number of occurrences of each result)
    counts = result.get_counts(qc)
    
    # Extract the bit string (there will only be one result since we have one shot)
    bit_string = list(counts.keys())[0]
    
    return bit_string

@app.route('/random_bit_string', methods=['GET'])
def random_bit_string():
    try:
        n = int(request.args.get('n'))
        if n <= 0:
            return jsonify({"error": "The value of n must be a positive integer."}), 400
        
        bit_string = generate_random_bit_string(n)
        return jsonify({"bit_string": bit_string})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide a positive integer value for n."}), 400

if __name__ == '__main__':
    app.run(debug=True)
