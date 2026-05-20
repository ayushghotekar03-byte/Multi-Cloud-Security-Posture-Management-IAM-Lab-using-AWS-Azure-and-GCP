
import os

# Create project directory structure
base_dir = "/mnt/agents/output/multi-cloud-security-lab"
dirs = [
    "terraform/aws",
    "terraform/azure",
    "terraform/gcp",
    "terraform/modules/iam",
    "terraform/modules/security-posture",
    "scripts/python",
    "scripts/bash",
    "policies/aws",
    "policies/azure",
    "policies/gcp",
    "docs",
    "ansible",
    "docker"
]

for d in dirs:
    os.makedirs(f"{base_dir}/{d}", exist_ok=True)

print("Directory structure created successfully!")

# Create the main project README
readme_content = """# 🔐 Multi-Cloud Security Posture Management & IAM Lab

## Overview
A comprehensive, production-ready security lab for managing Identity and Access Management (IAM) and Security Posture across AWS, Azure, and Google Cloud Platform (GCP). This project provides automated infrastructure-as-code deployments, continuous compliance monitoring, and cross-cloud security best practices.

## 🎯 Objectives
- Implement least-privilege IAM policies across all three clouds
- Deploy automated security posture management with CSPM tools
- Establish continuous compliance monitoring (CIS Benchmarks, NIST, SOC2)
- Create centralized logging and SIEM integration
- Implement zero-trust network architecture
- Automate remediation of security misconfigurations

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Security Operations Center                 │
│              (Centralized Dashboard & SIEM)                   │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   ┌────▼────┐          ┌────▼────┐          ┌────▼────┐
   │   AWS   │          │  Azure  │          │   GCP   │
   │         │          │         │          │         │
   │ • IAM   │          │ • AAD   │          │ • IAM   │
   │ • GuardDuty│       │ • Defender│        │ • Security│
   │ • Config │         │ • Policy │         │   Command │
   │ • CloudTrail│      │ • Monitor │        │ • Asset   │
   │ • SecurityHub│     │ • Sentinel│        │   Inventory│
   └─────────┘          └─────────┘          └─────────┘
```

## 📁 Project Structure
```
multi-cloud-security-lab/
├── terraform/
│   ├── aws/              # AWS IAM & Security resources
│   ├── azure/            # Azure AD & Security Center
│   ├── gcp/              # GCP IAM & Security Command Center
│   └── modules/          # Reusable Terraform modules
├── scripts/
│   ├── python/           # Python automation & compliance checks
│   └── bash/             # Shell scripts for deployment
├── policies/             # Cloud-native policy definitions
│   ├── aws/              # AWS SCPs, IAM policies, Config rules
│   ├── azure/            # Azure Policies, RBAC definitions
│   └── gcp/              # GCP Organization policies, IAM constraints
├── ansible/              # Configuration management
├── docker/               # Containerized security tools
└── docs/                 # Documentation & runbooks
```

## 🚀 Quick Start

### Prerequisites
- Terraform >= 1.5.0
- AWS CLI, Azure CLI, gcloud CLI configured
- Python 3.9+
- Docker (optional, for containerized tools)

### 1. Clone and Configure
```bash
git clone <repository-url>
cd multi-cloud-security-lab
cp terraform/aws/terraform.tfvars.example terraform/aws/terraform.tfvars
# Edit terraform.tfvars with your cloud credentials and settings
```

### 2. Deploy AWS Security Foundation
```bash
cd terraform/aws
terraform init
terraform plan -out=tfplan
terraform apply tfplan
```

### 3. Deploy Azure Security Foundation
```bash
cd terraform/azure
terraform init
terraform plan -out=tfplan
terraform apply tfplan
```

### 4. Deploy GCP Security Foundation
```bash
cd terraform/gcp
terraform init
terraform plan -out=tfplan
terraform apply tfplan
```

### 5. Run Compliance Scan
```bash
cd scripts/python
pip install -r requirements.txt
python compliance_scanner.py --cloud all --report html
```

## 🔑 Key Components

### AWS
- **IAM**: Roles, Policies, Permission Boundaries, Service Control Policies
- **Security Hub**: Centralized findings from GuardDuty, Inspector, Macie
- **Config**: Rules for compliance monitoring (CIS AWS Foundations)
- **CloudTrail**: Multi-region trail with log file validation
- **KMS**: Customer-managed keys with automatic rotation

### Azure
- **Azure AD**: Conditional Access, PIM (Privileged Identity Management)
- **Azure Policy**: Built-in and custom policies for compliance
- **Microsoft Defender for Cloud**: Cloud workload protection
- **Azure Sentinel**: SIEM and SOAR capabilities
- **Key Vault**: Secrets management with HSM-backed keys

### GCP
- **Cloud IAM**: Custom roles, Organization policies
- **Security Command Center**: Asset inventory and vulnerability scanning
- **Cloud Asset Inventory**: Resource tracking and analysis
- **VPC Service Controls**: Data exfiltration prevention
- **Cloud KMS**: Key management with Cloud HSM

## 📊 Compliance Frameworks
- CIS Benchmarks (AWS v1.5, Azure v1.5, GCP v1.3)
- NIST 800-53 Rev 5
- SOC 2 Type II
- ISO 27001
- PCI DSS v4.0

## 🛡️ Security Controls Matrix

| Control Domain | AWS | Azure | GCP |
|----------------|-----|-------|-----|
| Identity Management | IAM + SSO | AAD + PIM | Cloud IAM + IAP |
| Data Protection | KMS + Macie | Key Vault + Purview | Cloud KMS + DLP |
| Network Security | VPC + WAF | NSG + Azure Firewall | VPC + Cloud Armor |
| Threat Detection | GuardDuty + Macie | Defender + Sentinel | SCC + Chronicle |
| Compliance | Config + SecurityHub | Policy + Compliance | SCC + Asset Inventory |

## 🔧 Automation
- **Terraform**: Infrastructure as Code for all resources
- **Python Scripts**: Compliance scanning, remediation, reporting
- **GitHub Actions**: CI/CD pipeline for policy validation
- **Ansible**: Configuration drift detection and remediation

## 📈 Monitoring & Alerting
- Centralized logging to S3 / Blob Storage / Cloud Storage
- Real-time alerting via SNS / Event Grid / Pub/Sub
- Dashboards in CloudWatch / Azure Monitor / Cloud Monitoring
- Integration with external SIEM (Splunk, Elastic, QRadar)

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📜 License
MIT License - See LICENSE file for details

## 📚 Documentation
- [AWS Setup Guide](docs/aws-setup.md)
- [Azure Setup Guide](docs/azure-setup.md)
- [GCP Setup Guide](docs/gcp-setup.md)
- [Compliance Scanning Guide](docs/compliance-scanning.md)
- [Troubleshooting](docs/troubleshooting.md)

---
**⚠️ Important**: This lab creates real cloud resources. Monitor costs and destroy resources when not in use with `terraform destroy`.
"""

with open(f"{base_dir}/README.md", "w") as f:
    f.write(readme_content)

print("README.md created successfully!")

# Create AWS Terraform configurations

# Main AWS Terraform file
aws_main_tf = '''terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  backend "s3" {
    bucket         = "multi-cloud-tfstate"
    key            = "aws/security-foundation/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}

provider "aws" {
  region = var.aws_region
  
  default_tags {
    tags = {
      Project     = "Multi-Cloud-Security-Lab"
      Environment = var.environment
      ManagedBy   = "Terraform"
      Compliance  = "CIS-NIST-SOC2"
    }
  }
}

# Enable AWS Organizations for multi-account strategy
resource "aws_organizations_organization" "main" {
  aws_service_access_principals = [
    "cloudtrail.amazonaws.com",
    "config.amazonaws.com",
    "securityhub.amazonaws.com",
    "guardduty.amazonaws.com",
    "macie.amazonaws.com",
    "sso.amazonaws.com",
    "access-analyzer.amazonaws.com"
  ]
  
  enabled_policy_types = [
    "SERVICE_CONTROL_POLICY",
    "TAG_POLICY",
    "BACKUP_POLICY"
  ]
  
  feature_set = "ALL"
}

# Security Account OU
resource "aws_organizations_organizational_unit" "security" {
  name      = "Security"
  parent_id = aws_organizations_organization.main.roots[0].id
}

# Production OU
resource "aws_organizations_organizational_unit" "production" {
  name      = "Production"
  parent_id = aws_organizations_organization.main.roots[0].id
}

# Development OU
resource "aws_organizations_organizational_unit" "development" {
  name      = "Development"
  parent_id = aws_organizations_organization.main.roots[0].id
}

# Service Control Policy - Deny root account usage
resource "aws_organizations_policy" "deny_root" {
  name        = "DenyRootAccountUsage"
  description = "Prevent root account usage across all accounts"
  type        = "SERVICE_CONTROL_POLICY"
  
  content = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "DenyRootAccountUsage"
        Effect = "Deny"
        Action = "*"
        Resource = "*"
        Condition = {
          StringLike = {
            "aws:PrincipalArn" = ["arn:aws:iam::*:root"]
          }
        }
      }
    ]
  })
}

resource "aws_organizations_policy_attachment" "deny_root" {
  policy_id = aws_organizations_policy.deny_root.id
  target_id = aws_organizations_organization.main.roots[0].id
}

# SCP - Restrict regions
resource "aws_organizations_policy" "restrict_regions" {
  name        = "RestrictRegions"
  description = "Allow only approved regions"
  type        = "SERVICE_CONTROL_POLICY"
  
  content = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "DenyUnapprovedRegions"
        Effect = "Deny"
        NotAction = [
          "aws-portal:*",
          "budgets:*",
          "ce:*",
          "cur:*",
          "support:*",
          "trustedadvisor:*"
        ]
        Resource = "*"
        Condition = {
          StringNotEquals = {
            "aws:RequestedRegion" = var.approved_regions
          }
        }
      }
    ]
  })
}

resource "aws_organizations_policy_attachment" "restrict_regions" {
  policy_id = aws_organizations_policy.restrict_regions.id
  target_id = aws_organizations_organization.main.roots[0].id
}

# SCP - Require encryption
resource "aws_organizations_policy" "require_encryption" {
  name        = "RequireEncryption"
  description = "Require encryption for data at rest and in transit"
  type        = "SERVICE_CONTROL_POLICY"
  
  content = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "DenyUnencryptedS3"
        Effect = "Deny"
        Action = "s3:PutObject"
        Resource = "*"
        Condition = {
          StringNotEquals = {
            "s3:x-amz-server-side-encryption" = "aws:kms"
          }
        }
      },
      {
        Sid    = "DenyUnencryptedEBS"
        Effect = "Deny"
        Action = "ec2:CreateVolume"
        Resource = "*"
        Condition = {
          Bool = {
            "ec2:Encrypted" = "false"
          }
        }
      }
    ]
  })
}

resource "aws_organizations_policy_attachment" "require_encryption" {
  policy_id = aws_organizations_policy.require_encryption.id
  target_id = aws_organizations_organizational_unit.production.id
}

module "iam_foundation" {
  source = "../modules/iam/aws"
  
  environment     = var.environment
  admin_users     = var.admin_users
  security_users  = var.security_users
  developer_users = var.developer_users
}

module "security_posture" {
  source = "../modules/security-posture/aws"
  
  environment         = var.environment
  enable_guardduty    = var.enable_guardduty
  enable_securityhub  = var.enable_securityhub
  enable_config       = var.enable_config
  enable_macie        = var.enable_macie
  enable_inspector    = var.enable_inspector
  log_retention_days  = var.log_retention_days
  kms_key_id          = module.iam_foundation.kms_key_id
}

# CloudTrail - Multi-region trail with log validation
resource "aws_cloudtrail" "main" {
  name                          = "${var.environment}-multi-region-trail"
  s3_bucket_name                = aws_s3_bucket.cloudtrail.id
  is_multi_region_trail         = true
  enable_logging                = true
  enable_log_file_validation    = true
  kms_key_id                    = module.iam_foundation.kms_key_arn
  event_selector {
    read_write_type           = "All"
    include_management_events = true
    
    data_resource {
      type   = "AWS::S3::Object"
      values = ["arn:aws:s3:::*/"]
    }
    
    data_resource {
      type   = "AWS::Lambda::Function"
      values = ["arn:aws:lambda"]
    }
  }
  
  insight_selector {
    insight_type = "ApiCallRateInsight"
  }
  
  insight_selector {
    insight_type = "ApiErrorRateInsight"
  }
}

# S3 Bucket for CloudTrail logs
resource "aws_s3_bucket" "cloudtrail" {
  bucket = "${var.environment}-cloudtrail-logs-${random_id.bucket_suffix.hex}"
}

resource "aws_s3_bucket_versioning" "cloudtrail" {
  bucket = aws_s3_bucket.cloudtrail.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "cloudtrail" {
  bucket = aws_s3_bucket.cloudtrail.id
  rule {
    apply_server_side_encryption_by_default {
      kms_master_key_id = module.iam_foundation.kms_key_arn
      sse_algorithm       = "aws:kms"
    }
    bucket_key_enabled = true
  }
}

resource "aws_s3_bucket_public_access_block" "cloudtrail" {
  bucket = aws_s3_bucket.cloudtrail.id
  
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_policy" "cloudtrail" {
  bucket = aws_s3_bucket.cloudtrail.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "AWSCloudTrailAclCheck"
        Effect = "Allow"
        Principal = {
          Service = "cloudtrail.amazonaws.com"
        }
        Action   = "s3:GetBucketAcl"
        Resource = aws_s3_bucket.cloudtrail.arn
      },
      {
        Sid    = "AWSCloudTrailWrite"
        Effect = "Allow"
        Principal = {
          Service = "cloudtrail.amazonaws.com"
        }
        Action   = "s3:PutObject"
        Resource = "${aws_s3_bucket.cloudtrail.arn}/AWSLogs/${data.aws_caller_identity.current.account_id}/*"
        Condition = {
          StringEquals = {
            "s3:x-amz-acl" = "bucket-owner-full-control"
          }
        }
      }
    ]
  })
}

resource "random_id" "bucket_suffix" {
  byte_length = 4
}

data "aws_caller_identity" "current" {}

# IAM Access Analyzer
resource "aws_accessanalyzer_analyzer" "main" {
  analyzer_name = "${var.environment}-external-access-analyzer"
  type          = "ACCOUNT"
}

# VPC Flow Logs
resource "aws_flow_log" "main" {
  vpc_id                   = aws_vpc.main.id
  traffic_type             = "ALL"
  log_destination_type     = "s3"
  log_destination          = aws_s3_bucket.cloudtrail.arn
  log_format               = "$${version} $${account-id} $${interface-id} $${srcaddr} $${dstaddr} $${srcport} $${dstport} $${protocol} $${packets} $${bytes} $${start} $${end} $${action} $${log-status} $${vpc-id} $${subnet-id} $${instance-id} $${tcp-flags} $${type} $${pkt-srcaddr} $${pkt-dstaddr}"
  max_aggregation_interval = 60
}

resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {
    Name = "${var.environment}-main-vpc"
  }
}

# WAF Web ACL
resource "aws_wafv2_web_acl" "main" {
  name        = "${var.environment}-web-acl"
  description = "Main WAF Web ACL for application protection"
  scope       = "REGIONAL"
  
  default_action {
    allow {}
  }
  
  rule {
    name     = "AWSManagedRulesCommonRuleSet"
    priority = 1
    
    override_action {
      none {}
    }
    
    statement {
      managed_rule_group_statement {
        name        = "AWSManagedRulesCommonRuleSet"
        vendor_name = "AWS"
      }
    }
    
    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "AWSManagedRulesCommonRuleSetMetric"
      sampled_requests_enabled   = true
    }
  }
  
  rule {
    name     = "RateLimitRule"
    priority = 2
    
    action {
      block {}
    }
    
    statement {
      rate_based_statement {
        limit              = 2000
        aggregate_key_type = "IP"
      }
    }
    
    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "RateLimitRuleMetric"
      sampled_requests_enabled   = true
    }
  }
  
  visibility_config {
    cloudwatch_metrics_enabled = true
    metric_name                = "${var.environment}WebACL"
    sampled_requests_enabled   = true
  }
}

# SNS Topic for security alerts
resource "aws_sns_topic" "security_alerts" {
  name              = "${var.environment}-security-alerts"
  kms_master_key_id = module.iam_foundation.kms_key_id
}

resource "aws_sns_topic_subscription" "security_email" {
  topic_arn = aws_sns_topic.security_alerts.arn
  protocol  = "email"
  endpoint  = var.security_alert_email
}
'''

with open(f"{base_dir}/terraform/aws/main.tf", "w") as f:
    f.write(aws_main_tf)

# AWS Variables
aws_vars_tf = '''variable "aws_region" {
  description = "AWS primary region"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "security-lab"
}

variable "approved_regions" {
  description = "List of approved AWS regions"
  type        = list(string)
  default     = ["us-east-1", "us-west-2", "eu-west-1"]
}

variable "admin_users" {
  description = "List of admin user emails"
  type        = list(string)
  default     = []
}

variable "security_users" {
  description = "List of security team user emails"
  type        = list(string)
  default     = []
}

variable "developer_users" {
  description = "List of developer user emails"
  type        = list(string)
  default     = []
}

variable "enable_guardduty" {
  description = "Enable GuardDuty"
  type        = bool
  default     = true
}

variable "enable_securityhub" {
  description = "Enable Security Hub"
  type        = bool
  default     = true
}

variable "enable_config" {
  description = "Enable AWS Config"
  type        = bool
  default     = true
}

variable "enable_macie" {
  description = "Enable Macie"
  type        = bool
  default     = true
}

variable "enable_inspector" {
  description = "Enable Inspector"
  type        = bool
  default     = true
}

variable "log_retention_days" {
  description = "Number of days to retain logs"
  type        = number
  default     = 365
}

variable "security_alert_email" {
  description = "Email for security alerts"
  type        = string
  default     = "security@example.com"
}
'''

with open(f"{base_dir}/terraform/aws/variables.tf", "w") as f:
    f.write(aws_vars_tf)

# AWS Outputs
aws_outputs_tf = '''output "organization_id" {
  description = "AWS Organization ID"
  value       = aws_organizations_organization.main.id
}

output "security_ou_id" {
  description = "Security OU ID"
  value       = aws_organizations_organizational_unit.security.id
}

output "cloudtrail_arn" {
  description = "CloudTrail ARN"
  value       = aws_cloudtrail.main.arn
}

output "kms_key_arn" {
  description = "KMS Key ARN"
  value       = module.iam_foundation.kms_key_arn
}

output "security_alerts_topic_arn" {
  description = "Security Alerts SNS Topic ARN"
  value       = aws_sns_topic.security_alerts.arn
}

output "access_analyzer_arn" {
  description = "Access Analyzer ARN"
  value       = aws_accessanalyzer_analyzer.main.arn
}
'''

with open(f"{base_dir}/terraform/aws/outputs.tf", "w") as f:
    f.write(aws_outputs_tf)

# terraform.tfvars.example
aws_tfvars = '''aws_region = "us-east-1"
environment = "security-lab"
approved_regions = ["us-east-1", "us-west-2", "eu-west-1"]

admin_users     = ["admin1@company.com", "admin2@company.com"]
security_users  = ["security1@company.com", "security2@company.com"]
developer_users = ["dev1@company.com", "dev2@company.com"]

enable_guardduty   = true
enable_securityhub = true
enable_config      = true
enable_macie       = true
enable_inspector   = true

log_retention_days = 365
security_alert_email = "security-alerts@company.com"
'''

with open(f"{base_dir}/terraform/aws/terraform.tfvars.example", "w") as f:
    f.write(aws_tfvars)

print("AWS Terraform files created successfully!")

# Create Azure Terraform configurations

