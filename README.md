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