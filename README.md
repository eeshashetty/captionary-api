# captionary-api
API for Captionary

## Steps to Run

Install requirements
```
pip install -r requirements.txt
```

Run Flask App
```
python app.py
```

## To Make a Request

call route `/score` with arguments `image_url` and `id`

where  
`image_url` is the URL for the image to be scored
`id` is the label ID to be checked against (for mappings - [label-id map](https://github.com/eeshashetty/captionary-api/blob/1b326137879a68b19ea77d81f22dd0c2eb601452/id_label_map.py))

returns `0` (no match) or `1` (match)

Example Request

```
GET localhost:8000/score?image_url=https://replicate.delivery/pbxt/NFSsdG1sVxqUOJrduzNnh8jmON5hKcZBjHYze1qTXNe52siQA/output_1.png&id=2
```

returns `1`
