data "archive_file" "restaurant_lambda_file" {
  type = "zip"

  source_dir  = "../scripts"
  output_path = "../scripts.zip"
}


data "archive_file" "lambda_layer" {
  type = "zip"

  source_dir  = "../scripts"
  output_path = "../scripts.zip"
}

