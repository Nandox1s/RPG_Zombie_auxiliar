Requisitos: Python apenas, Baixar e abrir o main para usar o app

🎯 Objetivo
Facilitar a execução de testes e rolagens do sistema Zombie_RPG.

Gerar eventos aleatórios como encontros e loot.

Guardar e carregar personagens em arquivos JSON, incluindo inventário, atributos e evolução.

Controlar necessidades básicas (fome, sede, sono) de forma automática.

Registrar o tempo de jogo (dia, hora, minuto) e aplicar efeitos conforme o passar do tempo.

⚙️ Funcionalidades principais
Criação e carregamento de personagens: cada personagem é salvo em JSON e pode ser recuperado em sessões futuras.

Sistema de tempo: controla horas, minutos e dias, aplicando efeitos como cansaço e necessidades.

Necessidades automáticas: fome, sede e sono são atualizados conforme o tempo passa.

Testes de jogo: inclui funções para combate (zumbis, armas, fuga), testes de sorte, habilidade e atributos.

Inventário: adicionar, remover e usar itens, com limite de espaço.

Eventos aleatórios: geração de loot e encontros com zumbis.

Persistência: evolução do personagem e tempo são salvos no JSON.

🚀 Como usar
Execute o programa principal (main.py).

Escolha carregar um personagem existente ou criar um novo.

Use os comandos disponíveis para realizar ações (combate, explorar, descansar, etc.).

O sistema atualiza automaticamente o tempo e as necessidades dos personagens.

Ao sair, os personagens são salvos com suas evoluções e tempo atual.

📖 Exemplos de comandos
criar → cria um novo personagem.

zombieAtaque → enfrenta um ataque de zumbi.

lootear → tenta coletar loot em um local.

comer / beber → consome itens do inventário e reduz fome/sede.

dormir → descansa e recupera sono.

tempo → mostra o tempo atual (dia:hora:minuto).

help → lista todos os comandos disponíveis.

🧩 Observações
Este sistema é apenas um auxiliar para o RPG de mesa Zombie_RPG.

Ele não substitui a narração ou as regras originais, mas automatiza partes repetitivas.

O tempo e evolução dos personagens são salvos em JSON, permitindo continuar campanhas em sessões diferentes.

OBS: Basicamente é um sistema quase de um jogo eletrónico, poderia criar um jogo de fato com base nas regras aqui. Fiz ele sem interface gráfica para ser mais fácil e o usuário ter apenas o python puro
