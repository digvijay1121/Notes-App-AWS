import json
import boto3
import logging

# Initialize S3 Client
s3 = boto3.client("s3")

# S3 Bucket Name
BUCKET_NAME = "notes-storage-12345"

# Configure Logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Common CORS Headers
CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "*",
    "Access-Control-Allow-Methods": "GET,POST,OPTIONS"
}


def lambda_handler(event, context):

    logger.info("Received Event: %s", json.dumps(event))

    try:

        method = event["requestContext"]["http"]["method"]
        path = event["rawPath"]

        # ==========================
        # OPTIONS (CORS)
        # ==========================
        if method == "OPTIONS":
            return {
                "statusCode": 200,
                "headers": CORS_HEADERS,
                "body": ""
            }

        # ==========================
        # POST /note
        # ==========================
        elif method == "POST" and path == "/note":

            body = json.loads(event["body"])

            filename = body["filename"]
            content = body["content"]

            s3.put_object(
                Bucket=BUCKET_NAME,
                Key=filename,
                Body=content
            )

            logger.info(f"Uploaded File : {filename}")

            return {
                "statusCode": 200,
                "headers": CORS_HEADERS,
                "body": json.dumps({
                    "message": "File saved successfully."
                })
            }

        # ==========================
        # GET /note?filename=...
        # ==========================
        elif method == "GET" and path == "/note":

            params = event.get("queryStringParameters")

            if not params or "filename" not in params:
                return {
                    "statusCode": 400,
                    "headers": CORS_HEADERS,
                    "body": json.dumps({
                        "error": "filename query parameter is required."
                    })
                }

            filename = params["filename"]

            response = s3.get_object(
                Bucket=BUCKET_NAME,
                Key=filename
            )

            content = response["Body"].read().decode("utf-8")

            logger.info(f"Read File : {filename}")

            return {
                "statusCode": 200,
                "headers": CORS_HEADERS,
                "body": json.dumps({
                    "filename": filename,
                    "content": content
                })
            }

        # ==========================
        # GET /notes
        # ==========================
        elif method == "GET" and path == "/notes":

            response = s3.list_objects_v2(Bucket=BUCKET_NAME)

            notes = []

            if "Contents" in response:
                for obj in response["Contents"]:
                    notes.append(obj["Key"])

            notes.sort(key=str.lower)

            logger.info("========== Notes ==========")
            for note in notes:
                logger.info(note)
            logger.info("===========================")

            return {
                "statusCode": 200,
                "headers": CORS_HEADERS,
                "body": json.dumps({
                    "total_notes": len(notes),
                    "notes": notes
                })
            }

        # ==========================
        # GET /files
        # ==========================
        elif method == "GET" and path == "/files":

            response = s3.list_objects_v2(Bucket=BUCKET_NAME)

            files = []

            if "Contents" in response:
                for obj in response["Contents"]:
                    files.append(obj["Key"])

            files.sort(key=str.lower)

            logger.info("========== Files in S3 Bucket ==========")

            for file in files:
                logger.info(file)

            logger.info("========================================")

            return {
                "statusCode": 200,
                "headers": CORS_HEADERS,
                "body": json.dumps({
                    "total_files": len(files),
                    "files": files
                })
            }

        # ==========================
        # GET /file?name=...
        # ==========================
        elif method == "GET" and path == "/file":

            params = event.get("queryStringParameters")

            if not params or "name" not in params:
                return {
                    "statusCode": 400,
                    "headers": CORS_HEADERS,
                    "body": json.dumps({
                        "error": "name query parameter is required."
                    })
                }

            filename = params["name"]

            response = s3.head_object(
                Bucket=BUCKET_NAME,
                Key=filename
            )

            file_size = response["ContentLength"]

            last_modified = response["LastModified"].strftime(
                "%Y-%m-%d %H:%M:%S UTC"
            )

            logger.info("========== File Details ==========")
            logger.info(f"File Name     : {filename}")
            logger.info(f"File Size     : {file_size} Bytes")
            logger.info(f"Last Modified : {last_modified}")
            logger.info("==================================")

            return {
                "statusCode": 200,
                "headers": CORS_HEADERS,
                "body": json.dumps({
                    "file_name": filename,
                    "file_size_bytes": file_size,
                    "last_modified": last_modified
                })
            }

        # ==========================
        # Invalid Route
        # ==========================
        else:

            return {
                "statusCode": 404,
                "headers": CORS_HEADERS,
                "body": json.dumps({
                    "message": "Route Not Found"
                })
            }

    except Exception as e:

        logger.exception("Application Error")

        return {
            "statusCode": 500,
            "headers": CORS_HEADERS,
            "body": json.dumps({
                "error": str(e)
            })
        }
