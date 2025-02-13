provider "aws" {
  region = "us-east-1"
}

# IAM Role for Lambda Execution
resource "aws_iam_role" "lambda_role" {
  name = "RetailEdgeLambdaRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_iam_policy_attachment" "lambda_basic" {
  name       = "lambda_basic_attachment"
  roles      = [aws_iam_role.lambda_role.name]
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# DynamoDB for Inventory & Sales
resource "aws_dynamodb_table" "inventory" {
  name         = "RetailEdgeInventory"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "itemId"

  attribute {
    name = "itemId"
    type = "S"
  }
}

resource "aws_dynamodb_table" "sales" {
  name         = "RetailEdgeSales"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "saleId"

  attribute {
    name = "saleId"
    type = "S"
  }
}

# AWS QuickSight for Analytics
#resource "aws_quicksight_dataset" "sales_dashboard" {
#  name      = "RetailEdgeSalesData"
#  import_mode = "SPICE"

#  physical_table_map {
#    dynamodb_table {
#      table_name = aws_dynamodb_table.sales.name
#    }
#  }
#}

# Lambda for Processing Sales
#resource "aws_lambda_function" "sales_lambda" {
#  function_name = "RetailEdgeSalesProcessor"
#  role          = aws_iam_role.lambda_role.arn
#  handler       = "app.lambda_handler"
#  runtime       = "python3.9"

#  filename         = "lambda.zip"
#  source_code_hash = filebase64sha256("lambda.zip")
#}

# API Gateway
resource "aws_api_gateway_rest_api" "retail_api" {
  name        = "RetailEdgeAPI"
  description = "API Gateway for RetailEdge"
}

resource "aws_api_gateway_resource" "sales" {
  rest_api_id = aws_api_gateway_rest_api.retail_api.id
  parent_id   = aws_api_gateway_rest_api.retail_api.root_resource_id
  path_part   = "sales"
}

resource "aws_api_gateway_method" "sales_post" {
  rest_api_id   = aws_api_gateway_rest_api.retail_api.id
  resource_id   = aws_api_gateway_resource.sales.id
  http_method   = "POST"
  authorization = "NONE"
}

# Cognito for Authentication
resource "aws_cognito_user_pool" "user_pool" {
  name = "RetailEdgeUsers"
}

resource "aws_cognito_user_pool_client" "app_client" {
  name         = "RetailEdgeClient"
  user_pool_id = aws_cognito_user_pool.user_pool.id
}

# Outputs
#output "api_gateway_url" {
#  value = aws_api_gateway_rest_api.retail_api.endpoint
#}

output "cognito_user_pool_id" {
  value = aws_cognito_user_pool.user_pool.id
}
#resource "aws_lambda_function" "yoco_payment_lambda" {
#  function_name = "RetailEdgeYocoPaymentProcessor"
#  role          = aws_iam_role.lambda_role.arn
#  handler       = "payments.lambda_handler"
#  runtime       = "python3.9"
#
#  filename         = "payments.zip"
#  source_code_hash = filebase64sha256("payments.zip")
#}

resource "aws_api_gateway_resource" "payments" {
  rest_api_id = aws_api_gateway_rest_api.retail_api.id
  parent_id   = aws_api_gateway_rest_api.retail_api.root_resource_id
  path_part   = "payments"
}

resource "aws_api_gateway_method" "payments_post" {
  rest_api_id   = aws_api_gateway_rest_api.retail_api.id
  resource_id   = aws_api_gateway_resource.payments.id
  http_method   = "POST"
  authorization = "NONE"
}

output "payment_api_url" {
  value = aws_api_gateway_rest_api.retail_api.endpoint
}

