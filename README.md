# desafio_pf
Repositório para o desafio do processo seletivo para estágio na Polícia Federal.

Link para o problema escolhido: https://olimpiada.ic.unicamp.br/pratique/pj/2018/f3/batalha/

O problema consiste em armazenar bolas de diferentes pesos em baldes, e encontrar qual a maior diferença absoluta entre bolas dado um intervalo de baldes.

Para solucionar o problema foi utilizado uma lista para representar os baldes, em que cada balde será uma lista dentro da lista de baldes. A lista de cada balde terá os pesos de suas bolas.Mantendo a lista de cada balde sempre ordenada facilita achar qual a menor e qual a maior bola do balde.

Para a operação de inserir uma bola em uma balde, basta adicionarmos um novo item a lista do respectivo balde com seu valor sendo o peso. Lembrar que o indice na lista de Python começa em 0, por isso precisamos subtrair 1 do indice dado no comando.

Para a operação de achar a maior diferença absoluta iremos comparar a maior bola do primeiro balde do intervalo com as menores bolas dos outros baldes, e comparar a menor bola do primeiro balde com as maiores dos outros baldes, toda vez que acharmos uma diferença absoluta maior, a diferença será atualizada para esta, sendo que a diferença começa em 0. Após isso faremos a mesma coisa, porém, com o segundo balde e sem comparar com o primeiro balde, já que este já foi comparado. Isso continua até chegarmos no último balde, a diferença encontrada então será definitivamente a maior naquele intervalo.