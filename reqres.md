# Graphene.List or DjangoListField

## Request

```JSON
{
  allQuizzes {
    id,
    title,
    category {
      id,
      name
    },
    dateCreated
  }
}
```
## Response

```JSON
{
  "data": {
    "allQuizzes": [
      {
        "id": "1",
        "title": "CQuiz",
        "category": {
          "id": "1",
          "name": "Coding"
        },
        "dateCreated": "2021-11-08T15:31:12.577354+00:00"
      }
    ]
  }
}
```

# Graphene Field (Parameterize queries)

## Request

```JSON
{
  allQuestions(id:1){
    title
  }
}
```

## Response

```JSON
{
  "data": {
    "allQuestions": {
      "title": "What is you fav programming language?"
    }
  }
}
```


## Request

```JSON
{
  allQuestions(id:1){
    title
  }
  allAnswers(id:1){
    answerText
  }
}
```

## Response

```JSON
{
  "data": {
    "allQuestions": {
      "title": "What is you fav programming language?"
    },
    "allAnswers": [
      {
        "answerText": "Python"
      },
      {
        "answerText": "JS"
      },
      {
        "answerText": "GO"
      }
    ]
  }
}
```
