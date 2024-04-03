from azure_manager import AzureServiceBusManager

#change

# dit zijn vaste variabelen (voor je account)
subscription_id = 'ac58b4ec-0810-44c4-9167-58a33cd159cd'
manager = AzureServiceBusManager(subscription_id)
resource_group_name = 'l.grim-rg'
namespace_name = 'aardappel'

# dit zijn flexibele variabelen voor topic en subscription
## TODO: Wat als er al een topic of subscription bestaat?
topic_name = 'automationTest' 
subscription_name = 'subOne'

# Create a topic
manager.create_topic(resource_group_name, namespace_name, topic_name)

# Create a subscription
manager.create_subscription(resource_group_name, namespace_name, topic_name, subscription_name)