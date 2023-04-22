# language: es

Característica: Busqueda (Google)

    Como usuario no registrado
    Quiero poder realizar una busqueda
    Para encontrar resultados acorde

    Antecedentes: 
    Dado Un usuario que se encuentra en la pagina "Principal"

    @NoRegistrado
    Esquema del escenario: Usuario no resgistrado

        Dado Un usuario no registrado
        Cuando Realiza la busqueda de <algo>
        Entonces Encuentra resultados que contengan <algo>
        
        Ejemplos: Busqueda
            | algo          |
            | Neoris        |
            | Messi         |
            | Gherkin       |


