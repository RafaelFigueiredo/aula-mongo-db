# Mongo DB

## O que é Mongo DB
O Mongo DB é um banco de dados não relacional (no-sql) capaz de armazenar "documentos" tipo JSON. No nosso contexto de python, podemos pensar no mongo como um repositório para dicionários que provê persistência e busca.

## Termos a prióri:
Banco de dados
Coleção
Documento
Atributos

## Operações básicas
Em desenvolvimento nos referimos muito ao termo CRUD, abreviação de:
* Create(Criar), 
* Read(Ler), 
* Update(Atualizar), e 
* Delete(Deletar).

### Inserir um documentos
```python
user = {
    'username': 'r',
    'admin': True,
}
mongo.db.users.insert_one(user)
```
### Inserir múltiplos documentos
```python
albums = [
    {
        "title": "System of a Down",
        "released": "June 30, 1998"
    },
    {
        "title": "Toxicity",
        "released": "September 4, 2001"
    },
    {
        "title": "Steal This Album!",
        "released": "November 26, 2002"
    },
    {
        "title": "Mezmerize",
        "released": "May 17, 2005"
    },
    {
        "title": "Hypnotize",
        "released": "November 22, 2005"
    }
]
mongo.db.albums.insert_many(albums)
```

### Ler um documento
```python
album = mongo.db.albums.find_one({'title':'Mezmerize'})
print(album)
```

### Ler múltiplos documentos
```python
for book in mongo.db.books.find({'author': 'Douglas Noel Adams'}):
    print(book)
```

### Atualizar um documento
```python
filter = { 'codigo_do_pedido': 'ABCD' }
new_values = {"$set": { 'status': 'aprovado' }}
mongo.db.vendas.update_one(filter, new_values)
```

### Atualiza múltiplos documentos
```python
# atualiza todos os produtos, para terem desconto de 10%
filter = {}
new_values = {"$set": { 'desconto_percentual': 10 }}
mongo.db.produtos.update_many(filter, new_values )
```

### Apagar um documentos
```python
mondo.db.users.delete_one({'user': 'guest'})
```

### Apagar múltiplos documentos documento
```python
filter = {"Name": {"$regex": "^A"}}
mongo.db.my_collection.delete_many(filter)
```

## Nosso projeto de test

**REQ1:** Construir uma API de telemetria com duas rotas:
* POST `/telemetry` - Essa rota deve receber uma leitura de telemetria no formato JSON, contendo valores para vários atributos e armazena-la.  
Exemplo de requisição:
```sh
curl --request POST \
  --url http://localhost:5000/telemetry \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: Insomnia/2023.5.6' \
  --data '{
	"temperature": 36.0,
	"pressure": 1022
}'
```
* GET `/query/<attribute>` - Essa rota deve retornar todas as leituras de um atributo dado um intervalo de tempo.  
Exemplo de requisição:
```sh
curl --request GET \
  --url http://localhost:5000/query/temperature \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: Insomnia/2023.5.6' \
  --data '{
	"begin": "2023-07-29T00:00:00",
	"end": "2023-08-29T23:59:59"
}'
```
**REQ2:** Os devem ser enviados no formato JSON
**REQ3:** Os timestamps devem ser no formato ISO

