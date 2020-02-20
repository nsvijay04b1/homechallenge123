# security group to be attached to our instance
resource "aws_security_group" "three-tier-application-security-group" {
  name        = "three-tier Application Security Group"
  description = "three-tier Application Security Group"

  # allowing SSH
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # allowing web connections since it runs a web server
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  vpc_id =  aws_vpc.vpc_application.id 
}