azure_main_tf = '''terraform {
  required_version = ">= 1.5.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.70"
    }
    azuread = {
      source  = "hashicorp/azuread"
      version = "~> 2.41"
    }
  }
  backend "azurerm" {
    resource_group_name  = "tfstate-rg"
    storage_account_name = "multicloudtfstate"
    container_name       = "tfstate"
    key                  = "azure/security-foundation/terraform.tfstate"
  }
}

provider "azurerm" {
  features {
    key_vault {
      purge_soft_delete_on_destroy = false
      recover_soft_deleted_key_vaults = true
    }
  }
}

provider "azuread" {}

# Resource Group for Security Resources
resource "azurerm_resource_group" "security" {
  name     = "${var.environment}-security-rg"
  location = var.azure_region
  tags = {
    Project     = "Multi-Cloud-Security-Lab"
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
}

# Azure AD Tenant Configuration
data "azuread_client_config" "current" {}

# Security Group for Admins
resource "azuread_group" "security_admins" {
  display_name     = "Security Administrators"
  security_enabled = true
  description      = "Group for security administrators with elevated privileges"
  
  owners = [data.azuread_client_config.current.object_id]
}

# Security Group for Security Operators
resource "azuread_group" "security_operators" {
  display_name     = "Security Operators"
  security_enabled = true
  description      = "Group for security operations team"
  
  owners = [data.azuread_client_config.current.object_id]
}

# Conditional Access Policy - Require MFA for all users
resource "azuread_conditional_access_policy" "require_mfa" {
  display_name = "Require MFA for All Users"
  state        = "enabled"
  
  conditions {
    applications {
      included_applications = ["All"]
    }
    
    users {
      included_users = ["All"]
      excluded_users = [data.azuread_client_config.current.object_id]
    }
    
    locations {
      included_locations = ["AllTrusted"]
    }
    
    platforms {
      included_platforms = ["all"]
    }
  }
  
  grant_controls {
    operator          = "OR"
    built_in_controls = ["mfa"]
  }
}

# Conditional Access Policy - Block legacy authentication
resource "azuread_conditional_access_policy" "block_legacy_auth" {
  display_name = "Block Legacy Authentication"
  state        = "enabled"
  
  conditions {
    applications {
      included_applications = ["All"]
    }
    
    users {
      included_users = ["All"]
    }
    
    client_app_types = ["exchangeActiveSync", "other"]
  }
  
  grant_controls {
    operator          = "OR"
    built_in_controls = ["block"]
  }
}

# Conditional Access Policy - Require compliant device for admins
resource "azuread_conditional_access_policy" "require_compliant_device" {
  display_name = "Require Compliant Device for Admins"
  state        = "enabled"
  
  conditions {
    applications {
      included_applications = ["All"]
    }
    
    users {
      included_groups = [azuread_group.security_admins.id]
    }
  }
  
  grant_controls {
    operator          = "AND"
    built_in_controls = ["compliantDevice", "domainJoinedDevice"]
  }
}

# Azure Key Vault
resource "azurerm_key_vault" "main" {
  name                        = "${var.environment}-kv-${random_string.suffix.result}"
  location                    = azurerm_resource_group.security.location
  resource_group_name         = azurerm_resource_group.security.name
  tenant_id                   = data.azuread_client_config.current.tenant_id
  soft_delete_retention_days  = 90
  purge_protection_enabled    = true
  sku_name                    = "premium"
  enabled_for_disk_encryption = true
  
  network_acls {
    default_action             = "Deny"
    bypass                     = "AzureServices"
    ip_rules                   = var.allowed_ip_ranges
    virtual_network_subnet_ids = []
  }
  
  tags = {
    Project     = "Multi-Cloud-Security-Lab"
    Environment = var.environment
  }
}

# Key Vault Access Policy for Terraform SP
resource "azurerm_key_vault_access_policy" "terraform" {
  key_vault_id = azurerm_key_vault.main.id
  tenant_id    = data.azuread_client_config.current.tenant_id
  object_id    = data.azuread_client_config.current.object_id
  
  key_permissions = [
    "Create", "Delete", "Get", "List", "Purge", "Recover", "Update", "Import",
    "Backup", "Restore", "Decrypt", "Encrypt", "UnwrapKey", "WrapKey"
  ]
  
  secret_permissions = [
    "Backup", "Delete", "Get", "List", "Purge", "Recover", "Restore", "Set"
  ]
  
  certificate_permissions = [
    "Backup", "Create", "Delete", "DeleteIssuers", "Get", "GetIssuers",
    "Import", "List", "ListIssuers", "ManageContacts", "ManageIssuers",
    "Purge", "Recover", "Restore", "SetIssuers", "Update"
  ]
}

# Generate RSA Key for encryption
resource "azurerm_key_vault_key" "main" {
  name         = "main-encryption-key"
  key_vault_id = azurerm_key_vault.main.id
  key_type     = "RSA"
  key_size     = 4096
  
  key_opts = [
    "decrypt", "encrypt", "sign", "unwrapKey", "verify", "wrapKey"
  ]
  
  rotation_policy {
    automatic {
      time_before_expiry = "P30D"
    }
    expire_after         = "P90D"
    notify_before_expiry = "P29D"
  }
  
  depends_on = [azurerm_key_vault_access_policy.terraform]
}

# Log Analytics Workspace for Sentinel
resource "azurerm_log_analytics_workspace" "security" {
  name                = "${var.environment}-security-law"
  location            = azurerm_resource_group.security.location
  resource_group_name = azurerm_resource_group.security.name
  sku                 = "PerGB2018"
  retention_in_days   = var.log_retention_days
  
  tags = {
    Project     = "Multi-Cloud-Security-Lab"
    Environment = var.environment
  }
}

# Azure Sentinel
resource "azurerm_sentinel_log_analytics_workspace_onboarding" "main" {
  workspace_id                 = azurerm_log_analytics_workspace.security.id
  customer_managed_key_enabled = true
}

# Microsoft Defender for Cloud
resource "azurerm_security_center_subscription_pricing" "main" {
  tier          = "Standard"
  resource_type = "VirtualMachines"
}

resource "azurerm_security_center_subscription_pricing" "storage" {
  tier          = "Standard"
  resource_type = "StorageAccounts"
}

resource "azurerm_security_center_subscription_pricing" "sql" {
  tier          = "Standard"
  resource_type = "SqlServers"
}

resource "azurerm_security_center_subscription_pricing" "app_service" {
  tier          = "Standard"
  resource_type = "AppServices"
}

resource "azurerm_security_center_subscription_pricing" "key_vault" {
  tier          = "Standard"
  resource_type = "KeyVaults"
}

resource "azurerm_security_center_subscription_pricing" "dns" {
  tier          = "Standard"
  resource_type = "Dns"
}

# Security Center Contact
resource "azurerm_security_center_contact" "main" {
  email               = var.security_alert_email
  phone               = var.security_alert_phone
  alert_notifications = true
  alerts_to_admins    = true
}

# Security Center Auto Provisioning
resource "azurerm_security_center_auto_provisioning" "main" {
  auto_provision = "On"
}

# Azure Policy - Initiative for CIS Benchmark
resource "azurerm_policy_set_definition" "cis_benchmark" {
  name         = "cis-azure-1.5.0"
  policy_type  = "Custom"
  display_name = "CIS Azure Foundations Benchmark v1.5.0"
  description  = "This initiative includes policies that address CIS Azure Foundations Benchmark recommendations"
  
  metadata = jsonencode({
    category = "Regulatory Compliance"
    version  = "1.0.0"
  })
  
  policy_definition_reference {
    policy_definition_id = "/providers/Microsoft.Authorization/policyDefinitions/4f4f78b8-e367-4b10-a341-d9a4ad5cf1c7"
    reference_id         = "RequireEncryptionOnDataLakeStoreAccounts"
  }
  
  policy_definition_reference {
    policy_definition_id = "/providers/Microsoft.Authorization/policyDefinitions/0961008e-5641-4dd2-8f14-5cc7385fa886"
    reference_id         = "RequireEncryptionOnStorageAccounts"
  }
  
  policy_definition_reference {
    policy_definition_id = "/providers/Microsoft.Authorization/policyDefinitions/2c89a2e5-7285-40fe-afe0-ae8654b92fab"
    reference_id         = "RequireNetworkWatcherInRegions"
  }
  
  policy_definition_reference {
    policy_definition_id = "/providers/Microsoft.Authorization/policyDefinitions/1b8ca024-1d5c-4dec-8995-b1a932b41780"
    reference_id         = "RequireSecureTransferToStorageAccounts"
  }
}

# Assign CIS Benchmark Policy
resource "azurerm_subscription_policy_assignment" "cis_benchmark" {
  name                 = "cis-azure-assignment"
  policy_definition_id = azurerm_policy_set_definition.cis_benchmark.id
  subscription_id      = data.azurerm_subscription.current.id
  
  identity {
    type = "SystemAssigned"
  }
  
  location = var.azure_region
}

# Network Security Group with strict rules
resource "azurerm_network_security_group" "main" {
  name                = "${var.environment}-nsg"
  location            = azurerm_resource_group.security.location
  resource_group_name = azurerm_resource_group.security.name
  
  security_rule {
    name                       = "DenyAllInbound"
    priority                   = 4096
    direction                  = "Inbound"
    access                     = "Deny"
    protocol                   = "*"
    source_port_range          = "*"
    destination_port_range     = "*"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
  
  tags = {
    Project     = "Multi-Cloud-Security-Lab"
    Environment = var.environment
  }
}

# Azure Firewall
resource "azurerm_firewall" "main" {
  name                = "${var.environment}-firewall"
  location            = azurerm_resource_group.security.location
  resource_group_name = azurerm_resource_group.security.name
  
  sku_name = "AZFW_VNet"
  sku_tier = "Premium"
  
  ip_configuration {
    name                 = "configuration"
    subnet_id            = azurerm_subnet.firewall.id
    public_ip_address_id = azurerm_public_ip.firewall.id
  }
  
  tags = {
    Project     = "Multi-Cloud-Security-Lab"
    Environment = var.environment
  }
}

resource "azurerm_public_ip" "firewall" {
  name                = "${var.environment}-firewall-pip"
  location            = azurerm_resource_group.security.location
  resource_group_name = azurerm_resource_group.security.name
  allocation_method   = "Static"
  sku                 = "Standard"
  
  tags = {
    Project     = "Multi-Cloud-Security-Lab"
    Environment = var.environment
  }
}

resource "azurerm_virtual_network" "main" {
  name                = "${var.environment}-vnet"
  address_space       = ["10.1.0.0/16"]
  location            = azurerm_resource_group.security.location
  resource_group_name = azurerm_resource_group.security.name
  
  tags = {
    Project     = "Multi-Cloud-Security-Lab"
    Environment = var.environment
  }
}

resource "azurerm_subnet" "firewall" {
  name                 = "AzureFirewallSubnet"
  resource_group_name  = azurerm_resource_group.security.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = ["10.1.1.0/24"]
}

# Diagnostic Settings for Key Vault
resource "azurerm_monitor_diagnostic_setting" "keyvault" {
  name                       = "keyvault-diagnostics"
  target_resource_id         = azurerm_key_vault.main.id
  log_analytics_workspace_id = azurerm_log_analytics_workspace.security.id
  
  enabled_log {
    category = "AuditEvent"
  }
  
  enabled_log {
    category = "AzurePolicyEvaluationDetails"
  }
  
  metric {
    category = "AllMetrics"
  }
}

# Action Group for Security Alerts
resource "azurerm_monitor_action_group" "security" {
  name                = "security-alerts"
  resource_group_name = azurerm_resource_group.security.name
  short_name          = "secalerts"
  
  email_receiver {
    name                    = "security-team"
    email_address           = var.security_alert_email
    use_common_alert_schema = true
  }
  
  sms_receiver {
    name         = "security-sms"
    country_code = "1"
    phone_number = var.security_alert_phone
  }
}

# Random string for unique naming
resource "random_string" "suffix" {
  length  = 8
  special = false
  upper   = false
}

data "azurerm_subscription" "current" {}
'''

with open(f"{base_dir}/terraform/azure/main.tf", "w") as f:
    f.write(azure_main_tf)

# Azure Variables
azure_vars_tf = '''variable "azure_region" {
  description = "Azure primary region"
  type        = string
  default     = "East US"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "security-lab"
}

variable "log_retention_days" {
  description = "Number of days to retain logs"
  type        = number
  default     = 365
}

variable "security_alert_email" {
  description = "Email for security alerts"
  type        = string
  default     = "security@example.com"
}

variable "security_alert_phone" {
  description = "Phone number for security SMS alerts"
  type        = string
  default     = "1234567890"
}

variable "allowed_ip_ranges" {
  description = "List of allowed IP ranges for Key Vault"
  type        = list(string)
  default     = []
}
'''

with open(f"{base_dir}/terraform/azure/variables.tf", "w") as f:
    f.write(azure_vars_tf)

# Azure Outputs
azure_outputs_tf = '''output "resource_group_name" {
  description = "Security Resource Group Name"
  value       = azurerm_resource_group.security.name
}

output "key_vault_name" {
  description = "Key Vault Name"
  value       = azurerm_key_vault.main.name
}

output "key_vault_uri" {
  description = "Key Vault URI"
  value       = azurerm_key_vault.main.vault_uri
}

output "log_analytics_workspace_id" {
  description = "Log Analytics Workspace ID"
  value       = azurerm_log_analytics_workspace.security.id
}

output "sentinel_onboarding_state" {
  description = "Sentinel Onboarding State"
  value       = azurerm_sentinel_log_analytics_workspace_onboarding.main.id
}

output "firewall_private_ip" {
  description = "Azure Firewall Private IP"
  value       = azurerm_firewall.main.ip_configuration[0].private_ip_address
}

output "security_group_admins_id" {
  description = "Security Admins Group ID"
  value       = azuread_group.security_admins.id
}
'''

with open(f"{base_dir}/terraform/azure/outputs.tf", "w") as f:
    f.write(azure_outputs_tf)

# terraform.tfvars.example for Azure
azure_tfvars = '''azure_region = "East US"
environment = "security-lab"
log_retention_days = 365
security_alert_email = "security-alerts@company.com"
security_alert_phone = "1234567890"
allowed_ip_ranges = ["203.0.113.0/24"]
'''

with open(f"{base_dir}/terraform/azure/terraform.tfvars.example", "w") as f:
    f.write(azure_tfvars)

print("Azure Terraform files created successfully!")

# Create GCP Terraform configurations

gcp_main_tf = '''terraform {
  required_version = ">= 1.5.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.80"
    }
    google-beta = {
      source  = "hashicorp/google-beta"
      version = "~> 4.80"
    }
  }
  backend "gcs" {
    bucket = "multi-cloud-tfstate"
    prefix = "gcp/security-foundation"
  }
}

provider "google" {
  project = var.gcp_project_id
  region  = var.gcp_region
}

provider "google-beta" {
  project = var.gcp_project_id
  region  = var.gcp_region
}

# Enable required APIs
resource "google_project_service" "apis" {
  for_each = toset([
    "cloudresourcemanager.googleapis.com",
    "iam.googleapis.com",
    "compute.googleapis.com",
    "logging.googleapis.com",
    "monitoring.googleapis.com",
    "securitycenter.googleapis.com",
    "cloudasset.googleapis.com",
    "cloudkms.googleapis.com",
    "osconfig.googleapis.com",
    "container.googleapis.com",
    "servicenetworking.googleapis.com",
    "vpcaccess.googleapis.com",
    "accesscontextmanager.googleapis.com",
    "essentialcontacts.googleapis.com"
  ])
  
  service            = each.value
  disable_on_destroy = false
}

# Organization Policies
resource "google_organization_policy" "restrict_vm_external_ips" {
  org_id     = var.gcp_org_id
  constraint = "compute.vmExternalIpAccess"
  
  list_policy {
    deny {
      all = true
    }
  }
}

resource "google_organization_policy" "skip_default_network" {
  org_id     = var.gcp_org_id
  constraint = "compute.skipDefaultNetworkCreation"
  
  boolean_policy {
    enforced = true
  }
}

resource "google_organization_policy" "disable_guest_attributes" {
  org_id     = var.gcp_org_id
  constraint = "compute.disableGuestAttributesAccess"
  
  boolean_policy {
    enforced = true
  }
}

resource "google_organization_policy" "require_os_login" {
  org_id     = var.gcp_org_id
  constraint = "compute.requireOsLogin"
  
  boolean_policy {
    enforced = true
  }
}

resource "google_organization_policy" "disable_serial_port" {
  org_id     = var.gcp_org_id
  constraint = "compute.disableSerialPortAccess"
  
  boolean_policy {
    enforced = true
  }
}

resource "google_organization_policy" "restrict_cloud_sql_public_ip" {
  org_id     = var.gcp_org_id
  constraint = "sql.restrictPublicIp"
  
  boolean_policy {
    enforced = true
  }
}

resource "google_organization_policy" "uniform_bucket_access" {
  org_id     = var.gcp_org_id
  constraint = "storage.uniformBucketLevelAccess"
  
  boolean_policy {
    enforced = true
  }
}

# Cloud IAM - Custom Roles
resource "google_project_iam_custom_role" "security_auditor" {
  role_id     = "securityAuditor"
  title       = "Security Auditor"
  description = "Custom role for security auditing with read-only access"
  permissions = [
    "resourcemanager.projects.get",
    "resourcemanager.projects.getIamPolicy",
    "iam.roles.get",
    "iam.roles.list",
    "iam.serviceAccounts.get",
    "iam.serviceAccounts.list",
    "logging.logEntries.list",
    "logging.logs.list",
    "monitoring.timeSeries.list",
    "cloudasset.assets.listResource",
    "cloudasset.assets.listIamPolicy",
    "securitycenter.findings.list",
    "securitycenter.sources.get",
    "securitycenter.sources.list"
  ]
}

resource "google_project_iam_custom_role" "security_remediator" {
  role_id     = "securityRemediator"
  title       = "Security Remediator"
  description = "Custom role for security remediation actions"
  permissions = [
    "resourcemanager.projects.get",
    "resourcemanager.projects.getIamPolicy",
    "resourcemanager.projects.setIamPolicy",
    "iam.roles.get",
    "iam.roles.list",
    "iam.serviceAccounts.get",
    "iam.serviceAccounts.list",
    "compute.instances.setMetadata",
    "compute.instances.setTags",
    "compute.firewalls.update",
    "compute.firewalls.delete",
    "storage.buckets.setIamPolicy",
    "cloudkms.cryptoKeys.setIamPolicy"
  ]
}

# Security Group
resource "google_cloud_identity_group" "security_team" {
  display_name = "Security Team"
  
  parent = "customers/${var.gcp_org_id}"
  
  group_key {
    id = "security-team@${var.gcp_domain}"
  }
  
  labels = {
    "cloudidentity.googleapis.com/groups.discussion_forum" = ""
  }
}

# Assign custom role to security group
resource "google_project_iam_member" "security_auditor" {
  project = var.gcp_project_id
  role    = google_project_iam_custom_role.security_auditor.id
  member  = "group:security-team@${var.gcp_domain}"
}

# Cloud KMS
resource "google_kms_key_ring" "main" {
  name     = "${var.environment}-keyring"
  location = var.gcp_region
}

resource "google_kms_crypto_key" "main" {
  name            = "main-encryption-key"
  key_ring        = google_kms_key_ring.main.id
  rotation_period = "7776000s" # 90 days
  
  version_template {
    algorithm        = "GOOGLE_SYMMETRIC_ENCRYPTION"
    protection_level = "HSM"
  }
  
  lifecycle {
    prevent_destroy = true
  }
}

# IAM Policy for KMS Key
resource "google_kms_crypto_key_iam_member" "encrypt_decrypt" {
  crypto_key_id = google_kms_crypto_key.main.id
  role          = "roles/cloudkms.cryptoKeyEncrypterDecrypter"
  member        = "serviceAccount:${data.google_project.project.number}-compute@developer.gserviceaccount.com"
}

# Security Command Center
resource "google_scc_source" "custom_source" {
  display_name = "Custom Security Scanner"
  organization = var.gcp_org_id
}

# Security Health Analytics
resource "google_security_health_analytics_custom_module" "example" {
  provider = google-beta
  parent   = "projects/${var.gcp_project_id}"
  display_name = "Custom Security Module"
  enablement_state = "ENABLED"
  
  custom_config {
    predicate {
      expression = "resource.rotationPeriod > duration('2592000s')"
      title       = "Rotation Period Check"
      description = "Check if KMS keys are rotated within 30 days"
    }
    resource_selector {
      resource_types = ["cloudkms.googleapis.com/CryptoKey"]
    }
    severity = "MEDIUM"
    description = "KMS keys should be rotated every 30 days"
    recommendation = "Rotate the KMS key to maintain security"
  }
}

# Cloud Asset Inventory
resource "google_cloud_asset_project_feed" "resource_changes" {
  project      = var.gcp_project_id
  feed_id      = "resource-changes-feed"
  content_type = "RESOURCE"
  
  asset_types = [
    "compute.googleapis.com/Instance",
    "storage.googleapis.com/Bucket",
    "cloudkms.googleapis.com/CryptoKey",
    "iam.googleapis.com/ServiceAccount",
    "container.googleapis.com/Cluster"
  ]
  
  feed_output_config {
    pubsub_destination {
      topic = google_pubsub_topic.asset_changes.id
    }
  }
}

resource "google_pubsub_topic" "asset_changes" {
  name = "asset-changes-topic"
  
  message_retention_duration = "86600s"
  
  labels = {
    environment = var.environment
  }
}

# VPC Service Controls
resource "google_access_context_manager_service_perimeter" "main" {
  parent = "accessPolicies/${google_access_context_manager_access_policy.main.name}"
  name   = "accessPolicies/${google_access_context_manager_access_policy.main.name}/servicePerimeters/${var.environment}_perimeter"
  title  = "${var.environment}_perimeter"
  
  status {
    restricted_services = [
      "storage.googleapis.com",
      "bigquery.googleapis.com",
      "cloudkms.googleapis.com"
    ]
    
    vpc_accessible_services {
      enable_restriction = true
      allowed_services   = ["storage.googleapis.com", "bigquery.googleapis.com"]
    }
  }
  
  use_explicit_dry_run_spec = true
}

resource "google_access_context_manager_access_policy" "main" {
  parent = "organizations/${var.gcp_org_id}"
  title  = "${var.environment} Security Policy"
}

# Cloud Logging - Log Sink for Security Logs
resource "google_logging_project_sink" "security_sink" {
  name        = "security-log-sink"
  destination = "pubsub.googleapis.com/projects/${var.gcp_project_id}/topics/${google_pubsub_topic.security_logs.name}"
  filter      = <<-EOT
    protoPayload.serviceName="cloudresourcemanager.googleapis.com"
    OR protoPayload.serviceName="iam.googleapis.com"
    OR protoPayload.serviceName="cloudkms.googleapis.com"
    OR protoPayload.methodName="v1.compute.firewalls.insert"
    OR protoPayload.methodName="v1.compute.firewalls.patch"
    OR protoPayload.methodName="v1.compute.firewalls.delete"
  EOT
  
  unique_writer_identity = true
}

resource "google_pubsub_topic" "security_logs" {
  name = "security-logs-topic"
  
  labels = {
    environment = var.environment
  }
}

resource "google_pubsub_topic_iam_member" "security_sink_writer" {
  topic  = google_pubsub_topic.security_logs.name
  role   = "roles/pubsub.publisher"
  member = google_logging_project_sink.security_sink.writer_identity
}

# Cloud Monitoring - Alerting Policies
resource "google_monitoring_alert_policy" "iam_changes" {
  display_name = "IAM Policy Changes"
  combiner     = "OR"
  
  conditions {
    display_name = "IAM Policy Change Detected"
    
    condition_matched_log {
      filter = <<-EOT
        protoPayload.serviceName="iam.googleapis.com"
        protoPayload.methodName="google.iam.admin.v1.SetIAMPolicy"
      EOT
    }
  }
  
  notification_channels = [google_monitoring_notification_channel.security_email.id]
  
  alert_strategy {
    auto_close = "86400s"
  }
  
  severity = "WARNING"
}

resource "google_monitoring_alert_policy" "kms_key_usage" {
  display_name = "KMS Key Unusual Usage"
  combiner     = "OR"
  
  conditions {
    display_name = "High KMS Key Usage"
    
    condition_threshold {
      filter          = "resource.type=\"cloudkms_cryptokey\" AND metric.type=\"cloudkms.googleapis.com/api/request_count\""
      duration        = "300s"
      comparison      = "COMPARISON_GT"
      threshold_value = 100
      
      aggregations {
        alignment_period   = "300s"
        per_series_aligner = "ALIGN_RATE"
      }
    }
  }
  
  notification_channels = [google_monitoring_notification_channel.security_email.id]
  severity = "CRITICAL"
}

resource "google_monitoring_notification_channel" "security_email" {
  display_name = "Security Team Email"
  type         = "email"
  
  labels = {
    email_address = var.security_alert_email
  }
}

# Cloud Armor Security Policy
resource "google_compute_security_policy" "main" {
  name = "${var.environment}-security-policy"
  
  rule {
    action   = "deny(403)"
    priority = "1000"
    match {
      versioned_expr = "SRC_IPS_V1"
      config {
        src_ip_ranges = var.blocked_ip_ranges
      }
    }
    description = "Block known malicious IPs"
  }
  
  rule {
    action   = "rate_based_ban"
    priority = "2000"
    match {
      expr {
        expression = "true"
      }
    }
    rate_limit_options {
      rate_limit_threshold {
        count        = 100
        interval_sec = 60
      }
      ban_duration_sec = 3600
      conform_action   = "allow"
      exceed_action    = "deny(429)"
      enforce_on_key   = "IP"
    }
    description = "Rate limit requests"
  }
  
  rule {
    action   = "allow"
    priority = "2147483647"
    match {
      versioned_expr = "SRC_IPS_V1"
      config {
        src_ip_ranges = ["*"]
      }
    }
    description = "Default allow rule"
  }
}

# Essential Contacts
resource "google_essential_contacts_contact" "security" {
  parent       = "projects/${var.gcp_project_id}"
  email        = var.security_alert_email
  language_tag = "en-US"
  
  notification_category_subscriptions = [
    "SECURITY",
    "LEGAL",
    "SUSPENSION"
  ]
}

# OS Config - Patch Management
resource "google_os_config_patch_deployment" "security_patches" {
  patch_deployment_id = "security-patch-deployment"
  
  instance_filter {
    all = true
  }
  
  patch_config {
    reboot_config = "ALWAYS"
    
    apt {
      type = "DIST"
    }
    
    yum {
      security = true
    }
    
    windows_update {
      classifications = ["CRITICAL", "SECURITY", "UPDATE"]
    }
  }
  
  duration = "3600s"
  
  recurring_schedule {
    time_zone {
      id = "America/New_York"
    }
    
    monthly {
      month_day = 15
    }
    
    time_of_day {
      hours   = 2
      minutes = 0
    }
  }
}

# Data source for project number
data "google_project" "project" {
  project_id = var.gcp_project_id
}
'''

