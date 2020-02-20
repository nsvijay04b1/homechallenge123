# three-tier-app-aws-terraform
Simple three-tier app example deployed to AWS using Terraform.

# Requirements
- Terraform >= `0.11.1`
- `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables exported.

# Usage
Clone this repository and run:

Initializing Terrraform remote backend:
```
λ ~/three-tier-app-aws-terraform/ terraform init -backend-config=terraform.remote
```

Terraform plan:
```
λ ~/three-tier-app-aws-terraform/ terraform plan
```

Terraform apply:
```
λ ~/three-tier-app-aws-terraform/ terraform apply
```

After the process is completed, should then be able to connect to `http://EC2_INSTANCE_IP/app1` and `http://EC2_INSTANCE_IP/app2` in your browser.

# References
- https://github.com/lbracken/docker-example (for the example three-tier application)
- https://www.terraform.io/docs/index.html
- https://nickcharlton.net/posts/terraform-aws-vpc.html (provided me a quick overview of resources to be created after the VPC, like proper route association)
