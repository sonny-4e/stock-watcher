terraform {
  required_version = ">= 1.10"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region  = "eu-north-1"
  profile = "stock-watcher"

  default_tags {
    tags = {
      Project   = "stock-watcher"
      ManagedBy = "terraform"
    }
  }
}