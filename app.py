from modulo import *

if __name__ == "__main__":
    # instancia dos objetivos
    endereco_pessoal = Endereco('','','','')
    usuario = Pessoa('',0,'','')
    contato = Telefone('','','')
  # entrada de dados do usuario
    usuario.nome = input('Informe o nome do usuário: ')
    usuario.idade = int(input('Informe a idade do usuário: '))
   #usuario.telefone = ('Informe o telefone para  contato:')
    
   
    #composição usuário-endereço
    usuario.endereco= endereco_pessoal
    usuario.contato = contato
    
    
    #entrada de dados do endereço
    
    usuario.endereco.cep = input('Informe  seu cep: ')
    usuario.endereco.uf = input('Informe a UF: ')
    usuario.endereco.cidade = input('Informe a cidade:')
    usuario.endereco.bairro = input('Informe o bairro:')
    usuario.telefone_contato = ('Informe o telefone para  contato:')
    usuario.telefone_residensial=('Informe o telefone residencial: ')
    usuario.telefone_celular = ('Informe o relefone celular')
    
    
    
    
    # entrada de dados
    
    # saida de dados
    
    print(usuario.obter_info_pessoal())