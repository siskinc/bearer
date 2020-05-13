# export-data-from-database-to-something
## generate model from database
### support database type
    - mysql
    - influxdb
#### generate demo
```shell script
python -m tools.generate_model --mysql-host mysql-host --mysql-user mysql-user --mysql-password mysql-password --mysql-port 3306 --database database --table table1 --table table2 --file-path a.py
```

## data reader
### support

- [x] MySQL
- [x] InfluxDB
- [ ] MongoDB

### export

#### support

- [x] xlsx

## TODO
- [ ] Job Config operation(like datax)