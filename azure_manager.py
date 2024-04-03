from azure.mgmt.servicebus import ServiceBusManagementClient
from azure.identity import DefaultAzureCredential

class AzureServiceBusManager:
    def __init__(self, subscription_id):
        self.subscription_id = subscription_id
        self.credential = DefaultAzureCredential()

    def create_topic(self, resource_group_name, namespace_name, topic_name):
        with ServiceBusManagementClient(self.credential, self.subscription_id) as client:
            client.topics.create_or_update(
                resource_group_name, 
                namespace_name, 
                topic_name,
                {}
            )
            print(f"Topic '{topic_name}' created successfully.")

    def create_subscription(self, resource_group_name, namespace_name, topic_name, subscription_name):
        with ServiceBusManagementClient(self.credential, self.subscription_id) as client:
            client.subscriptions.create_or_update(
                resource_group_name,
                namespace_name,
                topic_name,
                subscription_name,
                {}
            )
            print(f"Subscription '{subscription_name}' created successfully.")

