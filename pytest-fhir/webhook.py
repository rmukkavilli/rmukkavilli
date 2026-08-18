from flask import Flask, request, jsonify

app = Flask(__name__)

_jobs:dict[str,dict] = {}


def create_job(job_id:str, str = "PENDING") -> None:
    _jobs[job_id] = {"status": status, "completion_count": 0}

def get_job(job_id: str) -> dict | None:
    return _job.get(job_id)

@app.route("/webhooks/fhir-export", methods=["POST"])
def handle_export_webhook():
    # if the body is not valid by default, 
    # teling flaks not to raise an error and crash request with 400
    payload = request.get_json(silent=True)
    if not payload or "job_id" not in payload or "result"  not in payload:
        return justify({"error":"invalid payload"}), 400
    
    job = get_job(payload["job_id"])
     if job is None:
        return justify({"error": "Unknown Job id"}), 404
    
    if payload["result"] == "success":
        if job["status"]!= "COMPLETE":
            job["completion_count"] +=1
        job["status"] = "COMPLETE"
    else:
        job["status"] = "FAILED"
        job["failure_reason"] = payload.get("reason", "unknown")
    return jsonity({"message": "processed"}), 200
