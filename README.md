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
    BAIRRO_ENDER,
    BAIRRO_ENDER_ENVIO,
    COD_CIDADE_NASC,
    COD_CONTINE,
    COD_CONTINE_ENVIO,
    COD_CONTINE_NASC,
    ZONA_TITULO
FROM [lib://Exemplo.qvd]
(qvd);

LOAD
    CD_INSTIT_TITULACAO,
    NR_MATRICULA,
    NR_MILITAR,
    RUA_ENDER_ENVIO,
    SECAO_TITULO,
    UF_CRM,
    UF_EXP_RG,
    ZONA_TITULO
FROM [lib://Exemplo.qvd]
(qvd);

```

Formated script.


```

Load
    BAIRRO_ENDER                                      as BAIRRO_ENDER
,   BAIRRO_ENDER_ENVIO                                as BAIRRO_ENDER_ENVIO
,   COD_CIDADE_NASC                                   as COD_CIDADE_NASC
,   COD_CONTINE                                       as COD_CONTINE
,   COD_CONTINE_ENVIO                                 as COD_CONTINE_ENVIO
,   COD_CONTINE_NASC                                  as COD_CONTINE_NASC
,   ZONA_TITULO                                       as ZONA_TITULO
From [lib://Exemplo.qvd]
(qvd);


Load
    CD_INSTIT_TITULACAO                               as CD_INSTIT_TITULACAO
,   NR_MATRICULA                                      as NR_MATRICULA
,   NR_MILITAR                                        as NR_MILITAR
,   RUA_ENDER_ENVIO                                   as RUA_ENDER_ENVIO
,   SECAO_TITULO                                      as SECAO_TITULO
,   UF_CRM                                            as UF_CRM
,   UF_EXP_RG                                         as UF_EXP_RG
,   ZONA_TITULO                                       as ZONA_TITULO
From [lib://Exemplo.qvd]
(qvd);



```

## Requirements

* Python 3.




 Created by [Victor Hugo Cercasin](https://github.com/VictorCercasin)
 Project's [GitHub](https://github.com/VictorCercasin/QlikLoadFormatter) page
