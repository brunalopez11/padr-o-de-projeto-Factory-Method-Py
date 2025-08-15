# Classe de Base de Veiculo:
class Veiculo:
    def __init__(self, modelo):
        self.modelo = modelo

    def mostrarDetalhes(self):
        print(f"Modelo: {self.modelo}")

# Subclasse de Veiculos:
class Carro(Veiculo):
    def __init__(self, modelo):
        super().__init__(modelo)

class Moto(Veiculo):
    def __init__(self, modelo):
        super().__init__(modelo)

class Caminhao(Veiculo):
    def __init__(self, modelo):
        super().__init__(modelo)

# Fabrica abstrata de veiculo:
class FabricaDeVeiculo:
    def criarVeiculo(self, modelo):
        raise NotImplementedError("O método deve ser implementado pela subclasse")

# Fabrica Concreta de Carro:
class FabricaDeCarro(FabricaDeVeiculo):
    def criarVeiculo(self, modelo):
        return Carro(modelo)

# Fabrica Concreta de moto:
class FabricaDeMoto(FabricaDeVeiculo):
    def criarVeiculo(self, modelo):
        return Moto(modelo)

# Fabrica Concreta de Caminhao:
class FabricaDeCaminhao(FabricaDeVeiculo):
    def criarVeiculo(self, modelo):
        return Caminhao(modelo)
    
# USO DO PADRÃO DO PROJETO - FABRICA:
fabrica_carro = FabricaDeCarro()
fabrica_moto = FabricaDeMoto()
fabrica_caminhao = FabricaDeCaminhao()

carro1 = fabrica_carro.criarVeiculo('Sedan')
carro2 = fabrica_carro.criarVeiculo('Esportivo')
moto1 = fabrica_moto.criarVeiculo('Yamaha-660')
moto2 = fabrica_moto.criarVeiculo('Honda-CG160')
caminhao1 = fabrica_caminhao.criarVeiculo('Scania')
caminhao2 = fabrica_caminhao.criarVeiculo('VW-Cargo')

carro1.mostrarDetalhes()
carro2.mostrarDetalhes()
moto1.mostrarDetalhes()
moto2.mostrarDetalhes()
caminhao1.mostrarDetalhes()
caminhao2.mostrarDetalhes()
