# boxrec-scrapper
![Python package](https://github.com/Victor-DS/boxrec-scrapper/workflows/Python%20package/badge.svg?branch=master&event=push)

A web scrapper for Boxrec data

## How to

Clone the repo:
```
git clone https://github.com/Victor-DS/boxrec-scrapper
```

Go into the folder:
```
cd boxrec-scrapper
```

Build it:
```
python -m pip install -e .
```

Use it:
```
boxrec-scrapper boxer --id 474 --id 584 --output sample
```

For more options:
```
boxrec-scrapper --help
```

## Sample Output
```
{
  "474": {
    "fights": [
      {
        "fight_result": "L",
        "fight_date": "2005-06-11",
        "fight_result_type": "RTD",
        "opponent": "Kevin McBride"
      },
      ...
      {
        "fight_result": "W",
        "fight_date": "1985-03-06",
        "fight_result_type": "TKO",
        "opponent": "Hector Mercedes"
      }
    ],
    "name": "Mike Tyson"
  },
  "584": {
    "fights": [
      {
        "fight_result": "W",
        "fight_date": "1999-02-19",
        "fight_result_type": "TKO",
        "opponent": "Andre Crowder"
      },
      ...
      {
        "fight_result": "W",
        "fight_date": "1981-07-23",
        "fight_result_type": "UD",
        "opponent": "Mike Lear"
      }
    ],
    "name": "James Douglas"
  }
}
```