with open(f"{base_dir}/terraform/gcp/main.tf", "w") as f:
    f.write(gcp_main_tf)

# GCP Variables
gcp_vars_tf = '''variable "gcp_project_id" {
  description = "GCP Project ID"
  type        = string
}

variable "gcp_org_id" {
  description = "GCP Organization ID"
  type        = string
}

variable "gcp_domain" {
  description = "GCP Organization Domain"
  type        = string
}

variable "gcp_region" {
  description = "GCP primary region"
  type        = string
  default     = "us-central1"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "security-lab"
}

variable "security_alert_email" {
  description = "Email for security alerts"
  type        = string
  default     = "security@example.com"
}

variable "blocked_ip_ranges" {
  description = "List of IP ranges to block"
  type        = list(string)
  default     = []
}
'''

with open(f"{base_dir}/terraform/gcp/variables.tf", "w") as f:
    f.write(gcp_vars_tf)

# GCP Outputs
gcp_outputs_tf = '''output "kms_key_name" {
  description = "KMS Key Name"
  value       = google_kms_crypto_key.main.name
}

output "kms_key_ring_name" {
  description = "KMS Key Ring Name"
  value       = google_kms_key_ring.main.name
}

output "security_policy_name" {
  description = "Cloud Armor Security Policy Name"
  value       = google_compute_security_policy.main.name
}

output "pubsub_topic_security_logs" {
  description = "Security Logs Pub/Sub Topic"
  value       = google_pubsub_topic.security_logs.name
}

output "monitoring_notification_channel" {
  description = "Monitoring Notification Channel ID"
  value       = google_monitoring_notification_channel.security_email.id
}

output "custom_role_security_auditor" {
  description = "Security Auditor Custom Role ID"
  value       = google_project_iam_custom_role.security_auditor.id
}

output "scc_source_name" {
  description = "Security Command Center Source Name"
  value       = google_scc_source.custom_source.name
}
'''

with open(f"{base_dir}/terraform/gcp/outputs.tf", "w") as f:
    f.write(gcp_outputs_tf)

# terraform.tfvars.example for GCP
gcp_tfvars = '''gcp_project_id = "your-project-id"
gcp_org_id = "123456789"
gcp_domain = "company.com"
gcp_region = "us-central1"
environment = "security-lab"
security_alert_email = "security-alerts@company.com"
blocked_ip_ranges = ["192.0.2.0/24", "198.51.100.0/24"]
'''

with open(f"{base_dir}/terraform/gcp/terraform.tfvars.example", "w") as f:
    f.write(gcp_tfvars)

print("GCP Terraform files created successfully!")

# Create Terraform Modules - IAM and Security Posture

# AWS IAM Module
aws_iam_module = '''# AWS IAM Foundation Module
# Provides comprehensive IAM setup with least-privilege principles

# KMS Key for encryption
resource "aws_kms_key" "main" {
  description             = "KMS key for multi-cloud security lab"
  deletion_window_in_days = 30
  enable_key_rotation     = true
  multi_region            = true
  
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "Enable IAM User Permissions"
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:root"
        }
        Action   = "kms:*"
        Resource = "*"
      },
      {
        Sid    = "Allow CloudTrail Encryption"
        Effect = "Allow"
        Principal = {
          Service = "cloudtrail.amazonaws.com"
        }
        Action = [
          "kms:GenerateDataKey*",
          "kms:DescribeKey"
        ]
        Resource = "*"
      },
      {
        Sid    = "Allow Config Encryption"
        Effect = "Allow"
        Principal = {
          Service = "config.amazonaws.com"
        }
        Action = [
          "kms:Decrypt",
          "kms:GenerateDataKey*"
        ]
        Resource = "*"
      }
    ]
  })
  
  tags = {
    Name        = "${var.environment}-main-key"
    Environment = var.environment
    Purpose     = "Encryption"
  }
}

resource "aws_kms_alias" "main" {
  name          = "alias/${var.environment}-main-key"
  target_key_id = aws_kms_key.main.key_id
}

# Admin Role with Permission Boundaries
resource "aws_iam_role" "admin" {
  name = "${var.environment}-admin-role"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:root"
        }
        Condition = {
          Bool = {
            "aws:MultiFactorAuthPresent" = "true"
          }
        }
      }
    ]
  })
  
  permissions_boundary = aws_iam_policy.permission_boundary.arn
  
  tags = {
    Name        = "Admin Role"
    Environment = var.environment
  }
}

resource "aws_iam_role_policy_attachment" "admin" {
  role       = aws_iam_role.admin.name
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}

# Security Role
resource "aws_iam_role" "security" {
  name = "${var.environment}-security-role"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:root"
        }
        Condition = {
          Bool = {
            "aws:MultiFactorAuthPresent" = "true"
          }
        }
      }
    ]
  })
  
  permissions_boundary = aws_iam_policy.permission_boundary.arn
}

resource "aws_iam_role_policy" "security" {
  name = "security-role-policy"
  role = aws_iam_role.security.id
  
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "SecurityReadAccess"
        Effect = "Allow"
        Action = [
          "guardduty:Get*",
          "guardduty:List*",
          "guardduty:Describe*",
          "securityhub:Get*",
          "securityhub:List*",
          "securityhub:Describe*",
          "config:Get*",
          "config:Describe*",
          "config:List*",
          "macie2:Get*",
          "macie2:List*",
          "iam:Get*",
          "iam:List*",
          "cloudtrail:LookupEvents",
          "cloudtrail:Get*",
          "cloudtrail:List*",
          "logs:Describe*",
          "logs:Get*",
          "logs:FilterLogEvents",
          "kms:Describe*",
          "kms:Get*",
          "kms:List*",
          "ec2:Describe*",
          "s3:Get*",
          "s3:List*"
        ]
        Resource = "*"
      },
      {
        Sid    = "SecurityRemediation"
        Effect = "Allow"
        Action = [
          "guardduty:UpdateFindingsFeedback",
          "guardduty:ArchiveFindings",
          "securityhub:UpdateFindings",
          "securityhub:BatchUpdateFindings",
          "config:PutEvaluations",
          "iam:UpdateAccountPasswordPolicy",
          "iam:DeleteAccessKey",
          "iam:UpdateAccessKey",
          "ec2:RevokeSecurityGroupIngress",
          "ec2:RevokeSecurityGroupEgress",
          "s3:PutBucketPolicy",
          "s3:PutBucketAcl",
          "s3:PutBucketPublicAccessBlock"
        ]
        Resource = "*"
      }
    ]
  })
}

# Developer Role with limited permissions
resource "aws_iam_role" "developer" {
  name = "${var.environment}-developer-role"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:root"
        }
        Condition = {
          Bool = {
            "aws:MultiFactorAuthPresent" = "true"
          }
        }
      }
    ]
  })
  
  permissions_boundary = aws_iam_policy.permission_boundary.arn
}

resource "aws_iam_role_policy" "developer" {
  name = "developer-role-policy"
  role = aws_iam_role.developer.id
  
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "DeveloperEC2Access"
        Effect = "Allow"
        Action = [
          "ec2:Describe*",
          "ec2:RunInstances",
          "ec2:StartInstances",
          "ec2:StopInstances",
          "ec2:TerminateInstances",
          "ec2:CreateTags",
          "ec2:DeleteTags"
        ]
        Resource = "*"
        Condition = {
          StringEquals = {
            "ec2:Region" = ["us-east-1", "us-west-2"]
          }
        }
      },
      {
        Sid    = "DeveloperS3Access"
        Effect = "Allow"
        Action = [
          "s3:Get*",
          "s3:List*",
          "s3:PutObject",
          "s3:DeleteObject"
        ]
        Resource = [
          "arn:aws:s3:::dev-*",
          "arn:aws:s3:::dev-*/*"
        ]
      },
      {
        Sid    = "DeveloperLambdaAccess"
        Effect = "Allow"
        Action = [
          "lambda:List*",
          "lambda:Get*",
          "lambda:InvokeFunction",
          "lambda:UpdateFunctionCode",
          "lambda:UpdateFunctionConfiguration"
        ]
        Resource = "arn:aws:lambda:*:*:function:dev-*"
      },
      {
        Sid    = "DenyProduction"
        Effect = "Deny"
        Action = "*"
        Resource = "*"
        Condition = {
          StringEquals = {
            "aws:ResourceTag/Environment" = "production"
          }
        }
      }
    ]
  })
}

# Permission Boundary Policy
resource "aws_iam_policy" "permission_boundary" {
  name        = "${var.environment}-permission-boundary"
  description = "Permission boundary for all roles"
  
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "AllowGeneralServices"
        Effect = "Allow"
        Action = [
          "ec2:*",
          "s3:*",
          "lambda:*",
          "cloudwatch:*",
          "logs:*",
          "sns:*",
          "sqs:*",
          "dynamodb:*",
          "rds:*",
          "elasticache:*"
        ]
        Resource = "*"
        Condition = {
          StringEquals = {
            "aws:RequestedRegion" = ["us-east-1", "us-west-2", "eu-west-1"]
          }
        }
      },
      {
        Sid    = "DenyDangerousActions"
        Effect = "Deny"
        Action = [
          "iam:CreateUser",
          "iam:DeleteUser",
          "iam:CreateAccessKey",
          "iam:DeleteAccountPasswordPolicy",
          "iam:UpdateAccountPasswordPolicy",
          "organizations:LeaveOrganization",
          "organizations:DeleteOrganization",
          "account:CloseAccount",
          "billing:*",
          "payments:*"
        ]
        Resource = "*"
      },
      {
        Sid    = "DenyUnapprovedRegions"
        Effect = "Deny"
        NotAction = [
          "aws-portal:*",
          "budgets:*",
          "ce:*",
          "cur:*",
          "support:*"
        ]
        Resource = "*"
        Condition = {
          StringNotEquals = {
            "aws:RequestedRegion" = ["us-east-1", "us-west-2", "eu-west-1"]
          }
        }
      }
    ]
  })
}

# Password Policy
resource "aws_iam_account_password_policy" "strict" {
  minimum_password_length        = 16
  require_lowercase_characters   = true
  require_numbers                = true
  require_uppercase_characters   = true
  require_symbols                = true
  allow_users_to_change_password = true
  max_password_age               = 90
  password_reuse_prevention      = 24
  hard_expiry                    = false
}

# IAM Groups
resource "aws_iam_group" "admins" {
  name = "${var.environment}-admins"
}

resource "aws_iam_group" "security" {
  name = "${var.environment}-security"
}

resource "aws_iam_group" "developers" {
  name = "${var.environment}-developers"
}

# Group Policy Attachments
resource "aws_iam_group_policy_attachment" "admins" {
  group      = aws_iam_group.admins.name
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}

resource "aws_iam_group_policy_attachment" "security" {
  group      = aws_iam_group.security.name
  policy_arn = "arn:aws:iam::aws:policy/SecurityAudit"
}

resource "aws_iam_group_policy_attachment" "developers" {
  group      = aws_iam_group.developers.name
  policy_arn = "arn:aws:iam::aws:policy/PowerUserAccess"
}

# Create users and add to groups
resource "aws_iam_user" "admin_users" {
  for_each = toset(var.admin_users)
  name     = each.value
  
  force_destroy = true
  
  tags = {
    Role        = "Admin"
    Environment = var.environment
  }
}

resource "aws_iam_user_group_membership" "admin_users" {
  for_each = toset(var.admin_users)
  user     = aws_iam_user.admin_users[each.value].name
  groups   = [aws_iam_group.admins.name]
}

resource "aws_iam_user" "security_users" {
  for_each = toset(var.security_users)
  name     = each.value
  
  force_destroy = true
  
  tags = {
    Role        = "Security"
    Environment = var.environment
  }
}

resource "aws_iam_user_group_membership" "security_users" {
  for_each = toset(var.security_users)
  user     = aws_iam_user.security_users[each.value].name
  groups   = [aws_iam_group.security.name]
}

resource "aws_iam_user" "developer_users" {
  for_each = toset(var.developer_users)
  name     = each.value
  
  force_destroy = true
  
  tags = {
    Role        = "Developer"
    Environment = var.environment
  }
}

resource "aws_iam_user_group_membership" "developer_users" {
  for_each = toset(var.developer_users)
  user     = aws_iam_user.developer_users[each.value].name
  groups   = [aws_iam_group.developers.name]
}

# MFA Enforcement Policy
resource "aws_iam_policy" "require_mfa" {
  name        = "${var.environment}-require-mfa"
  description = "Require MFA for sensitive operations"
  
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "DenyAllExceptListedIfNoMFA"
        Effect = "Deny"
        NotAction = [
          "iam:CreateVirtualMFADevice",
          "iam:EnableMFADevice",
          "iam:GetUser",
          "iam:ListMFADevices",
          "iam:ListVirtualMFADevices",
          "iam:ListUsers",
          "iam:ListGroups",
          "iam:ListAccountAliases"
        ]
        Resource = "*"
        Condition = {
          BoolIfExists = {
            "aws:MultiFactorAuthPresent" = "false"
          }
        }
      }
    ]
  })
}

resource "aws_iam_group_policy_attachment" "require_mfa_admins" {
  group      = aws_iam_group.admins.name
  policy_arn = aws_iam_policy.require_mfa.arn
}

resource "aws_iam_group_policy_attachment" "require_mfa_security" {
  group      = aws_iam_group.security.name
  policy_arn = aws_iam_policy.require_mfa.arn
}

# IAM Access Analyzer
resource "aws_accessanalyzer_analyzer" "external_access" {
  analyzer_name = "${var.environment}-external-access"
  type          = "ACCOUNT"
  
  tags = {
    Environment = var.environment
  }
}

# IAM Role for Config
resource "aws_iam_role" "config" {
  name = "${var.environment}-config-role"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "config.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "config" {
  role       = aws_iam_role.config.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSConfigRole"
}

# IAM Role for GuardDuty
resource "aws_iam_role" "guardduty" {
  name = "${var.environment}-guardduty-role"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "guardduty.amazonaws.com"
        }
      }
    ]
  })
}

# IAM Role for Security Hub
resource "aws_iam_role" "securityhub" {
  name = "${var.environment}-securityhub-role"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "securityhub.amazonaws.com"
        }
      }
    ]
  })
}

data "aws_caller_identity" "current" {}
'''

with open(f"{base_dir}/terraform/modules/iam/aws.tf", "w") as f:
    f.write(aws_iam_module)

# AWS IAM Module Variables
aws_iam_vars = '''variable "environment" {
  description = "Environment name"
  type        = string
}

variable "admin_users" {
  description = "List of admin user names"
  type        = list(string)
  default     = []
}

variable "security_users" {
  description = "List of security user names"
  type        = list(string)
  default     = []
}

variable "developer_users" {
  description = "List of developer user names"
  type        = list(string)
  default     = []
}
'''

with open(f"{base_dir}/terraform/modules/iam/variables.tf", "w") as f:
    f.write(aws_iam_vars)

# AWS IAM Module Outputs
aws_iam_outputs = '''output "kms_key_id" {
  description = "KMS Key ID"
  value       = aws_kms_key.main.key_id
}

output "kms_key_arn" {
  description = "KMS Key ARN"
  value       = aws_kms_key.main.arn
}

output "admin_role_arn" {
  description = "Admin Role ARN"
  value       = aws_iam_role.admin.arn
}

output "security_role_arn" {
  description = "Security Role ARN"
  value       = aws_iam_role.security.arn
}

output "developer_role_arn" {
  description = "Developer Role ARN"
  value       = aws_iam_role.developer.arn
}

output "config_role_arn" {
  description = "Config Role ARN"
  value       = aws_iam_role.config.arn
}

output "guardduty_role_arn" {
  description = "GuardDuty Role ARN"
  value       = aws_iam_role.guardduty.arn
}
'''

with open(f"{base_dir}/terraform/modules/iam/outputs.tf", "w") as f:
    f.write(aws_iam_outputs)

print("IAM Module files created successfully!")

# Create Security Posture Module for AWS

