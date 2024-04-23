from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

def is_medico(user):
    return DadosMedico.objects.filter(user=user).exists()

class Especialidades(models.Model):
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return self.especialidade
    
class DadosMedico(models.Model):
    crm = models.CharField(max_length=30)
    nome = models.CharField(max_length=100)
    cep = models.CharField(max_length=15)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.IntegerField()
    rg = models.ImageField(upload_to='rgs')
    cedula_indentidade_medica = models.ImageField(upload_to='cim')
    foto = models.ImageField(upload_to='fotos_perfil')
    descricao = models.TextField()
    valor_consulta = models.FloatField(default=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)        
    especialidade = models.ForeignKey(Especialidades, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username
    
    @property
    def proxima_data(self):
        proxima_data = DatasAbertas.objects.filter(user = self.user).filter(data__gt=datetime.now()).filter(agendado=False).order_by('data').first()
        


        return proxima_data
    
class DatasAbertas(models.Model):
    data = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    agendado = models.BooleanField(default=False)

    def __str__(self):
        return str(self.data)
    
from paciente.models import Consulta

class Documento(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=30)
    documento = models.FileField(upload_to='documentos')

    def __str__(self):
        return self.titulo