class Carro:
    def __init__(
        self,
        fabricante,
        modelo,
        ano,
        quilometragem,
        motorizacao,
        valor,
        cor,
        placa,
    ):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem
        self.motorizacao = motorizacao
        self.valor = valor
        self.cor = cor
        self.placa = placa

    def __str__(self):
        return (
            f"Fabricante: {self.fabricante}, Modelo: {self.modelo}, "
            f"Ano: {self.ano}, Quilometragem: {self.quilometragem}, "
            f"Motorizacao: {self.motorizacao}, Valor: {self.valor}, "
            f"Cor: {self.cor}, Placa: {self.placa}"
        )
