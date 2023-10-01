class Descripcion:
    def __init__(self, red_list, resident):
        self.red_list = red_list
        self.resident = resident

    def __str__(self):
        return f"Red List: {self.red_list}, Resident: {self.resident}"


class Taxonomia:
    def __init__(self, phylum, clase, familia):
        self.phylum = phylum
        self.clase = clase
        self.familia = familia

    def __str__(self):
        return f"Phylum: {self.phylum}, Clase: {self.clase}, Familia: {self.familia}"


class Animalia(Taxonomia, Descripcion):
    def __init__(self, name, scientific_name, phylum, clase, familia, red_list, resident):
        self.name = name
        self.scientific_name = scientific_name
        super().__init__(phylum, clase, familia)
        Descripcion.__init__(self, red_list, resident)

    def __str__(self):
        return f"Nombre: {self.name} ({self.scientific_name}), {super().__str__()}, {Descripcion.__str__(self)}"


animal1 = Animalia("Rana venenosa", "Ameerega rubriventris",
                   "Chordata", 'Amphibia', 'Dendrobatidae',
                   "Endangered", "Perú")

animal2 = Animalia("Loro Cabeciamarillo", "Amazona oratrix",
                   "Chordata", 'Aves', 'Psittacidae',
                   "Endangered", "América del Sur")
print(animal1, " \n\n",  animal2)




