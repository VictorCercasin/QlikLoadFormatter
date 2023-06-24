# QlikLoadFormatter

> Python script for converting Qlik Sense's default load script format into a more suitable format, as stated by `Bitmetric Qlik Sense Coding Conventions`, available [HERE](https://www.bitmetric.nl/blog/bitmetric-qlik-sense-coding-conventions-free-download/).

## Usage

1. Paste Qlik Sense's default load script into input.txt file.
2. Run QlikLoadFormatter.py from the terminal or by double clicking it. 
3. Formatted script will be written in output.txt file.


* Use -l flag to set line width. Default is 50.


## Example

Qlik Sense's default load script format.

```
LOAD
    FIELD1,
    FIELD2,
    FIELD3
FROM [lib://TEST/table1.qvd]
(qvd);


LOAD
    FIELD1,
    FIELD2,
    FIELD3
FROM [lib://TEST/table2.qvd]
(qvd);



```

Formated script.


```

Load
    FIELD1                                            as FIELD1
,   FIELD2                                            as FIELD2
,   FIELD3                                            as FIELD3
From [lib://TEST/table1.qvd]
(qvd);



Load
    FIELD1                                            as FIELD1
,   FIELD2                                            as FIELD2
,   FIELD3                                            as FIELD3
From [lib://TEST/table2.qvd]
(qvd);



```

## Requirements

* Python 3.




 Created by [Victor Hugo Cercasin](https://github.com/VictorCercasin)
 Project's [GitHub](https://github.com/VictorCercasin/QlikLoadFormatter) page
