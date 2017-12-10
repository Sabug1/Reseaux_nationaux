from django.contrib import admin

from .models import CNPE, Personne, Reseau, Metier
from .actions import export_as_csv_action

PERSONNE_EXPORT_FIELDS = (
    'nom', 'prenom', 'cnpe',
)

class PersonneAdmin(admin.ModelAdmin):
    # ...
    list_display = ('cnpe','liste_reseaux', 'nom', 'prenom', 'telephone', 'mail')
    list_filter = ('cnpe', 'cnpe__palier', 'reseaux')
    search_fields = ('cnpe__nom','reseaux__nom', 'nom', 'prenom', 'telephone', 'mail')
    list_display_links = ('nom', 'prenom')
    actions = [export_as_csv_action("Export CSV", fields=PERSONNE_EXPORT_FIELDS, delimiter=';', encoding='iso8859-15'),]

    def liste_reseaux (self, personne):
        return ', '.join(reseau.nom for reseau in personne.reseaux.all()[0:8] )


# Register your models here.
admin.site.register(CNPE)
admin.site.register(Personne, PersonneAdmin)
admin.site.register(Reseau)
admin.site.register(Metier)


# Filtres

