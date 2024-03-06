import os
from jinja2 import Environment, FileSystemLoader

# Diretório onde estão os templates do Terraform
template_dir = 'templates'

# Carrega o ambiente Jinja2
env = Environment(loader=FileSystemLoader(template_dir))

# Carrega o template do Terraform
template = env.get_template('terraform_template.tf.j2')

# Define os dados que serão usados para substituir no template
data = {
    'nome': os.getenv('NOME'),
    'sobrenome': os.getenv('SOBRENOME'),
    'idade': os.getenv('IDADE')
}

# Renderiza o template com os dados fornecidos
output = template.render(data)

# Escreve o resultado no arquivo de configuração final
with open('terraform_config.tf', 'w') as f:
    f.write(output)

print("Arquivo de configuração do Terraform gerado com sucesso.")
