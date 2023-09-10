# Government Digital Services, CC4.0 Data Engineering Intern Test
This repository contains the code for the submission of Government Digital Services, CC4.0 Data Engineering Intern Test. <br></br>
The `.github/workflows` directory contains a Github Action that conducts checks on code quality
using Pylint and ensures that all unit tests created can be executed successfully before a code
is merged back to main branch. <br></br>
The `sample_output` directory contains the CSV files output when `python main.py` is run (in the `scripts` directory). <br></br>
The `scripts` directory contains the data cleaning scripts. Run `python main.py` in this directory
to generate the CSV files for Q1 and Q2 (saved to `sample_output` directory) and the console output
answers for Q3. <br></br>
The `terraform` directory contains code to automate the deployment of AWS resources for the scripts.

## Assumptions
1) The restaurants.json data provided (ie https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json) appears to resemble the result of
a GET API, possibly from the Zomato website. Hence, I have decided to ingest that data using python's requests.get() method to mimick how I would make an API GET request (instead of downloading the json to my local computer and uploading it again into my repository).
2) The `res_id` field in `R` and `id` field in `restaurant` both refer to restaurant ID (just that they have different data types), and hence can be used interchangeably.
3) If 2 events have the same name, same start and end date, same restaurant, they can still be considered different events if they have a different event id.
4) For the Photo URL column required in Q2, all photos of an event should be extracted. If there are more than 1 photos associated with an event, I have concatenated their URLs together with a comma delimiter.
   
## Instructions to run the source code
Clone this repository to your local computer <br></br>
`git clone https://github.com/ongyongen/govtech-gds-data-engineering-assessment.git`

Navigate to the root directory <br></br>
`cd govtech-gds-data-engineering-assessment`

Set up a virtual environment <br></br>
`python -m venv .venv`

Activate the virtual environment <br></br>
`source .venv/bin/activate`

Install the required libraries <br></br>
`pip install -r requirements.txt`

After installing the required libraries, you can navigate to the scripts directory to run the main.py file  <br></br>
`cd scripts`  <br></br>
`python main.py`

The output (preview of CSV files and the explanation for Q3) will be printed to the console as shown below. CSV files for Q1 and Q2 are saved to the `sample_output` directory. <br></br>
<img width="1148" alt="Screenshot 2023-09-10 at 6 10 11 PM" src="https://github.com/ongyongen/govtech-gds-data-engineering-assessment/assets/97529863/6026f88c-b797-438f-9044-e7a496262a3a">
<img width="1155" alt="Screenshot 2023-09-10 at 9 44 52 PM" src="https://github.com/ongyongen/govtech-gds-data-engineering-assessment/assets/97529863/7a6b60d0-a99b-4102-91ed-9a4887bc10f9">
<img width="1151" alt="Screenshot 2023-09-10 at 9 47 16 PM" src="https://github.com/ongyongen/govtech-gds-data-engineering-assessment/assets/97529863/91ae456b-87f7-4d2e-9076-9a37e363afc9">

At the root directory, you can run tests on the codes using Pytest <br></br>
`python -m pytest`

At the root directory, you can run Pylint checks on the codes in `scripts` directory <br></br>
`pylint ./scripts`

Note : Ensure that Pylint's import strategy is set to `fromEnvironment` in your VSCode's Settings file <br></br>
<img width="863" alt="Screenshot 2023-09-10 at 8 27 49 PM" src="https://github.com/ongyongen/govtech-gds-data-engineering-assessment/assets/97529863/cc31a97b-0ca3-4ddf-885b-58249019ad1a">

## Instructions to deploy scripts to AWS
Ensure that you have installed terraform : https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli <br></br>
Navigate to the `terraform` directory <br></br>
Run `terraform init` to set up the terraform config files. <br></br>
Run `terraform plan` to preview the changes that Terraform plans to make to your infrastructure. <br></br>
Run `terraform apply` to execute the actions propose in Terraform plan. <br></br>
Run `terraform destroy` to remove all resources previously configured by Terraform. <br></br>

Along the way you may be promopted to provide your AWS Access Key and AWS Secret Key. <br></br>
<img width="893" alt="Screenshot 2023-09-10 at 6 31 57 PM" src="https://github.com/ongyongen/govtech-gds-data-engineering-assessment/assets/97529863/725551d3-86b5-44fc-a64a-0bb16cc35615">