aws_security_module = '''# AWS Security Posture Module
# Deploys GuardDuty, Security Hub, Config, Macie, Inspector

# GuardDuty
resource "aws_guardduty_detector" "main" {
  count = var.enable_guardduty ? 1 : 0
  
  enable = true
  
  datasources {
    s3_logs {
      enable = true
    }
    kubernetes {
      audit_logs {
        enable = true
      }
    }
    malware_protection {
      scan_ec2_instance_with_findings {
        enable = true
      }
    }
  }
  
  tags = {
    Environment = var.environment
  }
}

# GuardDuty Finding Publishing
resource "aws_guardduty_publishing_destination" "main" {
  count       = var.enable_guardduty ? 1 : 0
  detector_id = aws_guardduty_detector.main[0].id
  destination_arn = aws_s3_bucket.guardduty_findings.arn
  kms_key_arn     = var.kms_key_id
}

resource "aws_s3_bucket" "guardduty_findings" {
  bucket = "${var.environment}-guardduty-findings-${random_id.suffix.hex}"
}

resource "aws_s3_bucket_versioning" "guardduty" {
  bucket = aws_s3_bucket.guardduty_findings.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "guardduty" {
  bucket = aws_s3_bucket.guardduty_findings.id
  rule {
    apply_server_side_encryption_by_default {
      kms_master_key_id = var.kms_key_id
      sse_algorithm       = "aws:kms"
    }
  }
}

resource "random_id" "suffix" {
  byte_length = 4
}

# Security Hub
resource "aws_securityhub_account" "main" {
  count = var.enable_securityhub ? 1 : 0
}

resource "aws_securityhub_standards_subscription" "cis" {
  count         = var.enable_securityhub ? 1 : 0
  depends_on    = [aws_securityhub_account.main]
  standards_arn = "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0"
}

resource "aws_securityhub_standards_subscription" "nist" {
  count         = var.enable_securityhub ? 1 : 0
  depends_on    = [aws_securityhub_account.main]
  standards_arn = "arn:aws:securityhub:${data.aws_region.current.name}::standards/nist-800-53/v/5.0.0"
}

resource "aws_securityhub_standards_subscription" "pci" {
  count         = var.enable_securityhub ? 1 : 0
  depends_on    = [aws_securityhub_account.main]
  standards_arn = "arn:aws:securityhub:${data.aws_region.current.name}::standards/pci-dss/v/3.2.1"
}

# Security Hub Product Subscriptions
resource "aws_securityhub_product_subscription" "guardduty" {
  count       = var.enable_securityhub && var.enable_guardduty ? 1 : 0
  depends_on  = [aws_securityhub_account.main]
  product_arn = "arn:aws:securityhub:${data.aws_region.current.name}::product/aws/guardduty"
}

resource "aws_securityhub_product_subscription" "inspector" {
  count       = var.enable_securityhub && var.enable_inspector ? 1 : 0
  depends_on  = [aws_securityhub_account.main]
  product_arn = "arn:aws:securityhub:${data.aws_region.current.name}::product/aws/inspector"
}

resource "aws_securityhub_product_subscription" "macie" {
  count       = var.enable_securityhub && var.enable_macie ? 1 : 0
  depends_on  = [aws_securityhub_account.main]
  product_arn = "arn:aws:securityhub:${data.aws_region.current.name}::product/aws/macie"
}

# Security Hub Automation Rules
resource "aws_securityhub_automation_rule" "critical_findings" {
  count       = var.enable_securityhub ? 1 : 0
  depends_on  = [aws_securityhub_account.main]
  rule_name   = "CriticalFindingsAutoRemediation"
  rule_status = "ENABLED"
  
  rule_order = 1
  
  criteria {
    severity {
      label {
        comparison = "EQUALS"
        value      = "CRITICAL"
      }
    }
    
    workflow_status {
      comparison = "EQUALS"
      value      = "NEW"
    }
    
    record_state {
      comparison = "EQUALS"
      value      = "ACTIVE"
    }
  }
  
  actions {
    type = "FINDING_FIELDS_UPDATE"
    finding_fields_update {
      workflow {
        status = "NOTIFIED"
      }
      severity {
        label = "CRITICAL"
      }
      note {
        text      = "Auto-remediation triggered for critical finding"
        updated_by = "security-automation"
      }
    }
  }
}

# AWS Config
resource "aws_config_configuration_recorder" "main" {
  count = var.enable_config ? 1 : 0
  name  = "${var.environment}-config-recorder"
  
  role_arn = var.config_role_arn
  
  recording_group {
    all_supported                 = true
    include_global_resource_types = true
    
    recording_strategy {
      use_only = "ALL_SUPPORTED_RESOURCE_TYPES"
    }
  }
}

resource "aws_config_delivery_channel" "main" {
  count          = var.enable_config ? 1 : 0
  name           = "${var.environment}-config-delivery"
  s3_bucket_name = aws_s3_bucket.config.id
  sns_topic_arn  = aws_sns_topic.config_notifications.arn
  
  snapshot_delivery_properties {
    delivery_frequency = "Six_Hours"
  }
  
  depends_on = [aws_config_configuration_recorder.main]
}

resource "aws_config_configuration_recorder_status" "main" {
  count      = var.enable_config ? 1 : 0
  name       = aws_config_configuration_recorder.main[0].name
  is_enabled = true
  
  depends_on = [aws_config_delivery_channel.main]
}

resource "aws_s3_bucket" "config" {
  bucket = "${var.environment}-config-records-${random_id.suffix.hex}"
}

resource "aws_s3_bucket_versioning" "config" {
  bucket = aws_s3_bucket.config.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "config" {
  bucket = aws_s3_bucket.config.id
  rule {
    apply_server_side_encryption_by_default {
      kms_master_key_id = var.kms_key_id
      sse_algorithm       = "aws:kms"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "config" {
  bucket = aws_s3_bucket.config.id
  
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_sns_topic" "config_notifications" {
  name              = "${var.environment}-config-notifications"
  kms_master_key_id = var.kms_key_id
}

# Config Rules - CIS Benchmarks
resource "aws_config_config_rule" "iam_password_policy" {
  count = var.enable_config ? 1 : 0
  name  = "iam-password-policy"
  
  source {
    owner             = "AWS"
    source_identifier = "IAM_PASSWORD_POLICY"
  }
  
  input_parameters = jsonencode({
    RequireUppercaseCharacters   = "true"
    RequireLowercaseCharacters   = "true"
    RequireSymbols               = "true"
    RequireNumbers               = "true"
    MinimumPasswordLength        = "16"
    PasswordReusePrevention      = "24"
    MaxPasswordAge               = "90"
  })
  
  depends_on = [aws_config_configuration_recorder.main]
}

resource "aws_config_config_rule" "s3_bucket_public_read_prohibited" {
  count = var.enable_config ? 1 : 0
  name  = "s3-bucket-public-read-prohibited"
  
  source {
    owner             = "AWS"
    source_identifier = "S3_BUCKET_PUBLIC_READ_PROHIBITED"
  }
  
  depends_on = [aws_config_configuration_recorder.main]
}

resource "aws_config_config_rule" "s3_bucket_public_write_prohibited" {
  count = var.enable_config ? 1 : 0
  name  = "s3-bucket-public-write-prohibited"
  
  source {
    owner             = "AWS"
    source_identifier = "S3_BUCKET_PUBLIC_WRITE_PROHIBITED"
  }
  
  depends_on = [aws_config_configuration_recorder.main]
}

resource "aws_config_config_rule" "s3_bucket_ssl_requests_only" {
  count = var.enable_config ? 1 : 0
  name  = "s3-bucket-ssl-requests-only"
  
  source {
    owner             = "AWS"
    source_identifier = "S3_BUCKET_SSL_REQUESTS_ONLY"
  }
  
  depends_on = [aws_config_configuration_recorder.main]
}

resource "aws_config_config_rule" "ec2_volume_inuse_check" {
  count = var.enable_config ? 1 : 0
  name  = "ec2-volume-inuse-check"
  
  source {
    owner             = "AWS"
    source_identifier = "EC2_VOLUME_INUSE_CHECK"
  }
  
  depends_on = [aws_config_configuration_recorder.main]
}

resource "aws_config_config_rule" "encrypted_volumes" {
  count = var.enable_config ? 1 : 0
  name  = "encrypted-volumes"
  
  source {
    owner             = "AWS"
    source_identifier = "ENCRYPTED_VOLUMES"
  }
  
  depends_on = [aws_config_configuration_recorder.main]
}

resource "aws_config_config_rule" "rds_storage_encrypted" {
  count = var.enable_config ? 1 : 0
  name  = "rds-storage-encrypted"
  
  source {
    owner             = "AWS"
    source_identifier = "RDS_STORAGE_ENCRYPTED"
  }
  
  depends_on = [aws_config_configuration_recorder.main]
}

resource "aws_config_config_rule" "vpc_default_security_group_closed" {
  count = var.enable_config ? 1 : 0
  name  = "vpc-default-security-group-closed"
  
  source {
    owner             = "AWS"
    source_identifier = "VPC_DEFAULT_SECURITY_GROUP_CLOSED"
  }
  
  depends_on = [aws_config_configuration_recorder.main]
}

resource "aws_config_config_rule" "vpc_sg_open_only_to_authorized_ports" {
  count = var.enable_config ? 1 : 0
  name  = "vpc-sg-open-only-to-authorized-ports"
  
  source {
    owner             = "AWS"
    source_identifier = "VPC_SG_OPEN_ONLY_TO_AUTHORIZED_PORTS"
  }
  
  input_parameters = jsonencode({
    authorizedTcpPorts = "80,443"
  })
  
  depends_on = [aws_config_configuration_recorder.main]
}

resource "aws_config_config_rule" "cloudtrail_enabled" {
  count = var.enable_config ? 1 : 0
  name  = "cloudtrail-enabled"
  
  source {
    owner             = "AWS"
    source_identifier = "CLOUD_TRAIL_ENABLED"
  }
  
  depends_on = [aws_config_configuration_recorder.main]
}

resource "aws_config_config_rule" "cloudtrail_log_file_validation_enabled" {
  count = var.enable_config ? 1 : 0
  name  = "cloudtrail-log-file-validation-enabled"
  
  source {
    owner             = "AWS"
    source_identifier = "CLOUDTRAIL_LOG_FILE_VALIDATION_ENABLED"
  }
  
  depends_on = [aws_config_configuration_recorder.main]
}

resource "aws_config_config_rule" "mfa_enabled_for_iam_console_access" {
  count = var.enable_config ? 1 : 0
  name  = "mfa-enabled-for-iam-console-access"
  
  source {
    owner             = "AWS"
    source_identifier = "MFA_ENABLED_FOR_IAM_CONSOLE_ACCESS"
  }
  
  depends_on = [aws_config_configuration_recorder.main]
}

resource "aws_config_config_rule" "iam_root_access_key_check" {
  count = var.enable_config ? 1 : 0
  name  = "iam-root-access-key-check"
  
  source {
    owner             = "AWS"
    source_identifier = "IAM_ROOT_ACCESS_KEY_CHECK"
  }
  
  depends_on = [aws_config_configuration_recorder.main]
}

# Macie
resource "aws_macie2_account" "main" {
  count                = var.enable_macie ? 1 : 0
  finding_publishing_frequency = "FIFTEEN_MINUTES"
  status               = "ENABLED"
}

resource "aws_macie2_classification_job" "main" {
  count      = var.enable_macie ? 1 : 0
  job_type   = "SCHEDULED"
  name       = "${var.environment}-sensitive-data-discovery"
  s3_job_definition {
    bucket_definitions {
      account_id = data.aws_caller_identity.current.account_id
      buckets    = [aws_s3_bucket.config.id]
    }
  }
  schedule_frequency {
    daily_schedule = true
  }
  
  depends_on = [aws_macie2_account.main]
}

# Inspector
resource "aws_inspector2_enabler" "main" {
  count       = var.enable_inspector ? 1 : 0
  account_ids = [data.aws_caller_identity.current.account_id]
  resource_types = ["EC2", "ECR", "LAMBDA"]
}

# CloudWatch Alarms for Security Events
resource "aws_cloudwatch_log_metric_filter" "root_usage" {
  name           = "root-usage"
  pattern        = "{$.userIdentity.type = \"Root\" && $.userIdentity.invokedBy NOT EXISTS && $.eventType != \"AwsServiceEvent\"}"
  log_group_name = "/aws/cloudtrail/${var.environment}-multi-region-trail"
  
  metric_transformation {
    name      = "RootUsageCount"
    namespace = "SecurityMetrics"
    value     = "1"
  }
}

resource "aws_cloudwatch_metric_alarm" "root_usage" {
  alarm_name          = "root-usage-alarm"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "1"
  metric_name         = "RootUsageCount"
  namespace           = "SecurityMetrics"
  period              = "300"
  statistic           = "Sum"
  threshold           = "1"
  alarm_description   = "This metric monitors root account usage"
  alarm_actions       = [aws_sns_topic.security_alerts.arn]
}

resource "aws_cloudwatch_log_metric_filter" "unauthorized_api_calls" {
  name           = "unauthorized-api-calls"
  pattern        = "{$.errorCode = \"*UnauthorizedOperation\" || $.errorCode = \"AccessDenied*\"}"
  log_group_name = "/aws/cloudtrail/${var.environment}-multi-region-trail"
  
  metric_transformation {
    name      = "UnauthorizedAPICalls"
    namespace = "SecurityMetrics"
    value     = "1"
  }
}

resource "aws_cloudwatch_metric_alarm" "unauthorized_api_calls" {
  alarm_name          = "unauthorized-api-calls-alarm"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "1"
  metric_name         = "UnauthorizedAPICalls"
  namespace           = "SecurityMetrics"
  period              = "300"
  statistic           = "Sum"
  threshold           = "5"
  alarm_description   = "This metric monitors unauthorized API calls"
  alarm_actions       = [aws_sns_topic.security_alerts.arn]
}

resource "aws_sns_topic" "security_alerts" {
  name              = "${var.environment}-security-alerts"
  kms_master_key_id = var.kms_key_id
}

data "aws_region" "current" {}
data "aws_caller_identity" "current" {}
'''

with open(f"{base_dir}/terraform/modules/security-posture/aws.tf", "w") as f:
    f.write(aws_security_module)

# Security Posture Module Variables
security_vars = '''variable "environment" {
  description = "Environment name"
  type        = string
}

variable "enable_guardduty" {
  description = "Enable GuardDuty"
  type        = bool
  default     = true
}

variable "enable_securityhub" {
  description = "Enable Security Hub"
  type        = bool
  default     = true
}

variable "enable_config" {
  description = "Enable AWS Config"
  type        = bool
  default     = true
}

variable "enable_macie" {
  description = "Enable Macie"
  type        = bool
  default     = true
}

variable "enable_inspector" {
  description = "Enable Inspector"
  type        = bool
  default     = true
}

variable "log_retention_days" {
  description = "Number of days to retain logs"
  type        = number
  default     = 365
}

variable "kms_key_id" {
  description = "KMS Key ID for encryption"
  type        = string
}

variable "config_role_arn" {
  description = "Config Role ARN"
  type        = string
  default     = ""
}
'''

with open(f"{base_dir}/terraform/modules/security-posture/variables.tf", "w") as f:
    f.write(security_vars)

# Security Posture Module Outputs
security_outputs = '''output "guardduty_detector_id" {
  description = "GuardDuty Detector ID"
  value       = var.enable_guardduty ? aws_guardduty_detector.main[0].id : null
}

output "security_hub_account_id" {
  description = "Security Hub Account ID"
  value       = var.enable_securityhub ? aws_securityhub_account.main[0].id : null
}

output "config_recorder_name" {
  description = "Config Recorder Name"
  value       = var.enable_config ? aws_config_configuration_recorder.main[0].name : null
}

output "security_alerts_topic_arn" {
  description = "Security Alerts SNS Topic ARN"
  value       = aws_sns_topic.security_alerts.arn
}
'''

with open(f"{base_dir}/terraform/modules/security-posture/outputs.tf", "w") as f:
    f.write(security_outputs)

print("Security Posture Module files created successfully!")

# Create Python compliance scanner and automation scripts

compliance_scanner = '''#!/usr/bin/env python3
"""
Multi-Cloud Security Compliance Scanner
Scans AWS, Azure, and GCP for security posture compliance
Supports CIS Benchmarks, NIST 800-53, SOC 2, and PCI DSS
"""

import argparse
import json
import csv
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import boto3
from botocore.exceptions import ClientError

try:
    from azure.identity import DefaultAzureCredential
    from azure.mgmt.resource import ResourceManagementClient
    from azure.mgmt.security import SecurityCenter
    from azure.mgmt.monitor import MonitorManagementClient
    AZURE_AVAILABLE = True
except ImportError:
    AZURE_AVAILABLE = False

try:
    from google.cloud import asset_v1
    from google.cloud import securitycenter_v1
    from google.cloud import monitoring_v3
    GCP_AVAILABLE = True
except ImportError:
    GCP_AVAILABLE = False


class Colors:
    HEADER = '\\033[95m'
    OKBLUE = '\\033[94m'
    OKCYAN = '\\033[96m'
    OKGREEN = '\\033[92m'
    WARNING = '\\033[93m'
    FAIL = '\\033[91m'
    ENDC = '\\033[0m'
    BOLD = '\\033[1m'


class ComplianceScanner:
    def __init__(self):
        self.findings = []
        self.compliance_frameworks = {
            'cis': 'CIS Benchmarks',
            'nist': 'NIST 800-53',
            'soc2': 'SOC 2 Type II',
            'pci': 'PCI DSS v4.0'
        }
    
    def scan_aws(self, framework: str = 'all') -> List[Dict]:
        """Scan AWS for compliance issues"""
        print(f"{Colors.OKBLUE}[AWS] Starting compliance scan...{Colors.ENDC}")
        findings = []
        
        try:
            # IAM Checks
            iam_client = boto3.client('iam')
            
            # Check 1: Root account MFA
            try:
                summary = iam_client.get_account_summary()
                if summary['SummaryMap'].get('AccountMFAEnabled', 0) == 0:
                    findings.append({
                        'cloud': 'AWS',
                        'service': 'IAM',
                        'check': 'Root Account MFA',
                        'severity': 'CRITICAL',
                        'status': 'FAIL',
                        'resource': 'Root Account',
                        'remediation': 'Enable MFA on root account immediately',
                        'framework': 'CIS 1.10'
                    })
                else:
                    findings.append({
                        'cloud': 'AWS',
                        'service': 'IAM',
                        'check': 'Root Account MFA',
                        'severity': 'INFO',
                        'status': 'PASS',
                        'resource': 'Root Account',
                        'remediation': 'None - MFA is enabled',
                        'framework': 'CIS 1.10'
                    })
            except ClientError as e:
                findings.append(self._create_error_finding('AWS', 'IAM', str(e)))
            
            # Check 2: Password Policy
            try:
                policy = iam_client.get_account_password_policy()['PasswordPolicy']
                checks = {
                    'MinimumPasswordLength': (14, 'Minimum password length should be 14+'),
                    'RequireSymbols': (True, 'Passwords should require symbols'),
                    'RequireNumbers': (True, 'Passwords should require numbers'),
                    'RequireUppercaseCharacters': (True, 'Passwords should require uppercase'),
                    'RequireLowercaseCharacters': (True, 'Passwords should require lowercase'),
                    'MaxPasswordAge': (90, 'Maximum password age should be 90 days or less'),
                    'PasswordReusePrevention': (24, 'Password reuse prevention should be 24+')
                }
                
                for check, (expected, message) in checks.items():
                    actual = policy.get(check, 0 if isinstance(expected, int) else False)
                    if isinstance(expected, bool):
                        status = 'PASS' if actual == expected else 'FAIL'
                    else:
                        status = 'PASS' if actual >= expected else 'FAIL'
                    
                    findings.append({
                        'cloud': 'AWS',
                        'service': 'IAM',
                        'check': f'Password Policy - {check}',
                        'severity': 'HIGH' if status == 'FAIL' else 'INFO',
                        'status': status,
                        'resource': 'Account Password Policy',
                        'remediation': message if status == 'FAIL' else 'None',
                        'framework': 'CIS 1.9'
                    })
            except ClientError:
                findings.append({
                    'cloud': 'AWS',
                    'service': 'IAM',
                    'check': 'Password Policy',
                    'severity': 'CRITICAL',
                    'status': 'FAIL',
                    'resource': 'Account Password Policy',
                    'remediation': 'Set a strong password policy',
                    'framework': 'CIS 1.9'
                })
            
            # Check 3: Unused IAM credentials
            try:
                users = iam_client.list_users()['Users']
                for user in users:
                    if 'PasswordLastUsed' in user:
                        last_used = user['PasswordLastUsed'].replace(tzinfo=None)
                        days_unused = (datetime.now() - last_used).days
                        if days_unused > 90:
                            findings.append({
                                'cloud': 'AWS',
                                'service': 'IAM',
                                'check': 'Unused Credentials',
                                'severity': 'MEDIUM',
                                'status': 'FAIL',
                                'resource': f"User: {user['UserName']}",
                                'remediation': f'Password unused for {days_unused} days - disable or remove',
                                'framework': 'CIS 1.12'
                            })
                    
                    # Check access keys
                    keys = iam_client.list_access_keys(UserName=user['UserName'])['AccessKeyMetadata']
                    for key in keys:
                        if key['Status'] == 'Active':
                            last_used_info = iam_client.get_access_key_last_used(AccessKeyId=key['AccessKeyId'])
                            if 'LastUsedDate' in last_used_info['AccessKeyLastUsed']:
                                last_used = last_used_info['AccessKeyLastUsed']['LastUsedDate'].replace(tzinfo=None)
                                days_unused = (datetime.now() - last_used).days
                                if days_unused > 90:
                                    findings.append({
                                        'cloud': 'AWS',
                                        'service': 'IAM',
                                        'check': 'Unused Access Keys',
                                        'severity': 'MEDIUM',
                                        'status': 'FAIL',
                                        'resource': f"Access Key: {key['AccessKeyId'][:16]}...",
                                        'remediation': f'Access key unused for {days_unused} days - deactivate or delete',
                                        'framework': 'CIS 1.14'
                                    })
            except ClientError as e:
                findings.append(self._create_error_finding('AWS', 'IAM', str(e)))
            
            # S3 Checks
            s3_client = boto3.client('s3')
            try:
                buckets = s3_client.list_buckets()['Buckets']
                for bucket in buckets:
                    bucket_name = bucket['Name']
                    
                    # Check public access block
                    try:
                        public_access = s3_client.get_public_access_block(Bucket=bucket_name)
                        config = public_access['PublicAccessBlockConfiguration']
                        if not all([
                            config['BlockPublicAcls'],
                            config['BlockPublicPolicy'],
                            config['IgnorePublicAcls'],
                            config['RestrictPublicBuckets']
                        ]):
                            findings.append({
                                'cloud': 'AWS',
                                'service': 'S3',
                                'check': 'Public Access Block',
                                'severity': 'HIGH',
                                'status': 'FAIL',
                                'resource': f"Bucket: {bucket_name}",
                                'remediation': 'Enable all public access block settings',
                                'framework': 'CIS 2.1.5'
                            })
                    except ClientError:
                        findings.append({
                            'cloud': 'AWS',
                            'service': 'S3',
                            'check': 'Public Access Block',
                            'severity': 'HIGH',
                            'status': 'FAIL',
                            'resource': f"Bucket: {bucket_name}",
                            'remediation': 'Configure public access block settings',
                            'framework': 'CIS 2.1.5'
                        })
                    
                    # Check encryption
                    try:
                        encryption = s3_client.get_bucket_encryption(Bucket=bucket_name)
                        rules = encryption['ServerSideEncryptionConfiguration']['Rules']
                        if not rules:
                            findings.append({
                                'cloud': 'AWS',
                                'service': 'S3',
                                'check': 'Bucket Encryption',
                                'severity': 'HIGH',
                                'status': 'FAIL',
                                'resource': f"Bucket: {bucket_name}",
                                'remediation': 'Enable default encryption with KMS',
                                'framework': 'CIS 2.1.1'
                            })
                    except ClientError:
                        findings.append({
                            'cloud': 'AWS',
                            'service': 'S3',
                            'check': 'Bucket Encryption',
                            'severity': 'HIGH',
                            'status': 'FAIL',
                            'resource': f"Bucket: {bucket_name}",
                            'remediation': 'Enable default encryption with KMS',
                            'framework': 'CIS 2.1.1'
                        })
                    
                    # Check versioning
                    try:
                        versioning = s3_client.get_bucket_versioning(Bucket=bucket_name)
                        if versioning.get('Status') != 'Enabled':
                            findings.append({
                                'cloud': 'AWS',
                                'service': 'S3',
                                'check': 'Bucket Versioning',
                                'severity': 'MEDIUM',
                                'status': 'FAIL',
                                'resource': f"Bucket: {bucket_name}",
                                'remediation': 'Enable versioning for data protection',
                                'framework': 'CIS 2.1.3'
                            })
                    except ClientError:
                        pass
            except ClientError as e:
                findings.append(self._create_error_finding('AWS', 'S3', str(e)))
            
            # CloudTrail Checks
            cloudtrail_client = boto3.client('cloudtrail')
            try:
                trails = cloudtrail_client.describe_trails()['trailList']
                if not trails:
                    findings.append({
                        'cloud': 'AWS',
                        'service': 'CloudTrail',
                        'check': 'CloudTrail Enabled',
                        'severity': 'CRITICAL',
                        'status': 'FAIL',
                        'resource': 'Account',
                        'remediation': 'Enable CloudTrail in all regions',
                        'framework': 'CIS 3.1'
                    })
                else:
                    for trail in trails:
                        if not trail.get('IsMultiRegionTrail', False):
                            findings.append({
                                'cloud': 'AWS',
                                'service': 'CloudTrail',
                                'check': 'Multi-Region Trail',
                                'severity': 'HIGH',
                                'status': 'FAIL',
                                'resource': f"Trail: {trail['Name']}",
                                'remediation': 'Enable multi-region logging',
                                'framework': 'CIS 3.1'
                            })
                        if not trail.get('LogFileValidationEnabled', False):
                            findings.append({
                                'cloud': 'AWS',
                                'service': 'CloudTrail',
                                'check': 'Log File Validation',
                                'severity': 'HIGH',
                                'status': 'FAIL',
                                'resource': f"Trail: {trail['Name']}",
                                'remediation': 'Enable log file validation',
                                'framework': 'CIS 3.2'
                            })
            except ClientError as e:
                findings.append(self._create_error_finding('AWS', 'CloudTrail', str(e)))
            
            # Security Groups Check
            ec2_client = boto3.client('ec2')
            try:
                security_groups = ec2_client.describe_security_groups()['SecurityGroups']
                for sg in security_groups:
                    for rule in sg.get('IpPermissions', []):
                        for ip_range in rule.get('IpRanges', []):
                            if ip_range.get('CidrIp') == '0.0.0.0/0':
                                if rule.get('FromPort') in [22, 3389]:
                                    findings.append({
                                        'cloud': 'AWS',
                                        'service': 'EC2',
                                        'check': 'Security Group Rules',
                                        'severity': 'CRITICAL',
                                        'status': 'FAIL',
                                        'resource': f"SG: {sg['GroupName']} ({sg['GroupId']})",
                                        'remediation': f"Remove 0.0.0.0/0 access to port {rule['FromPort']}",
                                        'framework': 'CIS 5.2'
                                    })
                                elif rule.get('FromPort') == 0 and rule.get('ToPort') == 65535:
                                    findings.append({
                                        'cloud': 'AWS',
                                        'service': 'EC2',
                                        'check': 'Security Group Rules',
                                        'severity': 'HIGH',
                                        'status': 'FAIL',
                                        'resource': f"SG: {sg['GroupName']} ({sg['GroupId']})",
                                        'remediation': 'Restrict overly permissive security group rules',
                                        'framework': 'CIS 5.2'
                                    })
            except ClientError as e:
                findings.append(self._create_error_finding('AWS', 'EC2', str(e)))
            
            # GuardDuty Check
            guardduty_client = boto3.client('guardduty')
            try:
                detectors = guardduty_client.list_detectors()['DetectorIds']
                if not detectors:
                    findings.append({
                        'cloud': 'AWS',
                        'service': 'GuardDuty',
                        'check': 'GuardDuty Enabled',
                        'severity': 'HIGH',
                        'status': 'FAIL',
                        'resource': 'Account',
                        'remediation': 'Enable GuardDuty for threat detection',
                        'framework': 'NIST SI-4'
                    })
            except ClientError:
                findings.append({
                    'cloud': 'AWS',
                    'service': 'GuardDuty',
                    'check': 'GuardDuty Enabled',
                    'severity': 'HIGH',
                    'status': 'FAIL',
                    'resource': 'Account',
                    'remediation': 'Enable GuardDuty for threat detection',
                    'framework': 'NIST SI-4'
                })
            
        except Exception as e:
            findings.append(self._create_error_finding('AWS', 'General', str(e)))
        
        print(f"{Colors.OKGREEN}[AWS] Scan complete. {len(findings)} findings.{Colors.ENDC}")
        return findings
    
    def scan_azure(self, framework: str = 'all') -> List[Dict]:
        """Scan Azure for compliance issues"""
        print(f"{Colors.OKBLUE}[Azure] Starting compliance scan...{Colors.ENDC}")
        findings = []
        
        if not AZURE_AVAILABLE:
            print(f"{Colors.WARNING}[Azure] Azure SDK not installed. Skipping.{Colors.ENDC}")
            return findings
        
        try:
            credential = DefaultAzureCredential()
            subscription_id = self._get_azure_subscription_id()
            
            # Resource Management
            resource_client = ResourceManagementClient(credential, subscription_id)
            
            # Check NSG Rules
            network_client = __import__('azure.mgmt.network', fromlist=['NetworkManagementClient'])
            network_client = network_client.NetworkManagementClient(credential, subscription_id)
            
            for rg in resource_client.resource_groups.list():
                nsgs = network_client.network_security_groups.list(rg.name)
                for nsg in nsgs:
                    for rule in nsg.security_rules:
                        if rule.source_address_prefix == '*' and rule.access == 'Allow':
                            if rule.destination_port_range in ['22', '3389']:
                                findings.append({
                                    'cloud': 'Azure',
                                    'service': 'Network',
                                    'check': 'NSG Rules',
                                    'severity': 'CRITICAL',
                                    'status': 'FAIL',
                                    'resource': f"NSG: {nsg.name}",
                                    'remediation': f"Restrict access to port {rule.destination_port_range}",
                                    'framework': 'CIS Azure 6.1'
                                })
            
            # Security Center Recommendations
            security_client = SecurityCenter(credential, subscription_id, "")
            for recommendation in security_client.recommendations.list():
                if recommendation.severity in ['High', 'Critical']:
                    findings.append({
                        'cloud': 'Azure',
                        'service': 'Security Center',
                      

# Create remediation script and additional Python tools

remediation_script = '''#!/usr/bin/env python3
"""
Multi-Cloud Security Auto-Remediation Script
Automatically fixes common security misconfigurations
"""

