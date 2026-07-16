# ☁️ AWS Serverless Notes App

A modern serverless Notes Application built using **AWS Lambda**, **Amazon S3**, **API Gateway**, and a responsive **HTML, CSS, JavaScript** frontend.

The application allows users to create, save, and read text notes stored securely in an Amazon S3 bucket without managing any servers.

---

## 📌 Features

- 📝 Create Notes
- ☁️ Store Notes in Amazon S3
- 📄 View Saved Notes
- ⚡ Fast REST APIs
- 📂 List All Notes
- 📖 Read Note Content
- 🔄 Refresh Notes
- 🌐 Responsive Modern UI
- 📊 CloudWatch Logging
- 🔒 Serverless Architecture

---

# 🏗️ Architecture

```

HTML/CSS/JavaScript
│
▼
Amazon API Gateway
│
▼
AWS Lambda (Python)
│
▼
Amazon S3
(Store Notes)

```

---

# 🛠️ AWS Services Used

| Service | Purpose |
|----------|----------|
| AWS Lambda | Backend Logic |
| Amazon API Gateway | REST APIs |
| Amazon S3 | Store Notes |
| IAM | Access Permissions |
| CloudWatch | Logging & Monitoring |

---

# 📂 Folder Structure

```

NotesApp/
│
├── index.html
├── style.css
├── script.js
└── README.md

```

---

# 🚀 Application Workflow

1. User enters filename and note.
2. Frontend sends a POST request to API Gateway.
3. API Gateway invokes AWS Lambda.
4. Lambda stores the note inside Amazon S3.
5. User can refresh to view all notes.
6. Clicking a note fetches its content from S3.
7. Lambda returns the content to the frontend.

---

# 📡 API Endpoints

## Save Note

**POST**

```

/note

```

Request

```json
{
  "filename": "Hello.txt",
  "content": "Good Morning"
}
```

Response

```json
{
  "message": "File saved successfully."
}
```

---

## Read Note

**GET**

```

/note?filename=Hello.txt

```

Response

```json
{
  "filename": "Hello.txt",
  "content": "Good Morning"
}
```

---

## List Notes

**GET**

```

/notes

```

Response

```json
{
  "total_notes": 3,
  "notes": [
    "Hello.txt",
    "meeting.txt",
    "Project.txt"
  ]
}
```

---

## List Files

**GET**

```

/files

```

Returns all files stored in the S3 bucket.

---

## File Information

**GET**

```

/file?name=Hello.txt

```

Returns

- File Name
- File Size
- Last Modified Time

---

# 📸 User Interface

The application includes:

- Left Sidebar
  - Create Note
  - Filename Input
  - Note Content
  - Save Button

- Right Panel
  - Notes List
  - Refresh Button
  - Selected Note Viewer

---

# ⚙️ Technologies Used

### Frontend

- HTML5
- CSS3
- JavaScript (Vanilla)

### Backend

- Python
- boto3

### Cloud Services

- AWS Lambda
- Amazon S3
- API Gateway
- IAM
- CloudWatch

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/your-username/aws-serverless-notes-app.git
```

Open

```

index.html

```

Update the API Gateway URL inside **script.js**

```javascript
const API_URL = "YOUR_API_GATEWAY_URL";
```

Run using VS Code Live Server.

---

# 📋 Prerequisites

- AWS Account
- Amazon S3 Bucket
- AWS Lambda Function
- API Gateway
- IAM Role
- VS Code

---

# 📊 Logging

CloudWatch automatically records

- Incoming Requests
- Uploaded Notes
- Read Requests
- Errors
- API Logs

---

# 🔐 IAM Permissions

Required S3 permissions

```
s3:PutObject
s3:GetObject
s3:ListBucket
s3:HeadObject
```

---

# 🌟 Future Improvements

- Edit Note
- Delete Note
- User Authentication
- Search Notes
- Categories
- Dark Mode
- Markdown Support
- DynamoDB Integration

---

# 📚 Learning Outcomes

This project demonstrates

- Serverless Computing
- REST API Development
- AWS Lambda
- Amazon S3
- API Gateway
- IAM Roles
- CloudWatch
- boto3 SDK
- JavaScript Fetch API

---

# 📸 Application Screenshots

## 🏠 Home Page

Displays the modern dashboard where users can create new notes, view all saved notes, and read selected notes.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/0e4d6085-06aa-4848-9ceb-10e49f347bd5" />


---

## ☁️ Amazon S3 Bucket

Shows all text notes successfully stored inside the S3 bucket.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/36637e2b-89a4-481e-80bb-ce2a42e3cba6" />


---

## ⚡ AWS Lambda Function

Python Lambda function that processes API requests and interacts with Amazon S3.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/727b0438-6236-4437-b650-f0f9d3b75035" />

---

## 🌐 API Gateway Routes

REST API endpoints that connect the frontend with the Lambda function.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/0b955a44-84cf-4e41-8d7c-24b6c366bdb1" />

---

## 📝 Creating a New Note

Users can enter a filename and note content, then save it directly to Amazon S3.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9aec3bca-acdc-4807-a9b9-b50909371b40" />

---

## 📖 Viewing a Saved Note

Clicking any note loads its content instantly from Amazon S3 using the API.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5002cbee-fc79-4418-a43b-733dffd9cd27" />
