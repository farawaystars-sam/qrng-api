To configure a Google Cloud Run service for an API application with two endpoints (`/this_a` and `/this_b`) that accept different parameters, you can follow these steps:

### 1. **Prepare Your Application**

Ensure your application is designed to handle the specified endpoints and parameters. For instance, if you're using a Python Flask application, it might look like this:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/this_a', methods=['GET'])
def endpoint_a():
    n = request.args.get('n')
    if not n:
        return jsonify({"error": "Parameter 'n' is required"}), 400
    return jsonify({"received_n": n})

@app.route('/this_b', methods=['GET'])
def endpoint_b():
    n = request.args.get('n')
    m = request.args.get('m')
    if not n or not m:
        return jsonify({"error": "Parameters 'n' and 'm' are required"}), 400
    return jsonify({"received_n": n, "received_m": m})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

### 2. **Containerize Your Application**

You need to create a Docker container for your application. Here’s a basic `Dockerfile` for a Python Flask app:

```dockerfile
# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the environment variable to specify the port
ENV PORT 8080

# Run the application
CMD ["python", "app.py"]
```

Make sure you have a `requirements.txt` file that lists your dependencies, for example:

```
Flask==2.1.2
```

### 3. **Build and Push Your Container Image**

Build the Docker image and push it to Google Container Registry (GCR) or Artifact Registry.

```bash
# Build the Docker image
docker build -t gcr.io/your-project-id/your-image-name:tag .

# Push the Docker image to GCR
docker push gcr.io/your-project-id/your-image-name:tag
```

Replace `your-project-id`, `your-image-name`, and `tag` with appropriate values.

### 4. **Deploy Your Container to Cloud Run**

You can deploy your container to Cloud Run using the Google Cloud Console or the command line.

**Using the Command Line:**

```bash
gcloud run deploy your-service-name \
    --image gcr.io/your-project-id/your-image-name:tag \
    --platform managed \
    --region your-region \
    --allow-unauthenticated
```

Replace `your-service-name`, `your-project-id`, `your-image-name`, `tag`, and `your-region` with your specific values.

**Using the Google Cloud Console:**

1. Go to the [Cloud Run page](https://console.cloud.google.com/run).
2. Click on "Create Service."
3. Configure your service by providing the container image URL (`gcr.io/your-project-id/your-image-name:tag`).
4. Set other configuration options as needed and click "Create."

### 5. **Test Your Endpoints**

Once your service is deployed, you can test your endpoints. The URL for your Cloud Run service will be something like `https://your-service-name-<random-id>.run.app`.

- For `/this_a`, you can test with: `https://your-service-name-<random-id>.run.app/this_a?n=value`
- For `/this_b`, you can test with: `https://your-service-name-<random-id>.run.app/this_b?n=value&m=value`

### 6. **Monitor and Manage**

Monitor your service using the Cloud Run dashboard to check logs, request metrics, and manage revisions.

By following these steps, you'll have a Cloud Run service configured for your API application with the specified endpoints and parameters.