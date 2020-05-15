# bearer
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

## config file
### example
```json
{
  "database": {
    "host": "host",
    "username": "username",
    "password": "password",
    "port": 3306,
    "data_base_type": 0, // 0 is mysql, 1 is influx
    "database_name": "database_name",
    "misc": {
      "table_name": "table_name"
    }
  },
  "models": [
    {
      "name": "DemoModel",
      "fields": [
        "auto_id",
        "f_a",
        "f_b"
      ],
      "comments": [
        "auto_id",
        "A",
        "B"
      ]
    }
  ],
  "jobs": [
    {
      "name": "job a",
      "where": "f_a=1",
      "batch_size": 1000,
      "export": {
        "output_file_path": "job_a.xlsx",
        "export_type": 0 // 0 is excel
      },
      "model": "DemoModel"
    }
  ]
}
```

## run with config
```bash
python -m bearer --config-path config.json
```

## TODO
- [x] Job Config operation(like datax)