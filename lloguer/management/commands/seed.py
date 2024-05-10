# scripts/seed.py
import random
from faker import Faker
from lloguer.models import Categoria, Automobil
from django.core.management.base import BaseCommand

fake = Faker()

class Command(BaseCommand):
    help = 'Populate database with fake data'

    def handle(self, *args, **kwargs):
        self.seed()

    def seed(self):
        for _ in range(10):
            Categoria.objects.create(nom=fake.word(), descripcion=fake.text())

        categorias = Categoria.objects.all()

        for _ in range(200):
            marca = fake.company()
            modelo = fake.word()
            matricula = fake.license_plate()

            categoria = random.choice(categorias)

            Automobil.objects.create(marca=marca, model=modelo, matricula=matricula, categoria=categoria)

        self.stdout.write(self.style.SUCCESS('Seed completed successfully.'))
