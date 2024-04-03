from azure_manager import AzureServiceBusManager

subscription_id = 'ac58b4ec-0810-44c4-9167-58a33cd159cd'
manager = AzureServiceBusManager(subscription_id)


resource_group_name = 'l.grim-rg'
namespace_name = 'aardappel'
topic_name = 'automationTest'
subscription_name = 'subOne'

# Create a topic
manager.create_topic(resource_group_name, namespace_name, topic_name)

# Create a subscription
manager.create_subscription(resource_group_name, namespace_name, topic_name, subscription_name)