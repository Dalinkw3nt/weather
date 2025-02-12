# RetailEdge Lite - Cloud-Based POS & Sales Dashboard

RetailEdge Lite is a scalable, cloud-based **Point of Sale (POS) and Sales Dashboard** solution for small retailers. Built on **AWS** with **React Native** for mobile and **React** for the dashboard, it integrates **Yoco Payment Gateway** for secure transactions.

## **Features**
- **Cloud-Based POS System** (React Native, AWS Lambda, DynamoDB)
- **Smart Inventory Tracking** (DynamoDB, Amazon SNS for low-stock alerts)
- **Real-Time Sales Dashboard** (React + AWS QuickSight)
- **Yoco Payment Gateway Integration** (Card payments via Yoco SDK)
- **Offline Mode** (Transactions sync to AWS after internet recovery)
- **Scalable & Cost-Effective AWS Infrastructure** (Serverless architecture)

---

## **1. Prerequisites**
- **Node.js** (v16+)
- **AWS CLI** (configured with necessary IAM permissions)
- **Terraform** (for infrastructure provisioning)
- **Yoco API Key** (Register at [Yoco](https://www.yoco.com/))

---

## **2. Deployment Instructions**

### **Step 1: Clone the Repository**
```sh
git clone https://github.com/your-repo/retailedge-lite.git
cd retailedge-lite
```

### **Step 2: Deploy AWS Infrastructure (Terraform)**
```sh
cd infrastructure
terraform init
terraform apply -auto-approve
```
💡 **Terraform will create:**
- API Gateway for POS transactions
- AWS Lambda for sales processing
- DynamoDB for inventory & sales
- Amazon QuickSight for analytics
- Cognito for authentication

### **Step 3: Deploy Backend (AWS Lambda - Python)**
```sh
cd backend
zip -r lambda.zip .
aws lambda update-function-code --function-name RetailEdgeSalesProcessor --zip-file fileb://lambda.zip
```

### **Step 4: Run the POS System (React Native)**
```sh
cd pos
npm install
npm start
```
To test on an emulator, run:
```sh
npx react-native run-android  # For Android
echo 'Use Xcode for iOS'
```

### **Step 5: Run the Sales Dashboard (React Web App)**
```sh
cd dashboard
npm install
npm start
```

---

## **3. Yoco Payment Gateway Integration**
- **Set your Yoco Public Key in POS System:**
  ```sh
  export YOCO_PUBLIC_KEY='your-public-key'
  ```
- **Set Yoco Secret Key for Lambda:**
  ```sh
  export YOCO_SECRET_KEY='your-secret-key'
  ```
- **Test a Payment in the POS System:**
  - Enter sale details in the app.
  - Click **Pay with Yoco**.
  - Use a test card from Yoco’s [documentation](https://developer.yoco.com/).

---

## **4. APIs**
### **POS Transactions**
- **Endpoint:** `POST /sales`
- **Payload:**
  ```json
  {
    "saleId": "12345",
    "itemId": "ABC001",
    "quantity": 2
  }
  ```

### **Yoco Payment Processing**
- **Endpoint:** `POST /payments`
- **Payload:**
  ```json
  {
    "saleId": "12345",
    "token": "yoco-payment-token",
    "amount": 100.00
  }
  ```

---

## **5. Security & Authentication**
- **Cognito Authentication** for secure user login.
- **AWS KMS Encryption** for sensitive data.
- **AWS Shield** for DDoS protection.

---

## **6. Next Steps & Enhancements**
✅ Multi-Store Support
✅ Mobile Money Integration (MTN, Vodacom Pay)
✅ Supplier Order Automation

---

## **7. Contributors**
- **Your Name** - [GitHub](https://github.com/your-profile)
- **Your Team**

---

## **8. License**
MIT License. See `LICENSE` for details.


