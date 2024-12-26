import random
import string
import qrcode
from io import BytesIO
from django.core.files import File
from django.db import models

# Créez votre modèle QR_code
class QR_code(models.Model):
    data = models.CharField(max_length=255)
    qr_code = models.ImageField(upload_to='qr_code/', null=True, blank=True)

    def save(self, *args, **kwargs):
        # Génération du QR code avec la donnée
        qr_image = qrcode.make(self.data)

        # Utilisation de BytesIO pour enregistrer l'image dans un fichier en mémoire
        buffer = BytesIO()
        qr_image.save(buffer, format='PNG')  # Sauvegarde de l'image dans le buffer

        # Sauvegarde du fichier dans l'ImageField
        file_name = f"qr_code-{self.data}.png"
        self.qr_code.save(file_name, File(buffer), save=False)  # Enregistrement dans le modèle

        # Appel de la méthode de sauvegarde parente
        return super().save(*args, **kwargs)

class Clientqrcode(models.Model):
    nom = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=100)
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=200)
    numero_cni = models.CharField(max_length=50, unique=True)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nom} {self.prenoms}"


class Attestation(models.Model):
    TYPE_CHOICES = [
        ('cession', 'Attestation de Cession'),
        ('villageoise', 'Attestation Villageoise'),
    ]

    type_attestation = models.CharField(max_length=50, choices=TYPE_CHOICES)
    numero = models.CharField(max_length=9, unique=True, editable=False)
    client = models.ForeignKey(Clientqrcode, on_delete=models.CASCADE)
    lot_numero = models.CharField(max_length=50)
    superficie = models.DecimalField(max_digits=10, decimal_places=2)
    lotissement = models.CharField(max_length=255)
    arrete_reference = models.CharField(max_length=255)

    class Meta:
        unique_together = ('lot_numero', 'lotissement')

    def __str__(self):
        return f"{self.type_attestation} - {self.numero}"

    def save(self, *args, **kwargs):
        if not self.numero:
            self.numero = self._generate_unique_numero()
        super().save(*args, **kwargs)

    def _generate_unique_numero(self):
        while True:
            numero = ''.join(random.choices(string.digits, k=9))
            if not Attestation.objects.filter(numero=numero).exists():
                return numero
