# Script for download of movie video of YouTube

## commands to run

```
  pipenv --python 3.8
  pipenv install
  python app.py
```

## Dicas para entender os filtros do youtube

https://gist.github.com/sidneys/7095afe4da4ae58694d128b1034e01e2

## (Edit 18-10-2020) FIX de erro do youtube

Atualmente o youtube mudou o nome de uma das variaveis internas da api e está estourando um erro ao executar o pytube.
Para corrigir o mesmo basta abrir o aquivo "extract.py" do pacote "pytube" e mudar a linha

```python
parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)
```

para

```python
parse_qs(formats[i]["signatureCipher"]) for i, data in enumerate(formats)
```
