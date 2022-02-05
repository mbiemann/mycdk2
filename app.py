#!/usr/bin/env python3

from aws_cdk import App, Stack, aws_lambda
from constructs import Construct


class MyStack2(Stack):

    def __init__(self, scope: Construct) -> None:
        
        construct_id: str = "MyStack2"
        super().__init__(scope, construct_id)

        layer1_arn = self.format_arn(
            service="lambda",
            resource="layer:global-my-lambda-layer-1:1"
        )
        
        layer1 = aws_lambda.LayerVersion.from_layer_version_arn(
            self,
            "GlobalMyLayer1",
            layer1_arn
        )

        aws_lambda.Function(self, "MyFunction2",
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            handler="index.handler",
            code=aws_lambda.Code.from_asset("code_lambda"),
            layers=[layer1]
        )


app = App()
MyStack2(app)
app.synth()
