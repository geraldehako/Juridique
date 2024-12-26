from django import forms
from .models import Clientqrcode, Attestation

class ClientForm(forms.ModelForm):
    class Meta:
        model = Clientqrcode
        fields = ['nom', 'prenoms', 'date_naissance', 'adresse', 'numero_cni', 'telephone']


class AttestationForm(forms.ModelForm):
    class Meta:
        model = Attestation
        fields = ['type_attestation', 'lot_numero', 'superficie', 'lotissement', 'arrete_reference']
