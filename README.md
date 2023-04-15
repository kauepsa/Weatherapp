# Projeto Django de Previsão do Tempo
Este é um projeto Django que permite ao usuário pesquisar por cidades e receber informações meteorológicas atualizadas. O projeto utiliza uma API de terceiros para buscar informações meteorológicas de diferentes cidades ao redor do mundo.

![image](https://user-images.githubusercontent.com/93888091/232176327-00df2305-e8cf-471e-94ba-48beeb33dc77.png)
![image](https://user-images.githubusercontent.com/93888091/232176333-2ff098ad-b5d8-4cb0-ac48-86ec033dabdb.png)



## Instalação

1- Clone o repositório para sua máquina local usando o comando:
``` git clone https://github.com/kauepsa/Weatherapp.git ```

2- Certifique-se de que o Python 3 está instalado em sua máquina.

3- Instale as dependências do projeto com o seguinte comando:
``` pip install -r requirements.txt ```

4- Rode as migrações com o seguinte comando:
```
python manage.py makemigrations
python manage.py migrate
```

5- Crie um arquivo .env na raiz do projeto com as seguintes variáveis:
```
DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui
OPENWEATHERMAP_API_KEY=sua-chave-da-api-openweathermap-aqui 
```

6- Inicie o servidor local com o seguinte comando:
``` python manage.py runserver ```

7- Abra o navegador e acesse http://localhost:8000 para ver a página inicial do projeto.

## Utilização
Na página inicial, o usuário pode pesquisar por uma cidade na caixa de pesquisa e clicar no botão de busca para receber informações meteorológicas atualizadas sobre a cidade. As informações incluem a temperatura atual, a pressão atmosférica, a umidade relativa do ar e a previsão do tempo para os próximos dias.

O projeto utiliza a API da OpenWeatherMap para buscar as informações meteorológicas. A chave de API da OpenWeatherMap deve ser adicionada ao arquivo .env do projeto para que a API funcione corretamente.

## Contribuição
Contribuições para o projeto são bem-vindas! Se você encontrar um bug ou tiver uma sugestão de melhoria, sinta-se à vontade para abrir uma issue ou enviar uma pull request.
