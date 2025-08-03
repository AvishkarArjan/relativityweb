from django.contrib import admin
from .models import (
    Portfolio,
    Framework,
    DataSource,
    Holding
    )

admin.site.register(Portfolio)
admin.site.register(Framework)
admin.site.register(DataSource)
admin.site.register(Holding)