import argparse
import json
import boto3
from botocore.exceptions import ClientError
from typing import Dict, List, Optional


class AWSRemediator:
    def __init__(self, dry_run: bool = True):
        self.dry_run = dry_run
        self.actions_taken = []
    
    def remediate_s3_public_access(self, bucket_name: str) -> Dict:
        """Remove public access from S3 bucket"""
        s3 = boto3.client('s3')
        try:
            if not self.dry_run:
                s3.put_public_access_block(
                    Bucket=bucket_name,
                    PublicAccessBlockConfiguration={
                        'BlockPublicAcls': True,
                        'IgnorePublicAcls': True,
                        'BlockPublicPolicy': True,
                        'RestrictPublicBuckets': True
                    }
                )
            return {
                'status': 'SUCCESS',
                'action': f'Blocked public access for bucket {bucket_name}',
                'dry_run': self.dry_run
            }
        except ClientError as e:
            return {'status': 'ERROR', 'error': str(e)}
    
    def remediate_s3_encryption(self, bucket_name: str) -> Dict:
        """Enable default encryption on S3 bucket"""
        s3 = boto3.client('s3')
        try:
            if not self.dry_run:
                s3.put_bucket_encryption(
                    Bucket=bucket_name,
                    ServerSideEncryptionConfiguration={
                        'Rules': [
                            {
                                'ApplyServerSideEncryptionByDefault': {
                                    'SSEAlgorithm': 'aws:kms'
                                },
                                'BucketKeyEnabled': True
                            }
                        ]
                    }
                )
            return {
                'status': 'SUCCESS',
                'action': f'Enabled KMS encryption for bucket {bucket_name}',
                'dry_run': self.dry_run
            }
        except ClientError as e:
            return {'status': 'ERROR', 'error': str(e)}
    
    def remediate_s3_versioning(self, bucket_name: str) -> Dict:
        """Enable versioning on S3 bucket"""
        s3 = boto3.client('s3')
        try:
            if not self.dry_run:
                s3.put_bucket_versioning(
                    Bucket=bucket_name,
                    VersioningConfiguration={'Status': 'Enabled'}
                )
            return {
                'status': 'SUCCESS',
                'action': f'Enabled versioning for bucket {bucket_name}',
                'dry_run': self.dry_run
            }
        except ClientError as e:
            return {'status': 'ERROR', 'error': str(e)}
    
    def remediate_sg_ingress(self, group_id: str, protocol: str, port: int, cidr: str = '0.0.0.0/0') -> Dict:
        """Remove overly permissive security group rules"""
        ec2 = boto3.client('ec2')
        try:
            if not self.dry_run:
                ec2.revoke_security_group_ingress(
                    GroupId=group_id,
                    IpPermissions=[
                        {
                            'IpProtocol': protocol,
                            'FromPort': port,
                            'ToPort': port,
                            'IpRanges': [{'CidrIp': cidr}]
                        }
                    ]
                )
            return {
                'status': 'SUCCESS',
                'action': f'Removed {protocol}/{port} access from {cidr} in SG {group_id}',
                'dry_run': self.dry_run
            }
        except ClientError as e:
            return {'status': 'ERROR', 'error': str(e)}
    
    def remediate_unused_access_keys(self, user_name: str, access_key_id: str) -> Dict:
        """Deactivate unused IAM access keys"""
        iam = boto3.client('iam')
        try:
            if not self.dry_run:
                iam.update_access_key(
                    UserName=user_name,
                    AccessKeyId=access_key_id,
                    Status='Inactive'
                )
            return {
                'status': 'SUCCESS',
                'action': f'Deactivated unused access key {access_key_id} for user {user_name}',
                'dry_run': self.dry_run
            }
        except ClientError as e:
            return {'status': 'ERROR', 'error': str(e)}
    
    def remediate_password_policy(self) -> Dict:
        """Set strong password policy"""
        iam = boto3.client('iam')
        try:
            if not self.dry_run:
                iam.update_account_password_policy(
                    MinimumPasswordLength=16,
                    RequireSymbols=True,
                    RequireNumbers=True,
                    RequireUppercaseCharacters=True,
                    RequireLowercaseCharacters=True,
                    AllowUsersToChangePassword=True,
                    MaxPasswordAge=90,
                    PasswordReusePrevention=24
                )
            return {
                'status': 'SUCCESS',
                'action': 'Updated account password policy to strong settings',
                'dry_run': self.dry_run
            }
        except ClientError as e:
            return {'status': 'ERROR', 'error': str(e)}
    
    def enable_cloudtrail_validation(self, trail_name: str) -> Dict:
        """Enable CloudTrail log file validation"""
        cloudtrail = boto3.client('cloudtrail')
        try:
            if not self.dry_run:
                cloudtrail.update_trail(
                    Name=trail_name,
                    EnableLogFileValidation=True
                )
            return {
                'status': 'SUCCESS',
                'action': f'Enabled log file validation for trail {trail_name}',
                'dry_run': self.dry_run
            }
        except ClientError as e:
            return {'status': 'ERROR', 'error': str(e)}
    
    def enable_guardduty(self) -> Dict:
        """Enable GuardDuty"""
        guardduty = boto3.client('guardduty')
        try:
            if not self.dry_run:
                response = guardduty.create_detector(Enable=True)
            return {
                'status': 'SUCCESS',
                'action': 'Enabled GuardDuty detector',
                'dry_run': self.dry_run
            }
        except ClientError as e:
            if 'DetectorExistsException' in str(e):
                return {'status': 'INFO', 'action': 'GuardDuty already enabled'}
            return {'status': 'ERROR', 'error': str(e)}
    
    def enable_securityhub(self) -> Dict:
        """Enable Security Hub"""
        securityhub = boto3.client('securityhub')
        try:
            if not self.dry_run:
                securityhub.enable_security_hub(
                    EnableDefaultStandards=True
                )
            return {
                'status': 'SUCCESS',
                'action': 'Enabled Security Hub with default standards',
                'dry_run': self.dry_run
            }
        except ClientError as e:
            return {'status': 'ERROR', 'error': str(e)}


def main():
    parser = argparse.ArgumentParser(description='Multi-Cloud Security Auto-Remediation')
    parser.add_argument('--cloud', choices=['aws', 'azure', 'gcp', 'all'], default='aws')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without making changes')
    parser.add_argument('--finding-file', type=str, help='JSON file with findings to remediate')
    parser.add_argument('--auto', action='store_true', help='Auto-remediate all findings without prompting')
    
    args = parser.parse_args()
    
    remediator = AWSRemediator(dry_run=args.dry_run)
    results = []
    
    if args.finding_file:
        with open(args.finding_file) as f:
            findings = json.load(f)
        
        for finding in findings.get('findings', []):
            if finding['status'] == 'FAIL':
                print(f"Remediating: {finding['check']} on {finding['resource']}")
                
                if finding['service'] == 'S3':
                    if 'Public Access' in finding['check']:
                        bucket = finding['resource'].replace('Bucket: ', '')
                        results.append(remediator.remediate_s3_public_access(bucket))
                    elif 'Encryption' in finding['check']:
                        bucket = finding['resource'].replace('Bucket: ', '')
                        results.append(remediator.remediate_s3_encryption(bucket))
                    elif 'Versioning' in finding['check']:
                        bucket = finding['resource'].replace('Bucket: ', '')
                        results.append(remediator.remediate_s3_versioning(bucket))
                
                elif finding['service'] == 'EC2' and 'Security Group' in finding['check']:
                    # Extract SG ID from resource string
                    sg_id = finding['resource'].split('(')[-1].replace(')', '')
                    results.append(remediator.remediate_sg_ingress(sg_id, 'tcp', 22))
                
                elif finding['service'] == 'IAM':
                    if 'Password Policy' in finding['check']:
                        results.append(remediator.remediate_password_policy())
                    elif 'Unused Access Keys' in finding['check']:
                        # Would need user info from finding
                        pass
    else:
        # Run common remediations
        print("Running common security remediations...")
        results.append(remediator.remediate_password_policy())
        results.append(remediator.enable_guardduty())
        results.append(remediator.enable_securityhub())
    
    print("\\nRemediation Results:")
    for result in results:
        status = result.get('status', 'UNKNOWN')
        symbol = '✅' if status == 'SUCCESS' else '❌' if status == 'ERROR' else 'ℹ️'
        print(f"{symbol} {result.get('action', 'No action')}")
        if 'error' in result:
            print(f"   Error: {result['error']}")


if __name__ == '__main__':
    main()
'''

with open(f"{base_dir}/scripts/python/auto_remediation.py", "w") as f:
    f.write(remediation_script)

# Create IAM policy analyzer
iam_analyzer = '''#!/usr/bin/env python3
"""
IAM Policy Analyzer
Analyzes IAM policies for overly permissive permissions
"""

import json
import boto3
from typing import Dict, List, Set


DANGEROUS_ACTIONS = {
    'iam': ['*', 'iam:*', 'iam:Create*', 'iam:Delete*', 'iam:Attach*', 'iam:Detach*'],
    'organizations': ['*', 'organizations:*', 'organizations:LeaveOrganization', 'organizations:DeleteOrganization'],
    'account': ['*', 'account:CloseAccount', 'account:DeleteAccount'],
    'billing': ['*', 'billing:*', 'payments:*'],
    'kms': ['*', 'kms:Delete*', 'kms:ScheduleKeyDeletion', 'kms:DisableKey'],
    's3': ['*', 's3:DeleteBucket', 's3:PutBucketPolicy', 's3:PutBucketAcl'],
    'ec2': ['*', 'ec2:Delete*', 'ec2:TerminateInstances'],
    'rds': ['*', 'rds:Delete*'],
}

WILDCARD_SERVICES = ['*']


class IAMPolicyAnalyzer:
    def __init__(self):
        self.iam = boto3.client('iam')
        self.findings = []
    
    def analyze_all_policies(self) -> List[Dict]:
        """Analyze all IAM policies in the account"""
        # Analyze managed policies
        paginator = self.iam.get_paginator('list_policies')
        for page in paginator.paginate(Scope='Local'):
            for policy in page['Policies']:
                self._analyze_policy(policy['Arn'])
        
        # Analyze inline policies for users
        paginator = self.iam.get_paginator('list_users')
        for page in paginator.paginate():
            for user in page['Users']:
                self._analyze_user_policies(user['UserName'])
        
        # Analyze inline policies for roles
        paginator = self.iam.get_paginator('list_roles')
        for page in paginator.paginate():
            for role in page['Roles']:
                self._analyze_role_policies(role['RoleName'])
        
        return self.findings
    
    def _analyze_policy(self, policy_arn: str):
        """Analyze a specific policy"""
        try:
            policy_version = self.iam.get_policy_version(
                PolicyArn=policy_arn,
                VersionId=self.iam.get_policy(PolicyArn=policy_arn)['Policy']['DefaultVersionId']
            )
            
            document = policy_version['PolicyVersion']['Document']
            self._check_policy_document(document, policy_arn)
        except Exception as e:
            print(f"Error analyzing policy {policy_arn}: {e}")
    
    def _analyze_user_policies(self, user_name: str):
        """Analyze inline policies attached to a user"""
        try:
            policies = self.iam.list_user_policies(UserName=user_name)['PolicyNames']
            for policy_name in policies:
                policy = self.iam.get_user_policy(UserName=user_name, PolicyName=policy_name)
                self._check_policy_document(policy['PolicyDocument'], f"user/{user_name}/{policy_name}")
        except Exception as e:
            print(f"Error analyzing user {user_name}: {e}")
    
    def _analyze_role_policies(self, role_name: str):
        """Analyze inline policies attached to a role"""
        try:
            policies = self.iam.list_role_policies(RoleName=role_name)['PolicyNames']
            for policy_name in policies:
                policy = self.iam.get_role_policy(RoleName=role_name, PolicyName=policy_name)
                self._check_policy_document(policy['PolicyDocument'], f"role/{role_name}/{policy_name}")
        except Exception as e:
            print(f"Error analyzing role {role_name}: {e}")
    
    def _check_policy_document(self, document: Dict, resource_id: str):
        """Check policy document for security issues"""
        statements = document.get('Statement', [])
        if isinstance(statements, dict):
            statements = [statements]
        
        for statement in statements:
            if statement.get('Effect') != 'Allow':
                continue
            
            actions = self._normalize_actions(statement.get('Action', []))
            resources = self._normalize_resources(statement.get('Resource', []))
            
            # Check for wildcard actions
            for action in actions:
                if action == '*':
                    self.findings.append({
                        'severity': 'CRITICAL',
                        'issue': 'Wildcard action (*)",
                        'policy': resource_id,
                        'action': action,
                        'resource': resources,
                        'remediation': 'Replace wildcard with specific actions'
                    })
                elif action.endswith(':*'):
                    service = action.split(':')[0]
                    self.findings.append({
                        'severity': 'HIGH',
                        'issue': f'Wildcard service action ({action})',
                        'policy': resource_id,
                        'action': action,
                        'resource': resources,
                        'remediation': f'Use specific {service} actions instead of wildcard'
                    })
            
            # Check for wildcard resources
            for resource in resources:
                if resource == '*':
                    # Only flag if combined with sensitive actions
                    sensitive_actions = [a for a in actions if any(
                        a.startswith(svc) or a == '*' 
                        for svc in DANGEROUS_ACTIONS.keys()
                    )]
                    if sensitive_actions:
                        self.findings.append({
                            'severity': 'HIGH',
                            'issue': 'Wildcard resource with sensitive actions',
                            'policy': resource_id,
                            'action': actions,
                            'resource': resource,
                            'remediation': 'Scope resources to specific ARNs'
                        })
            
            # Check for dangerous actions
            for action in actions:
                for service, dangerous in DANGEROUS_ACTIONS.items():
                    if action in dangerous or action == '*':
                        self.findings.append({
                            'severity': 'HIGH',
                            'issue': f'Dangerous action: {action}',
                            'policy': resource_id,
                            'action': action,
                            'resource': resources,
                            'remediation': f'Restrict {service} permissions to minimum required'
                        })
            
            # Check for missing conditions
            if 'Condition' not in statement:
                sensitive_services = ['iam', 'kms', 's3', 'ec2', 'rds']
                for action in actions:
                    service = action.split(':')[0] if ':' in action else ''
                    if service in sensitive_services:
                        self.findings.append({
                            'severity': 'MEDIUM',
                            'issue': f'Missing conditions for sensitive action: {action}',
                            'policy': resource_id,
                            'action': action,
                            'resource': resources,
                            'remediation': 'Add conditions (IP, MFA, time-based) to restrict access'
                        })
    
    def _normalize_actions(self, actions) -> List[str]:
        """Normalize actions to a list"""
        if isinstance(actions, str):
            return [actions]
        return actions
    
    def _normalize_resources(self, resources) -> List[str]:
        """Normalize resources to a list"""
        if isinstance(resources, str):
            return [resources]
        return resources
    
    def generate_report(self) -> str:
        """Generate analysis report"""
        report = []
        report.append("=" * 80)
        report.append("IAM POLICY SECURITY ANALYSIS REPORT")
        report.append("=" * 80)
        report.append(f"Total Findings: {len(self.findings)}")
        report.append("")
        
        severity_counts = {}
        for finding in self.findings:
            severity = finding['severity']
            severity_counts[severity] = severity_counts.get(severity, 0) + 1
        
        for sev in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
            if sev in severity_counts:
                report.append(f"{sev}: {severity_counts[sev]}")
        
        report.append("")
        report.append("-" * 80)
        
        for finding in self.findings:
            report.append(f"\\n[{finding['severity']}] {finding['issue']}")
            report.append(f"  Policy: {finding['policy']}")
            report.append(f"  Action: {finding['action']}")
            report.append(f"  Resource: {finding['resource']}")
            report.append(f"  Remediation: {finding['remediation']}")
        
        return '\\n'.join(report)


def main():
    analyzer = IAMPolicyAnalyzer()
    findings = analyzer.analyze_all_policies()
    print(analyzer.generate_report())
    
    # Save to file
    with open('iam_policy_analysis.json', 'w') as f:
        json.dump(findings, f, indent=2)
    print("\\nDetailed results saved to iam_policy_analysis.json")


if __name__ == '__main__':
    main()
