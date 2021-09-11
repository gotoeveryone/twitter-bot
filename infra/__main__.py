'''An AWS Python Pulumi program'''

import json

import pulumi
import pulumi_aws as aws

bot_messages = aws.dynamodb.Table('bot_messages',
                                  attributes=[aws.dynamodb.TableAttributeArgs(
                                      name='key',
                                      type='S',
                                  )],
                                  billing_mode='PROVISIONED',
                                  hash_key='key',
                                  name='bot_messages',
                                  read_capacity=5,
                                  write_capacity=5,
                                  opts=pulumi.ResourceOptions(protect=True))

pulumi.export('bot_messages', bot_messages.id)

policy = aws.iam.Policy('TwitterBotPolicy',
                        description='Twitter Bot Policy',
                        policy=json.dumps({
                            'Version': '2012-10-17',
                            'Statement': [
                                {
                                    'Effect': 'Allow',
                                    'Action': [
                                        'ssm:GetParameter',
                                        'sts:AssumeRole',
                                        'dynamodb:GetItem',
                                    ],
                                    'Resource': '*'
                                },
                            ],
                        }))

role = aws.iam.Role('TwitterBotRole',
                    path='/service-role/',
                    assume_role_policy=json.dumps({
                        'Version': '2012-10-17',
                        'Statement': [
                            {
                                'Effect': 'Allow',
                                'Action': 'sts:AssumeRole',
                                'Principal': {
                                    'Service': 'lambda.amazonaws.com'
                                },
                            },
                        ],
                    }))

aws.iam.RolePolicyAttachment('TwitterBotRolePolicyAttachment',
                             role=role,
                             policy_arn=policy.arn)
