
# resume.jesseislam.com · Backend

A simple Flask‑based backend for [resume.jesseislam.com](https://resume.jesseislam.com). It exposes a single POST `/` endpoint that increments and returns a page‑view counter stored in Firestore.

<img width="3840" height="1716" alt="Image" src="https://github.com/user-attachments/assets/8677f884-1e78-476f-ad30-61b3c000fe63" />

---

## Features

- **Flask** app with CORS support  
- **Firestore** integration via Firebase Admin SDK  
- **Dockerized** for deployment to Cloud Run  
- **API Gateway** proxy in front of Cloud Run  
- **CI/CD** pipeline with Google Cloud Build

---

## Repository Layout

```

.
├── Dockerfile
├── cloudbuild.yaml      # Cloud Build pipeline (tests → build → deploy)
├── main.py              # Flask application
├── requirements.txt     # Python dependencies
└── tests/               # Unit tests (pytest)
└── test\_main.py

````

---

## Prerequisites

- **Python 3.8+**  
- [Google Cloud SDK](https://cloud.google.com/sdk)  
- A GCP project with these APIs enabled:
  - Firestore (Native mode)  
  - Cloud Run  
  - API Gateway  
  - Cloud Build  
- A service account (or user) with roles:
  - `roles/datastore.user`  
  - `roles/run.admin`  
  - `roles/secretmanager.secretAccessor` (if using Secret Manager)  

---

## Local Development (still in testing)

1. **Clone repository**  
   ```bash
   git clone https://github.com/Jesse-Islam/resume.jesseislam.com.backend.git
   cd resume.jesseislam.com.backend
```

2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Set Google credentials**

   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account.json"
   ```

5. **Run the app**

   ```bash
   flask run --host=0.0.0.0 --port=8080
   ```

   Then test:

   ```bash
   curl -X POST http://localhost:8080/
   ```

---

## Testing

Unit tests are written with **pytest** in the `tests/` directory.

```bash
pip install pytest
pytest --maxfail=1 --disable-warnings -q
```

---

## Docker

Build and run the container locally:

```bash
docker build -t resume-backend .
docker run -p 8080:8080 \
  -e GOOGLE_APPLICATION_CREDENTIALS="/path/in/container/key.json" \
  resume-backend
```

---

## CI/CD with Cloud Build

The included `cloudbuild.yaml`:

1. Runs **pytest**
2. Builds and pushes the Docker image to Artifact Registry
3. Deploys the image to Cloud Run

To enable:

1. In GCP Console → Cloud Build → Triggers, create a trigger on your `main` branch.
2. Point it to this repo and use the default `cloudbuild.yaml`.
3. Push to GitHub to start the pipeline.

---

## Usage

Once deployed behind API Gateway, your endpoint is:

```
POST https://<YOUR_API_GATEWAY_DOMAIN>/
```

Response:

```json
{ "view_count": 42 }
```

---

## Contact

Jesse Islam · [resume.jesseislam.com](https://resume.jesseislam.com) · [jesse@jesseislam.com](mailto:jesse@jesseislam.com)

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.


## Purpose

- https://github.com/Jesse-Islam/resume.jesseislam.terraform
- https://github.com/Jesse-Islam/resume.jesseislam.com.backend
- https://github.com/Jesse-Islam/resume.jesseislam.com.frontend

These three repositories automatically update the different components that go into https://resume.jesseislam.com



