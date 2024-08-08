# Quantum Random Number Generator (QRNG) API

## Overview
This project presents the development and deployment of a Quantum Random Number Generator (QRNG) API utilizing Qiskit, an open-source quantum computing software development framework by IBM. Random number generation is a critical component in various applications such as cryptography, simulations, and gaming. Traditional methods of generating random numbers rely on classical algorithms that can be predictable and lack true randomness. Quantum mechanics offers a fundamentally different approach to randomness, providing numbers that are truly random and secure.

## Features
- **Quantum Random Number Generation**: Leverage quantum mechanics to generate true random numbers.
- **Qiskit Integration**: Utilize IBM's Qiskit framework for creating and executing quantum circuits.
- **Scalable Deployment**: Deploy the API using Google Cloud Run for automatic scaling based on demand.
- **Containerization**: Ensure portability and ease of deployment with Docker.
- **Simple RESTful Interface**: Access the QRNG API via a straightforward RESTful interface.

## Technology Stack
- **Quantum Computing**: IBM Qiskit
- **Containerization**: Docker
- **Cloud Platform**: Google Cloud Run
- **Programming Language**: Python

## Installation
### Prerequisites
- Serve locally:
  - Python 3.10 or higher
  - Pip v22 or higher
  - requirements from *requirements.txt*
- Use congirued service:
  - Browser
  - Python 3.10 or higher

## Usage
### Steps to serve locally
1. **Clone the repository**
   ```bash
   git clone https://github.com/farawaystars-sam/qrng-api.git
   cd qrng-api/test_scripts
   ```
2. **Run the test scripts**
   run the scripts to test the endpoints, locally and use the local host url. Modify the parameters to your preference.
   ```bash
   python3.10 test*.py
   ```
   
### Steps to use the Cloud app
Similar to running locally, clone and navigate to the test scripts, and simply uncomment the cloud url lines. Play around with the parameters to the end points.
<br> *or*
<br>
Use bash command:
```bash
curl -X GET "https://qrng-api-v001-wmoc4p3wpa-uc.a.run.app/random_bit_string?n=<your-n-value>"
curl -X GET "https://qrng-api-v001-wmoc4p3wpa-uc.a.run.app/random_int?max=<your-max-value>&min=<your-min-value>"
```
<br> *or*
<br>
Use browser to browse the link:
1. https://qrng-api-v001-wmoc4p3wpa-uc.a.run.app/random_bit_string?n=<your-n-value>
2. https://qrng-api-v001-wmoc4p3wpa-uc.a.run.app/random_int?max=<your-max-value>&min=<your-min-value>

## For Further help
For further help required read *Help/doc.md* file.

## Acknowledgements
1. **Literature**:
  - Partial Loopholes Free Device Independent Quantum Random Number Generator Using IBM’s Quantum Computers, [link] (https://arxiv.org/pdf/2309.05299)
  - and others
2. **Youtube**:
    - Follow this [link.](https://www.youtube.com/watch?v=2DeLrLEagU0&list=PLKMY3XNPiQ7t-LORep_Hj47qOM8qVcuii&index=10)

## Contribute
If you wish to contribute towards this project, Please feel free to fork the repository and initiate a pull request.

## Contact
For any questions or inquiries, please reach out at [farawaystars-sam@github.com].