Upon successful deployment, you can verify that 2 S3 buckets are created. <br></br>
<img width="985" alt="Screenshot 2023-09-10 at 6 32 41 PM" src="https://github.com/ongyongen/govtech-gds-data-engineering-assessment/assets/97529863/83574a4a-4879-4d1d-9e4c-9bb8ae031a60">

The lambda function for the scripts will also be created. <br></br>
<img width="808" alt="Screenshot 2023-09-10 at 6 33 35 PM" src="https://github.com/ongyongen/govtech-gds-data-engineering-assessment/assets/97529863/fa910a6a-46c3-4ee1-bd74-021191aa4786">

You can create a test event to test the lambda function. Once executed successfully, this will be the result shown. <br></br>
<img width="1106" alt="Screenshot 2023-09-10 at 6 37 28 PM" src="https://github.com/ongyongen/govtech-gds-data-engineering-assessment/assets/97529863/e79f962d-ecca-4458-a032-a7128c1b908a">

Once the function execution is a success, the CSV files would be output to the `restaurants-output-bucket`, ready for export. The EventBridge trigger is configured to run the script every day from Monday to Friday at 5pm. <br></br>
<img width="1069" alt="Screenshot 2023-09-10 at 6 38 57 PM" src="https://github.com/ongyongen/govtech-gds-data-engineering-assessment/assets/97529863/a75d0cb5-b598-4f41-a3e2-e449d256f157">

## Architecture diagram for current cloud services deployed
This is the current cloud architecture diagram set up for the scripts. These resources are provisioned using Terraform. <br></br>
2 S3 buckets are provisioned (1 to store the lambda.zip file, 1 to store the output CSV files for Q1 and Q2). <br></br>
An EventBridge trigger is created and linked to the lambda function for the scripts. This trigger will run the lambda function every day from Monday to Friday, at 5pm. Once the 
lambda function is run, the data cleaning script will process the restaurants data and output the CSV file for Q1 and Q2 to `restaurants-output-bucket`. The CSV files can be
downloaded directly from the output S3 bucket. <br></br>

<img width="458" alt="Screenshot 2023-09-10 at 6 54 39 PM" src="https://github.com/ongyongen/govtech-gds-data-engineering-assessment/assets/97529863/60ce2d50-680d-4faa-997f-365ccd1d3600">

## Architecture design decisions and considerations
1. Server vs Serverless based architecture <br></br>
The first consideration taken into account was whether to design the infrasturcture in a server or serverless based architecture. I decided to design the cloud architecutre in a serverless approach. With a serverless architecture, I will only need to pay for compute resources used during the execution of my data cleaning script. Given that the nature of my task (data processing) is event-driven, and probably does not need to be running 24/7, a serverless architecture will be more cost effective in the long run. Additionally, due to the time constraints of this task, a serverless approach is more feasible as it is more straightforward to set up.

2. Reproducibility <br></br>
Additionally, I also considered how I could make the deployment process more automated, so as to reduce the need to manually provision resources on the AWS console. To do so, I've decided to use Terraform to automate the provisiong and removal of my AWS resources, making the deployment process more predictable and easily auditable.

## Proposed architecture diagram for future iterations of the project
At the current stage, there are some limitations in the architecture design. 

Firstly, AWS Lambda imposesa limit of 50MB for zipped and direct upload files, and 250MB for uncompressed packages. Hence, we may face file size limits if we were to add any more layers or code in our lambda function. To tackle this issue, the lambda function codes can be deployed to a Docker container and pushed to an Amazon Elastic Container Repository (ECR), since the maximum size of a Docker image can be up to 10GB.

Secondly, business insights from the data is currently not easily accessible to business users. Business users have to download the CSV files from the S3 bucket, before they can view the CSV files and analyze the restaurants data separately. Hence, we can configure Amazon Athena to link to the output S3 buckets containing the CSV files, and write SQL queries to create tables for the restaurants data. Subsequently, Amazon Athena can be linked to an Amazon QuickSight dashboard, where we can create charts to visualize the data. As such, business users can access the dashboard and view key metrics relating to the datasets, for business reporting purposes. 

<img width="712" alt="Screenshot 2023-09-10 at 7 08 53 PM" src="https://github.com/ongyongen/govtech-gds-data-engineering-assessment/assets/97529863/42a05b87-9888-4006-96cd-b0f43c176824">
