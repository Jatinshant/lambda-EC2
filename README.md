# lambda-EC2
# Launch and Terminate Instance by using Lambda Function
# 🚀 EC2 Control Panel (AWS Lambda + API Gateway + HTML)

This project provides a **web-based control panel** to launch and terminate EC2 instances in AWS using **Lambda functions**, exposed through **API Gateway** endpoints. The dashboard is built using **HTML, CSS, and JavaScript**, and communicates with AWS services through secure HTTP requests.

---

## 📸 Screenshot

![image](https://github.com/user-attachments/assets/da31da01-966b-4360-b81e-cfebd435c81b)


## 🧰 Tech Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: AWS Lambda (Python)
- **API Layer**: AWS API Gateway
- **Cloud Provider**: AWS (EC2, Lambda, IAM)

---

## ✨ Features

- 🚀 Launch EC2 Instances with:
  - AMI ID
  - Instance Type
  - Custom Name (Tag)
- 🛑 Terminate EC2 Instances by ID
- 🎨 Beautiful, responsive UI with animations
- ⚡ Instant feedback and error handling
- 🔐 Easily extendable with API security (API Key, Cognito, etc.)

---

## 📁 Project Structure
├── lambda-EC2/projects-aws/lambda-functions/EC2-launch.py  
# Lambda function to launch EC2

├── lambda-EC2/projects-aws/lambda-functions/EC2-terminate.py  
# Lambda function to terminate EC2

├── lambda-EC2/projects-aws/EC2.html  
# Frontend HTML dashboard

├── lambda-EC2/projects-aws/README.md  
# Project documentation

---

## 🚀 Getting Started

### 1. Set up Lambda Functions

- Go to **AWS Lambda Console**
- Create two functions:
  - `launch-ec2`
  - `terminate-ec2`
- Use the Python code from `launch_lambda.py` and `terminate_lambda.py`
- Assign an IAM Role with the following permissions:
  ```json
  {
    "Effect": "Allow",
    "Action": [
      "ec2:RunInstances",
      "ec2:TerminateInstances",
      "ec2:DescribeInstances"
    ],
    "Resource": "*"
  }
  
### 2. Create API Gateway Endpoints
Create a REST API or HTTP API

Set up two endpoints:

POST /launch → connected to launch-ec2 Lambda

POST /terminate → connected to terminate-ec2 Lambda

Enable CORS on both endpoints

Deploy the API and note the base URL

### 3. Configure the Frontend
Open ec2-control-panel.html

Replace the following with your actual API endpoints:
---
const LAUNCH_API_ENDPOINT = 'https://your-api-id.execute-api.region.amazonaws.com/prod/launch';
const TERMINATE_API_ENDPOINT = 'https://your-api-id.execute-api.region.amazonaws.com/prod/terminate';

---
🙌 Credits
Built by Jatin Shant – DevOps enthusiast with a passion for automation and cloud.

---

Let me know if you want me to:
- Add the Lambda code files (`launch_lambda.py`, `terminate_lambda.py`)
- Auto-generate a `LICENSE`
- Generate a sample screenshot or GitHub Pages version of the dashboard

Would you like a `project.zip` with all this structured and ready to push to GitHub?


