# NETFLIX RATING MULTICLASS CLASSICATION

![netflix multiclass classification](/home/valcilio/respos/eleflow/entregaveis/netflix_classification/net_mult.png)

## **PREMISSAS:**

Vamos supor que você foi contratada pela empresa Netflix e ela deseja um modelo preditivo para prever as notas de filmes, para assim decidir se vale a pena ou não colocar esse filme no catálogo. Você daria conta desse desafio?

**Entregáveis:**

-  Tratamento dos dados.

- Feature engeneering.

- Divisão da base de dados entre dataset teste e dataset treino.

- A Matriz de Confusão do seu modelo de testes assim como o gráfico de precision e recall do seu modelo.

- Tendo em vista o resultado final o que você faria para melhorar o modelo?

## **Plano de Solução:**

With the objective to help the company to be better organized will be make a predict of how much time is take to the slips be in and out with these following steps:

**1 -** Descrever os dados para poder obter uma melhor compreensão deles.

**2 -** Derivar novas features das features existentes e ajustá-las caso necessário.

**3 -** Analisar os dados para produzir insights.

**4 -** Preparar os dados para poder realizar previsões .

**5 -** Traduzir os resultados do modelo.

## **Retorno Financeiro Esperado:**

Infelizmente, como o desempenho do modelo foi baixo, não há um grande retorno financeiro visualmente citável, mas, **se formos considerar que o modelo tivesse ao menos 90% de precision e recall**, o tornando utilizável, esse modelo poderia ajudar a Netflix em vários pontos como:

- Melhor planejamento do investimento em certas shows.


- Compreender quanto cada show deve render em média.


- Compreender quais os gêneros de shows mais amados pelas pessoas.


- Identificar quais shows devem receber uma sequência ou não.


- Compreender quais shows de terceiros devem ter maior investimento na aquisição.


- Realizar o valuation por show.


- Identificar qual show irá precisar de maior marketing ou terá melhor efeito caso receba mais atenção.


- Identificar qual capa de show deverá ser utilizado para divulgar novos lançamentos (devido a ter uma tendência de obter melhores avaliações e servir como uma melhor primeira impressão).

Esses pontos poderiam ajudar muito a Netflix reduzindo bastante suas despesas, aumentando bastante sua receita e também direcionando melhor seus investimentos, tudo isso em conjunto poderia aumentar seu lucro em cerca de 30% a 50%, pois os shows são de fato o "main business" da Netflix e cada informação referente a eles poderiam ajudar a Netflix a melhorar seu desempenho como empresa.

## **Próximos Passos**:

**Para Um Modelo Melhor:**

Tendo em vista que o modelo possui uma performance bem abaixo do requerido para poder ser utilizável, eu recomendo inicialmente passos para poder melhorar a performance desse modelo que seriam os seguintes:

- Obter mais features que possam ter relação com as notas como o tempo assistido de cada show.


- Obter variáveis como a quantidade de visitas (mesmo que sem ser assistidas) cada show recebe.


- Obter informações de outras plataformas de streaming, caso possível, de shows já presentes na Netflix para comparação.


- Obter informações de shows de outras plataformas de streaming para que o modelo possa ter uma base ainda melhor para comparação.


- Obter features do time de marketing, como o valor do investimento em marketing de cada show e a quantidade de tempo que ele passou sendo divulgado.


- Obter features do time de compras informando fornecendo um rating anterior recebido pelo filme quando estava em outras plataformas (caso não seja original Netflix).


- Criar uma ferramenta de pesquisa (seleção) para clientes que colocaram o rating explicar o motivo de colocarem esse rating e podermos ter mais uma variável de peso explicando o rating dos filmes.

Através da obtenção dessas features será possível ter uma base mais sólida na quando for realizar o treinament odo modelo. Porém ainda é importante citar que **o número de linhas (shows) fornecidos é muito baixo logo precisaria ser aumentado** e sobre o quanto precisaria ser aumentado, eu estipulo o seguinte:

Acredito que o rating iria de 0 até 100, fazendo com que haja um total de 101 ratings diferentes e, para cada rating, seria necessário cerca de 3500 produtos, esse julgamento é tendo em base que existem cerca de 330 produtos com rating 0 e esse rating 0 foi o único que começou a ter bons retornos de métrica (apresentou um recall por volta de 70%, mesmo que as outras métricas tenham sido bem baixas ainda), desse modo julgo que seria necessário aproximadamente 10 vezes essa quantidade, fazendo algo por volta de 3500. Logo adicionado também:

- Obter cerca de 3500 shows por rating (total de 353500 shows para poder haver uma previsão utilizável).

Ademais, também admito que o **ideal nesse caso seria utilizar uma rede neural que poderia considerar os padrões nos outros shows para poder identificar o rating que deve ser adquirido em cada show**, logo, adiciono mais essa medida a ser tomada:

- Estudar e implementar uma rede neural que possa considerar padrões em outras notas e consequentemente ter um melhor desempenho ao classificar as notas dos shows.

Enfim, é plausível acreditar que seguindo esses passos seja possível criar um modelo que seja capaz de prever de forma eficiente as notas que cada filme deve vir a receber.

**Pós-Desenvolvimento De Um Modelo Com Melhor Desempenho:**

Uma vez que um modelo com melhor desempenho tenha sido desenvolvido, é necessário passar para os próximos passos que seria ensinar o time de negócios a utilizá-lo após pô-lo em produção. Desse modo, **deve ser feita uma reunião** onde irá ser levantando os seguintes pontos:

- Explicação do contexto de negócio.


- Explicação do porquê aquele projeto foi necessário.


- Explicação da performance do modelo.


- Explicação de como esse modelo pode ser útil para o time.


- Explicação sobre como o aplicativo web funcionará.


- Explicação sobre como o resultado desse modelo ajudará toda a empresa (incluindo o efeito dominó dele).


- Explicação sobre o retorno financeiro dele.


Uma vez feita essa reunião e explicado tudo isso será necessário que haja então mais algumas reuniões com o time que irá mais se beneficiar e utilizar a aplicação web para que ele possa compreender a fundo como ela funciona e extrair o máximo de resultado que a aplicaçao web poderá fornecer.

## **Conclusão:**

Enfim, uma vez concluídos os passos da parte "**12.1. Próximos Passos**" deverá ser possível ter um modelo eficiente que trará os resultados financeiros esperados pela "**Etapa 11**", assim possibilitando a Netflix e ao time de dados produzirem outros modelos que possam ajudar a Netflix a produzir ainda mais insights para seu negócio, além de estar sempre trabalhando na atualização do modelo já produzido para garantir que ele não perca sua funcionalidade.

## Aprendizados:

Nesse projeto, tive a oportunidade de aprender mais sobre classificação multiclass e também sobre o modelo de negócio de streaming, além de também poder aprender mais um pouco sobre cross validation e até passar a criar minha própria função para realizar essa atividade.