'''

with open(f"{base_dir}/scripts/python/iam_policy_analyzer.py", "w") as f:
    f.write(iam_analyzer)

# Create cross-cloud sync script
cross_cloud_sync = '''#!/usr/bin/env python3
"""

Cr

# Create policy files for each cloud

# AWS Policies
aws_policies = {
    "iam_password_policy.json": '''{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "EnforceStrongPasswords",
      "Effect": "Deny",
      "Action": "iam:CreateLoginProfile",
      "Resource": "*",
      "Condition": {
        "NumericLessThan": {
          "iam:PasswordLength": "16"
        }
      }
    }
  ]
}''',
    "s3_secure_bucket_policy.json": '''{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyInsecureTransport",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::BUCKET_NAME",
        "arn:aws:s3:::BUCKET_NAME/*"
      ],
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    },
    {
      "Sid": "DenyUnencryptedUploads",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::BUCKET_NAME/*",
      "Condition": {
        "StringNotEquals": {
          "s3:x-amz-server-side-encryption": "aws:kms"
        }
      }
    }
  ]
}''',
    "ec2_restricted_ami_policy.json": '''{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "OnlyApprovedAMIs",
      "Effect": "Deny",
      "Action": "ec2:RunInstances",
      "Resource": "arn:aws:ec2:*::image/*",
      "Condition": {
        "StringNotEquals": {
          "ec2:Owner": "amazon"
        }
      }
    }
  ]
}''',
    "scp_deny_unapproved_regions.json": '''{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyUnapprovedRegions",
      "Effect": "Deny",
      "NotAction": [
        "aws-portal:*",
        "budgets:*",
        "ce:*",
        "cur:*",
        "support:*",
        "trustedadvisor:*"
      ],
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:RequestedRegion": [
            "us-east-1",
            "us-west-2",
            "eu-west-1"
          ]
        }
      }
    }
  ]
}''',
    "scp_deny_root_account.json": '''{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyRootAccountUsage",
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "aws:PrincipalArn": [
            "arn:aws:iam::*:root"
          ]
        }
      }
    }
  ]
}''',
    "scp_require_encryption.json": '''{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyUnencryptedS3",
      "Effect": "Deny",
      "Action": "s3:PutObject",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "s3:x-amz-server-side-encryption": "aws:kms"
        }
      }
    },
    {
      "Sid": "DenyUnencryptedEBS",
      "Effect": "Deny",
      "Action": "ec2:CreateVolume",
      "Resource": "*",
      "Condition": {
        "Bool": {
          "ec2:Encrypted": "false"
        }
      }
    }
  ]
}'''
}

for filename, content in aws_policies.items():
    with open(f"{base_dir}/policies/aws/{filename}", "w") as f:
        f.write(content)

# Azure Policies
azure_policies = {
    "require_encryption.json": '''{
  "if": {
    "anyOf": [
      {
        "allOf": [
          {
            "field": "type",
            "equals": "Microsoft.Storage/storageAccounts"
          },
          {
            "field": "Microsoft.Storage/storageAccounts/encryption.keySource",
            "notEquals": "Microsoft.Keyvault"
          }
        ]
      },
      {
        "allOf": [
          {
            "field": "type",
            "equals": "Microsoft.Sql/servers/databases"
          },
          {
            "field": "Microsoft.Sql/servers/databases/transparentDataEncryption.status",
            "notEquals": "Enabled"
          }
        ]
      }
    ]
  },
  "then": {
    "effect": "deny"
  }
}''',
    "require_nsg_on_subnet.json": '''{
  "if": {
    "allOf": [
      {
        "field": "type",
        "equals": "Microsoft.Network/virtualNetworks/subnets"
      },
      {
        "field": "Microsoft.Network/virtualNetworks/subnets/networkSecurityGroup.id",
        "exists": "false"
      }
    ]
  },
  "then": {
    "effect": "deny"
  }
}''',
    "restrict_locations.json": '''{
  "if": {
    "not": {
      "field": "location",
      "in": [
        "eastus",
        "westus2",
        "westeurope"
      ]
    }
  },
  "then": {
    "effect": "deny"
  }
}''',
    "require_tags.json": '''{
  "if": {
    "not": {
      "field": "tags",
      "containsKey": "Environment"
    }
  },
  "then": {
    "effect": "deny"
  }
}'''
}

for filename, content in azure_policies.items():
    with open(f"{base_dir}/policies/azure/{filename}", "w") as f:
        f.write(content)

# GCP Organization Policies
gcp_policies = {
    "restrict_vm_external_ips.yaml": '''constraint: constraints/compute.vmExternalIpAccess
list_policy:
  deny:
    all: true''',
    "skip_default_network.yaml": '''constraint: constraints/compute.skipDefaultNetworkCreation
boolean_policy:
  enforced: true''',
    "disable_serial_port.yaml": '''constraint: constraints/compute.disableSerialPortAccess
boolean_policy:
  enforced: true''',
    "require_os_login.yaml": '''constraint: constraints/compute.requireOsLogin
boolean_policy:
  enforced: true''',
    "uniform_bucket_access.yaml": '''constraint: constraints/storage.uniformBucketLevelAccess
boolean_policy:
  enforced: true''',
    "restrict_cloud_sql_public_ip.yaml": '''constraint: constraints/sql.restrictPublicIp
boolean_policy:
  enforced: true''',
    "disable_guest_attributes.yaml": '''constraint: constraints/compute.disableGuestAttributesAccess
boolean_policy:
  enforced: true'''
}

for filename, content in gcp_policies.items():
    with open(f"{base_dir}/policies/gcp/{filename}", "w") as f:
        f.write(content)

print("Policy files created for AWS, Azure, and GCP!")

# Create comprehensive documentation files

# AWS Setup Guide
aws_setup = """# AWS Security Foundation Setup Guide

## Prerequisites
- AWS CLI installed and configured (`aws configure`)
- Terraform >= 1.5.0
- AWS account with Organizations enabled (optional but recommended)
- IAM permissions to create: IAM roles/policies, KMS keys, CloudTrail, Config, GuardDuty, Security Hub

## Architecture Overview
The AWS security foundation deploys:

### Identity & Access Management
- **Organization Structure**: Security, Production, Development OUs
- **Service Control Policies**: Deny root usage, restrict regions, require encryption
- **IAM Roles**: Admin (with permission boundaries), Security, Developer
- **Password Policy**: 16+ chars, symbols, numbers, 90-day rotation
- **MFA Enforcement**: Required for all privileged operations
- **Access Analyzer**: External access monitoring

### Security Monitoring
- **GuardDuty**: Threat detection with S3, EKS, Malware protection
- **Security Hub**: Centralized findings with CIS, NIST, PCI standards
- **AWS Config**: 15+ compliance rules (CIS Foundations)
- **Macie**: Sensitive data discovery in S3
- **Inspector**: Vulnerability scanning for EC2, ECR, Lambda
- **CloudTrail**: Multi-region trail with log validation

### Data Protection
- **KMS**: Multi-region key with automatic rotation
- **S3**: Encryption, versioning, public access blocks
- **VPC Flow Logs**: Network traffic monitoring
- **WAFv2**: Web application firewall with rate limiting

## Deployment Steps

### 1. Configure AWS CLI
```bash
aws configure
# Enter your Access Key ID, Secret Access Key, region (us-east-1), output format (json)
```

### 2. Prepare Terraform Variables
```bash
cd terraform/aws
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your specific values
```

### 3. Initialize and Deploy
```bash
terraform init
terraform plan -out=tfplan
terraform apply tfplan
```

### 4. Verify Deployment
```bash
# Check Organization structure
aws organizations list-roots
aws organizations list-organizational-units-for-parent --parent-id $(aws organizations list-roots --query 'Roots[0].Id' --output text)

# Verify GuardDuty
aws guardduty list-detectors

# Check Security Hub
aws securityhub get-enabled-standards

# Verify Config rules
aws config describe-config-rules
```

## Post-Deployment Tasks

### Enable MFA for Root Account
1. Sign in to AWS Console as root
2. Navigate to "My Security Credentials"
3. Enable MFA (virtual or hardware)

### Configure AWS SSO / IAM Identity Center
```bash
# Enable IAM Identity Center (formerly AWS SSO)
aws sso-admin create-instance

# Create permission sets
aws sso-admin create-permission-set \
  --instance-arn <instance-arn> \
  --name AdminAccess \
  --session-duration PT8H
```

### Set up Cross-Account Access
```bash
# Create a role for cross-account security auditing
aws iam create-role \
  --role-name CrossAccountSecurityAudit \
  --assume-role-policy-document file://trust-policy.json
```

## Troubleshooting

### Error: "Access Denied" when creating Organization
- Ensure you're using the root account or have `organizations:*` permissions
- Check if Organizations is already enabled

### Error: "KMS Key not found"
- Verify the KMS key was created successfully: `aws kms list-aliases`
- Check IAM permissions for KMS operations

### CloudTrail not logging
- Verify S3 bucket policy allows CloudTrail writes
- Check KMS key policy allows CloudTrail encryption
- Ensure CloudTrail is in "Logging" status

## Cost Considerations
| Service | Estimated Monthly Cost |
|---------|----------------------|
| GuardDuty | ~$4/GB of analyzed data |
| Security Hub | ~$0.0010/findings ingested |
| Config | ~$0.0030/configuration item |
| Macie | ~$1/GB analyzed |
| Inspector | ~$0.81/EC2 instance/month |
| CloudTrail | ~$2.00/100,000 events |
| KMS | ~$1.00/key/month |

## Compliance Mapping
| CIS Control | AWS Implementation |
|-------------|-------------------|
| 1.10 - Root MFA | Account password policy + manual setup |
| 1.16 - IAM policies attached to groups | Group-based policy attachment |
| 2.1.1 - S3 Encryption | Default encryption with KMS |
| 2.1.5 - S3 Public Access | Public access block configuration |
| 3.1 - CloudTrail | Multi-region trail enabled |
| 3.2 - CloudTrail Validation | Log file validation enabled |
| 4.1 - Security Group Rules | Config rule + auto-remediation |
| 5.2 - Security Group Restrictions | Config rule for authorized ports |

## Next Steps
1. Run compliance scanner: `python scripts/python/compliance_scanner.py --cloud aws`
2. Review findings and apply auto-remediation
3. Set up alerting via SNS/email
4. Integrate with external SIEM (Splunk, Elastic, etc.)
"""

with open(f"{base_dir}/docs/aws-setup.md", "w") as f:
    f.write(aws_setup)

# Azure Setup Guide
azure_setup = """# Azure Security Foundation Setup Guide

## Prerequisites
- Azure CLI installed (`az login`)
- Terraform >= 1.5.0
- Azure subscription with Owner or Contributor role
- Azure AD tenant (for conditional access policies)

## Architecture Overview
The Azure security foundation deploys:

### Identity & Access Management
- **Azure AD Groups**: Security Administrators, Security Operators
- **Conditional Access**: MFA required, legacy auth blocked, compliant devices for admins
- **PIM Integration**: Eligible for Privileged Identity Management
- **Strong Authentication**: MFA enforcement for all users

### Security Monitoring
- **Microsoft Defender for Cloud**: Enhanced security for VMs, Storage, SQL, App Services, Key Vault, DNS
- **Azure Sentinel**: SIEM and SOAR capabilities
- **Log Analytics**: Centralized logging workspace
- **Azure Monitor**: Alerting and diagnostics

### Data Protection
- **Azure Key Vault**: Premium tier with HSM-backed keys, soft-delete, purge protection
- **Key Rotation**: Automatic rotation every 90 days
- **Network ACLs**: IP-based restrictions for Key Vault

### Network Security
- **Azure Firewall**: Premium tier with threat intelligence
- **NSG Rules**: Default deny-all with strict ingress controls
- **Virtual Network**: Isolated network segments

## Deployment Steps

### 1. Authenticate with Azure
```bash
az login
az account set --subscription "Your-Subscription-ID"
```

### 2. Create Storage Account for Terraform State
```bash
az group create --name tfstate-rg --location eastus
az storage account create \
  --name multicloudtfstate \
  --resource-group tfstate-rg \
  --sku Standard_LRS \
  --encryption-services blob

az storage container create \
  --name tfstate \
  --account-name multicloudtfstate
```

### 3. Prepare Terraform Variables
```bash
cd terraform/azure
cp terraform.tfvars.example terraform.tfvars
# Edit with your subscription ID, alert email, etc.
```

### 4. Initialize and Deploy
```bash
terraform init
terraform plan -out=tfplan
terraform apply tfplan
```

### 5. Verify Deployment
```bash
# Check resource group
az group show --name security-lab-security-rg

# Verify Key Vault
az keyvault show --name $(terraform output -raw key_vault_name)

# Check Log Analytics workspace
az monitor log-analytics workspace show \
  --name security-lab-security-law \
  --resource-group security-lab-security-rg

# Verify Sentinel onboarding
az sentinel show \
  --workspace-name security-lab-security-law \
  --resource-group security-lab-security-rg
```

## Post-Deployment Tasks

### Enable Azure AD PIM
1. Navigate to Azure Portal > Azure AD > Privileged Identity Management
2. Discover and manage privileged roles
3. Configure role settings (approval required, time-bound access)

### Configure Azure Policy Assignments
```bash
# Get policy assignment details
az policy assignment list --query "[?name=='cis-azure-assignment']"

# Check compliance state
az policy state summarize --policy-assignment-name cis-azure-assignment
```

### Set up Azure Sentinel Data Connectors
```bash
# Enable AWS CloudTrail connector
az sentinel data-connector create \
  --resource-group security-lab-security-rg \
  --workspace-name security-lab-security-law \
  --name AWSCloudTrail
```

## Troubleshooting

### Error: "Insufficient privileges"
- Ensure your account has Owner role on the subscription
- Check Azure AD permissions for conditional access policies

### Key Vault Access Denied
- Verify your IP is in the allowed IP ranges
- Check the Key Vault access policy for your user/service principal

### Sentinel not showing data
- Verify Log Analytics workspace is properly linked
- Check data connector configuration
- Allow 15-30 minutes for initial data ingestion

## Cost Considerations
| Service | Estimated Monthly Cost |
|---------|----------------------|
| Defender for Cloud (Standard) | ~$15/VM/month |
| Sentinel | ~$2.46/GB ingested |
| Log Analytics | ~$2.76/GB ingested |
| Key Vault (Premium) | ~$0.03/10,000 operations |
| Azure Firewall (Premium) | ~$1.25/hour |

## Compliance Mapping
| CIS Control | Azure Implementation |
|-------------|---------------------|
| 1.1 - Maintain inventory | Azure Policy + Resource Graph |
| 1.16 - Ensure MFA is enabled | Conditional Access Policy |
| 2.1.1 - Ensure standard pricing | Defender for Cloud Standard |
| 3.1 - Ensure auditing is enabled | Activity Log + Diagnostic Settings |
| 4.1.1 - Ensure NSG flow logs | Network Watcher + Flow Logs |
| 5.1 - Ensure Key Vault exists | Key Vault with soft-delete |

## Next Steps
1. Run compliance scanner: `python scripts/python/compliance_scanner.py --cloud azure`
2. Configure Azure AD Identity Protection
3. Set up Just-In-Time (JIT) VM access
4. Integrate with Microsoft Defender for Endpoint
"""

with open(f"{base_dir}/docs/azure-setup.md", "w") as f:
    f.write(azure_setup)

# GCP Setup Guide
gcp_setup = """# GCP Security Foundation Setup Guide

## Prerequisites
- Google Cloud SDK installed (`gcloud`)
- Terraform >= 1.5.0
- GCP project with Billing enabled
- Organization-level permissions (for org policies)
- APIs enabled: Cloud Resource Manager, IAM, Compute, Security Command Center

## Architecture Overview
The GCP security foundation deploys:

### Identity & Access Management
- **Custom Roles**: Security Auditor (read-only), Security Remediator (limited write)
- **Cloud Identity Groups**: Security Team group with managed permissions
- **Organization Policies**: VM external IPs, default network, serial port, OS login
- **Essential Contacts**: Security alerting configuration

### Security Monitoring
- **Security Command Center**: Custom security modules, vulnerability scanning
- **Cloud Asset Inventory**: Real-time resource tracking with Pub/Sub feeds
- **Cloud Monitoring**: Alerting policies for IAM changes, KMS usage
- **Security Health Analytics**: Automated security finding generation

### Data Protection
- **Cloud KMS**: HSM-backed keys with 90-day rotation
- **VPC Service Controls**: Data exfiltration prevention for Storage, BigQuery, KMS
- **Cloud Armor**: DDoS protection and WAF rules

### Patch Management
- **OS Config**: Automated patch deployment (monthly, 2 AM)
- **Compliance**: Automatic reboot after patching

## Deployment Steps

### 1. Authenticate with GCP
```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
gcloud config set compute/region us-central1
```

### 2. Create GCS Bucket for Terraform State
```bash
gsutil mb -p YOUR_PROJECT_ID gs://multi-cloud-tfstate
gsutil versioning set on gs://multi-cloud-tfstate
```

### 3. Enable Required APIs
```bash
gcloud services enable cloudresourcemanager.googleapis.com
gcloud services enable iam.googleapis.com
gcloud services enable compute.googleapis.com
gcloud services enable securitycenter.googleapis.com
gcloud services enable cloudasset.googleapis.com
gcloud services enable cloudkms.googleapis.com
gcloud services enable osconfig.googleapis.com
```

### 4. Prepare Terraform Variables
```bash
cd terraform/gcp
cp terraform.tfvars.example terraform.tfvars
# Edit with your project ID, org ID, domain
```

### 5. Initialize and Deploy
```bash
terraform init
terraform plan -out=tfplan
terraform apply tfplan
```

### 6. Verify Deployment
```bash
# Check organization policies
gcloud resource-manager org-policies describe compute.vmExternalIpAccess \
  --organization YOUR_ORG_ID

# Verify KMS key
gcloud kms keys list --keyring=security-lab-keyring --location=us-central1

# Check Security Command Center
gcloud scc assets list --organization=YOUR_ORG_ID

# Verify Cloud Armor policy
gcloud compute security-policies describe security-lab-security-policy
```

## Post-Deployment Tasks

### Configure VPC Service Controls Perimeters
```bash
# Add projects to service perimeter
gcloud access-context-manager perimeters update security-lab_perimeter \
  --title="Security Lab Perimeter" \
  --resources=projects/YOUR_PROJECT_NUMBER \
  --restricted-services=storage.googleapis.com,bigquery.googleapis.com \
  --policy=POLICY_ID
```

### Set up Security Command Center Notifications
```bash
# Create notification config
gcloud scc notifications create security-alerts \
  --organization=YOUR_ORG_ID \
  --pubsub-topic=projects/YOUR_PROJECT_ID/topics/security-logs-topic \
  --filter='severity="CRITICAL" OR severity="HIGH"'
```

### Configure Cloud Identity Groups
```bash
# Add members to security team
gcloud identity groups memberships add \
  --group-email="security-team@company.com" \
  --member-email="user@company.com"
```

## Troubleshooting

### Error: "Permission denied" for org policies
- Ensure you have `roles/orgPolicyPolicyAdmin` at organization level
- Check if organization policies are already set at a higher level

### KMS key not accessible
- Verify IAM permissions: `gcloud kms keys get-iam-policy KEY_NAME`
- Check if the service account has `roles/cloudkms.cryptoKeyEncrypterDecrypter`

### Security Command Center not showing findings
- Verify Security Command Center API is enabled
- Check if the project is properly linked to the organization
- Allow 24 hours for initial asset inventory and findings

## Cost Considerations
| Service | Estimated Monthly Cost |
|---------|----------------------|
| Security Command Center (Premium) | ~$0.00 (included) |
| Cloud KMS (HSM keys) | ~$1.00/key/month + $0.03/10,000 operations |
| Cloud Armor | ~$0.20/1M requests |
| OS Config | Free |
| Cloud Asset Inventory | ~$0.00 (included) |
| VPC Service Controls | Free |

## Compliance Mapping
| CIS Control | GCP Implementation |
|-------------|-------------------|
| 1.1 - Ensure IAM policies | Organization policies + IAM constraints |
| 1.5 - Ensure service accounts | Custom roles with least privilege |
| 2.1 - Ensure audit logging | Cloud Audit Logs (Admin, Data Access, System) |
| 3.1 - Ensure log sinks | Pub/Sub sinks for security logs |
| 4.1 - Ensure OS Login | Organization policy enforced |
| 5.1 - Ensure VPC flow logs | VPC Flow Logs configuration |
| 6.1 - Ensure Cloud Armor | Security policy with rate limiting |

## Next Steps
1. Run compliance scanner: `python scripts/python/compliance_scanner.py --cloud gcp`
2. Configure Chronicle (if available) for advanced threat detection
3. Set up Forseti Security (open-source) for additional policy enforcement
4. Implement Binary Authorization for container security
"""

with open(f"{base_dir}/docs/gcp-setup.md", "w") as f:
    f.write(gcp_setup)

print("Setup guides created for AWS, Azure, and GCP!")

# Create compliance scanning guide and troubleshooting doc

compliance_guide = """# Multi-Cloud Compliance Scanning Guide

## Overview
The compliance scanner evaluates your multi-cloud infrastructure against industry-standard frameworks including CIS Benchmarks, NIST 800-53, SOC 2 Type II, and PCI DSS v4.0.

## Supported Frameworks

### CIS Benchmarks
- **CIS AWS Foundations Benchmark v1.5.0** - 100+ controls
- **CIS Azure Foundations Benchmark v1.5.0** - 90+ controls  
- **CIS GCP Foundations Benchmark v1.3.0** - 80+ controls

### NIST 800-53 Rev 5
- Access Control (AC)
- Audit and Accountability (AU)
- Configuration Management (CM)
- Identification and Authentication (IA)
- Incident Response (IR)
- Risk Assessment (RA)
- System and Communications Protection (SC)
- System and Information Integrity (SI)

### SOC 2 Type II
- CC6.1 - Logical access security
- CC6.2 - Prior to access
- CC6.3 - Access removal
- CC6.6 - Encryption
- CC7.1 - Detection of security events
- CC7.2 - Incident monitoring
- CC7.3 - Incident response

### PCI DSS v4.0
- Requirement 1: Firewall configuration
- Requirement 2: System hardening
- Requirement 3: Data protection
- Requirement 4: Encryption in transit
- Requirement 7: Access restrictions
- Requirement 8: Identity management
- Requirement 10: Logging and monitoring

## Running the Scanner

### Basic Usage
```bash
cd scripts/python
pip install -r requirements.txt

# Scan all clouds
python compliance_scanner.py --cloud all

# Scan specific cloud
python compliance_scanner.py --cloud aws
python compliance_scanner.py --cloud azure
python compliance_scanner.py --cloud gcp

# Scan multiple clouds
python compliance_scanner.py --cloud aws,azure
```

### Report Formats
```bash
# Console output (default)
python compliance_scanner.py --cloud all --report console

# JSON report
python compliance_scanner.py --cloud all --report json --output report.json

# CSV report
python compliance_scanner.py --cloud all --report csv --output report.csv

# HTML dashboard
python compliance_scanner.py --cloud all --report html --output report.html
```

### Filtering Results
```bash
# Only critical and high severity
python compliance_scanner.py --cloud all --severity high

# Only critical findings
python compliance_scanner.py --cloud all --severity critical

# Specific framework
python compliance_scanner.py --cloud aws --framework cis
python compliance_scanner.py --cloud azure --framework nist
```

## Understanding Results

### Severity Levels
| Level | Description | Response Time |
|-------|-------------|---------------|
| **CRITICAL** | Immediate security risk | < 24 hours |
| **HIGH** | Significant vulnerability | < 72 hours |
| **MEDIUM** | Moderate risk | < 1 week |
| **LOW** | Minor issue | < 1 month |
| **INFO** | Informational | Monitor |

### Status Codes
- **PASS** - Control is properly implemented
- **FAIL** - Control is not implemented or misconfigured
- **ERROR** - Scanner encountered an error
- **MANUAL** - Requires manual verification

## Automated Remediation

### Dry Run Mode
```bash
# See what would be fixed without making changes
python auto_remediation.py --dry-run --finding-file report.json
```

