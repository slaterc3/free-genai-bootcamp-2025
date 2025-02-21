# OPEA Components Setup Guide

This guide explains how to set up the Ollama LLM server component on AWS EC2.

## EC2 Instance Requirements

- Instance Type: t3.large
- Storage: 20GB
- RAM: 8GB
- Operating System: Ubuntu
- Security Group: Allow inbound traffic on port 8008

## Prerequisites

1. AWS Account with EC2 access
2. Docker and Docker Compose installed
3. Git installed

## Setup Instructions

### 1. EC2 Instance Setup

1. Launch a t3.large EC2 instance with Ubuntu
2. Configure security group to allow inbound traffic on port 8008
3. Connect to your instance:
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-ip
   ```

### 2. Repository Setup

1. Clone the repository:
   ```bash
   cd /home/ubuntu
   git clone https://github.com/intel/free-genai-bootcamp-2025.git
   cd free-genai-bootcamp-2025/opea-comps
   ```

### 3. Environment Configuration

1. Create .env file with required settings:

   ```bash
   # Port configuration
   LLM_ENDPOINT_PORT=8008

   # Model configuration
   LLM_MODEL_ID=llama3.2:1b

   # EC2 host IP - replace with your EC2 public IP
   host_ip=your-ec2-public-ip

   # Proxy settings (if needed)
   http_proxy=
   https_proxy=
   no_proxy=
   ```

### 4. Docker Compose Deployment

1. Start the Ollama server:

   ```bash
   docker-compose up -d
   ```

2. Pull the LLM model:
   ```bash
   docker exec ollama-server ollama pull llama3.2:1b
   ```

### 5. Testing the Setup

1. Test locally on EC2:

   ```bash
   curl http://localhost:8008/api/generate -d '{
     "model": "llama3.2:1b",
     "prompt": "Hello, how are you?"
   }'
   ```

2. Test remotely (replace with your EC2 IP):
   ```bash
   curl http://your-ec2-ip:8008/api/generate -d '{
     "model": "llama3.2:1b",
     "prompt": "Hello, how are you?"
   }'
   ```

## Volume Management

The setup includes a Docker volume `ollama_data` that persists model data between container restarts.

## Troubleshooting

1. Check container status:

   ```bash
   docker ps
   ```

2. View container logs:

   ```bash
   docker-compose logs -f
   ```

3. Check model list:
   ```bash
   docker exec ollama-server ollama list
   ```

## API Integration

The Ollama server exposes an HTTP API endpoint at port 8008. Example Python integration:
