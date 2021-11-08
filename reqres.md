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
