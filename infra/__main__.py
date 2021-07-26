"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws

bot_messages = aws.dynamodb.Table("bot_messages",
                                  attributes=[aws.dynamodb.TableAttributeArgs(
                                      name="key",
                                      type="S",
                                  )],
                                  billing_mode="PROVISIONED",
                                  hash_key="key",
                                  name="bot_messages",
                                  read_capacity=5,
                                  write_capacity=5,
                                  opts=pulumi.ResourceOptions(protect=True))

pulumi.export('bot_messages', bot_messages.id)
