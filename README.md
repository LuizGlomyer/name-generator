# name-generator


Based on this [tutorial](https://medium.com/@onejohi/building-a-simple-rest-api-with-python-and-flask-b404371dc699)

<p>
  Made with Flask and deployed on Heroku. <br>
  Send requests to:
</p>


> https://simple-name-generator.herokuapp.com/

<p>
  Available routes:
</p>

- **/fantasy_name** - generates a fantasy name
- **/br_surname** - generates a Brazilian surname
- **/br_male_name** - generates a Brazilian male name
- **/br_complete_male_name** - generates a complete Brazilian male name
- **/br_female_name** - generates a Brazilian female name
- **/br_complete_female_name** - generates a Complete Brazilian female name
- **/br_cpf** - generates a Brazilian CPF
- **/br_number generates** - a Brazilian telephone number
- **/br_cellphone_number** - generates a Brazilian cellphone number
- **/date** - generates a random date
- **/time** - generates a random time   
<br>
- **/** - sends all available routes
- **/help** - sends all available routes
- **/dev** - Info about the developer

---
<br>
To run the server locally, open the terminal in the root folder and use:

```
$ FLASK_APP=main.py FLASK_ENV=development flask run
```
or
```
$ gunicorn app:app --reload 
```