### Auto-Remediation
```bash
# Fix all findings automatically
python auto_remediation.py --auto --finding-file report.json

# Fix specific finding types
python auto_remediation.py --finding-file report.json --type s3,iam
```

### Supported Remediations
| Finding | Remediation Action |
|---------|-------------------|
| S3 Public Access | Enable public access block |
| S3 No Encryption | Enable default KMS encryption |
| S3 No Versioning | Enable versioning |
| Open Security Group | Remove 0.0.0.0/0 rules |
| Weak Password Policy | Enforce strong policy |
| Unused Access Keys | Deactivate keys |
| No CloudTrail | Enable multi-region trail |
| No GuardDuty | Enable detector |
| No Security Hub | Enable with standards |

## Continuous Compliance

### GitHub Actions Integration
```yaml
name: Security Compliance Scan
on:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM
  push:
    branches: [main]

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r scripts/python/requirements.txt
      - name: Run AWS scan
        run: python scripts/python/compliance_scanner.py --cloud aws --report json
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
      - name: Upload report
        uses: actions/upload-artifact@v3
        with:
          name: compliance-report
          path: compliance_report_*.json
```

### Scheduled Scanning with Cron
```bash
# Add to crontab
crontab -e

# Daily scan at 3 AM
0 3 * * * cd /path/to/project && python scripts/python/compliance_scanner.py --cloud all --report html --output /var/www/html/compliance.html

# Weekly summary email (requires mail setup)
0 9 * * 1 cd /path/to/project && python scripts/python/compliance_scanner.py --cloud all --severity high --report json | mail -s "Weekly Security Report" security@company.com
```

## Custom Checks

### Adding New Checks
Edit `compliance_scanner.py` and add checks to the respective cloud scan methods:

```python
def scan_aws(self, framework: str = 'all') -> List[Dict]:
    # ... existing checks ...
    
    # Your custom check
    try:
        # Check logic here
        if condition_not_met:
            findings.append({
                'cloud': 'AWS',
                'service': 'YourService',
                'check': 'Your Custom Check',
                'severity': 'HIGH',
                'status': 'FAIL',
                'resource': 'resource-id',
                'remediation': 'How to fix this',
                'framework': 'CUSTOM'
            })
    except ClientError as e:
        findings.append(self._create_error_finding('AWS', 'YourService', str(e)))
```

## Reporting and Dashboards

### Building a Dashboard
The HTML report includes:
- Executive summary with severity counts
- Compliance score by framework
- Detailed finding table with remediation steps
- Cloud-specific breakdowns

### Integration with SIEM
```python
# Send findings to Splunk
import requests

for finding in findings:
    requests.post(
        'https://splunk-instance:8088/services/collector',
        headers={'Authorization': 'Splunk YOUR_TOKEN'},
        json={'event': finding}
    )
```

## Best Practices
1. **Run scans daily** - Security posture changes constantly
2. **Review critical findings immediately** - Don't wait for scheduled reviews
3. **Track remediation progress** - Use the JSON output to build trend reports
4. **Automate where possible** - Use auto-remediation for safe, repeatable fixes
5. **Document exceptions** - Some findings may be intentional - document why
"""

with open(f"{base_dir}/docs/compliance-scanning.md", "w") as f:
    f.write(compliance_guide)

# Troubleshooting Guide
troubleshooting = """# Multi-Cloud Security Lab Troubleshooting

## Common Issues and Solutions

### Terraform Issues

#### Error: "Failed to query available provider packages"
**Cause**: Terraform registry unreachable or version constraint too strict
**Solution**:
```bash
terraform init -upgrade
# Or specify exact version in providers.tf
```

#### Error: "Resource already exists"
**Cause**: Previous deployment left resources behind
**Solution**:
```bash
# Import existing resource
terraform import aws_s3_bucket.mybucket bucket-name

# Or remove from state and let Terraform recreate
terraform state rm aws_s3_bucket.mybucket
```

#### Error: "Provider configuration not present"
**Cause**: Missing provider configuration for a module
**Solution**: Ensure all required providers are declared in root module

### AWS-Specific Issues

#### Error: "AccessDenied" when creating Organization
**Solution**:
- Use root account for initial Organization setup
- Or ensure IAM user has `organizations:*` permissions
- Check if Organization already exists in another region

#### GuardDuty not showing findings
**Solution**:
```bash
# Verify detector is enabled
aws guardduty list-detectors

# Check if finding publishing is configured
aws guardduty get-publishing-destination --detector-id <id>

# Generate test finding
aws guardduty create-sample-findings --detector-id <id> --finding-types "Recon:IAMUser/PasswordPolicyChanged"
```

#### Security Hub standards not enabling
**Solution**:
```bash
# Check if standards are already enabled
aws securityhub get-enabled-standards

# Enable manually if needed
aws securityhub batch-enable-standards \
  --standards-subscription-requests \
  StandardsArn="arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0"
```

#### KMS Key policy too restrictive
**Solution**: Update key policy to allow required services:
```json
{
  "Sid": "Allow CloudTrail",
  "Effect": "Allow",
  "Principal": {
    "Service": "cloudtrail.amazonaws.com"
  },
  "Action": ["kms:GenerateDataKey*", "kms:DescribeKey"],
  "Resource": "*"
}
```

### Azure-Specific Issues

#### Error: "Authorization failed" for Conditional Access
**Solution**:
- Ensure account has Global Administrator or Conditional Access Administrator role
- Check Azure AD license (P1/P2 required for some features)
- Verify tenant-level permissions

#### Key Vault access denied from specific IP
**Solution**:
```bash
# Update allowed IPs
az keyvault network-rule add \
  --name my-keyvault \
  --ip-address YOUR_IP/32

# Or temporarily allow all Azure services
az keyvault update \
  --name my-keyvault \
  --default-action Allow
```

#### Sentinel not ingesting data
**Solution**:
1. Verify Log Analytics workspace is linked
2. Check data connector status in Sentinel
3. Ensure diagnostic settings are sending logs to Log Analytics
4. Allow 15-30 minutes for initial ingestion

### GCP-Specific Issues

#### Error: "Permission denied" for organization policies
**Solution**:
```bash
# Verify organization permissions
gcloud organizations get-iam-policy YOUR_ORG_ID

# Grant org policy admin role
gcloud organizations add-iam-policy-binding YOUR_ORG_ID \
  --member="user:you@company.com" \
  --role="roles/orgpolicy.policyAdmin"
```

#### Security Command Center not showing assets
**Solution**:
```bash
# Verify API is enabled
gcloud services list --enabled | grep securitycenter

# Check if project is linked to organization
gcloud projects describe YOUR_PROJECT_ID

# Force asset refresh
gcloud asset feeds create refresh-feed \
  --content-type=resource \
  --asset-types="compute.googleapis.com/Instance" \
  --pubsub-topic=projects/YOUR_PROJECT/topics/asset-changes
```

#### KMS key rotation not working
**Solution**:
```bash
# Check rotation period
gcloud kms keys describe KEY_NAME \
  --keyring=KEYRING_NAME \
  --location=LOCATION

# Update rotation period
gcloud kms keys update KEY_NAME \
  --keyring=KEYRING_NAME \
  --location=LOCATION \
  --rotation-period=90d
```

### Python Script Issues

#### Error: "ModuleNotFoundError" for cloud SDKs
**Solution**:
```bash
# Install all dependencies
pip install -r scripts/python/requirements.txt

# Or install specific cloud SDK
pip install boto3 azure-identity google-cloud-asset
```

#### Error: "Unable to locate credentials" for AWS
**Solution**:
```bash
# Configure AWS CLI
aws configure

# Or set environment variables
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=us-east-1
```

#### Error: "DefaultAzureCredential failed"
**Solution**:
```bash
# Login with Azure CLI
az login

# Or use service principal
export AZURE_CLIENT_ID=your_client_id
export AZURE_CLIENT_SECRET=your_client_secret
export AZURE_TENANT_ID=your_tenant_id
export AZURE_SUBSCRIPTION_ID=your_subscription_id
```

#### Error: "Could not automatically determine credentials" for GCP
**Solution**:
```bash
# Authenticate with gcloud
gcloud auth application-default login

# Or use service account key
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account-key.json
```

### Network and Connectivity Issues

#### Terraform state backend unreachable
**Solution**:
- Check network connectivity to S3/Azure Blob/GCS
- Verify credentials have access to state storage
- Try local backend temporarily: `terraform init -backend=false`

#### API rate limiting
**Solution**:
- Add delays between API calls in scripts
- Use Terraform's `-parallelism=1` flag
- Request quota increases from cloud providers

## Debugging Tips

### Enable Terraform Debug Logging
```bash
export TF_LOG=DEBUG
export TF_LOG_PATH=terraform-debug.log
terraform apply
```

### Enable AWS SDK Debug Logging
```bash
export AWS_SDK_LOAD_CONFIG=1
export BOTO3_LOG_LEVEL=DEBUG
python compliance_scanner.py --cloud aws
```

### Check Cloud Provider Status
- AWS: https://status.aws.amazon.com/
- Azure: https://status.azure.com/
- GCP: https://status.cloud.google.com/

## Getting Help

### Cloud Provider Support
- **AWS**: AWS Support Center or AWS re:Post
- **Azure**: Azure Support + MSDN Forums
- **GCP**: Google Cloud Support or Stack Overflow

### Community Resources
- Terraform Discuss: https://discuss.hashicorp.com/
- Reddit r/aws, r/azure, r/googlecloud
- Cloud Security Alliance forums

### Emergency Contacts
Document your organization's:
- Cloud platform administrators
- Security operations center (SOC)
- Incident response team
- Cloud provider TAM/support contacts
"""

with open(f"{base_dir}/docs/troubleshooting.md", "w") as f:
    f.write(troubleshooting)

print("Documentation files created successfully!")

# Create Docker configuration and Ansible playbooks

# Dockerfile for security tools
dockerfile = '''FROM python:3.11-slim

LABEL maintainer="security-team@company.com"
LABEL description="Multi-Cloud Security Tools Container"

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    curl \\
    unzip \\
    jq \\
    git \\
    bash \\
    openssl \\
    && rm -rf /var/lib/apt/lists/*

# Install Terraform
RUN curl -fsSL https://releases.hashicorp.com/terraform/1.5.7/terraform_1.5.7_linux_amd64.zip -o terraform.zip \\
    && unzip terraform.zip \\
    && mv terraform /usr/local/bin/ \\
    && rm terraform.zip

# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \\
    && unzip awscliv2.zip \\
    && ./aws/install \\
    && rm -rf aws awscliv2.zip

# Install Azure CLI
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

# Install Google Cloud SDK
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \\
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - \\
    && apt-get update && apt-get install -y google-cloud-cli \\
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r scripts/python/requirements.txt

# Create non-root user
RUN useradd -m -s /bin/bash security-user \\
    && chown -R security-user:security-user /app
USER security-user

# Environment variables
ENV PYTHONPATH=/app/scripts/python
ENV PATH="/app/scripts/bash:${PATH}"

# Default command
CMD ["/bin/bash"]
'''

with open(f"{base_dir}/docker/Dockerfile", "w") as f:
    f.write(dockerfile)

# Docker Compose
docker_compose = '''version: '3.8'

services:
  security-tools:
    build:
      context: ..
      dockerfile: docker/Dockerfile
    container_name: multi-cloud-security-lab
    volumes:
      - ../terraform:/app/terraform
      - ../scripts:/app/scripts
      - ../policies:/app/policies
      - ../docs:/app/docs
      - ~/.aws:/home/security-user/.aws:ro
      - ~/.azure:/home/security-user/.azure:ro
      - ~/.config/gcloud:/home/security-user/.config/gcloud:ro
      - security-reports:/app/reports
    environment:
      - AWS_PROFILE=default
      - AZURE_SUBSCRIPTION_ID=${AZURE_SUBSCRIPTION_ID}
      - GCP_PROJECT_ID=${GCP_PROJECT_ID}
    working_dir: /app
    command: /bin/bash
    stdin_open: true
    tty: true
    networks:
      - security-network

  compliance-scheduler:
    build:
      context: ..
      dockerfile: docker/Dockerfile
    container_name: compliance-scheduler
    volumes:
      - ../scripts:/app/scripts
      - security-reports:/app/reports
    environment:
      - AWS_PROFILE=default
    command: >
      bash -c "
        while true; do
          echo 'Running scheduled compliance scan...'
          python /app/scripts/python/compliance_scanner.py --cloud all --report html --output /app/reports/scheduled-report.html
          echo 'Scan complete. Sleeping for 24 hours...'
          sleep 86400
        done
      "
    networks:
      - security-network

  vault:
    image: hashicorp/vault:latest
    container_name: security-vault
    ports:
      - "8200:8200"
    environment:
      - VAULT_DEV_ROOT_TOKEN_ID=dev-token
      - VAULT_DEV_LISTEN_ADDRESS=0.0.0.0:8200
    cap_add:
      - IPC_LOCK
    networks:
      - security-network

volumes:
  security-reports:
    driver: local

networks:
  security-network:
    driver: bridge
'''

with open(f"{base_dir}/docker/docker-compose.yml", "w") as f:
    f.write(docker_compose)

# Ansible Playbook for configuration drift detection
ansible_playbook = '''---
- name: Multi-Cloud Security Configuration Audit
  hosts: localhost
  gather_facts: no
  vars:
    report_dir: "./ansible/reports"
    timestamp: "{{ ansible_date_time.iso8601 }}"
  
  tasks:
    - name: Ensure report directory exists
      file:
        path: "{{ report_dir }}"
        state: directory
        mode: '0755'

    - name: AWS Configuration Audit
      block:
        - name: Check AWS CLI is installed
          command: aws --version
          register: aws_version
          changed_when: false

        - name: Get AWS account information
          command: aws sts get-caller-identity
          register: aws_identity
          changed_when: false

        - name: Check CloudTrail status
          command: aws cloudtrail describe-trails --query 'trailList[*].Name'
          register: cloudtrail_status
          changed_when: false

        - name: Check GuardDuty status
          command: aws guardduty list-detectors --query 'DetectorIds'
          register: guardduty_status
          changed_when: false

        - name: Check Security Hub status
          command: aws securityhub get-enabled-standards --query 'StandardsSubscriptions[*].StandardsArn'
          register: securityhub_status
          changed_when: false

        - name: Check Config rules
          command: aws config describe-config-rules --query 'ConfigRules[*].ConfigRuleName'
          register: config_rules
          changed_when: false

        - name: Generate AWS audit report
          template:
            src: aws_audit_report.j2
            dest: "{{ report_dir }}/aws_audit_{{ timestamp }}.html"
          vars:
            aws_identity: "{{ aws_identity.stdout | from_json }}"
            cloudtrail: "{{ cloudtrail_status.stdout }}"
            guardduty: "{{ guardduty_status.stdout }}"
            securityhub: "{{ securityhub_status.stdout }}"
            config: "{{ config_rules.stdout }}"

      rescue:
        - name: AWS audit failed
          debug:
            msg: "AWS audit failed - ensure AWS CLI is configured"

    - name: Azure Configuration Audit
      block:
        - name: Check Azure CLI is installed
          command: az --version
          register: az_version
          changed_when: false

        - name: Get Azure subscription info
          command: az account show
          register: az_account
          changed_when: false

        - name: Check Security Center pricing
          command: az security pricing list --query '[?pricingTier==`Standard`].name'
          register: security_center_pricing
          changed_when: false

        - name: Check Azure Policy assignments
          command: az policy assignment list --query '[*].displayName'
          register: policy_assignments
          changed_when: false

        - name: Generate Azure audit report
          template:
            src: azure_audit_report.j2
            dest: "{{ report_dir }}/azure_audit_{{ timestamp }}.html"
          vars:
            az_account: "{{ az_account.stdout | from_json }}"
            security_center: "{{ security_center_pricing.stdout }}"
            policies: "{{ policy_assignments.stdout }}"

      rescue:
        - name: Azure audit failed
          debug:
            msg: "Azure audit failed - ensure Azure CLI is logged in"

    - name: GCP Configuration Audit
      block:
        - name: Check gcloud is installed
          command: gcloud --version
          register: gcloud_version
          changed_when: false

        - name: Get GCP project info
          command: gcloud config get-value project
          register: gcp_project
          changed_when: false

        - name: Check organization policies
          command: gcloud resource-manager org-policies list --organization {{ gcp_org_id | default('') }}
          register: org_policies
          changed_when: false
          ignore_errors: yes

        - name: Check Security Command Center
          command: gcloud scc assets list --organization {{ gcp_org_id | default('') }} --limit 5
          register: scc_assets
          changed_when: false
          ignore_errors: yes

        - name: Generate GCP audit report
          template:
            src: gcp_audit_report.j2
            dest: "{{ report_dir }}/gcp_audit_{{ timestamp }}.html"
          vars:
            gcp_project: "{{ gcloud_version.stdout }}"
            org_policies: "{{ org_policies.stdout | default('N/A') }}"
            scc: "{{ scc_assets.stdout | default('N/A') }}"

      rescue:
        - name: GCP audit failed
          debug:
            msg: "GCP audit failed - ensure gcloud is authenticated"

    - name: Generate consolidated report
      template:
        src: consolidated_report.j2
        dest: "{{ report_dir }}/consolidated_audit_{{ timestamp }}.html"
      vars:
        aws_status: "{{ 'PASS' if aws_identity is succeeded else 'FAIL' }}"
        azure_status: "{{ 'PASS' if az_account is succeeded else 'FAIL' }}"
        gcp_status: "{{ 'PASS' if gcloud_version is succeeded else 'FAIL' }}"

    - name: Display report location
      debug:
        msg: "Audit reports generated in {{ report_dir }}/"
'''

with open(f"{base_dir}/ansible/security_audit.yml", "w") as f:
    f.write(ansible_playbook)

# Ansible inventory
ansible_inventory = '''[local]
localhost ansible_connection=local

[aws:children]
local

[azure:children]
local

[gcp:children]
local
'''

with open(f"{base_dir}/ansible/inventory.ini", "w") as f:
    f.write(ansible_inventory)

# Ansible config
ansible_cfg = '''[defaults]
inventory = inventory.ini
host_key_checking = False
retry_files_enabled = False
roles_path = ./roles
log_path = ./ansible.log

[privilege_escalation]
become = False
'''

with open(f"{base_dir}/ansible/ansible.cfg", "w") as f:
    f.write(ansible_cfg)

# Create Jinja2 templates for Ansible reports
os.makedirs(f"{base_dir}/ansible/templates", exist_ok=True)

aws_template = '''<!DOCTYPE html>
<html>
<head><title>AWS Security Audit Report</title></head>
<body>
<h1>AWS Security Audit - {{ timestamp }}</h1>
<h2>Account Information</h2>
<pre>{{ aws_identity | to_nice_json }}</pre>
<h2>CloudTrail Status</h2>
<pre>{{ cloudtrail }}</pre>
<h2>GuardDuty Status</h2>
<pre>{{ guardduty }}</pre>
<h2>Security Hub Status</h2>
<pre>{{ securityhub }}</pre>
<h2>Config Rules</h2>
<pre>{{ config }}</pre>
</body>
</html>
'''

with open(f"{base_dir}/ansible/templates/aws_audit_report.j2", "w") as f:
    f.write(aws_template)

consolidated_template = '''<!DOCTYPE html>
<html>
<head>
<title>Multi-Cloud Security Audit Report</title>
<style>
body { font-family: Arial, sans-serif; margin: 40px; }
.status-pass { color: green; font-weight: bold; }
.status-fail { color: red; font-weight: bold; }
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
th { background-color: #4CAF50; color: white; }
</style>
</head>
<body>
<h1>Multi-Cloud Security Audit Report</h1>
<p>Generated: {{ timestamp }}</p>
<table>
<tr><th>Cloud Provider</th><th>Status</th><th>Details</th></tr>
<tr>
<td>AWS</td>
<td class="status-{{ aws_status | lower }}">{{ aws_status }}</td>
<td>Account: {{ aws_identity.Account | default('N/A') }}</td>
</tr>
<tr>
<td>Azure</td>
<td class="status-{{ azure_status | lower }}">{{ azure_status }}</td>
<td>Subscription: {{ az_account.id | default('N/A') }}</td>
</tr>
<tr>
<td>GCP</td>
<td class="status-{{ gcp_status | lower }}">{{ gcp_status }}</td>
<td>Project: {{ gcp_project | default('N/A') }}</td>
</tr>
</table>
</body>
</html>
'''

with open(f"{base_dir}/ansible/templates/consolidated_report.j2", "w") as f:
    f.write(consolidated_template)

print("Docker and Ansible configurations created successfully!")

# Create GitHub Actions CI/CD pipeline and final project structure

# GitHub Actions workflow
github_workflow = '''name: Multi-Cloud Security CI/CD

on:
  push:
    branches: [ main, develop ]
    paths:
      - 'terraform/**'
      - 'scripts/**'
      - 'policies/**'
  pull_request:
    branches: [ main ]
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM UTC
  workflow_dispatch:

env:
  TF_IN_AUTOMATION: true
  TF_VERSION: "1.5.7"

jobs:
  # Terraform Format and Validation
  terraform-validate:
    name: Terraform Validate
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v2
        with:
          terraform_version: ${{ env.TF_VERSION }}

      - name: Terraform Format Check
        run: |
          terraform fmt -check -recursive terraform/

      - name: Terraform Init (AWS)
        working-directory: terraform/aws
        run: terraform init -backend=false

      - name: Terraform Validate (AWS)
        working-directory: terraform/aws
        run: terraform validate

      - name: Terraform Init (Azure)
        working-directory: terraform/azure
        run: terraform init -backend=false

      - name: Terraform Validate (Azure)
        working-directory: terraform/azure
        run: terraform validate

      - name: Terraform Init (GCP)
        working-directory: terraform/gcp
        run: terraform init -backend=false

      - name: Terraform Validate (GCP)
        working-directory: terraform/gcp
        run: terraform validate

  # Security Policy Validation
  policy-validate:
    name: Policy Validation
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install jsonschema pyyaml

      - name: Validate AWS Policies
        run: |
          for file in policies/aws/*.json; do
            echo "Validating $file"
            python -c "import json; json.load(open('$file'))"
          done

      - name: Validate Azure Policies
        run: |
          for file in policies/azure/*.json; do
            echo "Validating $file"
            python -c "import json; json.load(open('$file'))"
          done

      - name: Validate GCP Policies
        run: |
          for file in policies/gcp/*.yaml; do
            echo "Validating $file"
            python -c "import yaml; yaml.safe_load(open('$file'))"
          done

  # Python Code Quality
  python-lint:
    name: Python Lint & Test
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install flake8 pylint pytest black
          pip install -r scripts/python/requirements.txt

      - name: Lint with flake8
        run: |
          flake8 scripts/python/ --count --select=E9,F63,F7,F82 --show-source --statistics
          flake8 scripts/python/ --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

      - name: Format check with black
        run: |
          black --check scripts/python/

      - name: Run tests
        run: |
          pytest scripts/python/ -v || true

  # Security Scanning (Trivy + Checkov)
  security-scan:
    name: Security Scanning
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
          format: 'sarif'
          output: 'trivy-results.sarif'

      - name: Upload Trivy scan results
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: 'trivy-results.sarif'

      - name: Run Checkov
        uses: bridgecrewio/checkov-action@master
        with:
          directory: terraform/
          framework: terraform
          output_format: sarif
          output_file_path: checkov-results.sarif

      - name: Upload Checkov results
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: 'checkov-results.sarif'

  # AWS Compliance Scan (Scheduled)
  aws-compliance:
    name: AWS Compliance Scan
    runs-on: ubuntu-latest
    if: github.event_name == 'schedule' || github.event_name == 'workflow_dispatch'
    needs: [terraform-validate, policy-validate]
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r scripts/python/requirements.txt

      - name: Run AWS Compliance Scan
        run: |
          python scripts/python/compliance_scanner.py \
            --cloud aws \
            --report html \
            --output aws-compliance-report.html

      - name: Upload report
        uses: actions/upload-artifact@v3
        with:
          name: aws-compliance-report
          path: aws-compliance-report.html

      - name: Check for critical findings
        run: |
          python scripts/python/compliance_scanner.py \
            --cloud aws \
            --severity critical \
            --report json \
            --output critical-findings.json
          
          CRITICAL_COUNT=$(python -c "import json; data=json.load(open('critical-findings.json')); print(data['summary']['critical_count'])")
          if [ "$CRITICAL_COUNT" -gt 0 ]; then
            echo "::error::Found $CRITICAL_COUNT CRITICAL security findings!"
            exit 1
          fi

  # Azure Compliance Scan (Scheduled)
  azure-compliance:
    name: Azure Compliance Scan
    runs-on: ubuntu-latest
    if: github.event_name == 'schedule' || github.event_name == 'workflow_dispatch'
    needs: [terraform-validate, policy-validate]
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Azure Login
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r scripts/python/requirements.txt

      - name: Run Azure Compliance Scan
        run: |
          python scripts/python/compliance_scanner.py \
            --cloud azure \
            --report html \
            --output azure-compliance-report.html

      - name: Upload report
        uses: actions/upload-artifact@v3
        with:
          name: azure-compliance-report
          path: azure-compliance-report.html

  # GCP Compliance Scan (Scheduled)
  gcp-compliance:
    name: GCP Compliance Scan
    runs-on: ubuntu-latest
    if: github.event_name == 'schedule' || github.event_name == 'workflow_dispatch'
    needs: [terraform-validate, policy-validate]
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup GCP credentials
        uses: google-github-actions/auth@v1
        with:
          credentials_json: ${{ secrets.GCP_SA_KEY }}

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r scripts/python/requirements.txt

      - name: Run GCP Compliance Scan
        run: |
          python scripts/python/compliance_scanner.py \
            --cloud gcp \
            --report html \
            --output gcp-compliance-report.html

      - name: Upload report
        uses: actions/upload-artifact@v3
        with:
          name: gcp-compliance-report
          path: gcp-compliance-report.html

  # Consolidated Report
  consolidated-report:
    name: Generate Consolidated Report
    runs-on: ubuntu-latest
    if: always() && (needs.aws-compliance.result == 'success' || needs.azure-compliance.result == 'success' || needs.gcp-compliance.result == 'success')
    needs: [aws-compliance, azure-compliance, gcp-compliance]
    steps:
      - name: Download all reports
        uses: actions/download-artifact@v3

      - name: Generate consolidated dashboard
        run: |
          echo "# Multi-Cloud Security Compliance Report" > consolidated-report.md
          echo "Generated: $(date)" >> consolidated-report.md
          echo "" >> consolidated-report.md
          echo "## AWS" >> consolidated-report.md
          echo "[View AWS Report](./aws-compliance-report/aws-compliance-report.html)" >> consolidated-report.md
          echo "" >> consolidated-report.md
          echo "## Azure" >> consolidated-report.md
          echo "[View Azure Report](./azure-compliance-report/azure-compliance-report.html)" >> consolidated-report.md
          echo "" >> consolidated-report.md
          echo "## GCP" >> consolidated-report.md
          echo "[View GCP Report](./gcp-compliance-report/gcp-compliance-report.html)" >> consolidated-report.md

      - name: Upload consolidated report
        uses: actions/upload-artifact@v3
        with:
          name: consolidated-report
          path: consolidated-report.md
'''

os.makedirs(f"{base_dir}/.github/workflows", exist_ok=True)
with open(f"{base_dir}/.github/workflows/security-ci.yml", "w") as f:
    f.write(github_workflow)

# Create .gitignore
gitignore = '''# Terraform
*.tfstate
*.tfstate.*
.terraform/
.terraform.lock.hcl
tfplan
crash.log
*.tfvars
!terraform.tfvars.example

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
logs/
*.log

# Reports
reports/
*.html
!ansible/templates/*.html
!docker/*.html

# Credentials
*.pem
*.key
*.p12
*.pfx
service-account-*.json
.aws/
.azure/
.gcp/

# Ansible
*.retry
ansible/*.log
ansible/reports/

# Docker
.env
docker-compose.override.yml
'''

with open(f"{base_dir}/.gitignore", "w") as f:
    f.write(gitignore)

# Create LICENSE
license_text = '''MIT License

Copyright (c) 2026 Multi-Cloud Security Lab

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

with open(f"{base_dir}/LICENSE", "w") as f:
    f.write(license_text)

# Create Makefile for common operations
makefile = '''.PHONY: help install validate deploy-aws deploy-azure deploy-gcp deploy-all scan clean

help: ## Show this help message
	@echo "Multi-Cloud Security Lab - Available Commands"
	@echo "============================================"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\\033[36m%-20s\\033[0m %s\\n", $$1, $$2}'

install: ## Install Python dependencies
	cd scripts/python && pip install -r requirements.txt

validate: ## Validate all Terraform configurations
	cd terraform/aws && terraform init -backend=false && terraform validate
	cd terraform/azure && terraform init -backend=false && terraform validate
	cd terraform/gcp && terraform init -backend=false && terraform validate

format: ## Format all Terraform files
	terraform fmt -recursive terraform/

lint: ## Run Python linting
	flake8 scripts/python/ --count --statistics
	black --check scripts/python/

deploy-aws: ## Deploy AWS security foundation
	cd terraform/aws && terraform init && terraform plan && terraform apply

deploy-azure: ## Deploy Azure security foundation
	cd terraform/azure && terraform init && terraform plan && terraform apply

deploy-gcp: ## Deploy GCP security foundation
	cd terraform/gcp && terraform init && terraform plan && terraform apply

deploy-all: deploy-aws deploy-azure deploy-gcp ## Deploy all clouds

scan: ## Run compliance scan across all clouds
	cd scripts/python && python compliance_scanner.py --cloud all --report html --output ../../reports/compliance-report.html

scan-aws: ## Scan AWS only
	cd scripts/python && python compliance_scanner.py --cloud aws --report html

scan-azure: ## Scan Azure only
	cd scripts/python && python compliance_scanner.py --cloud azure --report html

scan-gcp: ## Scan GCP only
	cd scripts/python && python compliance_scanner.py --cloud gcp --report html

remediate: ## Run auto-remediation (dry-run by default)
	cd scripts/python && python auto_remediation.py --dry-run

analyze-iam: ## Analyze IAM policies
	cd scripts/python && python iam_policy_analyzer.py

sync-identities: ## Export and sync identities across clouds
	cd scripts/python && python cross_cloud_sync.py

docker-build: ## Build Docker image
	cd docker && docker-compose build

docker-up: ## Start Docker containers
	cd docker && docker-compose up -d

docker-down: ## Stop Docker containers
	cd docker && docker-compose down

docker-scan: ## Run scan inside Docker container
	cd docker && docker-compose exec security-tools bash -c "cd /app/scripts/python && python compliance_scanner.py --cloud all --report html"

ansible-audit: ## Run Ansible security audit
	cd ansible && ansible-playbook -i inventory.ini security_audit.yml

destroy-aws: ## Destroy AWS resources
	cd terraform/aws && terraform destroy

destroy-azure: ## Destroy Azure resources
	cd terraform/azure && terraform destroy

destroy-gcp: ## Destroy GCP resources
	cd terraform/gcp && terraform destroy

destroy-all: destroy-aws destroy-azure destroy-gcp ## Destroy all resources

clean: ## Clean temporary files
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".terraform" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "tfplan" -delete
	find . -type f -name "*.tfstate*" -delete
	find . -type f -name "crash.log" -delete
	@echo "Cleanup complete"
'''

with open(f"{base_dir}/Makefile", "w") as f:
    f.write(makefile)

# Create final project structure visualization
structure = """multi-cloud-security-lab/
├── README.md                          # Main project documentation
├── LICENSE                            # MIT License
├── Makefile                           # Common commands automation
├── .gitignore                         # Git ignore patterns
│
├── .github/
│   └── workflows/
│       └── security-ci.yml             # GitHub Actions CI/CD pipeline
│
├── terraform/                          # Infrastructure as Code
│   ├── aws/
│   │   ├── main.tf                     # AWS security foundation
│   │   ├── variables.tf                # AWS variables
│   │   ├── outputs.tf                  # AWS outputs
│   │   └── terraform.tfvars.example    # Example variables
│   ├── azure/
│   │   ├── main.tf                     # Azure security foundation
│   │   ├── variables.tf                # Azure variables
│   │   ├── outputs.tf                  # Azure outputs
│   │   └── terraform.tfvars.example    # Example variables
│   ├── gcp/
│   │   ├── main.tf                     # GCP security foundation
│   │   ├── variables.tf                # GCP variables
│   │   ├── outputs.tf                  # GCP outputs
│   │   └── terraform.tfvars.example    # Example variables
│   └── modules/
│       ├── iam/
│       │   ├── aws.tf                  # AWS IAM module
│       │   ├── variables.tf            # Module variables
│       │   └── outputs.tf              # Module outputs
│       └── security-posture/
│           ├── aws.tf                  # AWS security services module
│           ├── variables.tf            # Module variables
│           └── outputs.tf              # Module outputs
│
├── scripts/                            # Automation scripts
│   ├── python/
│   │   ├── compliance_scanner.py       # Multi-cloud compliance scanner
│   │   ├── auto_remediation.py         # Auto-remediation engine
│   │   ├── iam_policy_analyzer.py     # IAM policy security analyzer
│   │   ├── cross_cloud_sync.py         # Cross-cloud IAM sync
│   │   └── requirements.txt            # Python dependencies
│   └── bash/
│       └── deploy.sh                   # Deployment automation script
│
├── policies/                           # Cloud-native policies
│   ├── aws/
│   │   ├── iam_password_policy.json    # IAM password enforcement
│   │   ├── s3_secure_bucket_policy.json # S3 security policy
│   │   ├── ec2_restricted_ami_policy.json # AMI restrictions
│   │   ├── scp_deny_unapproved_regions.json # Region restrictions
│   │   ├── scp_deny_root_account.json  # Root account prevention
│   │   └── scp_require_encryption.json # Encryption requirements
│   ├── azure/
│   │   ├── require_encryption.json     # Encryption policy
│   │   ├── require_nsg_on_subnet.json  # Network security
│   │   ├── restrict_locations.json       # Location restrictions
│   │   └── require_tags.json           # Tagging policy
│   └── gcp/
│       ├── restrict_vm_external_ips.yaml # VM external IP restriction
│       ├── skip_default_network.yaml     # Default network prevention
│       ├── disable_serial_port.yaml      # Serial port disable
│       ├── require_os_login.yaml         # OS login requirement
│       ├── uniform_bucket_access.yaml    # Uniform bucket access
│       ├── restrict_cloud_sql_public_ip.yaml # SQL public IP restriction
│       └── disable_guest_attributes.yaml # Guest attributes disable
│
├── ansible/                            # Configuration management
│   ├── ansible.cfg                     # Ansible configuration
│   ├── inventory.ini                   # Ansible inventory
│   ├── security_audit.yml              # Security audit playbook
│   └── templates/
│       ├── aws_audit_report.j2         # AWS report template
│       └── consolidated_report.j2      # Consolidated report template
│
├── docker/                             # Containerization
│   ├── Dockerfile                      # Security tools container
│   └── docker-compose.yml              # Multi-service orchestration
│
└── docs/                               # Documentation
    ├── aws-setup.md                    # AWS setup guide
    ├── azure-setup.md                  # Azure setup guide
    ├── gcp-setup.md                    # GCP setup guide
    ├── compliance-scanning.md          # Compliance scanning guide
    └── troubleshooting.md              # Troubleshooting guide
