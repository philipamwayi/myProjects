terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
    region = "us-east-1"
    alias = "primary_region"

}

provider "aws" {
    region = "us-west-2"
    alias = "secondary_region"
}

resource "aws_s3_bucket" "myBucket" {

    bucket = "AdventureTech-PA-bucket"
    bucket = "NatureEscape-PA-bucket"
    bucket = "DataSummit-PA-bucket"
    bucket = "CodeCarnival-PA-bucket"

    provider = aws.secondary_region
}

resource "aws_s3_bucket_ownership_controls" "israel" {
    bucket = aws_s3_bucket.myBucket
    rule {
        object_ownership = "BucketOwnerPreferred"
    }
}

resource "aws_s3_bucket_acl" "israel" {
    depends_on = [aws_s3_bucket_ownership_controls.israel]

    bucket = aws_s3_bucket.myBucket
    acl = "private"
}
/*
resource "aws_s3_bucket" "myBucket" {
    bucket = "NatureEscape-PA-bucket"
}

resource "aws_s3_bucket" "myBucket" {
    bucket = "DataSummit-PA-bucket"
}

resource "aws_s3_bucket" "myBucket" {
    bucket = "CodeCarnival-PA-bucket"
}
*/