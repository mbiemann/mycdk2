import aws_cdk as core
import aws_cdk.assertions as assertions

from mycdk2.mycdk2_stack import Mycdk2Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in mycdk2/mycdk2_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Mycdk2Stack(app, "mycdk2")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