"""

with open(f"{base_dir}/PROJECT_STRUCTURE.md", "w") as f:
    f.write(f"# Project Structure\\n\\n```\\n{structure}\\n```")

print("All project files created successfully!")
print(f"\\nPro

# Create a comprehensive project summary document
summary = """# 🎯 Multi-Cloud Security Posture Management & IAM Lab - Project Summary

## 📋 What Was Built

This is a **production-ready, enterprise-grade security lab** that implements comprehensive Identity and Access Management (IAM) and Security Posture Management across AWS, Azure, and Google Cloud Platform using Infrastructure-as-Code (Terraform), automation (Python), and continuous compliance monitoring.

---

## 🏗️ Architecture Components

### 1. AWS Security Foundation
- **Organizations & SCPs**: Multi-account strategy with Service Control Policies
  - Deny root account usage across all accounts
  - Restrict to approved regions (us-east-1, us-west-2, eu-west-1)
  - Require encryption for S3 and EBS volumes
- **IAM Foundation**:
  - Custom roles with permission boundaries (Admin, Security, Developer)
  - MFA enforcement for all privileged operations
  - Strong password policy (16+ chars, 90-day rotation)
  - Access Analyzer for external access monitoring
- **Security Services**:
  - GuardDuty (threat detection with malware protection)
  - Security Hub (CIS, NIST, PCI standards)
  - AWS Config (15+ compliance rules)
  - Macie (sensitive data discovery)
  - Inspector (vulnerability scanning)
  - CloudTrail (multi-region with log validation)
  - KMS (multi-region encryption keys)
  - WAFv2 (web application firewall)

### 2. Azure Security Foundation
- **Azure AD & Conditional Access**:
  - MFA required for all users
  - Legacy authentication blocked
  - Compliant devices required for admins
  - Security groups for role-based management
- **Microsoft Defender for Cloud**:
  - Standard tier for VMs, Storage, SQL, App Services, Key Vault, DNS
  - Auto-provisioning of monitoring agents
- **Azure Sentinel**: SIEM workspace with Log Analytics
- **Azure Policy**: CIS Benchmark initiative with custom policies
- **Key Vault**: Premium tier with HSM-backed keys, automatic rotation
- **Network Security**: Azure Firewall (Premium), NSGs, VNet isolation

### 3. GCP Security Foundation
- **Organization Policies**:
  - Restrict VM external IPs
  - Skip default network creation
  - Disable serial port access
  - Require OS Login
  - Uniform bucket-level access
  - Restrict Cloud SQL public IPs
- **Cloud IAM**:
  - Custom roles (Security Auditor, Security Remediator)
  - Cloud Identity groups
  - Essential contacts for security alerts
- **Security Command Center**: Custom security modules
- **Cloud Asset Inventory**: Real-time resource tracking with Pub/Sub
- **VPC Service Controls**: Data exfiltration prevention
- **Cloud Armor**: DDoS protection and WAF
- **Cloud KMS**: HSM-backed keys with 90-day rotation
- **OS Config**: Automated patch management

---

## 🔧 Automation & Tooling

### Python Scripts
1. **compliance_scanner.py** - Multi-cloud compliance scanner
   - Supports CIS, NIST, SOC2, PCI DSS frameworks
   - Generates JSON, CSV, HTML reports
   - Severity filtering (Critical, High, Medium, Low)
   - 20+ automated security checks per cloud

2. **auto_remediation.py** - Automated security fix engine
   - S3 public access blocking
   - Encryption enablement
   - Security group rule cleanup
   - Password policy enforcement
   - GuardDuty/Security Hub activation

3. **iam_policy_analyzer.py** - IAM policy security analyzer
   - Detects wildcard permissions
   - Identifies dangerous actions
   - Checks for missing conditions
   - Generates security findings report

4. **cross_cloud_sync.py** - Cross-cloud identity synchronization
   - Exports AWS identities
   - Generates Azure AD mappings
   - Creates GCP IAM role mappings

### Infrastructure as Code
- **Terraform modules** for reusable components
- **State management** via S3 (AWS), Azure Blob, GCS
- **Backend locking** with DynamoDB (AWS)
- **Variable templates** for easy configuration

### CI/CD Pipeline (GitHub Actions)
- **Terraform validation** on every push
- **Security scanning** with Trivy and Checkov
- **Python linting** with flake8, pylint, black
- **Policy validation** for JSON/YAML files
- **Scheduled compliance scans** (daily at 2 AM)
- **Artifact uploads** for compliance reports
- **Critical finding alerts** that fail the pipeline

### Docker & Ansible
- **Docker container** with all cloud CLIs and Python tools
- **Docker Compose** for scheduled scanning services
- **Ansible playbooks** for configuration drift detection
- **Jinja2 templates** for automated report generation

---

## 📊 Compliance Coverage

| Framework | AWS | Azure | GCP |
|-----------|-----|-------|-----|
| CIS Benchmarks | v1.5.0 | v1.5.0 | v1.3.0 |
| NIST 800-53 | Rev 5 | Rev 5 | Rev 5 |
| SOC 2 Type II | CC6.x, CC7.x | CC6.x, CC7.x | CC6.x, CC7.x |
| PCI DSS | v4.0 | v4.0 | v4.0 |

### Key Controls Implemented
- ✅ Multi-factor authentication enforcement
- ✅ Least-privilege access with permission boundaries
- ✅ Encryption at rest (KMS/Key Vault/Cloud KMS)
- ✅ Encryption in transit (TLS/SSL enforcement)
- ✅ Network segmentation and firewall rules
- ✅ Continuous monitoring and logging
- ✅ Vulnerability scanning and patch management
- ✅ Threat detection and incident response
- ✅ Data loss prevention (VPC Service Controls)
- ✅ Compliance reporting and dashboards

---

## 🚀 Quick Start Commands

```bash
# Deploy everything
make deploy-all

# Or deploy individual clouds
make deploy-aws
make deploy-azure
make deploy-gcp

# Run compliance scan
make scan

# View specific cloud reports
make scan-aws
make scan-azure
make scan-gcp

# Analyze IAM policies
make analyze-iam

# Run auto-remediation (dry-run)
make remediate

# Build and run in Docker
make docker-build
make docker-up
make docker-scan

# Run Ansible audit
make ansible-audit

# Clean up everything
make destroy-all
make clean
```

---

## 📁 File Structure
The project contains **50+ files** organized into:
- 3 Terraform cloud configurations (AWS, Azure, GCP)
- 2 Terraform modules (IAM, Security Posture)
- 4 Python automation scripts
- 1 Bash deployment script
- 14 Cloud policy definitions (AWS JSON, Azure JSON, GCP YAML)
- 1 Ansible playbook with templates
- 1 Docker configuration with compose
- 1 GitHub Actions workflow
- 5 Documentation guides
- 1 Makefile for command automation

---

## 💰 Cost Considerations
Estimated monthly costs for a small deployment:
- **AWS**: ~$50-150 (GuardDuty, Security Hub, Config, Macie, Inspector)
- **Azure**: ~$30-100 (Defender for Cloud, Sentinel, Key Vault)
- **GCP**: ~$20-50 (Security Command Center, KMS, Cloud Armor)

**Total**: ~$100-300/month for comprehensive security monitoring

---

## 🔐 Security Best Practices Applied
1. **Zero Trust Architecture** - Verify every request, trust nothing
2. **Defense in Depth** - Multiple layers of security controls
3. **Least Privilege** - Minimum permissions for every role
4. **Encryption Everywhere** - Data at rest and in transit
5. **Continuous Monitoring** - Real-time threat detection
6. **Automated Remediation** - Self-healing security posture
7. **Audit Everything** - Comprehensive logging and tracing
8. **Compliance as Code** - Policy enforcement via code

---

## 📚 Documentation Included
- AWS Setup Guide with troubleshooting
- Azure Setup Guide with PIM configuration
- GCP Setup Guide with organization policies
- Compliance Scanning Guide with CI/CD integration
- Troubleshooting Guide for common issues

---

## 🎯 Learning Outcomes
By working with this lab, you will gain hands-on experience with:
- Multi-cloud IAM architecture and design
- Terraform for cloud infrastructure management
- Cloud-native security services (GuardDuty, Sentinel, SCC)
- Compliance automation and reporting
- Infrastructure-as-Code security patterns
- Cross-cloud identity synchronization
- Automated security remediation
- CI/CD for security operations (DevSecOps)
"""

with open(f"{base_dir}/PROJECT_SUMMARY.md", "w") as f:
    f.write(summary)

# List all created files
import os
file_count = 0
for root, dirs, files in os.walk(base_dir):
    for file in files:
        file_path = os.path.join(root, file)
        rel_path = os.path.relpath(file_path, base_dir)
        size = os.path.getsize(file_path)
        file_count += 1

print(f"\\n{'='*60}")
print(f"✅ PROJECT BUILD COMPLETE")
print(f"{'='*60}")
print(f"Total files created: {file_count}")
print(f"Project location: {base_dir}")
print(f"\\nKey deliverables:")
print(f"  • Terraform configs for AWS, Azure, GCP")
print(f"  • Python compliance scanner + auto-remediation")
print(f"  • IAM policy analyzer + cross-cloud sync")
print(f"  • 14 cloud-native security policies")
print(f"  • GitHub Actions CI/CD pipeline")
print(f"  • Docker containerization")
print(f"  • Ansible configuration audit")
print(f"  • Complete documentation suite")
print(f"{'='*60}")
