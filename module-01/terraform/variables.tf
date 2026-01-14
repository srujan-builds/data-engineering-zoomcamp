variable "project" {
  description = "Project id"
  default     = "probable-analog-477614-m5"
}

variable "gcp_credentials" {
  description = "Service account credentials"
  default     = "./keys/my-creds.json"
}

variable "bucket" {
  description = "bucket name"
  default     = "probable-analog-477614-m5-bucket"
}

variable "dataset" {
  description = "BQ dataset"
  default     = "probable_analog_m5_dataset"
}

variable "location" {
  description = "Location"
  default     = "US"
}

variable "region" {
  description = "region for the project"
  default     = "us-central1"
}