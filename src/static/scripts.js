$(document).ready(function () {
    if (document.getElementById('tablaCentros') != null) {
        new gridjs.Grid({
            columns: [
                "Id", "Nombre", "Abreviatura", "Email administrativo",
                {
                    name: 'Acciones',
                    //width: '8%',
                    sort:false,
                    formatter: (_, row) => gridjs.html(`<a class="icono" href="#" onclick="alert( '${row.cells[0].data}');"><i class="bi bi-pencil-square"></i></a> <a href="#" class="icono" onclick="alert( '${row.cells[0].data}');"><i class="bi bi-trash3-fill"></i></a>`)
                },
            ],
            className: {
                td: "text-center",
                th: "text-center"
            },
            sort: true,
            search: true,
            width: "70%",
            data: [
                ["1", "Centro 1", "AA", "ubu@ubu.es", null],
                ["2", "Centro 2", "BB", "ubu@ubu.es", null],
                ["3", "Centro 3", "CC", "ubu@ubu.es", null],
                ["4", "Centro 4", "DD", "ubu@ubu.es", null],
                ["5", "Centro 5", "EE", "ubu@ubu.es", null]
            ]
        }).render(document.getElementById("tablaCentros"));
    }

    if (document.getElementById('tablaTitulaciones') != null) {
        new gridjs.Grid({
            columns: [
                "Id", "Nombre", "Abreviatura", "URL",
                {
                    name: 'Acciones',
                    formatter: (_, row) => gridjs.html(`<a class="icono" href="#" onclick="alert( '${row.cells[0].data}');"><i class="bi bi-pencil-square"></i></a> <a href="#" class="icono" onclick="alert( '${row.cells[0].data}');"><i class="bi bi-trash3-fill"></i></a>`)
                },
            ],
            className: {
                td: "text-center",
                th: "text-center"
            },
            sort: true,
            search: true,
            width: "70%",
            data: [
                ["1", "Grado 1", "AA", "www.ubu.es", null],
                ["2", "Grado 2", "BB", "www.ubu.es", null],
                ["3", "Grado 3", "CC", "www.ubu.es", null],
                ["4", "Grado 4", "DD", "www.ubu.es", null],
                ["5", "Grado 5", "EE", "www.ubu.es", null]
            ]
        }).render(document.getElementById("tablaTitulaciones"));
    }

    if (document.getElementById('tablaAsignaturas') != null) {
        new gridjs.Grid({
            columns: [
                "Id", "Nombre", "Tipo", "Titulación", "Créditos teoría", "Créditos práctica", "Curso", "Semestre", "Abreviaturas",
                {
                    name: 'Acciones',
                    formatter: (_, row) => gridjs.html(`<a class="icono" href="#" onclick="alert( '${row.cells[0].data}');"><i class="bi bi-pencil-square"></i></a> <a href="#" class="icono" onclick="alert( '${row.cells[0].data}');"><i class="bi bi-trash3-fill"></i></a>`)
                },
            ],
            className: {
                td: "text-center",
                th: "text-center"
            },
            sort: true,
            search: true,
            data: [
                ["1", "Asignatura 1", "Grado 1", "Obligatoria", 3, 3, "3º", 1, "AA, A1", null],
                ["2", "Asignatura 2", "Grado 2", "Optativa", 3, 3, "4º", 1, "BB", null],
                ["3", "Asignatura 3", "Grado 1", "Obligatoria", 3, 3, "2º", 2, "CC", null],
                ["4", "Asignatura 4", "Grado 1", "Básica", 3, 3, "1º", 1, "DD, D1", null],
                ["5", "Asignatura 5", "Grado 5", "Obligatoria", 3, 3, "3º", 2, "EE", null]
            ]
        }).render(document.getElementById("tablaAsignaturas"));
    }

    if (document.getElementById('tablaDocentes') != null) {
        new gridjs.Grid({
            columns: [
                "Id", "Nombre", "Apellidos", "Email", "Reducciones",
                {
                    name: 'Acciones',
                    formatter: (_, row) => gridjs.html(`<a class="icono" href="#" onclick="alert( '${row.cells[0].data}');"><i class="bi bi-pencil-square"></i></a> <a href="#" class="icono" onclick="alert( '${row.cells[0].data}');"><i class="bi bi-trash3-fill"></i></a>`)
                },
            ],
            className: {
                td: "text-center",
                th: "text-center"
            },
            sort: true,
            search: true,
            width: "70%",
            data: [
                ["1", "Nombre 1", "Apellido", "ubu@ubu.es", 3, null],
                ["2", "Nombre 2", "Apellido", "ubu@ubu.es", 3, null],
                ["3", "Nombre 3", "Apellido", "ubu@ubu.es", 3, null],
                ["4", "Nombre 4", "Apellido", "ubu@ubu.es", 3, null],
                ["5", "Nombre 5", "Apellido", "ubu@ubu.es", 3, null]
            ]
        }).render(document.getElementById("tablaDocentes"));
    }

    if (document.getElementById('tablaPlazas') != null) {
        new gridjs.Grid({
            columns: [
                "Id", "Nombre", "RPT", "Fecha incorporación", "Fecha cese", "Nº concursos contratación", "Docente", "Tipo contrato",
                {
                    name: 'Acciones',
                    formatter: (_, row) => gridjs.html(`<a class="icono" href="#" onclick="alert( '${row.cells[0].data}');"><i class="bi bi-pencil-square"></i></a> <a href="#" class="icono" onclick="alert( '${row.cells[0].data}');"><i class="bi bi-trash3-fill"></i></a>`)
                },
            ],
            sort: true,
            search: true,
            className: {
                td: "text-center",
                th: "text-center"
            },
            data: [
                ["1", "Nombre 1", "RPT", "01/01/2023", "01/01/2024", "Docente 1", "Tipo 1", 1, null],
                ["2", "Nombre 2", "RPT", "01/01/2023", "01/01/2024", "Docente 2", "Tipo 2", 1, null],
                ["3", "Nombre 3", "RPT", "01/01/2023", "01/01/2024", "Docente 3", "Tipo 1", 1, null],
                ["4", "Nombre 4", "RPT", "01/01/2023", "01/01/2024", "Ninguno", "Tipo 7", 1, null],
                ["5", "Nombre 5", "RPT", "01/01/2023", "01/01/2024", "Docente 4", "Tipo 5", 1, null]
            ]
        }).render(document.getElementById("tablaPlazas"));
    }

    if (document.getElementById('tablaContratos') != null) {
        new gridjs.Grid({
            columns: [
                "Id", "Nombre", "Abreviatura", "Capacidad anual",
                {
                    name: 'Acciones',
                    formatter: (_, row) => gridjs.html(`<a class="icono" href="#" onclick="alert( '${row.cells[0].data}');"><i class="bi bi-pencil-square"></i></a> <a href="#" class="icono" onclick="alert( '${row.cells[0].data}');"><i class="bi bi-trash3-fill"></i></a>`)
                },
            ],
            sort: true,
            search: true,
            width: "70%",
            className: {
                td: "text-center",
                th: "text-center"
            },
            data: [
                ["1", "Nombre 1", "AA", 800, null],
                ["2", "Nombre 2", "BB", 800, null],
                ["3", "Nombre 3", "CC", 800, null],
                ["4", "Nombre 4", "DD", 800, null],
                ["5", "Nombre 5", "EE", 800, null]
            ]
        }).render(document.getElementById("tablaContratos"));
    }

    if (document.getElementById('tablaAreas') != null) {
        new gridjs.Grid({
            columns: [
                "Id", "Nombre", "Abreviatura", "Departamento",
                {
                    name: 'Acciones',
                    formatter: (_, row) => gridjs.html(`<a class="icono" href="#" onclick="alert( '${row.cells[0].data}');"><i class="bi bi-pencil-square"></i></a> <a href="#" class="icono" onclick="alert( '${row.cells[0].data}');"><i class="bi bi-trash3-fill"></i></a>`)
                },
            ],
            sort: true,
            search: true,
            width: "70%",
            className: {
                td: "text-center",
                th: "text-center"
            },
            data: [
                ["1", "Nombre 1", "AA", "Departamento 1", null],
                ["2", "Nombre 2", "BB", "Departamento 1", null],
                ["3", "Nombre 3", "CC", "Departamento 1", null],
                ["4", "Nombre 4", "DD", "Departamento 1", null],
                ["5", "Nombre 5", "EE", "Departamento 1", null]
            ]
        }).render(document.getElementById("tablaAreas"));
    }

    if (document.getElementById('tablaDepartamentos') != null) {
        new gridjs.Grid({
            columns: [
                "Id", "Nombre", "Abreviatura",
                {
                    name: 'Acciones',
                    formatter: (_, row) => gridjs.html(`<button type="button" class="btn btn-primary" onclick="alert( '${row.cells[0].data}');">Modificar</button> <button type="button" class="btn btn-primary" onclick="alert( '${row.cells[0].data}');">Eliminar</button>`)
                },
            ],
            sort: true,
            search: true,
            data: [
                ["1", "Nombre 1", "AA", null],
                ["2", "Nombre 2", "BB", null],
                ["3", "Nombre 3", "CC", null],
                ["4", "Nombre 4", "DD", null],
                ["5", "Nombre 5", "EE", null]
            ]
        }).render(document.getElementById("tablaDepartamentos"));
    }

    if (document.getElementById('tablaCursos') != null) {
        new gridjs.Grid({
            columns: [
                "Id", "Año inicio", "Año fin",
                {
                    name: 'Acciones',
                    formatter: (_, row) => gridjs.html(`<button type="button" class="btn btn-primary">Modificar Año</button> <button type="button" class="btn btn-primary" onclick="alert( '${row.cells[0].data}');">Modificar</button> <button type="button" class="btn btn-primary">Duplicar</button> <button type="button" class="btn btn-primary" onclick="alert( '${row.cells[0].data}');">Eliminar</button>`)
                },
            ],
            className: {
                td: "text-center",
                th: "text-center"
            },
            sort: true,
            search: true,
            width: "70%",
            data: [
                ["1", "2020", "2021", null],
                ["2", "2021", "2022", null],
                ["3", "2022", "2023", null],
                ["4", "2023", "2024", null]
            ]
        }).render(document.getElementById("tablaCursos"));
    }

    if (document.getElementById('tablaGrupos') != null) {
        new gridjs.Grid({
            columns: [
                "Centro", "Titulación", "Asignatura", "Semestre", "Nº grupos teoría", "Nº grupos práctica", "Nº grupos online teoría", "Nº grupos online práctica", "Nº grupos inglés teoría", "Nº grupos inglés práctica",
                {
                    name: 'Acciones',
                    formatter: (_, row) => gridjs.html(`<button type="button" class="btn btn-primary" onclick="alert( '${row.cells[0].data}');">Gestionar grupos</button>`)
                },
            ],
            sort: true,
            search: true,
            data: [
                ["Centro 1", "Grado 1", "Asignatura 1", 1, 1, 1, 1, 1, 1, 1, null],
                ["Centro 2", "Grado 2", "Asignatura 1", 1, 1, 1, 1, 1, 1, 1, null],
                ["Centro 3", "Grado 3", "Asignatura 1", 2, 1, 1, 1, 1, 1, 1, null],
                ["Centro 4", "Grado 4", "Asignatura 1", 1, 1, 1, 1, 1, 1, 1, null]
            ]
        }).render(document.getElementById("tablaGrupos"));
    }

    if (document.getElementById('tablaCursos') != null) {
        new gridjs.Grid({
            columns: [
                "Id", "Año inicio", "Año fin",
                {
                    name: 'Acciones',
                    formatter: (_, row) => gridjs.html(`<button type="button" class="btn btn-primary">Modificar Año</button> <button type="button" class="btn btn-primary" onclick="alert( '${row.cells[0].data}');">Modificar</button> <button type="button" class="btn btn-primary">Duplicar</button> <button type="button" class="btn btn-primary" onclick="alert( '${row.cells[0].data}');">Eliminar</button>`)
                },
            ],
            sort: true,
            search: true,
            width: "70%",
            data: [
                ["1", "2020", "2021", null],
                ["2", "2021", "2022", null],
                ["3", "2022", "2023", null],
                ["4", "2023", "2024", null]
            ]
        }).render(document.getElementById("tablaCursos"));
    }

    if (document.getElementById('tablaHoras') != null) {
        new gridjs.Grid({
            columns: [
                "Centro", "Titulación", "Asignatura", "Semestre", "Id Grupo", "Plaza/Docente", "Horas", "Horas totales docente", "Plaza/Docente","Horas", "Horas totales docente", "Plaza/Docente","Horas", "Horas totales docente",
                {
                    name: 'Acciones',
                    formatter: (_, row) => gridjs.html(`<button type="button" class="btn btn-primary" onclick="alert( '${row.cells[0].data}');">Editar</button>`)
                },
            ],
            sort: true,
            search: true,
            data: [
                ["Centro 1", "Grado 1", "Asignatura 1", 1, 1, "Plaza 1", 1, 1, "Plaza 2", 1, 1, "Plaza 3", 1, 1, null],
                ["Centro 2", "Grado 2", "Asignatura 1", 1, 1, "Docente 1", 1, 1, "Plaza 2", 1, 1, "Plaza 3", 1, 1, null],
                ["Centro 3", "Grado 3", "Asignatura 1", 2, 1, "Plaza 5", 1, 1, "Plaza 3", 1, 1, "Plaza 4", 1, 1, null],
                ["Centro 4", "Grado 4", "Asignatura 1", 1, 1, "Plaza 3", 1, 1, "Plaza 2", 1, 1, "Plaza 3", 1, 1, null]
            ]
        }).render(document.getElementById("tablaHoras"));
    }


});