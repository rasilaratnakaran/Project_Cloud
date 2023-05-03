
from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    #account_name = os.environ['AZURE_ACCOUNT_NAME'] # Must be replaced by your <storage_account_name>
    account_name = 'c1059123'
    #account_key = os.environ['AZURE_ACCOUNT_KEY'] # Must be replaced by your <storage_account_key>
    account_key = 'ROjs3JVI66jVLigGYUU2yeWwdQTwnFwRUcTdrRU3Spgl/mRyD/JsQeHDP2Ve5+Tc54FTtiOJjgM+AStgkUjcQ=='
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    #account_name = os.environ['AZURE_ACCOUNT_NAME'] # Must be replaced by your storage_account_name
    account_name = 'c1059123'
    #account_key = os.environ['AZURE_ACCOUNT_KEY'] # Must be replaced by your <storage_account_key>
    account_key = 'fROjs3JVI66jVLigGYUU2yeWwdQTwnFwRUcTdrRU3Spgl/mRyD/JsQeHDP2Ve5+Tc54FTtiOJjgM+AStgkUjcQ=='
    azure_container = 'static'
    expiration_secs = None

    