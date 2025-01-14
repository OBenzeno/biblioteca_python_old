class Usuario:
    proximo_id = 1  # Variável de classe para o próximo ID
    def __init__(self, nome, contato, _id=None):
        if _id is None:
            self.id = Usuario.proximo_id
            Usuario.proximo_id += 1
        else:
            self.id = _id
        self.nome = nome
        self.contato = contato

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'contato': self.contato
        }
