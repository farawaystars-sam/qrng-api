from flask import Flask, request, jsonify

# quiskit no longer has Basic Aer insted has Aersimulator from qiskit_aer
#from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, BasicAer

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile

#import Aersim
from qiskit_aer import AerSimulator

app = Flask(__name__)

def get_random_bit_string(n):
    """
    Args:
    n (int): The length of bit string required
    
    Returns:
    str: The qrng bit string generated
    """
    
    # Number of shots needed to generate n bits
    num_shots = (n + 4) // 5
    
    # Create a Quantum Circuit with 5 qubits and 5 classical bits
    qc = QuantumCircuit(5, 5)
    
    # Apply a Hadamard gate on all qubits to create superposition
    for qubit in range(5):
        qc.h(qubit)
    
    # Measure all qubits
    qc.measure(range(5), range(5))
    
    # Use AerSimulator
    simulator = AerSimulator()
    
    # Transpile the circuit for the simulator
    compiled_circuit = transpile(qc, simulator)
    
    # Execute the circuit on the simulator with num_shots
    result = simulator.run(compiled_circuit, shots=num_shots, memory= True).result()
    
    # Get the memory (individual measurement results) from the result
    memory = result.get_memory()
    
    # Concatenate the results of the shots to form the final bit string
    bit_string = ''.join(memory)
    
    # Trim the bit string to the required length n
    return bit_string[:n]


def get_random_number(max_value=None, min_value=None, max_value_with_min=None):
    """
    Args:
    max_value (int): The maximum value (exclusive) if min_value is not provided.
    min_value (int): The minimum value (inclusive) if both min_value and max_value_with_min are provided.
    max_value_with_min (int): The maximum value (exclusive) if min_value is provided.
    
    Returns:
    int: The random number generated within the specified range
    """
    
    if max_value is not None:
        # Case 1: Range [0, max)
        max_value = int(max_value)
        bit_length = max_value.bit_length()
        bit_string = get_random_bit_string(bit_length)
        random_number = int(bit_string, 2)
        while random_number >= max_value:
            bit_string = get_random_bit_string(bit_length)
            random_number = int(bit_string, 2)
        return random_number
    
    elif min_value is not None and max_value_with_min is not None:
        # Case 2: Range [min, max)
        min_value = int(min_value)
        max_value_with_min = int(max_value_with_min)
        if min_value >= max_value_with_min:
            raise ValueError("min_value must be less than max_value_with_min")
        range_size = max_value_with_min - min_value
        bit_length = range_size.bit_length()
        bit_string = get_random_bit_string(bit_length)
        random_number = int(bit_string, 2)
        while random_number >= range_size:
            bit_string = get_random_bit_string(bit_length)
            random_number = int(bit_string, 2)
        return min_value + random_number
    
    else:
        raise ValueError("Either provide only max_value or both min_value and max_value_with_min")

@app.route('/random_bit_string', methods=['GET'])
def random_bit_string():
    try:
        n = int(request.args.get('n'))
        if n <= 0:
            return jsonify({"error": "The value of n must be a positive integer."}), 400
        
        bit_string = get_random_bit_string(n)
        return jsonify({"bit_string": bit_string})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide a positive integer value for n."}), 400

@app.route('/random_int', methods=['GET'])
def random_int():
    try:
        max_value = int(request.args.get('max'))
        if max_value < 0:
            return jsonify({"error": "The value of max must be a positive integer."}), 400
        
        min_value = request.args.get('min')
        if min_value is None:
            random_num = get_random_number(max_value)
        else:
            min_value = int(min_value)
            if min_value < 0:
                return jsonify({"error": "The value of min must be a positive integer."}), 400
            random_num = get_random_number(min_value=min_value, max_value_with_min=max_value)

        if min_value >= max_value:
            return jsonify({"error": "The value of min must be less than max."}), 400

        #random_num = get_random_number(max_value, min_value)
        return jsonify({"rand_int": random_num})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide positive integer values for max and min."}), 400


if __name__ == '__main__':
    app.run(debug=True)
