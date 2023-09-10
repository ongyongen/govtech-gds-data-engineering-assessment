# Provide AWS Access Key
variable "AWS_ACCESS_KEY" {
}

# Provide AWS Secret Key
variable "AWS_SECRET_KEY" {
}

# Using ap-southeast-1 as default region
variable "region" {
    default = "ap-southeast-1"
}

# Using the default python3.7 layer
variable "python37_layer_arn" {
    default = "arn:aws:lambda:ap-southeast-1:336392948345:layer:AWSSDKPandas-Python37:5"
}

variable "python_custom_layer_filepath" {
    default = "../scripts/layers/python.zip"
}