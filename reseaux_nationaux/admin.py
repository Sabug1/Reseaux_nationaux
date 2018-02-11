from django.contrib import admin

from .models import CNPE, Personne, Reseau, Metier
from .actions import export_as_csv_action

PERSONNE_EXPORT_FIELDS = (
   'user.first_name', 'user.last_name', 'user.email', 'cnpe',
)

class PersonneAdmin(admin.ModelAdmin):
    # ...
    list_display = ('user.first_name', 'user.last_name', 'user.email','cnpe','liste_reseaux', 'telephone' )
    list_filter = ('cnpe', 'cnpe__palier', 'reseaux')
    search_fields = ('cnpe__nom','reseaux__nom', 'user.first_name', 'user.last_name', 'user.email', 'telephone')
    list_display_links = ('user.first_name', 'user.last_name')
    actions = [export_as_csv_action("Export CSV", fields=PERSONNE_EXPORT_FIELDS, delimiter=';', encoding='iso8859-15'),]

    def liste_reseaux (self, personne):
        return ', '.join(reseau.nom for reseau in personne.reseaux.all()[0:8] )


# Register your models here.
admin.site.register(CNPE)
admin.site.register(Personne)
admin.site.register(Reseau)
admin.site.register(Metier)


# Filtres

