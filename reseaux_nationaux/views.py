from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import UserForm, PersonneForm
from django.contrib import messages
from account.decorators import login_required
from .models import Personne, Reseau
    
### Projetc views        
class HomeView(ListView):
    template_name = 'home.html'
    def get_queryset(self):
        personnes = Personne.objects.all()
        print(self.kwargs)
        if 'reseau' in self.request.GET and self.request.GET['reseau']:
            personnes = personnes.filter(reseaux=get_object_or_404(Reseau, id=self.request.GET['reseau']))
        return personnes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reseaux'] = Reseau.objects.all()
        return context


@login_required    
def editPersonne(request):
    user_form = UserForm(instance=request.user)
    personne = None
    try:
        personne = request.user.personne
    except:
        pass
    personne_form = PersonneForm(instance=personne)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        personne_form = PersonneForm(request.POST, instance=personne)
        
        if user_form.is_valid() and personne_form.is_valid():
            user_form.save()
            personne = personne_form.save(commit=False)
            personne.user = request.user
            personne.save()
            messages.add_message(request, messages.INFO, 'Vos informations ont été mises à jour')
            return HttpResponseRedirect('/')    
    
    return render(request, 'edit_personne.html', {
        'user_form': user_form,
        'personne_form': personne_form,
    })
    


