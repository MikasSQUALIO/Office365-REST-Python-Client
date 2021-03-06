import os

from settings import settings

from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

credentials = UserCredential(settings.get('user_credentials').get('username'),
                             settings.get('user_credentials').get('password'))
ctx = ClientContext(settings.get('url')).with_credentials(credentials)

path = "../../../tests/data/SharePoint User Guide.docx"
with open(path, 'rb') as content_file:
    file_content = content_file.read()

list_title = "Documents"
target_folder = ctx.web.lists.get_by_title(list_title).root_folder
name = os.path.basename(path)
target_file = target_folder.upload_file(name, file_content)
ctx.execute_query()
print("File url: {0}".format(target_file.serverRelativeUrl))
