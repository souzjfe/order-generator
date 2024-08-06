from typing import Any
from django.contrib import admin

class AdminSiteReorder(admin.AdminSite):
     # Text to put at the end of each page's <title>.
    site_title = 'My site admin'

    # Text to put in each page's <h1> (and above login form).
    site_header = 'My administration'

    # Text to put at the top of the admin index page.
    index_title = 'Acesse algum dos módulos abaixo'
    def get_app_list(self, request, app_label=None):
        """Reorder the models in the admin site.

        By default, django admin models are ordered alphabetically within their app.

        This method reorders the models into a single list, regardless of the app they belong to.
        """
        apps = super().get_app_list(request, app_label)
        models = []
        for app in apps:
            for model in app['models']:
                models.append(model)
        # Order the models alphabetically by object_name
        # models.sort(key=lambda model: model['object_name'])
        # return super().get_app_list(request, app_label)
        return [{
            'name': 'Cadastros',  # Assign a custom label to group all models
            'app_url': '/',
            'models': models,
        }]