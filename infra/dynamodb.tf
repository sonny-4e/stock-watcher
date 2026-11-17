resource "aws_dynamodb_table" "quotes" {
  name         = "stock-watcher-quotes"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "ticker"
  range_key    = "fetched_at"

  attribute {
    name = "ticker"
    type = "S"
  }

  attribute {
    name = "fetched_at"
    type = "S"
  }
}